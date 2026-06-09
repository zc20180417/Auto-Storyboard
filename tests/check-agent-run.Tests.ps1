$ErrorActionPreference = "Stop"

$RepoRoot = Resolve-Path -LiteralPath (Join-Path $PSScriptRoot "..")
$Checker = Join-Path $RepoRoot "tools\check-agent-run.ps1"

function New-CheckerFixtureRun {
    param(
        [int]$EpisodeCount = 2,
        [int]$SummaryFailures = 0
    )

    $root = Join-Path ([System.IO.Path]::GetTempPath()) ("auto-storyboard-check-" + [guid]::NewGuid().ToString("N"))
    $runDir = Join-Path $root "agent_runs\fixture-run"
    $outDir = Join-Path $root "outputs_agent_fixture"
    $episodesRoot = Join-Path $runDir "episodes"
    New-Item -ItemType Directory -Force -Path $episodesRoot, $outDir | Out-Null

    $episodes = @()
    for ($i = 1; $i -le $EpisodeCount; $i++) {
        $episodeId = "ep{0:D2}" -f $i
        $episodeDir = Join-Path $episodesRoot $episodeId
        New-Item -ItemType Directory -Force -Path $episodeDir | Out-Null

        Set-Content -LiteralPath (Join-Path $episodeDir "final.txt") -Encoding UTF8 -Value "fixture final $episodeId"
        @{
            reviewer_source = "storyboard-reviewer"
            pass = $true
            issues = @()
            warnings = @()
        } | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath (Join-Path $episodeDir "review.txt") -Encoding UTF8
        @{
            status = "done"
            reviewer_source = "storyboard-reviewer"
            reviewer_pass = $true
            reviewer_issues_count = 0
            reviewer_warnings_count = 0
        } | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath (Join-Path $episodeDir "status.json") -Encoding UTF8
        @{
            reviewer_source = "storyboard-reviewer"
        } | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath (Join-Path $episodeDir "episode.json") -Encoding UTF8

        $outputPath = Join-Path $outDir ("fixture-$episodeId.txt")
        $episodes += [ordered]@{
            episode_id = $episodeId
            display_name = "Fixture $episodeId"
            episode_dir = $episodeDir
            output_path = $outputPath
            reviewer_source = "storyboard-reviewer"
            reviewer_skill_name = "storyboard-reviewer"
        }
    }

    @{
        version = 1
        run_id = "fixture-run"
        project_root = $root
        out_dir = $outDir
        mode = "scene"
        episodes = $episodes
    } | ConvertTo-Json -Depth 20 | Set-Content -LiteralPath (Join-Path $runDir "manifest.json") -Encoding UTF8

    $summary = @(
        "# Agent Run Summary",
        "",
        "Copied: $EpisodeCount",
        "Validation/collection failures: $SummaryFailures"
    )
    Set-Content -LiteralPath (Join-Path $runDir "SUMMARY.md") -Encoding UTF8 -Value $summary

    [pscustomobject]@{
        Root = $root
        RunDir = $runDir
        EpisodesRoot = $episodesRoot
    }
}

function Invoke-CheckerJson {
    param([string]$RunDir)

    $output = & powershell -NoProfile -ExecutionPolicy Bypass -File $Checker -RunDir $RunDir -SkipValidate -Json 2>&1
    $text = ($output | Out-String).Trim()
    $parsed = $null
    try {
        if ($text) {
            $parsed = $text | ConvertFrom-Json
        }
    } catch {
        $parsed = $null
    }

    [pscustomobject]@{
        ExitCode = $LASTEXITCODE
        Text = $text
        Json = $parsed
    }
}

Describe "check-agent-run.ps1" {
    It "passes a complete collected run" {
        $fixture = New-CheckerFixtureRun
        try {
            $result = Invoke-CheckerJson -RunDir $fixture.RunDir

            $result.ExitCode | Should Be 0
            $result.Json.ok | Should Be $true
            $result.Json.episodes_checked | Should Be 2
            $result.Json.failures.Count | Should Be 0
        } finally {
            Remove-Item -LiteralPath $fixture.Root -Recurse -Force
        }
    }

    It "fails before validation when an episode artifact is missing" {
        $fixture = New-CheckerFixtureRun
        try {
            Remove-Item -LiteralPath (Join-Path $fixture.EpisodesRoot "ep02\status.json") -Force

            $result = Invoke-CheckerJson -RunDir $fixture.RunDir

            $result.ExitCode | Should Be 1
            $result.Json.ok | Should Be $false
            ($result.Json.failures -join "`n") | Should Match "ep02.*missing status.json"
        } finally {
            Remove-Item -LiteralPath $fixture.Root -Recurse -Force
        }
    }

    It "falls back to current run episodes when manifest paths are stale absolute paths" {
        $fixture = New-CheckerFixtureRun
        try {
            $manifestPath = Join-Path $fixture.RunDir "manifest.json"
            $manifest = Get-Content -LiteralPath $manifestPath -Raw -Encoding UTF8 | ConvertFrom-Json
            foreach ($episode in @($manifest.episodes)) {
                $episode.episode_dir = "Z:\old-workspace\agent_runs\fixture-run\episodes\$($episode.episode_id)"
            }
            $manifest | ConvertTo-Json -Depth 20 | Set-Content -LiteralPath $manifestPath -Encoding UTF8

            $result = Invoke-CheckerJson -RunDir $fixture.RunDir

            $result.ExitCode | Should Be 0
            $result.Json.ok | Should Be $true
            $result.Json.episodes_checked | Should Be 2
        } finally {
            Remove-Item -LiteralPath $fixture.Root -Recurse -Force
        }
    }

    It "fails when the collection summary reports failures" {
        $fixture = New-CheckerFixtureRun -SummaryFailures 1
        try {
            $result = Invoke-CheckerJson -RunDir $fixture.RunDir

            $result.ExitCode | Should Be 1
            $result.Json.ok | Should Be $false
            ($result.Json.failures -join "`n") | Should Match "Validation/collection failures: 1"
        } finally {
            Remove-Item -LiteralPath $fixture.Root -Recurse -Force
        }
    }
}
