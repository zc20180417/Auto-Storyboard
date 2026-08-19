# Claude Code SubagentStop hook: validate storyboard episodes after subagent completes.
# Mirrors .codex/hooks/subagent_validate_episode.ps1 logic for Claude Code's hook system.
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
    # Claude Code writes the hook payload as UTF-8. [Console]::In follows the console
    # input code page (GBK/936 on zh-CN Windows), which mangles multibyte characters in
    # last_assistant_message and breaks ConvertFrom-Json, silently skipping validation.
    # Read the raw stdin stream with an explicit UTF-8 decoder instead. Setting
    # [Console]::InputEncoding is avoided because it can throw when stdin is redirected.
    try {
        $stdinStream = [Console]::OpenStandardInput()
        $reader = New-Object System.IO.StreamReader($stdinStream, (New-Object System.Text.UTF8Encoding($false)))
        $raw = $reader.ReadToEnd()
        $reader.Dispose()
    } catch {
        $raw = [Console]::In.ReadToEnd()
    }
    if ([string]::IsNullOrWhiteSpace($raw)) {
        return [pscustomobject]@{ hook_event_name = "SubagentStop"; raw_input_empty = $true }
    }
    try {
        return $raw | ConvertFrom-Json
    } catch {
        Write-HookLog @{ event = "SubagentStop"; result = "skip"; error = $_.Exception.Message; raw = $raw.Substring(0, [Math]::Min(500, $raw.Length)) }
        return [pscustomobject]@{ hook_event_name = "SubagentStop"; invalid_json = $true }
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

function Get-AllStringValues {
    param([object]$Obj, [System.Collections.Generic.List[string]]$Accum)
    if ($null -eq $Obj) { return }
    if ($Obj -is [string]) {
        $Accum.Add($Obj) | Out-Null
        return
    }
    if ($Obj -is [System.Management.Automation.PSCustomObject]) {
        foreach ($prop in $Obj.PSObject.Properties) {
            Get-AllStringValues -Obj $prop.Value -Accum $Accum
        }
    } elseif ($Obj -is [array]) {
        foreach ($item in $Obj) {
            Get-AllStringValues -Obj $item -Accum $Accum
        }
    }
}

function Get-EpisodeDirsFromPayload {
    param([object]$Payload, [string]$RunDir)
    $found = [ordered]@{}

    # Collect all string values from the JSON payload
    $strings = New-Object System.Collections.Generic.List[string]
    Get-AllStringValues -Obj $Payload -Accum $strings
    $allText = $strings -join "`n"

    if ([string]::IsNullOrWhiteSpace($allText)) {
        return @()
    }

    $escapedRun = [regex]::Escape($RunDir)
    $patterns = @(
        "$escapedRun[\\/]+episodes[\\/]+(ep\d+)",
        "agent_runs[\\/]+[^\\/]+[\\/]+episodes[\\/]+(ep\d+)",
        "episodes[\\/]+(ep\d+)",
        "\b(ep\d{2,3})\b"
    )
    foreach ($pattern in $patterns) {
        foreach ($match in [regex]::Matches($allText, $pattern, [System.Text.RegularExpressions.RegexOptions]::IgnoreCase)) {
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

function Get-RecentlyModifiedEpisodes {
    param([string]$RunDir)
    $episodesDir = Join-Path $RunDir "episodes"
    if (-not (Test-Path -LiteralPath $episodesDir)) {
        return @()
    }
    # Return episodes that have review.txt (indicating work was done),
    # sorted by most recently modified
    return @(Get-ChildItem -LiteralPath $episodesDir -Directory |
        Where-Object {
            Test-Path -LiteralPath (Join-Path $_.FullName "review.txt")
        } |
        Sort-Object LastWriteTimeUtc -Descending |
        Select-Object -First 5 |
        ForEach-Object { $_.FullName })
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

# --- Main ---
$payload = Read-HookPayload
$runDir = Get-RunDir
if (-not $runDir) {
    Write-HookLog @{ event = "SubagentStop"; result = "skip"; reason = "no agent run found" }
    '{"continue":true}'
    exit 0
}

# Try to identify episode dirs from the hook payload
$episodeDirs = @(Get-EpisodeDirsFromPayload -Payload $payload -RunDir $runDir)

# Fallback: if payload didn't contain episode paths, use recently modified episodes
if ($episodeDirs.Count -eq 0) {
    $episodeDirs = @(Get-RecentlyModifiedEpisodes -RunDir $runDir)
}

if ($episodeDirs.Count -eq 0) {
    # Mirror Codex's gate: an active storyboard run exists but we could not tie this
    # subagent to any validated episode. Block once and ask for the episode_dir.
    # Loop guard: if the hook already fired and we still can't identify an episode,
    # this subagent is almost certainly not a storyboard worker -> downgrade to a
    # non-blocking warning so unrelated subagents are never trapped.
    if ($payload.stop_hook_active -eq $true) {
        Write-HookLog @{ event = "SubagentStop"; result = "warn"; run = $runDir; reason = "episode not identified (hook already active)" }
        @{ continue = $true; systemMessage = "SubagentStop could not identify a storyboard episode for this worker, and no episode output was validated. If this was a storyboard worker, its output was NOT gated." } | ConvertTo-Json -Compress
        exit 0
    }
    Write-HookLog @{ event = "SubagentStop"; result = "fail"; run = $runDir; reason = "episode not identified" }
    $reason = "SubagentStop could not identify which Auto-Storyboard episode this worker completed, and no validated episode output (review.txt) was found under the active run. If this subagent was a storyboard worker, state the exact episode_dir path and finish only that episode. If it was not a storyboard task, simply stop again to continue."
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
        event = "SubagentStop"
        result = "pass"
        run = $runDir
        episodes = @($episodeDirs | ForEach-Object { Split-Path -Leaf $_ })
    }
    '{"continue":true}'
    exit 0
}

Write-HookLog @{ event = "SubagentStop"; result = "fail"; run = $runDir; failures = $failures }
$summary = (($failures | ForEach-Object { "- $($_.episode): $($_.output)" }) -join "`n")
$reason = "Auto-Storyboard worker validation failed. Fix the listed episode output, rerun validate-episode, and stop again.`n$summary"
@{ decision = "block"; reason = $reason } | ConvertTo-Json -Compress
exit 0
