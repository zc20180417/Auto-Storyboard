<#
.SYNOPSIS
    Split 《撕通知书后我卖凉皮暴富》 script into per-episode files for scene mode.
#>
param(
    [string]$Source = ".\inputs\《撕通知书后我卖凉皮暴富》卡6付7.txt",
    [string]$OutDir = ".\split_scripts\shutongzhishu"
)

$ErrorActionPreference = "Stop"
Set-Location -LiteralPath $PSScriptRoot

python ".\split_shutongzhishu.py" --source $Source --out-dir $OutDir
