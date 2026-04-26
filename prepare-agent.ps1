param(
    [Parameter(Position = 0)]
    [ValidateSet("single", "scene")]
    [string]$Mode = "single",

    [Parameter(Position = 1)]
    [string]$RunName = "",

    [string]$Source = "",
    [string]$Prompt = "",
    [string]$OutDir = ".\outputs_agent_6688_clean",
    [string]$WorkspaceDir = ".\agent_runs",
    [ValidateSet("codex", "qwen")]
    [string]$Agent = "codex",
    [int]$Parallelism = 5,
    [string]$OutputModelSuffix = "agent-cli",
    [switch]$Force
)

$ErrorActionPreference = "Stop"
Set-Location -LiteralPath $PSScriptRoot

if (-not $Source) {
    $sourceFile = Get-ChildItem -LiteralPath . -Filter "*.docx" -File |
        Sort-Object LastWriteTime -Descending |
        Select-Object -First 1
    if (-not $sourceFile) {
        throw "No .docx source found in $PSScriptRoot. Pass -Source explicitly."
    }
    $Source = $sourceFile.FullName
}

if (-not $Prompt) {
    $promptFile = Get-ChildItem -LiteralPath . -Filter "6688*prompt*.txt" -File |
        Sort-Object LastWriteTime -Descending |
        Select-Object -First 1
    if (-not $promptFile) {
        $promptFile = Get-ChildItem -LiteralPath . -Filter "*prompt*.txt" -File |
            Sort-Object LastWriteTime -Descending |
            Select-Object -First 1
    }
    if (-not $promptFile) {
        throw "No *prompt*.txt found in $PSScriptRoot. Pass -Prompt explicitly."
    }
    $Prompt = $promptFile.FullName
}

$cmdArgs = @(
    ".\storyboard_agent_workspace.py",
    "prepare",
    "--source", $Source,
    "--prompt", $Prompt,
    "--out-dir", $OutDir,
    "--workspace-dir", $WorkspaceDir,
    "--agent", $Agent,
    "--parallelism", "$Parallelism",
    "--output-model-suffix", $OutputModelSuffix,
    "--mode", $Mode
)

if ($RunName) {
    $cmdArgs += @("--run-name", $RunName)
}

if ($Force) {
    $cmdArgs += "--force"
}

Write-Host "[prepare-agent] mode=$Mode"
Write-Host "[prepare-agent] source=$Source"
Write-Host "[prepare-agent] prompt=$Prompt"

python @cmdArgs
