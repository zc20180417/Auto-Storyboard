# Seedance 2.5 Profile Contract

Contract snapshot: 2026-08-15

## Model and output

- Profile ID: `seedance-2.5-live-vertical`
- Model ID: `doubao-seedance-2-5-260628`
- Task in scope: `multimodal_generation` only
- Actual material requirement: at least one image, video, or audio input
- Aspect: `9:16`
- Resolution enabled by this profile: `480p`, `720p`
- Default resolution: `720p` (`720x1280` for 9:16)
- FPS: `24`
- Duration: integer seconds in `[4, 30]`
- Native audio: enabled

1080p is intentionally not enabled in this contract snapshot. Update the machine profile, tests and this reference together after the official API availability is verified.

The profile does not fall back to text-only generation when material bindings are missing. Images, videos and audios are input materials within the one multimodal task; they do not select a separate reference-generation task.

## Multimodal limits

- Total multimodal materials: at most 50
- Images: at most 30
- Videos: at most 10; total video duration at most 30 seconds
- Audios: at most 10; total audio duration at most 30 seconds

Validate current format and size limits against the official API documentation before sending a request. Do not infer acceptance only from a file extension.

## Prompt principles

- Keep the only task type as `multimodal_generation`.
- Reject text-only generation, reference-generation mode, first/last-frame or keyframe generation, video editing, video extension/continuation, and track completion.
- A video may supply an explicit multimodal material duty, but it must never become an edit or extension target in this profile.
- Keep API parameters outside natural-language prompt text.
- Bind every used material to one explicit duty and state exclusions when ambiguity is likely.
- Preserve actual upload order in `@图片N`, `@视频N`, `@音频N` references.
- Use integer-second stages. For a long clip, assign one major state change to each stage and specify the end state.
- Prefer summarized ordinary actions; specify only key action mechanics.
- Add only focused negative constraints required by the scene.

## Official sources

- Model page: https://ark.volcengine.com/region:cn-beijing/model/detail?name=doubao-seedance-2-5
- API tutorial: https://ark.volcengine.com/region:cn-beijing/docs/82379/2607688?lang=zh
- Prompt guide: https://ark.volcengine.com/region:cn-beijing/docs/82379/2607689?lang=zh
