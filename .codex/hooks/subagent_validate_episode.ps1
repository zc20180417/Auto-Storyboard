$ErrorActionPreference = "Stop"

$hookRoot = Split-Path -Parent $PSScriptRoot
$workspace = Split-Path -Parent $hookRoot
$logPath = Join-Path $hookRoot "storyboard-subagent-validate.jsonl"

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
            if (Test-Path -LiteralPath $candidate) {
                return (Resolve-Path -LiteralPath $candidate).Path
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

function Get-LastAssistantText {
    param([object]$Payload)
    if ($Payload.last_assistant_message) {
        return [string]$Payload.last_assistant_message
    }
    return ""
}

function Get-TranscriptText {
    param([object]$Payload)
    if ($Payload.agent_transcript_path -and (Test-Path -LiteralPath $Payload.agent_transcript_path)) {
        return Get-Content -LiteralPath $Payload.agent_transcript_path -Raw -Encoding UTF8
    }
    return ""
}

function Get-EpisodeDirsFromText {
    param(
        [string]$Text,
        [string]$RunDir,
        [switch]$AllowStandaloneEpisodeId
    )
    $found = [ordered]@{}
    if ([string]::IsNullOrWhiteSpace($Text)) {
        return @()
    }

    $escapedRun = [regex]::Escape($RunDir)
    $patterns = @(
        "$escapedRun[\\/]+episodes[\\/]+(ep\d+)",
        "agent_runs[\\/]+[^\\/]+[\\/]+episodes[\\/]+(ep\d+)",
        "episodes[\\/]+(ep\d+)"
    )
    if ($AllowStandaloneEpisodeId) {
        $patterns += "\b(ep\d{2,3})\b"
    }
    foreach ($pattern in $patterns) {
        foreach ($match in [regex]::Matches($Text, $pattern, [System.Text.RegularExpressions.RegexOptions]::IgnoreCase)) {
            $episodeId = $match.Groups[1].Value
            $candidate = Join-Path (Join-Path $RunDir "episodes") $episodeId
            if (Test-Path -LiteralPath $candidate) {
                $resolved = (Resolve-Path -LiteralPath $candidate).Path
                $found[$resolved.ToLowerInvariant()] = $resolved
            }
        }
    }
    return @($found.Values)
}

function Get-TailText {
    param([object[]]$Lines)
    $text = (($Lines | Out-String).Trim())
    if (-not $text) {
        return "no output"
    }
    $split = $text -split "`r?`n"
    return (($split | Select-Object -Last 6) -join " / ")
}

$payload = Read-HookPayload
$runDir = Get-RunDir
if (-not $runDir) {
    Write-HookLog @{ event = $payload.hook_event_name; result = "skip"; reason = "no agent run found" }
    '{"continue":true}'
    exit 0
}

$lastAssistantText = Get-LastAssistantText -Payload $payload
$transcriptText = Get-TranscriptText -Payload $payload
$episodeDirs = @(Get-EpisodeDirsFromText -Text ($lastAssistantText + "`n" + $transcriptText) -RunDir $runDir)
if ($episodeDirs.Count -eq 0) {
    $episodeDirs = @(Get-EpisodeDirsFromText -Text $lastAssistantText -RunDir $runDir -AllowStandaloneEpisodeId)
}
if ($episodeDirs.Count -eq 0) {
    Write-HookLog @{ event = $payload.hook_event_name; result = "fail"; run = $runDir; reason = "episode not identified" }
    $reason = "SubagentStop could not identify which Auto-Storyboard episode this worker completed. Continue by stating the exact episode_dir path, then finish only that episode."
    @{ decision = "block"; reason = $reason } | ConvertTo-Json -Compress
    exit 0
}

$failures = @()
foreach ($episodeDir in $episodeDirs) {
    $output = & python (Join-Path $workspace "storyboard_agent_workspace.py") validate-episode --episode-dir $episodeDir 2>&1
    $exitCode = $LASTEXITCODE
    if ($exitCode -ne 0) {
        $failures += [ordered]@{
            episode = Split-Path -Leaf $episodeDir
            episode_dir = $episodeDir
            output = Get-TailText -Lines $output
        }
    }
}

if ($failures.Count -eq 0) {
    Write-HookLog @{
        event = $payload.hook_event_name
        result = "pass"
        run = $runDir
        episodes = @($episodeDirs | ForEach-Object { Split-Path -Leaf $_ })
    }
    '{"continue":true}'
    exit 0
}

Write-HookLog @{ event = $payload.hook_event_name; result = "fail"; run = $runDir; failures = $failures }
$summary = (($failures | ForEach-Object { "- $($_.episode): $($_.output)" }) -join "`n")
$reason = "Auto-Storyboard worker validation failed. Continue in the same worker context, fix only the listed episode output, rerun validate-episode, and stop again.`n$summary"
@{ decision = "block"; reason = $reason } | ConvertTo-Json -Compress
exit 0
