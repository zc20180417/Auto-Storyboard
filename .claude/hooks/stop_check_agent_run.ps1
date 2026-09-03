# Claude Code Stop hook: validate the full storyboard run before session ends.
# Mirrors .codex/hooks/stop_check_agent_run.ps1 logic for Claude Code's hook system.
$ErrorActionPreference = "Stop"

$hookRoot = Split-Path -Parent $PSScriptRoot
$workspace = Split-Path -Parent $hookRoot
$logPath = Join-Path $hookRoot "storyboard-stop-check.jsonl"

function Write-HookLog {
    param([hashtable]$Entry)
    $Entry.recorded_at = (Get-Date).ToUniversalTime().ToString("o")
    ($Entry | ConvertTo-Json -Compress -Depth 12) | Add-Content -LiteralPath $logPath -Encoding UTF8
}

function Read-HookPayload {
    # Claude Code writes the hook payload as UTF-8. [Console]::In follows the console
    # input code page (GBK/936 on zh-CN Windows), which mangles multibyte characters and
    # breaks ConvertFrom-Json, silently skipping the gate. Read stdin with an explicit
    # UTF-8 decoder instead. [Console]::InputEncoding is avoided: it can throw when
    # stdin is redirected.
    try {
        $stdinStream = [Console]::OpenStandardInput()
        $reader = New-Object System.IO.StreamReader($stdinStream, (New-Object System.Text.UTF8Encoding($false)))
        $raw = $reader.ReadToEnd()
        $reader.Dispose()
    } catch {
        $raw = [Console]::In.ReadToEnd()
    }
    if ([string]::IsNullOrWhiteSpace($raw)) {
        return [pscustomobject]@{ hook_event_name = "Stop"; raw_input_empty = $true }
    }
    try {
        return $raw | ConvertFrom-Json
    } catch {
        Write-HookLog @{ event = "Stop"; result = "skip"; error = $_.Exception.Message }
        return [pscustomobject]@{ hook_event_name = "Stop"; invalid_json = $true }
    }
}

function Get-RunDir {
    # Explicit binding only. This is a DELIVERY gate: falling back to "the most recently
    # touched run under agent_runs" made it block sessions that never worked on that run,
    # over failures they did not cause and are not scoped to fix. A gate that picks its own
    # target is worse than no gate. Bind a run by writing its path into
    # .claude/storyboard-hook-run.txt (or .codex/storyboard-hook-run.txt).
    foreach ($hintDir in @($hookRoot, (Join-Path $workspace ".codex"))) {
        $hintPath = Join-Path $hintDir "storyboard-hook-run.txt"
        if (-not (Test-Path -LiteralPath $hintPath)) {
            continue
        }
        $hint = (Get-Content -LiteralPath $hintPath -Raw).Trim()
        if (-not $hint) {
            continue
        }
        $candidate = if ([System.IO.Path]::IsPathRooted($hint)) { $hint } else { Join-Path $workspace $hint }
        if (Test-Path -LiteralPath (Join-Path $candidate "manifest.json")) {
            return (Resolve-Path -LiteralPath $candidate).Path
        }
    }

    return $null
}

function Get-FailureSummary {
    param([object]$Result)
    if ($null -eq $Result -or $null -eq $Result.failures) {
        return "No checker details were returned."
    }
    $failures = @($Result.failures)
    if ($failures.Count -eq 0) {
        return "No checker details were returned."
    }
    return (($failures | Select-Object -First 12 | ForEach-Object { "- $_" }) -join "`n")
}

# --- Main ---
$payload = Read-HookPayload

# Episode workers write draft/final/review/status incrementally. Validating while any of
# them is still running reports the half-written intermediate state as a gate failure:
# noisy, unactionable, and impossible for the main thread to fix without racing the
# worker's own writes. Worse, a worker blocked by that noise may step outside its assigned
# episode to "unblock" the run. Wait for the workers to finish instead.
$runningTasks = @()
if ($payload -and $payload.PSObject.Properties.Name -contains "background_tasks") {
    $runningTasks = @($payload.background_tasks | Where-Object { $_ -and $_.status -eq "running" })
}
if ($runningTasks.Count -gt 0) {
    $names = ($runningTasks | ForEach-Object { $_.description }) -join ", "
    Write-HookLog @{ event = "Stop"; result = "skip"; reason = "background workers still running"; running = $names }
    '{"continue":true}'
    exit 0
}

# This is a RUN-level gate: it requires every episode to validate and the run to be
# collected. That is the main thread's acceptance step, not an episode worker's job.
#
# An episode worker only owns its own episode. Blocking it because a *sibling* episode is
# incomplete gives it a failure it is not allowed to fix (its prompt scopes it to one
# episode) and no way to stop. In an earlier run a worker in exactly that position went
# outside its assigned episode and self-certified the edits to clear the gate. The
# background_tasks check above does not help here: a subagent's payload lists only its own
# children, so a sibling worker is invisible to it.
#
# So: inside a subagent session, stay out of the way and let the main thread run the gate.
$agentId = $null
if ($payload -and $payload.PSObject.Properties.Name -contains "agent_id") {
    $agentId = $payload.agent_id
}
if ($agentId) {
    Write-HookLog @{ event = "Stop"; result = "skip"; reason = "subagent session; run gate is the main thread's job"; agent_id = $agentId }
    '{"continue":true}'
    exit 0
}

$runDir = Get-RunDir
if (-not $runDir) {
    Write-HookLog @{ event = "Stop"; result = "skip"; reason = "no agent run found" }
    '{"continue":true}'
    exit 0
}

$checker = Join-Path (Join-Path $workspace "tools") "check-agent-run.ps1"
# $ErrorActionPreference = "Stop" turns any stderr writes from a native command into a
# terminating NativeCommandError. validate-episode/check-agent-run legitimately write to
# stderr, which killed this hook before it emitted any JSON -- i.e. no gate at all.
# Relax it around the call and rely on the exit code instead.
$previousEap = $ErrorActionPreference
$ErrorActionPreference = "Continue"
$checkerOutput = & powershell -NoProfile -ExecutionPolicy Bypass -File $checker -RunDir $runDir -Json 2>&1
$checkerExit = $LASTEXITCODE
$ErrorActionPreference = $previousEap
$checkerText = ($checkerOutput | Out-String).Trim()
$checkerResult = $null
try {
    if ($checkerText) {
        $checkerResult = $checkerText | ConvertFrom-Json
    }
} catch {
    $checkerResult = $null
}

if ($checkerExit -eq 0) {
    Write-HookLog @{ event = "Stop"; result = "pass"; run = $runDir; checker = $checkerResult }
    '{"continue":true}'
    exit 0
}

Write-HookLog @{ event = "Stop"; result = "fail"; run = $runDir; checker = $checkerResult; raw = $checkerText }
$summary = Get-FailureSummary -Result $checkerResult

$reason = "Auto-Storyboard run gate failed. Fix the listed issues, rerun per-episode validate, and collect the run before summarizing.`n$summary"
@{ decision = "block"; reason = $reason } | ConvertTo-Json -Compress
exit 0
