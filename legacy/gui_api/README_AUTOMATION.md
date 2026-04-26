# 自动化分镜工作流

这个仓库现在可以直接批量跑你目前的流程：

1. 读取 `竖屏古装分镜生产提示词prompt20260401.txt`
2. 逐个读取每一集 `docx` 剧本
3. 调用 DeepSeek 或 Qwen Chat API 生成分镜提示词
4. 自动保存到 `outputs/`

## 目录约定

- 总提示词：仓库根目录下的 `*prompt*.txt`
- 剧本：仓库根目录下的 `*.docx`
- 输出：`outputs/《被弃千金竟是顶级大佬》-ep01-storyboard.txt` 这种命名

## 先决条件

1. 申请 DeepSeek API Key、DashScope API Key，或 BLTCY API Key
2. 给本机准备一个可用的 Python 3
3. 在 PowerShell 里设置环境变量

```powershell
$env:DEEPSEEK_API_KEY = "你的 DeepSeek API Key"
```

如果你要跑 Qwen Chat，则使用：

```powershell
$env:DASHSCOPE_API_KEY = "你的 DashScope API Key"
```

如果你要跑 BLTCY Chat，则使用：

```powershell
$env:BLTCY_API_KEY = "你的 BLTCY API Key"
```

如果你希望长期保存，也可以执行：

```powershell
setx DEEPSEEK_API_KEY "你的 DeepSeek API Key"
```

或：

```powershell
setx DASHSCOPE_API_KEY "你的 DashScope API Key"
```

或：

```powershell
setx BLTCY_API_KEY "你的 BLTCY API Key"
```

设置完成后，重新打开一个 PowerShell 窗口。

## 先做一次不发请求的检查

```powershell
python .\batch_generate_storyboards.py --dry-run
```

这个命令会检查：

- 是否找到了总提示词
- 是否识别到了所有剧本
- 每个剧本会输出到哪个文件

## 正式批量生成

```powershell
python .\batch_generate_storyboards.py
```

如果想覆盖已经生成过的结果：

```powershell
python .\batch_generate_storyboards.py --overwrite
```

## 可选参数

```powershell
python .\batch_generate_storyboards.py `
  --provider deepseek `
  --model deepseek-v4-flash `
  --temperature 0.3 `
  --timeout-seconds 1800 `
  --parallelism 3 `
  --episodes-per-request 2 `
  --max-tokens 32768 `
  --delay-seconds 1.5
```

如果你要启用双-skill agent 模式：

```powershell
python .\batch_generate_storyboards.py `
  --provider deepseek `
  --model deepseek-v4-flash `
  --agent-review `
  --review-rounds 2 `
  --temperature 0.3 `
  --timeout-seconds 1800 `
  --parallelism 3 `
  --episodes-per-request 1 `
  --max-tokens 32768
```

如果你要切到更强的 DeepSeek 新模型：

```powershell
python .\batch_generate_storyboards.py `
  --provider deepseek `
  --model deepseek-v4-pro `
  --temperature 0.3 `
  --timeout-seconds 1800 `
  --parallelism 3 `
  --max-tokens 32768
```

Qwen Chat 示例：

```powershell
python .\batch_generate_storyboards.py `
  --provider qwen-chat `
  --model qwen3.6-plus `
  --api-base https://dashscope.aliyuncs.com/compatible-mode/v1 `
  --temperature 0.3 `
  --timeout-seconds 1800 `
  --parallelism 3 `
  --max-tokens 8000
```

BLTCY Chat 示例：

```powershell
python .\batch_generate_storyboards.py `
  --provider bltcy-chat `
  --model gpt-5.4 `
  --api-base https://api.bltcy.ai/v1/chat/completions `
  --temperature 0.3 `
  --timeout-seconds 1800 `
  --parallelism 3 `
  --max-tokens 12000
```

如果你要切到 Gemini：

```powershell
python .\batch_generate_storyboards.py `
  --provider bltcy-chat `
  --model gemini-3.1-pro-preview `
  --api-base https://api.bltcy.ai/v1/chat/completions `
  --temperature 0.3 `
  --timeout-seconds 1800 `
  --parallelism 3 `
  --max-tokens 12000
```

常用参数：

- `--prompt`：手动指定提示词文件
- `--provider`：选择 `deepseek`、`qwen-chat` 或 `bltcy-chat`
- `--scripts-glob`：指定剧本匹配规则
- `--out-dir`：指定输出目录
- `--disable-thinking`：兼容旧参数，等同于关闭“生成用思考”
- `--disable-generation-thinking`：关闭生成 skill 的思考模式
- `--enable-review-thinking`：开启审核 skill 的思考模式；默认关闭
- `--generation-reasoning-effort`：DeepSeek 生成思考强度；可选 `high`、`max`，默认 `high`
- `--review-reasoning-effort`：DeepSeek 审核思考强度；可选 `high`、`max`，默认 `high`
- `--timeout-seconds`：单次请求超时秒数；默认 1800
- `--parallelism`：并发处理的集数；默认 3
- `--episodes-per-request`：单次请求打包多少集；可选 `1-3`，默认 2。开启 `--agent-review` 时会自动按 1 集执行，优先保证质量和稳定性
- `--agent-review`：开启“生成 skill + 审核 skill + 回修”循环
- `--stable-segments`：开启分段稳定模式；与 `--agent-review` 配合使用时，会按场景拆段，每段在同一对话里生成/审核/回修，再拼接重编号，减少整集重写引入新错误
- `--review-rounds`：Agent 模式下最多生成/审核几轮；默认 2。批量阶段的审核也计入这个总轮数
- `--overwrite`：覆盖旧结果
- `--dry-run`：只检查，不调用 API

## 推荐做法

- DeepSeek 默认用 `deepseek-v4-flash`；如果更看重质量可以切 `deepseek-v4-pro`
- DeepSeek 旧别名 `deepseek-chat` / `deepseek-reasoner` 仍保留在工具里，方便兼容旧配置
- Qwen Chat 生成默认用 `qwen3.6-plus`，Agent 审核默认用 `qwen3.6-flash`；BLTCY Chat 默认用 `gpt-5.4`
- BLTCY Chat 也支持把模型切到 `gemini-3.1-pro-preview`
- DeepSeek thinking mode 对应 `thinking: {"type":"enabled"}`；Qwen Chat 对应 `enable_thinking: true`；BLTCY Chat 当前不附带 thinking 参数
- 默认推荐：生成 skill 可开思考，审核 skill 默认关思考，减少过度审查和过长 JSON 反馈
- 如果生成模型使用 `deepseek-v4-pro` 或 `deepseek-reasoner`，审核会自动切到更快的 `deepseek-v4-flash`；如果供应商使用 Qwen Chat，审核会自动切到 `qwen3.6-flash`
- 普通生成默认会按顺序每次请求处理 2 集，也可以改回单集或调到 3 集；Agent 模式会自动按单集请求执行，用并发数提速
- 对长剧本建议开启 `--stable-segments`，优先保证剧情段内稳定性；如果要对比旧整集回修流程，可以关闭该参数
- 并发数控制的是同时跑多少个请求批次；默认并发数是 3
- 保留同一个系统提示词，便于命中 DeepSeek 的上下文缓存
- DeepSeek 开启思考时，默认会把生成和审核的 `reasoning_effort` 都设为 `high`
- 输出文件默认跳过已完成项，适合断点续跑
- Agent 模式下，生成 skill 仍使用你当前的提示词文件；审核 skill 默认读取 `storyboard_review_skill.txt`。如果批量结果先审核失败再回落单集，已经消耗的轮次不会再重复算一遍
- Agent 模式下，审核 skill 会把阻断性硬错误放入 `issues`，把景别重复、轻微时长偏差等质检提醒放入 `warnings`。台词审核以 7 字/秒为可接受上限，6-7 字/秒会作为 warnings 打印并写入同名 `.review.txt`，但不触发回修
- Agent 模式最后仍未通过审核时，不再让整批任务失败；程序会保存当前最新版分镜，并写入同名 `.review.txt` 质检报告
- 如果批量请求里的某一集输出分隔异常或审核失败，程序会自动把那一集回落成单集重跑

## 不推荐的做法

继续模拟网页里的复制粘贴。原因很简单：

- 网页结构一变，自动化就坏
- 登录、验证码、风控都不稳定
- 批量任务不好做重试和断点续跑
- 输出不容易结构化保存

如果你必须走网页自动化，可以再补一层 Playwright，但那应该是 API 不可用时的备选方案，不该是主流程。
