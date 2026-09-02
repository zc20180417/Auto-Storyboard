# Seedance 2.5 Horizontal Xianxia 3D CG Model Contract

Contract snapshot: 2026-09-01

This reference separates official provider capability from the narrower product contract implemented by `seedance-2.5-horizontal-xianxia-3d-cg`. The machine-readable companion is `tests/fixtures/seedance25/provider-contract-reference.json`.

## Provider capability observed

- Model ID: `doubao-seedance-2-5-260628`
- Create endpoint: `POST https://ark.cn-beijing.volces.com/api/v3/contents/generations/tasks`
- Horizontal ratio: `16:9`
- Resolutions include `480p`, `720p`, and `1080p`
- Duration accepts integer seconds from `4`–`30`; provider automatic duration is `-1`
- Native audio is enabled with `generate_audio=true`
- Reference material roles are `reference_image`, `reference_video`, and `reference_audio`
- Limits are 30 images, 10 videos, 10 audios, and 50 reference items in total
- The documented output frame rate is 24 fps；它是结果/媒体 QA 条件，不是创建请求字段

No Seedance 2.5 sunset or deprecation notice was found on the cited model lifecycle page as of the snapshot date. This is an observation, not a permanent availability guarantee.

## Product contract

- Profile ID: `seedance-2.5-horizontal-xianxia-3d-cg`
- Aspect and output: `16:9`, `720p` (`1280×720`), expected 24 fps
- Duration: explicit integer `4`–`30`; `-1` is deliberately disabled
- Native audio: required
- Input: at least one actually serialized image/video/audio reference
- Internal task name: `multimodal_generation`
- Provider mapping: at least one reference content item plus `omni_reference_task_type=reference`
- Create body must not contain `fps` or the internal `video_task_type`

The word “reference” in the provider request does not enable local text-only, first/last-frame, keyframe, edit, extend, continuation, or track-completion flows. Those paths remain out of scope.

## Evidence and security boundary

Repository fixtures are public, field-redacted, non-replayable contract snapshots. Authorization headers, cookies, signing parameters, temporary result URLs, internal hosts, real account IDs, and real material IDs must not enter the repository, ordinary run directories, or CI artifacts. A raw transport capture belongs only in controlled external storage.

This snapshot proves the local Unit 1A contract. It does not prove that the target CPA/ManJuWeb account is enabled, passes every field through, or can submit a real `16:9` task. Those claims require a sanitized, authenticated Unit 1B preflight.

## Official sources

- https://docs.volcengine.com/docs/82379/2607688
- https://docs.volcengine.com/docs/82379/1520757
- https://docs.volcengine.com/docs/82379/2298881
- https://docs.volcengine.com/docs/82379/2637911
