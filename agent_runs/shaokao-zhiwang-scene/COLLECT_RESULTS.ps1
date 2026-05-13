param(
    [switch]$ExportIndex
)

$ErrorActionPreference = 'Stop'
$cmdArgs = @(
    "G:\Auto-Storyboard\storyboard_agent_workspace.py",
    "collect",
    "--run-dir",
    "G:\Auto-Storyboard\agent_runs\shaokao-zhiwang-scene"
)
if ($ExportIndex) {
    $cmdArgs += "--export-index"
}
python @cmdArgs
