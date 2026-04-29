param(
    [string]$Source = "",
    [string]$OutDir = ".\split_scripts\cangnan-fengyun"
)

$ErrorActionPreference = "Stop"
Set-Location -LiteralPath $PSScriptRoot

if ($Source) {
    python ".\split_cangnan_fengyun.py" --source $Source --out-dir $OutDir
} else {
    python ".\split_cangnan_fengyun.py" --out-dir $OutDir
}
