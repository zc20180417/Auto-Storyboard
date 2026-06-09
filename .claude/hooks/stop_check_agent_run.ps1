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
    $raw = [Console]::In.ReadToEnd()
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
