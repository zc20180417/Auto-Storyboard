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
    # Check hint files: .claude/storyboard-hook-run.txt, then .codex/storyboard-hook-run.txt
    foreach ($hintDir in @($hookRoot, (Join-Path $workspace ".codex"))) {
        $hintPath = Join-Path $hintDir "storyboard-hook-run.txt"
        if (Test-Path -LiteralPath $hintPath) {
            $hint = (Get-Content -LiteralPath $hintPath -Raw).Trim()
            if ($hint) {
                $candidate = if ([System.IO.Path]::IsPathRooted($hint)) { $hint } else { Join-Path $workspace $hint }
                if (Test-Path -LiteralPath $candidate) {
                    return (Resolve-Path -LiteralPath $candidate).Path
                }
            }
        }
    }

    $agentRuns = Join-Path $workspace "agent_runs"
    if (-not (Test-Path -LiteralPath $agentRuns)) {
        return $null
    }

    $latest = Get-ChildItem -LiteralPath $agentRuns -Directory |
        Where-Object { Test-Path -LiteralPath (Join-Path $_.FullName "manifest.json") } |
        Sort-Object LastWriteTimeUtc -Descending |
        Select-Object -First 1
    if ($null -eq $latest) {
        return $null
    }
    return $latest.FullName
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
$checkerOutput = & powershell -NoProfile -ExecutionPolicy Bypass -File $checker -RunDir $runDir -Json 2>&1
$checkerExit = $LASTEXITCODE
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
