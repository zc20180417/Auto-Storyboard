param(
    [Parameter(Position = 0)]
    [ValidateSet("single", "scene")]
    [string]$Mode = "single",

    [Parameter(Position = 1)]
    [string]$RunName = "",

    [string]$Source = "",
    [string]$Prompt = "",
    [switch]$AllowPromptOverride,
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

if ($Prompt -and -not $AllowPromptOverride) {
    throw "Prompt overrides are disabled by default. Use the mature agent_skills/storyboard-generator/SKILL.md, or pass -AllowPromptOverride if you intentionally need to rewrite that skill from a prompt file."
}

$cmdArgs = @(
    ".\storyboard_agent_workspace.py",
    "prepare",
    "--source", $Source,
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

if ($Prompt -and $AllowPromptOverride) {
    $cmdArgs += @("--prompt", $Prompt)
}

if ($Force) {
    $cmdArgs += "--force"
}

Write-Host "[prepare-agent] mode=$Mode"
Write-Host "[prepare-agent] source=$Source"
if ($Prompt -and $AllowPromptOverride) {
    Write-Host "[prepare-agent] prompt override=$Prompt"
} else {
    Write-Host "[prepare-agent] generation skill=agent_skills/storyboard-generator/SKILL.md"
}

python @cmdArgs
