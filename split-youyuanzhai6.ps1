param(
    [string]$Source = "",
    [string]$OutDir = ".\split_scripts\youyuanzhai-6"
)

$ErrorActionPreference = "Stop"
Set-Location -LiteralPath $PSScriptRoot

if ($Source) {
    python ".\split_youyuanzhai6.py" --source $Source --out-dir $OutDir
} else {
    python ".\split_youyuanzhai6.py" --out-dir $OutDir
}
