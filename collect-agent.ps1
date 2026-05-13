param(
    [Parameter(Position = 0)]
    [string]$RunDir = "",

    [string]$OutDir = "",

    [switch]$ExportIndex
)

$ErrorActionPreference = "Stop"
Set-Location -LiteralPath $PSScriptRoot

if (-not $RunDir) {
    $latestRun = Get-ChildItem -LiteralPath ".\agent_runs" -Directory |
        Sort-Object LastWriteTime -Descending |
        Select-Object -First 1
    if (-not $latestRun) {
        throw "No agent run found under .\agent_runs. Pass RunDir explicitly."
    }
    $RunDir = $latestRun.FullName
}

$cmdArgs = @(
    ".\storyboard_agent_workspace.py",
    "collect",
    "--run-dir", $RunDir
)

if ($OutDir) {
    $cmdArgs += @("--out-dir", $OutDir)
}

if ($ExportIndex) {
    $cmdArgs += "--export-index"
}

Write-Host "[collect-agent] run=$RunDir"
python @cmdArgs
exit $LASTEXITCODE
