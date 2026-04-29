# Prompt Patterns

Use this reference when a task needs concrete templates, model-specific phrasing, or consistent batch output.

## Nano Banana Pro Template

```text
写实电影剧照，[时代/地区/类型]场景：[场景名]。
画面内容：[地点、主体物件、人物动作、关键道具、背景关系]。
时代细节：[建筑、家具、车辆、服装、纸质文件、设备、磨损痕迹]；不要现代化装修。
镜头语言：竖屏9:16，35mm纪实摄影视角，中景到广角，主体清楚，前景/中景/背景有纵深，适合短剧分镜定场。
光影色彩：[时间、主光方向、冷暖关系、反射、雾气/灰尘/水汽]，低饱和胶片色彩，避免过曝。
质量要求：photorealistic, cinematic still, high detail, realistic Chinese faces if people appear, no western faces, no AI gloss, no plastic skin.
不要出现：[负面约束]。
```

Use Chinese for Nano Banana Pro by default when the source is Chinese. Keep the prompt structured and literal.

## GPT Image 2 Template

```text
Create a photorealistic vertical 9:16 cinematic still for [project type / genre / period]. Scene: [scene name].
The image should show: [location, required objects, action, people, background].
Keep all production design period-accurate: [materials, props, vehicles, furniture, documents, equipment]. The location should feel [used/local/lived-in/etc.], not [unwanted style].
Composition: documentary film still, 35mm lens feeling, medium-wide framing, clear spatial depth with foreground, midground, and background.
Lighting and color: [time of day, light direction, practical lights, reflections]. Use restrained film color, natural contrast, realistic texture, and no over-polished AI look.
If people are included, use [demographic / role / clothing / pose guidance].
Avoid: [negative constraints].
```

Use English for GPT Image 2 by default. It usually responds well to complete sentences and explicit scene intent.

## Common Negative Constraints

Choose only relevant items:

```text
cartoons, anime, illustration, oil painting, 3D render, plastic texture, modern objects, modern smartphones, LED displays, contemporary cars, English signage, fake readable text, subtitles, watermark, logo, distorted faces, merged faces, extra fingers, heavy blur, oversaturation, overexposure, strong HDR, luxury interior, fashion editorial styling
```

Chinese version:

```text
卡通、动漫、插画、油画、3D渲染、塑料质感、现代物件、现代手机、LED屏、当代汽车、英文招牌、虚假可读文字、字幕、水印、logo、面部扭曲、面部融合、多余手指、严重模糊、过饱和、过曝、强HDR、豪华装修、时尚大片感
```

## Lighting Phrases

- cold-chain / freezer: `冷白工业光与轻微冷雾，金属和水汽质感清晰`
- morning / daytime: `自然日光主导，真实环境反射补光`
- dusk: `傍晚侧逆光，暖色边缘光与环境冷色形成对比`
- night / roadside work: `低照度夜景，冷暖光源交叠，保留暗部细节`
- factory interior: `高窗斜光切入厂房，灰尘或水汽在光束中可见`

## Batch Output Rules

For scene lists, keep the original order. Do not compress multiple scenes into one prompt. If a scene has variants, create named variants such as:

- `空景版`
- `有人物调度版`
- `冲突剧情版`
- `产品/道具特写版`

Only create variants when useful for production; otherwise produce one strong prompt per model.
