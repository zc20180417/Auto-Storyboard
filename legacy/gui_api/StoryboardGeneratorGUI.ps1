param(
    [switch]$SmokeTest,
    [string]$BatchConfigPath
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing
Add-Type -AssemblyName System.IO.Compression.FileSystem

$script:DefaultApiBase = 'https://api.deepseek.com'
$script:DefaultModel = 'deepseek-chat'
$script:DefaultPromptGlob = '*prompt*.txt'
$script:SystemPromptHint = '下面是完整剧本。请严格遵守系统提示词中的全部规则，直接输出最终分镜提示词，不要解释，不要省略。'

function Convert-ChineseNumeralToInt {
    param([string]$Value)

    if ([string]::IsNullOrWhiteSpace($Value)) {
        return $null
    }

    if ($Value -match '^\d+$') {
        return [int]$Value
    }

    $map = @{
        '零' = 0
        '〇' = 0
        '一' = 1
        '二' = 2
        '两' = 2
        '三' = 3
        '四' = 4
        '五' = 5
        '六' = 6
        '七' = 7
        '八' = 8
        '九' = 9
    }

    if ($Value -eq '十') {
        return 10
    }

    if ($Value.Contains('十')) {
        $parts = $Value.Split('十', 2)
        $left = $parts[0]
        $right = $parts[1]
        $tens = if ([string]::IsNullOrEmpty($left)) { 1 } else { $map[$left] }
        $ones = if ([string]::IsNullOrEmpty($right)) { 0 } else { $map[$right] }
        if ($null -eq $tens -or $null -eq $ones) {
            return $null
        }
        return ($tens * 10 + $ones)
    }

    $total = 0
    foreach ($char in $Value.ToCharArray()) {
        $digit = $map[[string]$char]
        if ($null -eq $digit) {
            return $null
        }
        $total = $total * 10 + $digit
    }
    return $total
}

function Get-EpisodeNumber {
    param(
        [string]$Text,
        [string]$FallbackName
    )

    $sources = @($Text.Substring(0, [Math]::Min($Text.Length, 200)), $FallbackName)
    $patterns = @(
        '第\s*(\d+)\s*集',
        '第\s*([零〇一二两三四五六七八九十]+)\s*集'
    )

    foreach ($source in $sources) {
        foreach ($pattern in $patterns) {
            $match = [regex]::Match($source, $pattern)
            if ($match.Success) {
                $value = Convert-ChineseNumeralToInt -Value $match.Groups[1].Value
                if ($null -ne $value) {
                    return $value
                }
            }
        }
    }

    return $null
}

function Get-PromptFile {
    param(
        [string]$ProjectFolder,
        [string]$ExplicitPath
    )

    if (-not [string]::IsNullOrWhiteSpace($ExplicitPath)) {
        if (-not (Test-Path -LiteralPath $ExplicitPath -PathType Leaf)) {
            throw "提示词文件不存在：$ExplicitPath"
        }
        return (Resolve-Path -LiteralPath $ExplicitPath).Path
    }

    $matches = Get-ChildItem -LiteralPath $ProjectFolder -Filter $script:DefaultPromptGlob -File | Sort-Object Name
    if (-not $matches) {
        throw "在 $ProjectFolder 下没有找到提示词文件（$($script:DefaultPromptGlob)）。"
    }

    return $matches[0].FullName
}

function Get-SettingOrDefault {
    param(
        [hashtable]$Settings,
        [string]$Name,
        $DefaultValue
    )

    if ($Settings.ContainsKey($Name) -and $null -ne $Settings[$Name]) {
        return $Settings[$Name]
    }

    return $DefaultValue
}

function Protect-LocalSecret {
    param([string]$PlainText)

    if ([string]::IsNullOrWhiteSpace($PlainText)) {
        return ''
    }

    $secureString = ConvertTo-SecureString -String $PlainText -AsPlainText -Force
    return ConvertFrom-SecureString -SecureString $secureString
}

function Unprotect-LocalSecret {
    param([string]$CipherText)

    if ([string]::IsNullOrWhiteSpace($CipherText)) {
        return ''
    }

    try {
        $secureString = ConvertTo-SecureString -String $CipherText
        $bstr = [Runtime.InteropServices.Marshal]::SecureStringToBSTR($secureString)
        try {
            return [Runtime.InteropServices.Marshal]::PtrToStringBSTR($bstr)
        }
        finally {
            if ($bstr -ne [IntPtr]::Zero) {
                [Runtime.InteropServices.Marshal]::ZeroFreeBSTR($bstr)
            }
        }
    }
    catch {
        return ''
    }
}

function Get-DocxText {
    param([string]$Path)

    try {
        $archive = [System.IO.Compression.ZipFile]::OpenRead($Path)
    }
    catch [System.IO.IOException] {
        throw "剧本文件正在被其他程序占用，请先关闭后重试：$Path"
    }
    try {
        $entry = $archive.GetEntry('word/document.xml')
        if ($null -eq $entry) {
            throw "DOCX 文件缺少 word/document.xml：$Path"
        }

        $stream = $entry.Open()
        try {
            $reader = New-Object System.IO.StreamReader($stream, [System.Text.Encoding]::UTF8)
            try {
                $xmlText = $reader.ReadToEnd()
            }
            finally {
                $reader.Dispose()
            }
        }
        finally {
            $stream.Dispose()
        }
    }
    finally {
        $archive.Dispose()
    }

    [xml]$xml = $xmlText
    $ns = New-Object System.Xml.XmlNamespaceManager($xml.NameTable)
    $ns.AddNamespace('w', 'http://schemas.openxmlformats.org/wordprocessingml/2006/main')

    $lines = New-Object 'System.Collections.Generic.List[string]'
    $paragraphs = $xml.SelectNodes('//w:p', $ns)
    foreach ($paragraph in $paragraphs) {
        $texts = $paragraph.SelectNodes('.//w:t', $ns)
        if ($null -eq $texts -or $texts.Count -eq 0) {
            continue
        }

        $builder = New-Object System.Text.StringBuilder
        foreach ($node in $texts) {
            [void]$builder.Append($node.InnerText)
        }

        $line = $builder.ToString().Replace([string][char]0xA0, ' ').Trim()
        if (-not [string]::IsNullOrWhiteSpace($line)) {
            [void]$lines.Add($line)
        }
    }

    return ($lines -join "`n")
}

function Get-EpisodeInputs {
    param([string]$ProjectFolder)

    $files = Get-ChildItem -LiteralPath $ProjectFolder -Filter '*.docx' -File |
        Where-Object { -not $_.Name.StartsWith('~$') } |
        Sort-Object Name

    $episodes = New-Object 'System.Collections.Generic.List[object]'
    foreach ($file in $files) {
        $scriptText = Get-DocxText -Path $file.FullName
        $episodeNumber = Get-EpisodeNumber -Text $scriptText -FallbackName $file.BaseName
        $episodes.Add([pscustomobject]@{
                SourcePath    = $file.FullName
                DisplayName   = $file.BaseName
                EpisodeNumber = $episodeNumber
                ScriptText    = $scriptText
                CharCount     = $scriptText.Length
            })
    }

    return $episodes.ToArray()
}

function Get-OutputFileName {
    param(
        [pscustomobject]$Episode,
        [int]$SequenceIndex
    )

    $episodeNumber = if ($null -ne $Episode.EpisodeNumber) { [int]$Episode.EpisodeNumber } else { $SequenceIndex }
    return ('ep{0:d2}-storyboard.txt' -f $episodeNumber)
}

function New-UserMessage {
    param([pscustomobject]$Episode)

    return @(
        $script:SystemPromptHint
        ''
        "剧本文件：$([System.IO.Path]::GetFileName($Episode.SourcePath))"
        "剧本标题：$($Episode.DisplayName)"
        ''
        $Episode.ScriptText
    ) -join "`n"
}

function Invoke-DeepSeekCompletion {
    param(
        [string]$ApiBase,
        [string]$ApiKey,
        [string]$Model,
        [bool]$ThinkingEnabled,
        [string]$PromptText,
        [pscustomobject]$Episode,
        [double]$Temperature,
        [int]$TimeoutSeconds,
        [int]$MaxTokens,
        [int]$MaxRetries
    )

    $uri = $ApiBase.TrimEnd('/') + '/chat/completions'
    $payload = @{
        model       = $Model
        messages    = @(
            @{ role = 'system'; content = $PromptText }
            @{ role = 'user'; content = (New-UserMessage -Episode $Episode) }
        )
        temperature = $Temperature
        max_tokens  = $MaxTokens
        stream      = $false
    }

    if ($ThinkingEnabled) {
        $payload.thinking = @{
            type = 'enabled'
        }
    }

    $jsonBody = $payload | ConvertTo-Json -Depth 8
    $headers = @{
        Authorization = "Bearer $ApiKey"
    }

    for ($attempt = 1; $attempt -le $MaxRetries; $attempt++) {
        try {
            return Invoke-RestMethod -Method Post -Uri $uri -Headers $headers -ContentType 'application/json; charset=utf-8' -Body $jsonBody -TimeoutSec $TimeoutSeconds
        }
        catch {
            $statusCode = $null
            $responseBody = $null

            if ($_.Exception.Response) {
                try {
                    $statusCode = [int]$_.Exception.Response.StatusCode
                }
                catch {
                    try {
                        $statusCode = [int]$_.Exception.Response.StatusCode.value__
                    }
                    catch {
                        $statusCode = $null
                    }
                }

                try {
                    $stream = $_.Exception.Response.GetResponseStream()
                    if ($stream) {
                        $reader = New-Object System.IO.StreamReader($stream)
                        try {
                            $responseBody = $reader.ReadToEnd()
                        }
                        finally {
                            $reader.Dispose()
                        }
                    }
                }
                catch {
                    $responseBody = $null
                }
            }

            if (($statusCode -in 429, 500, 503) -and $attempt -lt $MaxRetries) {
                $sleepSeconds = 3 * $attempt
                Write-Output "[warn] HTTP $statusCode，$sleepSeconds 秒后重试（$attempt/$MaxRetries）..."
                Start-Sleep -Seconds $sleepSeconds
                continue
            }

            if ($statusCode) {
                throw "DeepSeek API 请求失败（HTTP $statusCode）：$responseBody"
            }

            throw "DeepSeek API 请求失败：$($_.Exception.Message)"
        }
    }

    throw 'DeepSeek API 请求在全部重试后仍然失败。'
}

function Write-StoryboardOutput {
    param(
        [string]$Path,
        [pscustomobject]$Episode,
        [object]$Response
    )

    $finishReason = $null
    if ($Response.choices -and $Response.choices.Count -gt 0) {
        $finishReason = $Response.choices[0].finish_reason
    }

    $headerLines = New-Object 'System.Collections.Generic.List[string]'
    [void]$headerLines.Add("# Source: $([System.IO.Path]::GetFileName($Episode.SourcePath))")
    [void]$headerLines.Add("# Title: $($Episode.DisplayName)")
    if ($null -ne $Episode.EpisodeNumber) {
        [void]$headerLines.Add("# Episode: $($Episode.EpisodeNumber)")
    }
    if ($finishReason) {
        [void]$headerLines.Add("# Finish Reason: $finishReason")
    }
    if ($Response.usage) {
        [void]$headerLines.Add("# Usage: prompt_tokens=$($Response.usage.prompt_tokens) completion_tokens=$($Response.usage.completion_tokens) total_tokens=$($Response.usage.total_tokens)")
    }

    $content = $Response.choices[0].message.content
    $fullText = ($headerLines -join "`r`n") + "`r`n`r`n" + $content.Trim() + "`r`n"
    [System.IO.File]::WriteAllText($Path, $fullText, [System.Text.UTF8Encoding]::new($false))
}

function Start-BatchGeneration {
    param(
        [string]$ProjectFolder,
        [string]$PromptPath,
        [string]$OutDir,
        [string]$ApiBase,
        [string]$ApiKey,
        [string]$Model,
        [bool]$ThinkingEnabled,
        [double]$Temperature,
        [int]$TimeoutSeconds,
        [int]$MaxTokens,
        [double]$DelaySeconds,
        [int]$MaxRetries,
        [bool]$Overwrite
    )

    if ([string]::IsNullOrWhiteSpace($ApiKey)) {
        throw '缺少 DEEPSEEK_API_KEY。'
    }

    if (-not (Test-Path -LiteralPath $ProjectFolder -PathType Container)) {
        throw "项目目录不存在：$ProjectFolder"
    }

    $resolvedPromptPath = Get-PromptFile -ProjectFolder $ProjectFolder -ExplicitPath $PromptPath
    $episodes = Get-EpisodeInputs -ProjectFolder $ProjectFolder
    if (-not $episodes -or $episodes.Count -eq 0) {
        throw "在 $ProjectFolder 下没有找到可处理的 docx 剧本。"
    }

    if (-not (Test-Path -LiteralPath $OutDir -PathType Container)) {
        [void](New-Item -ItemType Directory -Path $OutDir -Force)
    }

    $promptText = Get-Content -LiteralPath $resolvedPromptPath -Raw -Encoding UTF8

    Write-Output "[info] Prompt: $([System.IO.Path]::GetFileName($resolvedPromptPath))"
    Write-Output "[info] Episodes found: $($episodes.Count)"
    Write-Output "[info] Output directory: $OutDir"
    Write-Output "[info] Thinking mode: $(if ($ThinkingEnabled) { 'enabled' } else { 'disabled' })"
    Write-Output "[info] Request timeout: $TimeoutSeconds s"

    for ($index = 0; $index -lt $episodes.Count; $index++) {
        $episode = $episodes[$index]
        $outFileName = Get-OutputFileName -Episode $episode -SequenceIndex ($index + 1)
        Write-Output "[plan] $([System.IO.Path]::GetFileName($episode.SourcePath)) -> $outFileName (chars=$($episode.CharCount))"
    }

    for ($index = 0; $index -lt $episodes.Count; $index++) {
        $episode = $episodes[$index]
        $outFileName = Get-OutputFileName -Episode $episode -SequenceIndex ($index + 1)
        $outPath = Join-Path -Path $OutDir -ChildPath $outFileName

        if ((Test-Path -LiteralPath $outPath -PathType Leaf) -and -not $Overwrite) {
            Write-Output "[skip] $outFileName already exists."
            continue
        }

        Write-Output "[run] Generating $outFileName ..."
        $response = Invoke-DeepSeekCompletion `
            -ApiBase $ApiBase `
            -ApiKey $ApiKey `
            -Model $Model `
            -ThinkingEnabled $ThinkingEnabled `
            -PromptText $promptText `
            -Episode $episode `
            -Temperature $Temperature `
            -TimeoutSeconds $TimeoutSeconds `
            -MaxTokens $MaxTokens `
            -MaxRetries $MaxRetries

        Write-StoryboardOutput -Path $outPath -Episode $episode -Response $response
        Write-Output "[done] Saved $outPath"

        if ($DelaySeconds -gt 0) {
            Start-Sleep -Milliseconds ([int]($DelaySeconds * 1000))
        }
    }

    Write-Output '[done] Batch generation finished.'
}

function Invoke-BatchFromConfig {
    param([string]$ConfigPath)

    if (-not (Test-Path -LiteralPath $ConfigPath -PathType Leaf)) {
        throw "配置文件不存在：$ConfigPath"
    }

    $config = Get-Content -LiteralPath $ConfigPath -Raw -Encoding UTF8 | ConvertFrom-Json
    $apiKey = [string]$env:DEEPSEEK_API_KEY
    if ($config.PSObject.Properties.Name -contains 'ApiKey' -and -not [string]::IsNullOrWhiteSpace([string]$config.ApiKey)) {
        $apiKey = [string]$config.ApiKey
    }

    Start-BatchGeneration `
        -ProjectFolder ([string]$config.ProjectFolder) `
        -PromptPath ([string]$config.PromptPath) `
        -OutDir ([string]$config.OutDir) `
        -ApiBase ([string]$config.ApiBase) `
        -ApiKey $apiKey `
        -Model ([string]$config.Model) `
        -ThinkingEnabled ([bool]$config.ThinkingEnabled) `
        -Temperature ([double]$config.Temperature) `
        -TimeoutSeconds ([int]$config.TimeoutSeconds) `
        -MaxTokens ([int]$config.MaxTokens) `
        -DelaySeconds ([double]$config.DelaySeconds) `
        -MaxRetries ([int]$config.MaxRetries) `
        -Overwrite ([bool]$config.Overwrite)
}

function Invoke-SmokeTestMode {
    $projectFolder = Split-Path -Parent $PSCommandPath
    $promptPath = Get-PromptFile -ProjectFolder $projectFolder -ExplicitPath ''
    $episodes = Get-EpisodeInputs -ProjectFolder $projectFolder

    Write-Output "[info] Prompt: $([System.IO.Path]::GetFileName($promptPath))"
    Write-Output "[info] Episodes found: $($episodes.Count)"
    $outDir = Join-Path -Path $projectFolder -ChildPath 'outputs'
    Write-Output "[info] Output directory: $outDir"

    for ($index = 0; $index -lt $episodes.Count; $index++) {
        $episode = $episodes[$index]
        $outFileName = Get-OutputFileName -Episode $episode -SequenceIndex ($index + 1)
        Write-Output "[plan] $([System.IO.Path]::GetFileName($episode.SourcePath)) -> $outFileName (chars=$($episode.CharCount))"
    }
}

function Start-Gui {
    $settingsPath = Join-Path -Path (Split-Path -Parent $PSCommandPath) -ChildPath 'storyboard-gui.settings.json'
    $defaultProjectFolder = Split-Path -Parent $PSCommandPath

    $savedSettings = @{}
    $savedApiKey = ''
    if (Test-Path -LiteralPath $settingsPath -PathType Leaf) {
        try {
            $saved = Get-Content -LiteralPath $settingsPath -Raw -Encoding UTF8 | ConvertFrom-Json
            foreach ($prop in $saved.PSObject.Properties) {
                $savedSettings[$prop.Name] = $prop.Value
            }
            $savedApiKey = Unprotect-LocalSecret -CipherText ([string](Get-SettingOrDefault -Settings $savedSettings -Name 'ApiKeyProtected' -DefaultValue ''))
        }
        catch {
            $savedSettings = @{}
            $savedApiKey = ''
        }
    }

    if ([string]::IsNullOrWhiteSpace($savedApiKey)) {
        $savedApiKey = [string]$env:DEEPSEEK_API_KEY
    }

    $form = New-Object System.Windows.Forms.Form
    $form.Text = 'Auto-Storyboard 批量分镜生成器'
    $form.Size = New-Object System.Drawing.Size(980, 760)
    $form.StartPosition = 'CenterScreen'
    $form.MinimumSize = New-Object System.Drawing.Size(980, 760)

    $font = New-Object System.Drawing.Font('Microsoft YaHei UI', 9)
    $form.Font = $font

    $lblProject = New-Object System.Windows.Forms.Label
    $lblProject.Location = New-Object System.Drawing.Point(16, 18)
    $lblProject.Size = New-Object System.Drawing.Size(90, 24)
    $lblProject.Text = '项目目录'
    $form.Controls.Add($lblProject)

    $txtProject = New-Object System.Windows.Forms.TextBox
    $txtProject.Location = New-Object System.Drawing.Point(110, 16)
    $txtProject.Size = New-Object System.Drawing.Size(700, 24)
    $txtProject.Text = [string](Get-SettingOrDefault -Settings $savedSettings -Name 'ProjectFolder' -DefaultValue $defaultProjectFolder)
    $form.Controls.Add($txtProject)

    $btnProject = New-Object System.Windows.Forms.Button
    $btnProject.Location = New-Object System.Drawing.Point(825, 14)
    $btnProject.Size = New-Object System.Drawing.Size(120, 28)
    $btnProject.Text = '浏览目录'
    $form.Controls.Add($btnProject)

    $lblPrompt = New-Object System.Windows.Forms.Label
    $lblPrompt.Location = New-Object System.Drawing.Point(16, 56)
    $lblPrompt.Size = New-Object System.Drawing.Size(90, 24)
    $lblPrompt.Text = '提示词文件'
    $form.Controls.Add($lblPrompt)

    $txtPrompt = New-Object System.Windows.Forms.TextBox
    $txtPrompt.Location = New-Object System.Drawing.Point(110, 54)
    $txtPrompt.Size = New-Object System.Drawing.Size(700, 24)
    $txtPrompt.Text = [string](Get-SettingOrDefault -Settings $savedSettings -Name 'PromptPath' -DefaultValue '')
    $form.Controls.Add($txtPrompt)

    $btnPrompt = New-Object System.Windows.Forms.Button
    $btnPrompt.Location = New-Object System.Drawing.Point(825, 52)
    $btnPrompt.Size = New-Object System.Drawing.Size(120, 28)
    $btnPrompt.Text = '浏览文件'
    $form.Controls.Add($btnPrompt)

    $lblOutput = New-Object System.Windows.Forms.Label
    $lblOutput.Location = New-Object System.Drawing.Point(16, 94)
    $lblOutput.Size = New-Object System.Drawing.Size(90, 24)
    $lblOutput.Text = '输出目录'
    $form.Controls.Add($lblOutput)

    $txtOutput = New-Object System.Windows.Forms.TextBox
    $txtOutput.Location = New-Object System.Drawing.Point(110, 92)
    $txtOutput.Size = New-Object System.Drawing.Size(700, 24)
    $txtOutput.Text = [string](Get-SettingOrDefault -Settings $savedSettings -Name 'OutDir' -DefaultValue (Join-Path -Path $defaultProjectFolder -ChildPath 'outputs'))
    $form.Controls.Add($txtOutput)

    $btnOutput = New-Object System.Windows.Forms.Button
    $btnOutput.Location = New-Object System.Drawing.Point(825, 90)
    $btnOutput.Size = New-Object System.Drawing.Size(120, 28)
    $btnOutput.Text = '浏览目录'
    $form.Controls.Add($btnOutput)

    $lblApiKey = New-Object System.Windows.Forms.Label
    $lblApiKey.Location = New-Object System.Drawing.Point(16, 132)
    $lblApiKey.Size = New-Object System.Drawing.Size(90, 24)
    $lblApiKey.Text = 'DeepSeek Key'
    $form.Controls.Add($lblApiKey)

    $txtApiKey = New-Object System.Windows.Forms.TextBox
    $txtApiKey.Location = New-Object System.Drawing.Point(110, 130)
    $txtApiKey.Size = New-Object System.Drawing.Size(300, 24)
    $txtApiKey.Text = $savedApiKey
    $txtApiKey.UseSystemPasswordChar = $true
    $form.Controls.Add($txtApiKey)

    $lblModel = New-Object System.Windows.Forms.Label
    $lblModel.Location = New-Object System.Drawing.Point(420, 132)
    $lblModel.Size = New-Object System.Drawing.Size(50, 24)
    $lblModel.Text = '模型'
    $form.Controls.Add($lblModel)

    $txtModel = New-Object System.Windows.Forms.TextBox
    $txtModel.Location = New-Object System.Drawing.Point(470, 130)
    $txtModel.Size = New-Object System.Drawing.Size(110, 24)
    $txtModel.Text = [string](Get-SettingOrDefault -Settings $savedSettings -Name 'Model' -DefaultValue $script:DefaultModel)
    $form.Controls.Add($txtModel)

    $lblApiBase = New-Object System.Windows.Forms.Label
    $lblApiBase.Location = New-Object System.Drawing.Point(590, 132)
    $lblApiBase.Size = New-Object System.Drawing.Size(30, 24)
    $lblApiBase.Text = 'API'
    $form.Controls.Add($lblApiBase)

    $txtApiBase = New-Object System.Windows.Forms.TextBox
    $txtApiBase.Location = New-Object System.Drawing.Point(620, 130)
    $txtApiBase.Size = New-Object System.Drawing.Size(220, 24)
    $txtApiBase.Text = [string](Get-SettingOrDefault -Settings $savedSettings -Name 'ApiBase' -DefaultValue $script:DefaultApiBase)
    $form.Controls.Add($txtApiBase)

    $chkThinking = New-Object System.Windows.Forms.CheckBox
    $chkThinking.Location = New-Object System.Drawing.Point(845, 132)
    $chkThinking.Size = New-Object System.Drawing.Size(110, 24)
    $chkThinking.Text = '开启思考模式'
    $chkThinking.Checked = [bool](Get-SettingOrDefault -Settings $savedSettings -Name 'ThinkingEnabled' -DefaultValue $true)
    $form.Controls.Add($chkThinking)

    $lblTemp = New-Object System.Windows.Forms.Label
    $lblTemp.Location = New-Object System.Drawing.Point(16, 170)
    $lblTemp.Size = New-Object System.Drawing.Size(90, 24)
    $lblTemp.Text = 'Temperature'
    $form.Controls.Add($lblTemp)

    $numTemp = New-Object System.Windows.Forms.NumericUpDown
    $numTemp.Location = New-Object System.Drawing.Point(110, 168)
    $numTemp.Size = New-Object System.Drawing.Size(110, 24)
    $numTemp.DecimalPlaces = 1
    $numTemp.Increment = [decimal]0.1
    $numTemp.Minimum = [decimal]0
    $numTemp.Maximum = [decimal]2
    $numTemp.Value = [decimal]([double](Get-SettingOrDefault -Settings $savedSettings -Name 'Temperature' -DefaultValue 0.3))
    $form.Controls.Add($numTemp)

    $lblTokens = New-Object System.Windows.Forms.Label
    $lblTokens.Location = New-Object System.Drawing.Point(210, 170)
    $lblTokens.Size = New-Object System.Drawing.Size(80, 24)
    $lblTokens.Text = 'Max Tokens'
    $form.Controls.Add($lblTokens)

    $numTokens = New-Object System.Windows.Forms.NumericUpDown
    $numTokens.Location = New-Object System.Drawing.Point(290, 168)
    $numTokens.Size = New-Object System.Drawing.Size(90, 24)
    $numTokens.Minimum = [decimal]1000
    $numTokens.Maximum = [decimal]32000
    $numTokens.Increment = [decimal]500
    $numTokens.Value = [decimal]([int](Get-SettingOrDefault -Settings $savedSettings -Name 'MaxTokens' -DefaultValue 8000))
    $form.Controls.Add($numTokens)

    $lblTimeout = New-Object System.Windows.Forms.Label
    $lblTimeout.Location = New-Object System.Drawing.Point(740, 170)
    $lblTimeout.Size = New-Object System.Drawing.Size(70, 24)
    $lblTimeout.Text = '超时秒数'
    $form.Controls.Add($lblTimeout)

    $numTimeout = New-Object System.Windows.Forms.NumericUpDown
    $numTimeout.Location = New-Object System.Drawing.Point(810, 168)
    $numTimeout.Size = New-Object System.Drawing.Size(60, 24)
    $numTimeout.Minimum = [decimal]60
    $numTimeout.Maximum = [decimal]7200
    $numTimeout.Increment = [decimal]60
    $numTimeout.Value = [decimal]([int](Get-SettingOrDefault -Settings $savedSettings -Name 'TimeoutSeconds' -DefaultValue 1800))
    $form.Controls.Add($numTimeout)

    $lblDelay = New-Object System.Windows.Forms.Label
    $lblDelay.Location = New-Object System.Drawing.Point(400, 170)
    $lblDelay.Size = New-Object System.Drawing.Size(70, 24)
    $lblDelay.Text = '延迟秒数'
    $form.Controls.Add($lblDelay)

    $numDelay = New-Object System.Windows.Forms.NumericUpDown
    $numDelay.Location = New-Object System.Drawing.Point(470, 168)
    $numDelay.Size = New-Object System.Drawing.Size(90, 24)
    $numDelay.DecimalPlaces = 1
    $numDelay.Increment = [decimal]0.5
    $numDelay.Minimum = [decimal]0
    $numDelay.Maximum = [decimal]10
    $numDelay.Value = [decimal]([double](Get-SettingOrDefault -Settings $savedSettings -Name 'DelaySeconds' -DefaultValue 1.0))
    $form.Controls.Add($numDelay)

    $lblRetries = New-Object System.Windows.Forms.Label
    $lblRetries.Location = New-Object System.Drawing.Point(580, 170)
    $lblRetries.Size = New-Object System.Drawing.Size(70, 24)
    $lblRetries.Text = '重试次数'
    $form.Controls.Add($lblRetries)

    $numRetries = New-Object System.Windows.Forms.NumericUpDown
    $numRetries.Location = New-Object System.Drawing.Point(650, 168)
    $numRetries.Size = New-Object System.Drawing.Size(70, 24)
    $numRetries.Minimum = [decimal]1
    $numRetries.Maximum = [decimal]10
    $numRetries.Value = [decimal]([int](Get-SettingOrDefault -Settings $savedSettings -Name 'MaxRetries' -DefaultValue 3))
    $form.Controls.Add($numRetries)

    $chkOverwrite = New-Object System.Windows.Forms.CheckBox
    $chkOverwrite.Location = New-Object System.Drawing.Point(875, 170)
    $chkOverwrite.Size = New-Object System.Drawing.Size(80, 24)
    $chkOverwrite.Text = '覆盖旧结果'
    $chkOverwrite.Checked = [bool](Get-SettingOrDefault -Settings $savedSettings -Name 'Overwrite' -DefaultValue $false)
    $form.Controls.Add($chkOverwrite)

    $btnScan = New-Object System.Windows.Forms.Button
    $btnScan.Location = New-Object System.Drawing.Point(20, 208)
    $btnScan.Size = New-Object System.Drawing.Size(120, 32)
    $btnScan.Text = '扫描剧本'
    $form.Controls.Add($btnScan)

    $btnStart = New-Object System.Windows.Forms.Button
    $btnStart.Location = New-Object System.Drawing.Point(150, 208)
    $btnStart.Size = New-Object System.Drawing.Size(120, 32)
    $btnStart.Text = '开始生成'
    $form.Controls.Add($btnStart)

    $btnOpenOutput = New-Object System.Windows.Forms.Button
    $btnOpenOutput.Location = New-Object System.Drawing.Point(280, 208)
    $btnOpenOutput.Size = New-Object System.Drawing.Size(120, 32)
    $btnOpenOutput.Text = '打开输出目录'
    $form.Controls.Add($btnOpenOutput)

    $btnSaveSettings = New-Object System.Windows.Forms.Button
    $btnSaveSettings.Location = New-Object System.Drawing.Point(410, 208)
    $btnSaveSettings.Size = New-Object System.Drawing.Size(120, 32)
    $btnSaveSettings.Text = '保存设置'
    $form.Controls.Add($btnSaveSettings)

    $lblStatus = New-Object System.Windows.Forms.Label
    $lblStatus.Location = New-Object System.Drawing.Point(545, 213)
    $lblStatus.Size = New-Object System.Drawing.Size(400, 24)
    $lblStatus.Text = '状态：等待扫描'
    $form.Controls.Add($lblStatus)

    $progressBar = New-Object System.Windows.Forms.ProgressBar
    $progressBar.Location = New-Object System.Drawing.Point(20, 248)
    $progressBar.Size = New-Object System.Drawing.Size(925, 18)
    $progressBar.Minimum = 0
    $progressBar.Maximum = 100
    $progressBar.Value = 0
    $form.Controls.Add($progressBar)

    $grid = New-Object System.Windows.Forms.DataGridView
    $grid.Location = New-Object System.Drawing.Point(20, 280)
    $grid.Size = New-Object System.Drawing.Size(925, 220)
    $grid.ReadOnly = $true
    $grid.AllowUserToAddRows = $false
    $grid.AllowUserToDeleteRows = $false
    $grid.RowHeadersVisible = $false
    $grid.AutoSizeColumnsMode = 'Fill'
    $grid.SelectionMode = 'FullRowSelect'
    $grid.MultiSelect = $false
    [void]$grid.Columns.Add('EpisodeNumber', '集数')
    [void]$grid.Columns.Add('SourceName', '源文件')
    [void]$grid.Columns.Add('CharCount', '字符数')
    [void]$grid.Columns.Add('OutputName', '输出文件')
    $form.Controls.Add($grid)

    $txtLog = New-Object System.Windows.Forms.TextBox
    $txtLog.Location = New-Object System.Drawing.Point(20, 515)
    $txtLog.Size = New-Object System.Drawing.Size(925, 190)
    $txtLog.Multiline = $true
    $txtLog.ReadOnly = $true
    $txtLog.ScrollBars = 'Vertical'
    $txtLog.WordWrap = $false
    $txtLog.Font = New-Object System.Drawing.Font('Consolas', 9)
    $form.Controls.Add($txtLog)

    $folderDialog = New-Object System.Windows.Forms.FolderBrowserDialog
    $openDialog = New-Object System.Windows.Forms.OpenFileDialog
    $openDialog.Filter = 'Text Files (*.txt)|*.txt|All Files (*.*)|*.*'

    $script:GuiState = @{
        CurrentEpisodes   = @()
        WorkerProcess     = $null
        WorkerConfigPath  = $null
        WorkerFinished    = $false
        WorkerLineQueue   = [System.Collections.Concurrent.ConcurrentQueue[string]]::new()
        CompletedEpisodes = 0
        TotalEpisodes     = 0
    }

    function Add-LogLine {
        param([string]$Message)
        $timestamp = Get-Date -Format 'HH:mm:ss'
        $txtLog.AppendText("[$timestamp] $Message`r`n")
    }

    function Save-Settings {
        $settings = @{
            ProjectFolder = $txtProject.Text.Trim()
            PromptPath    = $txtPrompt.Text.Trim()
            OutDir        = $txtOutput.Text.Trim()
            ApiKeyProtected = Protect-LocalSecret -PlainText $txtApiKey.Text.Trim()
            Model         = $txtModel.Text.Trim()
            ApiBase       = $txtApiBase.Text.Trim()
            ThinkingEnabled = [bool]$chkThinking.Checked
            Temperature   = [double]$numTemp.Value
            TimeoutSeconds = [int]$numTimeout.Value
            MaxTokens     = [int]$numTokens.Value
            DelaySeconds  = [double]$numDelay.Value
            MaxRetries    = [int]$numRetries.Value
            Overwrite     = [bool]$chkOverwrite.Checked
        }
        $json = $settings | ConvertTo-Json -Depth 5
        [System.IO.File]::WriteAllText($settingsPath, $json, [System.Text.UTF8Encoding]::new($false))
    }

    function Refresh-Grid {
        $grid.Rows.Clear()
        for ($index = 0; $index -lt $script:GuiState.CurrentEpisodes.Count; $index++) {
            $episode = $script:GuiState.CurrentEpisodes[$index]
            $outputName = Get-OutputFileName -Episode $episode -SequenceIndex ($index + 1)
            $episodeLabel = if ($null -ne $episode.EpisodeNumber) { [string]$episode.EpisodeNumber } else { '-' }
            [void]$grid.Rows.Add($episodeLabel, [System.IO.Path]::GetFileName($episode.SourcePath), [string]$episode.CharCount, $outputName)
        }
    }

    function Scan-Episodes {
        $projectFolder = $txtProject.Text.Trim()
        if ([string]::IsNullOrWhiteSpace($projectFolder) -or -not (Test-Path -LiteralPath $projectFolder -PathType Container)) {
            throw '请先选择有效的项目目录。'
        }

        $resolvedPrompt = Get-PromptFile -ProjectFolder $projectFolder -ExplicitPath $txtPrompt.Text.Trim()
        $txtPrompt.Text = $resolvedPrompt

        $episodes = Get-EpisodeInputs -ProjectFolder $projectFolder
        if (-not $episodes -or $episodes.Count -eq 0) {
            throw '没有找到可处理的剧本文件。'
        }

        $script:GuiState.CurrentEpisodes = @($episodes)
        $script:GuiState.TotalEpisodes = $episodes.Count
        $script:GuiState.CompletedEpisodes = 0
        $progressBar.Value = 0
        Refresh-Grid
        $lblStatus.Text = "状态：已扫描到 $($episodes.Count) 集剧本"
        Add-LogLine "扫描完成：共 $($episodes.Count) 集，提示词文件：$([System.IO.Path]::GetFileName($resolvedPrompt))"
        Save-Settings
    }

    function Start-WorkerProcess {
        if (-not $script:GuiState.CurrentEpisodes -or $script:GuiState.CurrentEpisodes.Count -eq 0) {
            Scan-Episodes
        }

        $apiKey = $txtApiKey.Text.Trim()
        if ([string]::IsNullOrWhiteSpace($apiKey)) {
            throw '请填写 DeepSeek API Key。'
        }

        $projectFolder = $txtProject.Text.Trim()
        $outDir = $txtOutput.Text.Trim()
        if ([string]::IsNullOrWhiteSpace($outDir)) {
            throw '请填写输出目录。'
        }

        if (-not $chkOverwrite.Checked) {
            $existingOutputs = @()
            for ($index = 0; $index -lt $script:GuiState.CurrentEpisodes.Count; $index++) {
                $episode = $script:GuiState.CurrentEpisodes[$index]
                $outFileName = Get-OutputFileName -Episode $episode -SequenceIndex ($index + 1)
                $outPath = Join-Path -Path $outDir -ChildPath $outFileName
                if (Test-Path -LiteralPath $outPath -PathType Leaf) {
                    $existingOutputs += $outFileName
                }
            }

            if ($existingOutputs.Count -eq $script:GuiState.CurrentEpisodes.Count) {
                $existingList = $existingOutputs -join "`r`n"
                $message = "检测到所有输出文件都已存在：`r`n`r`n$existingList`r`n`r`n如果要重新生成，请先勾选 [覆盖旧结果]。"
                $lblStatus.Text = '状态：全部结果已存在'
                Add-LogLine '所有输出文件都已存在，当前不会重新生成。'
                [System.Windows.Forms.MessageBox]::Show(
                    $message,
                    '无需生成',
                    'OK',
                    'Information'
                ) | Out-Null
                return
            }
        }

        $config = @{
            ProjectFolder = $projectFolder
            PromptPath    = $txtPrompt.Text.Trim()
            OutDir        = $outDir
            ApiBase       = $txtApiBase.Text.Trim()
            ApiKey        = $apiKey
            Model         = $txtModel.Text.Trim()
            Temperature   = [double]$numTemp.Value
            TimeoutSeconds = [int]$numTimeout.Value
            MaxTokens     = [int]$numTokens.Value
            DelaySeconds  = [double]$numDelay.Value
            MaxRetries    = [int]$numRetries.Value
            ThinkingEnabled = [bool]$chkThinking.Checked
            Overwrite     = [bool]$chkOverwrite.Checked
        }

        if (-not (Test-Path -LiteralPath $outDir -PathType Container)) {
            [void](New-Item -ItemType Directory -Path $outDir -Force)
        }

        $configPath = Join-Path -Path $env:TEMP -ChildPath ("storyboard-batch-{0}.json" -f ([guid]::NewGuid().ToString('N')))
        [System.IO.File]::WriteAllText($configPath, ($config | ConvertTo-Json -Depth 5), [System.Text.UTF8Encoding]::new($false))

        $script:GuiState.WorkerConfigPath = $configPath
        $script:GuiState.WorkerFinished = $false
        $script:GuiState.CompletedEpisodes = 0
        $script:GuiState.TotalEpisodes = $script:GuiState.CurrentEpisodes.Count
        $script:GuiState.WorkerLineQueue = [System.Collections.Concurrent.ConcurrentQueue[string]]::new()
        $progressBar.Value = 0

        $psi = New-Object System.Diagnostics.ProcessStartInfo
        $psi.FileName = (Get-Command powershell.exe).Source
        $psi.Arguments = "-NoProfile -ExecutionPolicy Bypass -File `"$PSCommandPath`" -BatchConfigPath `"$configPath`""
        $psi.UseShellExecute = $false
        $psi.RedirectStandardOutput = $true
        $psi.RedirectStandardError = $true
        $psi.CreateNoWindow = $true
        $psi.EnvironmentVariables['DEEPSEEK_API_KEY'] = $apiKey

        $process = New-Object System.Diagnostics.Process
        $process.StartInfo = $psi
        $process.EnableRaisingEvents = $true

        $outputHandler = [System.Diagnostics.DataReceivedEventHandler]{
            param($sender, $args)
            if (-not [string]::IsNullOrWhiteSpace($args.Data)) {
                $script:GuiState.WorkerLineQueue.Enqueue($args.Data) | Out-Null
            }
        }

        $process.add_OutputDataReceived($outputHandler)
        $process.add_ErrorDataReceived($outputHandler)

        if (-not $process.Start()) {
            throw '无法启动后台生成进程。'
        }

        $process.BeginOutputReadLine()
        $process.BeginErrorReadLine()

        $script:GuiState.WorkerProcess = $process
        $btnStart.Enabled = $false
        $btnScan.Enabled = $false
        $lblStatus.Text = '状态：正在生成...'
        Add-LogLine "开始批量生成，共 $($script:GuiState.TotalEpisodes) 集。"
        Save-Settings
    }

    $timer = New-Object System.Windows.Forms.Timer
    $timer.Interval = 250
    $timer.Add_Tick({
        $line = $null
        while ($script:GuiState.WorkerLineQueue.TryDequeue([ref]$line)) {
            Add-LogLine $line
            if ($line.StartsWith('[done] Saved') -or $line.StartsWith('[skip] ')) {
                $script:GuiState.CompletedEpisodes++
                if ($script:GuiState.TotalEpisodes -gt 0) {
                    $percent = [Math]::Min(100, [int](($script:GuiState.CompletedEpisodes / $script:GuiState.TotalEpisodes) * 100))
                    $progressBar.Value = $percent
                    $lblStatus.Text = "状态：已完成 $($script:GuiState.CompletedEpisodes) / $($script:GuiState.TotalEpisodes)"
                }
            }
        }

        if ($script:GuiState.WorkerProcess -and -not $script:GuiState.WorkerFinished -and $script:GuiState.WorkerProcess.HasExited) {
            $script:GuiState.WorkerFinished = $true
            $timer.Stop()
            $exitCode = $script:GuiState.WorkerProcess.ExitCode
            $btnStart.Enabled = $true
            $btnScan.Enabled = $true

            if ($exitCode -eq 0) {
                $progressBar.Value = 100
                $lblStatus.Text = '状态：生成完成'
                Add-LogLine '全部任务执行完成。'
                [System.Windows.Forms.MessageBox]::Show('分镜生成完成。', '完成', 'OK', 'Information') | Out-Null
            }
            else {
                $lblStatus.Text = "状态：执行失败（ExitCode=$exitCode）"
                Add-LogLine "后台进程异常结束，ExitCode=$exitCode"
                [System.Windows.Forms.MessageBox]::Show("后台进程异常结束，ExitCode=$exitCode。请查看日志。", '失败', 'OK', 'Error') | Out-Null
            }

            if ($script:GuiState.WorkerConfigPath -and (Test-Path -LiteralPath $script:GuiState.WorkerConfigPath -PathType Leaf)) {
                Remove-Item -LiteralPath $script:GuiState.WorkerConfigPath -Force
            }
            $script:GuiState.WorkerProcess.Dispose()
            $script:GuiState.WorkerProcess = $null
            $script:GuiState.WorkerConfigPath = $null
        }
    })

    $btnProject.Add_Click({
        $folderDialog.SelectedPath = if (Test-Path -LiteralPath $txtProject.Text.Trim() -PathType Container) { $txtProject.Text.Trim() } else { $defaultProjectFolder }
        if ($folderDialog.ShowDialog() -eq 'OK') {
            $txtProject.Text = $folderDialog.SelectedPath
            if ([string]::IsNullOrWhiteSpace($txtOutput.Text.Trim())) {
                $txtOutput.Text = Join-Path -Path $folderDialog.SelectedPath -ChildPath 'outputs'
            }
        }
    })

    $btnPrompt.Add_Click({
        $openDialog.InitialDirectory = if (Test-Path -LiteralPath $txtProject.Text.Trim() -PathType Container) { $txtProject.Text.Trim() } else { $defaultProjectFolder }
        if ($openDialog.ShowDialog() -eq 'OK') {
            $txtPrompt.Text = $openDialog.FileName
        }
    })

    $btnOutput.Add_Click({
        $folderDialog.SelectedPath = if (Test-Path -LiteralPath $txtOutput.Text.Trim() -PathType Container) { $txtOutput.Text.Trim() } else { $txtProject.Text.Trim() }
        if ($folderDialog.ShowDialog() -eq 'OK') {
            $txtOutput.Text = $folderDialog.SelectedPath
        }
    })

    $btnScan.Add_Click({
        try {
            Scan-Episodes
        }
        catch {
            Add-LogLine "扫描失败：$($_.Exception.Message)"
            [System.Windows.Forms.MessageBox]::Show($_.Exception.Message, '扫描失败', 'OK', 'Error') | Out-Null
        }
    })

    $btnStart.Add_Click({
        try {
            Start-WorkerProcess
            $timer.Start()
        }
        catch {
            Add-LogLine "启动失败：$($_.Exception.Message)"
            if ($script:GuiState.WorkerConfigPath -and (Test-Path -LiteralPath $script:GuiState.WorkerConfigPath -PathType Leaf)) {
                Remove-Item -LiteralPath $script:GuiState.WorkerConfigPath -Force
            }
            $script:GuiState.WorkerConfigPath = $null
            [System.Windows.Forms.MessageBox]::Show($_.Exception.Message, '启动失败', 'OK', 'Error') | Out-Null
        }
    })

    $btnSaveSettings.Add_Click({
        try {
            Save-Settings
            $lblStatus.Text = '状态：设置已保存'
            Add-LogLine '设置已保存。API Key 以当前 Windows 用户加密方式存储。'
            [System.Windows.Forms.MessageBox]::Show('设置已保存。API Key 已加密写入本机当前用户配置。', '保存成功', 'OK', 'Information') | Out-Null
        }
        catch {
            Add-LogLine "保存设置失败：$($_.Exception.Message)"
            [System.Windows.Forms.MessageBox]::Show($_.Exception.Message, '保存失败', 'OK', 'Error') | Out-Null
        }
    })

    $btnOpenOutput.Add_Click({
        $target = $txtOutput.Text.Trim()
        if (-not [string]::IsNullOrWhiteSpace($target) -and (Test-Path -LiteralPath $target -PathType Container)) {
            Start-Process explorer.exe $target
        }
        else {
            [System.Windows.Forms.MessageBox]::Show('输出目录不存在。', '提示', 'OK', 'Warning') | Out-Null
        }
    })

    $form.Add_Shown({
        try {
            if ([string]::IsNullOrWhiteSpace($txtPrompt.Text.Trim())) {
                $txtPrompt.Text = Get-PromptFile -ProjectFolder $txtProject.Text.Trim() -ExplicitPath ''
            }
        }
        catch {
        }
    })

    $form.Add_FormClosing({
        try {
            Save-Settings
        }
        catch {
        }
    })

    [void]$form.ShowDialog()
}

if ($BatchConfigPath) {
    Invoke-BatchFromConfig -ConfigPath $BatchConfigPath
    exit 0
}

if ($SmokeTest) {
    Invoke-SmokeTestMode
    exit 0
}

Start-Gui
