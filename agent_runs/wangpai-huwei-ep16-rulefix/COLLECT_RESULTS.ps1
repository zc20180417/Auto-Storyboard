param(
    [switch]$ExportIndex
)

$ErrorActionPreference = 'Stop'
$cmdArgs = @(
    "H:\BaiduNetdiskDownload\Auto-Storyboard\storyboard_agent_workspace.py",
    "collect",
    "--run-dir",
    "H:\BaiduNetdiskDownload\Auto-Storyboard\agent_runs\wangpai-huwei-ep16-rulefix"
)
if ($ExportIndex) {
    $cmdArgs += "--export-index"
}
python @cmdArgs
