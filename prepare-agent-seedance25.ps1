param(
    [Parameter(Position = 0)]
    [ValidateSet("single", "scene")]
    [string]$Mode = "single",

    [Parameter(Position = 1)]
    [string]$RunName = "",

    [string]$Source = "",
    [string]$Prompt = "",
    [switch]$AllowPromptOverride,
    [string]$OutDir = ".\outputs_agent_seedance25",
    [string]$WorkspaceDir = ".\agent_runs",
    [ValidateSet("codex", "qwen", "kimi", "claude")]
    [string]$Agent = "codex",
    [int]$Parallelism = 5,
    [string]$OutputModelSuffix = "agent-cli",
    [ValidateSet("480p", "720p")]
    [string]$VideoResolution = "720p",
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
    Aspect = "vertical"
    VisualStyle = "live-action"
    VideoProfile = "seedance-2.5-live-vertical"
    VideoResolution = $VideoResolution
    Force = $Force
}

if ($Prompt) {
    $parameters.Prompt = $Prompt
    $parameters.AllowPromptOverride = $AllowPromptOverride
}

& $prepare @parameters
exit $LASTEXITCODE
