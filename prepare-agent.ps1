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
    [ValidateSet("codex", "qwen", "kimi", "claude")]
    [string]$Agent = "codex",
    [int]$Parallelism = 5,
    [string]$OutputModelSuffix = "agent-cli",
    [ValidateSet("vertical", "horizontal")]
    [string]$Aspect = "vertical",
    [ValidateSet("live-action", "3d-cg")]
    [string]$VisualStyle = "live-action",
    [ValidateSet("seedance-2.0", "seedance-2.5-live-vertical")]
    [string]$VideoProfile = "seedance-2.0",
    [string]$VideoResolution = "",
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
    "--visual-style", $VisualStyle,
    "--video-profile", $VideoProfile,
    "--mode", $Mode
)

if ($VideoResolution) {
    $cmdArgs += @("--video-resolution", $VideoResolution)
}

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
Write-Host "[prepare-agent] visual style=$VisualStyle"
Write-Host "[prepare-agent] video profile=$VideoProfile"
if ($VideoResolution) {
    Write-Host "[prepare-agent] video resolution=$VideoResolution"
}
Write-Host "[prepare-agent] source=$Source"
if ($Prompt -and $AllowPromptOverride) {
    Write-Host "[prepare-agent] prompt override=$Prompt"
} else {
    if ($VideoProfile -eq "seedance-2.5-live-vertical") {
        Write-Host "[prepare-agent] video task=multimodal_generation (only; actual image/video/audio required)"
        Write-Host "[prepare-agent] generation skill=agent_skills/seedance-2-5-live-vertical-generator/SKILL.md"
        Write-Host "[prepare-agent] review skill=agent_skills/seedance-2-5-live-vertical-reviewer/SKILL.md"
        Write-Host "[prepare-agent] profile skill=agent_skills/seedance-2-5-live-vertical/SKILL.md"
    } elseif ($Aspect -eq "horizontal") {
        Write-Host "[prepare-agent] generation skill=agent_skills/storyboard-horizontal-generator/SKILL.md"
        Write-Host "[prepare-agent] review skill=agent_skills/storyboard-horizontal-reviewer/SKILL.md"
    } else {
        Write-Host "[prepare-agent] generation skill=agent_skills/storyboard-generator/SKILL.md"
        Write-Host "[prepare-agent] review skill=agent_skills/storyboard-reviewer/SKILL.md"
    }
}

python @cmdArgs
