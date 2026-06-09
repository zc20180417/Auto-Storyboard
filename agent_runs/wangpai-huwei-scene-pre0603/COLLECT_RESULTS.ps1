param(
    [switch]$ExportIndex
)

$ErrorActionPreference = 'Stop'
$cmdArgs = @(
    "H:\BaiduNetdiskDownload\Auto-Storyboard\storyboard_agent_workspace.py",
    "collect",
    "--run-dir",
    "H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\wangpai-huwei-scene-pre0603"
)
if ($ExportIndex) {
    $cmdArgs += "--export-index"
}
python @cmdArgs
