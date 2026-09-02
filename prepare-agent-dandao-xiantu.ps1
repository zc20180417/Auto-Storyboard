param(
    [Parameter(Position = 0)]
    [ValidateSet("single")]
    [string]$Mode = "single",

    [Parameter(Position = 1)]
    [string]$RunName = "",

    [string]$Source = "",
    [string]$Prompt = "",
    [switch]$AllowPromptOverride,
    [string]$OutDir = ".\outputs_agent_dandao_xiantu",
    [string]$WorkspaceDir = ".\agent_runs",
    [ValidateSet("codex", "qwen", "kimi", "claude")]
    [string]$Agent = "codex",
    [int]$Parallelism = 5,
    [string]$OutputModelSuffix = "agent-cli",
    [switch]$Force
)

$ErrorActionPreference = "Stop"
$prepare = Join-Path $PSScriptRoot "prepare-agent.ps1"
$parameters = @{
    Mode = $Mode
    RunName = $RunName
    Source = $Source
    OutDir = $OutDir
    WorkspaceDir = $WorkspaceDir
    Agent = $Agent
    Parallelism = $Parallelism
    OutputModelSuffix = $OutputModelSuffix
    Aspect = "horizontal"
    VisualStyle = "3d-cg"
    VideoProfile = "seedance-2.5-horizontal-xianxia-3d-cg"
    VideoResolution = "720p"
    VisualStylePreset = "realistic-material-restrained-anime-outline"
    ProjectPackId = "dandao-xiantu"
    Force = $Force
}

if ($Prompt) {
    $parameters.Prompt = $Prompt
    $parameters.AllowPromptOverride = $AllowPromptOverride
}

& $prepare @parameters
exit $LASTEXITCODE
