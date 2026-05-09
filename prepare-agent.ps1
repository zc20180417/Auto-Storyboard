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
    [ValidateSet("codex", "qwen", "kimi")]
    [string]$Agent = "codex",
    [int]$Parallelism = 5,
    [string]$OutputModelSuffix = "agent-cli",
    [ValidateSet("vertical", "horizontal")]
    [string]$Aspect = "vertical",
    [ValidateSet("seedance", "happyhorse")]
    [string]$TargetVideoModel = "seedance",
    [switch]$Force
)

$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$env:PYTHONIOENCODING = "utf-8"
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
    throw "Prompt overrides are disabled by default. Use the aspect-specific mature agent_skills/*storyboard* generator SKILL.md, or pass -AllowPromptOverride if you intentionally need to rewrite that skill from a prompt file."
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
    "--aspect", $Aspect,
    "--target-video-model", $TargetVideoModel,
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
Write-Host "[prepare-agent] aspect=$Aspect"
Write-Host "[prepare-agent] target video model=$TargetVideoModel"
Write-Host "[prepare-agent] source=$Source"
if ($Prompt -and $AllowPromptOverride) {
    Write-Host "[prepare-agent] prompt override=$Prompt"
} else {
    if ($Aspect -eq "horizontal") {
        Write-Host "[prepare-agent] generation skill=agent_skills/storyboard-horizontal-generator/SKILL.md"
        Write-Host "[prepare-agent] review skill=agent_skills/storyboard-horizontal-reviewer/SKILL.md"
    } else {
        Write-Host "[prepare-agent] generation skill=agent_skills/storyboard-generator/SKILL.md"
        Write-Host "[prepare-agent] review skill=agent_skills/storyboard-reviewer/SKILL.md"
    }
}

python @cmdArgs
