# GUI 版使用说明

如果同事没有安装 Python，优先用 `.exe` 版本。

## 你需要的文件

- `Launch-StoryboardGenerator.bat`
- `AutoStoryboardGenerator.exe`

## 启动方式

最简单的是双击：

```text
AutoStoryboardGenerator.exe
```

如果你还是想保留一个统一入口，也可以双击：

```text
Launch-StoryboardGenerator.bat
```

它会优先启动同目录下的 `AutoStoryboardGenerator.exe`。

## GUI 里要填什么

- 项目目录：放提示词和剧本的文件夹
- 提示词文件：默认会自动识别 `*prompt*.txt`
- 输出目录：生成结果保存位置
- 供应商：可选 `deepseek`、`qwen-chat` 或 `bltcy-chat`
- API Key：当前供应商对应的 Key，可以直接在界面里输入
- 模型：DeepSeek 默认 `deepseek-v4-flash`，并预设 `deepseek-v4-pro`、`deepseek-chat`、`deepseek-reasoner`；Qwen Chat 生成默认 `qwen3.6-plus`，Agent 审核自动用 `qwen3.6-flash`；BLTCY Chat 预设 `gpt-5.4` 和 `gemini-3.1-pro-preview`
- API：DeepSeek 默认 `https://api.deepseek.com`；Qwen Chat 默认 `https://dashscope.aliyuncs.com/compatible-mode/v1`；BLTCY Chat 默认 `https://api.bltcy.ai/v1/chat/completions`
- 并发数：默认 `3`，表示同时跑 3 集
- 单次集数：默认 `2`，表示普通生成时每次请求把 2 集打包在一起；可选 `1`、`2`、`3`。开启 Agent 审核回修时会自动按单集请求执行，用并发提速
- 生成用思考：默认开启；控制生成 skill 是否启用思考
- 生成强度：DeepSeek 思考模式下默认 `high`；可选 `high`、`max`
- 审核用思考：默认关闭；控制审核 skill 是否启用思考
- 审核强度：DeepSeek 思考模式下默认 `high`；可选 `high`、`max`
- Agent审核回修：可选开启；开启后会走“生成 skill -> 审核 skill -> 回修”循环，批量阶段的审核也会计入总回修轮数；最后仍未通过时会保存草稿并生成 `.review.txt` 审核报告
- 分段稳定模式：建议与 Agent审核回修一起开启；程序会先按 `场xx-x` 等场景标题把单集拆成多个剧情段，每段在同一对话里完成生成、审核、必要回修，再由程序拼接并重编号，减少整集重写越修越歪
- 回修轮数：默认 `2`，表示最多生成/审核 2 轮
- Max Tokens：界面上限已放宽到 `393216`，可以覆盖 DeepSeek 新模型的更长输出能力
- 超时秒数：默认 1800，建议保持较大
- 如果把别家的 API Key 填到了当前供应商，程序会在开始前直接拦截并提示，不再整批跑完才报错
- 也可以直接把文件夹、提示词 `.txt`、剧本 `.docx` 拖进窗口

然后：

1. 可以先点“扫描剧本”，也可以直接把素材拖进窗口
2. 在界面里填好或修改 API Key
3. 按需要调整“并发数”，默认 `3`
4. 按需要调整“单次集数”，默认 `2`
5. 按需要决定是否保留“生成用思考”与“审核用思考”（如果供应商支持）
6. 点“保存设置”
7. 确认列表里识别到了每一集
8. 点“开始生成”

## API Key 保存方式

- API Key 可以直接在 GUI 里录入
- 点“保存设置”后，会保存到本机配置文件
- 下次打开 GUI 会自动回填
- 你随时可以改掉 Key，再点一次“保存设置”
- 保存时使用当前 Windows 用户的本地加密，不是明文直存

## 它会自动做的事

- 读取 `docx` 剧本
- 自动提取“第几集”
- 支持把文件夹、提示词 `.txt`、剧本 `.docx` 直接拖进窗口
- 拖入剧本后会自动回填项目目录并立即扫描
- 普通生成会按你设置的“单次集数”把剧本顺序打包；开启 Agent 审核回修时自动改为单集请求，避免跨集混写和批量分隔丢失
- 开启“分段稳定模式”后，单集内部会按场景分段生成，每段独立闭环后再拼接为最终文件
- 按你设置的并发数并行调用 DeepSeek、Qwen Chat 或 BLTCY Chat API，默认同时处理 3 个请求批次
- DeepSeek 新增 `deepseek-v4-flash` / `deepseek-v4-pro` 两个模型选项；生成和审核会分别控制 `thinking: {"type":"enabled"}`
- DeepSeek 在开启思考时，还会分别附带 `reasoning_effort`；默认生成和审核都用 `high`
- Qwen Chat 生成和审核会分别控制 `enable_thinking: true`，生成默认 `qwen3.6-plus`，审核自动切到 `qwen3.6-flash`；BLTCY Chat 当前不附带 thinking 参数
- 如果生成模型选的是 `deepseek-v4-pro` 或 `deepseek-reasoner`，审核默认会自动降到更快的 `deepseek-v4-flash`；如果供应商选 Qwen Chat，审核默认会自动使用 `qwen3.6-flash`
- 开启 Agent 审核回修后，程序会先生成分镜初稿，再调用 `storyboard_review_skill.txt` 做严格审核；如果某一集在批量结果里审核不过，会自动回落到单集重跑，但批量阶段已经消耗的审核轮次不会重复计算
- 审核 skill 会把阻断性硬错误放入 `issues`，把景别重复、轻微时长偏差等质检提醒放入 `warnings`；台词审核以 7 字/秒为可接受上限，6-7 字/秒会作为 warnings 记录。warnings 会打印到日志，并写入同名 `.review.txt`，但不触发回修
- 如果所有回修轮次用完仍未通过，程序不再判定整集失败：会把当前最新版分镜保存到原输出文件，并在同目录写入 `同名.review.txt` 作为质检报告
- 允许把单次请求超时拉长，避免长剧本在思考模式下过早失败
- 已有输出默认跳过
- 失败时按配置重试
- 把结果写到 `outputs/《被弃千金竟是顶级大佬》-ep01-storyboard.txt` 这种文件
- 每次点击“开始生成”都会在 `输出目录/logs/` 下生成一份独立运行日志；失败弹窗会直接显示这份日志路径

## 适合团队分发的方式

如果大家都是 Windows 电脑，直接分发 `AutoStoryboardGenerator.exe` 就行，不需要 Python，也不需要 PowerShell。

如果你后面还想继续压缩体积或签名，那是下一步交付问题；就“同事没装 Python”这个问题，现在直接发 `.exe` 就可以。
