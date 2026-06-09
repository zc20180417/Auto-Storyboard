param(
    [string]$RunDir = "",
    [string]$WorkspaceRoot = "",
    [switch]$SkipValidate,
    [switch]$SkipSummary,
    [switch]$Json
)

$ErrorActionPreference = "Stop"

$toolRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
if (-not $WorkspaceRoot) {
    $WorkspaceRoot = Split-Path -Parent $toolRoot
}
$WorkspaceRoot = (Resolve-Path -LiteralPath $WorkspaceRoot).Path

$failures = New-Object System.Collections.Generic.List[string]

function Add-Failure {
    param([string]$Message)
    $script:failures.Add($Message) | Out-Null
}

function Read-JsonFile {
    param(
        [string]$Path,
        [string]$Label
    )
    if (-not (Test-Path -LiteralPath $Path)) {
        Add-Failure "$Label missing"
        return $null
    }

    try {
        return Get-Content -LiteralPath $Path -Raw -Encoding UTF8 | ConvertFrom-Json
    } catch {
        Add-Failure "$Label is not valid JSON: $($_.Exception.Message)"
        return $null
    }
}

function Get-JsonProperty {
    param(
        [object]$Object,
        [string]$Name
    )
    if ($null -eq $Object) {
        return $null
    }
    $property = $Object.PSObject.Properties[$Name]
    if ($null -eq $property) {
        return $null
    }
    return $property.Value
}

function Has-JsonProperty {
    param(
        [object]$Object,
        [string]$Name
    )
    if ($null -eq $Object) {
        return $false
    }
    return $null -ne $Object.PSObject.Properties[$Name]
}

function Get-ArrayCount {
    param([object]$Value)
    if ($null -eq $Value) {
        return 0
    }
    if ($Value -is [array]) {
        return $Value.Count
    }
    return 1
}

function Get-LatestRunDir {
    $agentRuns = Join-Path $WorkspaceRoot "agent_runs"
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

function Resolve-EpisodeDir {
    param(
        [object]$Episode,
        [string]$RunPath
    )

    $episodeId = [string](Get-JsonProperty $Episode "episode_id")
    $episodeDirValue = Get-JsonProperty $Episode "episode_dir"
    if ($episodeDirValue) {
        $candidate = [string]$episodeDirValue
        if (-not [System.IO.Path]::IsPathRooted($candidate)) {
            $candidate = Join-Path $RunPath $candidate
        }
        if (Test-Path -LiteralPath $candidate) {
            return $candidate
        }
        if ($episodeId) {
            $fallback = Join-Path (Join-Path $RunPath "episodes") $episodeId
            if (Test-Path -LiteralPath $fallback) {
                return $fallback
            }
        }
        return $candidate
    }

    if ($episodeId) {
        return Join-Path (Join-Path $RunPath "episodes") $episodeId
    }
    return $null
}

function Get-ExpectedReviewer {
    param(
        [object]$Episode,
        [object]$Status
    )
    foreach ($name in @("reviewer_source", "reviewer_skill_name")) {
        $value = Get-JsonProperty $Episode $name
        if ($value) {
            return [string]$value
        }
    }
    $statusReviewer = Get-JsonProperty $Status "reviewer_source"
    if ($statusReviewer) {
        return [string]$statusReviewer
    }
    return "storyboard-reviewer"
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

if (-not $RunDir) {
    foreach ($hintDir in @((Join-Path $WorkspaceRoot ".claude"), (Join-Path $WorkspaceRoot ".codex"))) {
        $hintPath = Join-Path $hintDir "storyboard-hook-run.txt"
        if (Test-Path -LiteralPath $hintPath) {
            $hint = (Get-Content -LiteralPath $hintPath -Raw).Trim()
            if ($hint) {
                $RunDir = if ([System.IO.Path]::IsPathRooted($hint)) { $hint } else { Join-Path $WorkspaceRoot $hint }
                break
            }
        }
    }
}

if (-not $RunDir) {
    $RunDir = Get-LatestRunDir
}

if (-not $RunDir -or -not (Test-Path -LiteralPath $RunDir)) {
    Add-Failure "agent run not found"
    $resolvedRunDir = $RunDir
} else {
    $resolvedRunDir = (Resolve-Path -LiteralPath $RunDir).Path
}

$episodesChecked = 0
if ($failures.Count -eq 0) {
    $manifestPath = Join-Path $resolvedRunDir "manifest.json"
    $manifest = Read-JsonFile -Path $manifestPath -Label "manifest.json"
    $episodes = @()
    if ($null -ne $manifest) {
        $episodesValue = Get-JsonProperty $manifest "episodes"
        $episodes = @($episodesValue)
        if ($episodes.Count -eq 0 -or ($episodes.Count -eq 1 -and $null -eq $episodes[0])) {
            Add-Failure "manifest.json episodes is empty"
            $episodes = @()
        }
    }

    foreach ($episode in $episodes) {
        $episodeId = [string](Get-JsonProperty $episode "episode_id")
        if (-not $episodeId) {
            $episodeId = "episode[$episodesChecked]"
        }
        $episodesChecked += 1
        $episodeDir = Resolve-EpisodeDir -Episode $episode -RunPath $resolvedRunDir
        if (-not $episodeDir -or -not (Test-Path -LiteralPath $episodeDir)) {
            Add-Failure "${episodeId}: episode directory missing"
            continue
        }
        $episodeDir = (Resolve-Path -LiteralPath $episodeDir).Path

        foreach ($name in @("final.txt", "review.txt", "status.json")) {
            if (-not (Test-Path -LiteralPath (Join-Path $episodeDir $name))) {
                Add-Failure "${episodeId}: missing $name"
            }
        }

        $statusPath = Join-Path $episodeDir "status.json"
        $reviewPath = Join-Path $episodeDir "review.txt"
        $status = $null
        $review = $null
        if (Test-Path -LiteralPath $statusPath) {
            $status = Read-JsonFile -Path $statusPath -Label "${episodeId}: status.json"
        }
        if (Test-Path -LiteralPath $reviewPath) {
            $review = Read-JsonFile -Path $reviewPath -Label "${episodeId}: review.txt"
        }

        $expectedReviewer = Get-ExpectedReviewer -Episode $episode -Status $status
        if ($null -ne $status) {
            $statusValue = [string](Get-JsonProperty $status "status")
            if ($statusValue -ne "done") {
                Add-Failure "${episodeId}: status.json status must be done (was '$statusValue')"
            }
            if ([string](Get-JsonProperty $status "reviewer_source") -ne $expectedReviewer) {
                Add-Failure "${episodeId}: status.json reviewer_source must be $expectedReviewer"
            }
            if ((Get-JsonProperty $status "reviewer_pass") -ne $true) {
                Add-Failure "${episodeId}: status.json reviewer_pass must be true"
            }
            if ((Get-JsonProperty $status "reviewer_issues_count") -ne 0) {
                Add-Failure "${episodeId}: status.json reviewer_issues_count must be 0"
            }
            if (-not (Has-JsonProperty -Object $status -Name "reviewer_warnings_count")) {
                Add-Failure "${episodeId}: status.json missing reviewer_warnings_count"
            }
        }

        if ($null -ne $review) {
            if ((Get-JsonProperty $review "pass") -ne $true) {
                Add-Failure "${episodeId}: review.txt pass must be true"
            }
            if (-not (Has-JsonProperty -Object $review -Name "issues")) {
                Add-Failure "${episodeId}: review.txt missing issues array"
            } elseif ((Get-ArrayCount (Get-JsonProperty $review "issues")) -ne 0) {
                Add-Failure "${episodeId}: review.txt issues must be empty"
            }
            if (-not (Has-JsonProperty -Object $review -Name "warnings")) {
                Add-Failure "${episodeId}: review.txt missing warnings array"
            }

            if ($null -ne $status) {
                $reviewWarningsCount = Get-ArrayCount (Get-JsonProperty $review "warnings")
                if ((Get-JsonProperty $status "reviewer_warnings_count") -ne $reviewWarningsCount) {
                    Add-Failure "${episodeId}: status.json reviewer_warnings_count does not match review.txt warnings"
                }
            }
        }

        if (-not $SkipValidate) {
            $validationOutput = & python (Join-Path $WorkspaceRoot "storyboard_agent_workspace.py") validate-episode --episode-dir $episodeDir 2>&1
            $validationExit = $LASTEXITCODE
            if ($validationExit -ne 0) {
                Add-Failure "${episodeId}: validate-episode failed: $(Get-TailText -Lines $validationOutput)"
            }
        }
    }

    if (-not $SkipSummary) {
        $summaryPath = Join-Path $resolvedRunDir "SUMMARY.md"
        if (-not (Test-Path -LiteralPath $summaryPath)) {
            Add-Failure "SUMMARY.md missing; run collect-agent.ps1 before final delivery"
        } else {
            $summary = Get-Content -LiteralPath $summaryPath -Raw -Encoding UTF8
            if ($summary -match "Validation/collection failures:\s*([0-9]+)") {
                $failureCount = [int]$matches[1]
                if ($failureCount -ne 0) {
                    Add-Failure "SUMMARY.md reports Validation/collection failures: $failureCount"
                }
            } else {
                Add-Failure "SUMMARY.md missing Validation/collection failures line"
            }

            if ($summary -match "Copied:\s*([0-9]+)") {
                $copiedCount = [int]$matches[1]
                if ($copiedCount -ne $episodes.Count) {
                    Add-Failure "SUMMARY.md copied count $copiedCount does not match manifest episode count $($episodes.Count)"
                }
            } else {
                Add-Failure "SUMMARY.md missing Copied line"
            }
        }
    }
}

$ok = $failures.Count -eq 0
$result = [ordered]@{
    ok = $ok
    run = $resolvedRunDir
    episodes_checked = $episodesChecked
    skipped_validation = [bool]$SkipValidate
    skipped_summary = [bool]$SkipSummary
    failures = @($failures)
    checked_at = (Get-Date).ToUniversalTime().ToString("o")
}

if ($Json) {
    $result | ConvertTo-Json -Compress -Depth 12
} else {
    if ($ok) {
        Write-Host "[pass] $episodesChecked episode(s) checked: $resolvedRunDir"
    } else {
        Write-Host "[fail] agent run gate found $($failures.Count) issue(s): $resolvedRunDir"
        foreach ($failure in $failures) {
            Write-Host "- $failure"
        }
    }
}

if ($ok) {
    exit 0
}
exit 1
