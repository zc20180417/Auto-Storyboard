---
name: optimize-image-prompts
description: Optimize image generation prompts for cinematic scene, storyboard, character, prop, product, or poster generation. Use when the user provides rough prompts, scene lists, screenplay locations, storyboard descriptions, character/scene/prop settings, or prompt files and wants rewritten prompts for Nano Banana Pro, GPT Image 2, or other image models, especially for realistic short-drama, film still, Chinese period setting, brand-consistent, or multi-scene production workflows.
---

# Optimize Image Prompts

## Overview

Rewrite rough visual descriptions into model-ready image prompts that preserve story intent while improving controllability, period accuracy, composition, lighting, and negative constraints.

Default to practical production prompts: clear enough for batch generation, stable across scenes, and easy to paste into an API or image UI.

## Workflow

1. Identify the user's target model(s), output format, aspect ratio, and visual style.
2. Extract the essential visual facts from the source.
3. Build a reusable global style baseline when multiple prompts belong to one project.
4. Rewrite each prompt with model-specific phrasing.
5. Add controlled negative constraints without fighting the requested content.
6. Preserve IDs, scene names, episode ranges, and user-provided factual details.

If the user gives files, create a new optimized file unless they explicitly ask to overwrite the original.

## Input Handling

For each prompt or scene, preserve:

- scene number, title, episode range, location, and time of day
- required objects, props, people, action, environment, and story function
- period, region, genre, and continuity details
- existing model parameters only if they still make sense

Remove or rewrite:

- repeated low-value tags such as "4K" when better quality language is present
- syntax that only belongs to another model, such as `--neg`, unless the target model accepts it
- contradictions like "daylight night scene" or "empty room with many people"
- fake exact text requirements unless the target model is expected to render text well

## Model Targeting

Use these defaults unless the user specifies otherwise:

- **Nano Banana Pro**: Chinese structured prompt. Strong emphasis on semantic fidelity, object placement, period detail, real-world materials, and readable environment design.
- **GPT Image 2**: English natural-language prompt. Strong emphasis on concise intent, composition, lighting, production design, and explicit avoid-list.
- **Generic image model**: Chinese or bilingual prompt depending on the user's source language. Avoid model-specific syntax.

For detailed prompt templates and examples, read `references/prompt-patterns.md` only when needed.

## Rewrite Structure

For multiple scenes, output this structure:

```markdown
全局风格基准：
...

1. 场景名
出现集数：...
场景描述：...

Nano Banana Pro 优化提示词：
...

GPT Image 2 优化提示词：
...
```

For a single scene, use only the requested model sections and keep the answer concise.

## Prompt Quality Rules

Make every optimized prompt include:

- **subject and location**: what the image must show
- **production design**: period, region, materials, props, wear, signage limits
- **composition**: aspect ratio, shot size, lens feel, foreground/midground/background
- **lighting and color**: time of day, key light direction, practical lights, color restraint
- **style**: photorealistic, cinematic still, documentary realism, or the user's requested style
- **constraints**: what to avoid, especially modern objects, fake logos, watermarks, distorted anatomy, and unwanted illustration styles

Prefer concrete visual language over generic aesthetic stacking.

## Chinese Short-Drama Defaults

When the task involves Chinese short drama, period business stories, county-town factories, cold chain, retail terminals, or 1990s settings, apply these defaults:

- realistic 1990s China county-town or township production design
- used local spaces rather than polished studio sets
- paper documents, analog tools, older vehicles, worn walls, simple clothing, practical lighting
- realistic Chinese faces when people appear
- avoid modern phones, modern cars, LED displays, English signage, luxury interiors, and fashion editorial styling

## Batch File Output

When optimizing a prompt file:

1. Read the source as UTF-8.
2. Keep the original file unchanged unless asked to overwrite.
3. Save a sibling file with a clear suffix such as `_优化提示词` or `_optimized_prompts`.
4. Use UTF-8 BOM for Chinese `.txt` files on Windows if the original workflow depends on Notepad or PowerShell 5.1 compatibility.
5. Report the output path and count of processed scenes/prompts.

## Final Check

Before finalizing, verify:

- no source scene is dropped
- no required story object is removed
- model-specific syntax is not mixed accidentally
- negative constraints do not forbid required content
- the prompts remain usable without extra explanation
