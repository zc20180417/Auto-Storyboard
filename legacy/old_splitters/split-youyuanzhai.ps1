param(
    [string]$Source = "",
    [string]$OutDir = ".\split_scripts\youyuanzhai"
)

$ErrorActionPreference = "Stop"
Set-Location -LiteralPath $PSScriptRoot

if (-not $Source) {
    $sourceFile = Get-ChildItem -LiteralPath ".\inputs" -Filter "*.txt" -File |
        Sort-Object Length -Descending |
        Select-Object -First 1
    if (-not $sourceFile) {
        throw "No txt source found under .\inputs. Pass -Source explicitly."
    }
    $Source = $sourceFile.FullName
}

python ".\split_youyuanzhai.py" --source $Source --out-dir $OutDir
