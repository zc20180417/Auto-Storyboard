$ErrorActionPreference = "Stop"

$hookRoot = Split-Path -Parent $PSScriptRoot
$workspace = Split-Path -Parent $hookRoot
$logPath = Join-Path $hookRoot "storyboard-stop-check.jsonl"
$latestRunMaxAgeHours = 36

function Write-HookLog {
    param([hashtable]$Entry)
    $Entry.recorded_at = (Get-Date).ToUniversalTime().ToString("o")
    ($Entry | ConvertTo-Json -Compress -Depth 12) | Add-Content -LiteralPath $logPath -Encoding UTF8
}

function Read-HookPayload {
    $raw = [Console]::In.ReadToEnd()
    if ([string]::IsNullOrWhiteSpace($raw)) {
        return [pscustomobject]@{ hook_event_name = "unknown"; raw_input_empty = $true }
    }
    try {
        return $raw | ConvertFrom-Json
    } catch {
        Write-HookLog @{ event = "invalid_json"; result = "skip"; error = $_.Exception.Message; raw = $raw }
        return [pscustomobject]@{ hook_event_name = "unknown"; invalid_json = $true }
    }
}

function Get-RunDir {
    $hintPath = Join-Path $hookRoot "storyboard-hook-run.txt"
    if (Test-Path -LiteralPath $hintPath) {
        $hint = (Get-Content -LiteralPath $hintPath -Raw).Trim()
        if ($hint) {
            $candidate = if ([System.IO.Path]::IsPathRooted($hint)) { $hint } else { Join-Path $workspace $hint }
            return $candidate
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
    if ($latest.LastWriteTimeUtc -lt (Get-Date).ToUniversalTime().AddHours(-$latestRunMaxAgeHours)) {
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

$payload = Read-HookPayload
$runDir = Get-RunDir
if (-not $runDir) {
    Write-HookLog @{ event = $payload.hook_event_name; result = "skip"; reason = "no active recent agent run found" }
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
    Write-HookLog @{ event = $payload.hook_event_name; result = "pass"; run = $runDir; checker = $checkerResult }
    '{"continue":true}'
    exit 0
}

Write-HookLog @{ event = $payload.hook_event_name; result = "fail"; run = $runDir; checker = $checkerResult; raw = $checkerText }
$summary = Get-FailureSummary -Result $checkerResult

if ($payload.stop_hook_active -eq $true) {
    $message = "Auto-Storyboard run gate is still failing while the Stop hook is already active. Fix manually before final delivery.`n$summary"
    @{ continue = $true; systemMessage = $message } | ConvertTo-Json -Compress
    exit 0
}

$reason = "Auto-Storyboard run gate failed. Continue this thread by fixing the listed issues, rerunning per-episode validate, and collecting the run before summarizing.`n$summary"
@{ decision = "block"; reason = $reason } | ConvertTo-Json -Compress
exit 0
