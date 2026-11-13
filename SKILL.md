# Douyin AI Explainer — 抖音 AI 科普短视频生产线

## 这是什么

抖音 AI 科普系列的整条生产线：一支约 25 秒的竖版口播，由三段 10 秒视频拼接而成，同一位主播、同一套衣服、同一个场景；英文口播 + 定时中文字幕；封面竖版 + 4:3 横版；成片以 zip 交付，发布者自己在 09:00 发布。

生成走 Muse 内置视频能力，验证用 ffmpeg/ffprobe + `scripts/` 里的检查脚本。这个 skill 只写这条生产线锁死的东西：人物、脚本、提示词、验证标准、字幕封面、交付发布。动手之前先读对应的 `references/` 文件。

## 生产线

选题 → 脚本 → 首尾帧 → 生成 → 抽帧验证 → 波形验证 → 剪辑烧字幕 → 人工审核 → 发布复盘

## 锁死的规则

- 人物 v5 锁死：诺诺 / Luna，26 岁，中法混血，黑长发，无雀斑；一个系列一套衣服；场景固定。见 `references/persona-v5.md`。
- 一支 = 三段 10 秒，每段 fresh 生成，不用 resume；首尾帧锁定，镜头全程固定。见 `references/prompt-template.md`。
- 脚本每段 25–28 字，三段之间差 ≤2 字；任何换词后重跑 `scripts/check-script.py`。英文口播；口播里不提公众号；中英混说只留 "outline"。见 `references/script-rules.md`。
- 每段生成完先验后拼：分辨率、取景、烧进去的字、底噪、闭眼 / 笑场、脸部特写并排比对。见 `references/verification.md`。
- 字幕定时烧，只在说话时出现；封面只写“AI 科普”，竖版 + 横版同一张底图。见 `references/subtitles-and-covers.md`。
- 交付一个 zip（视频 + 竖版封面 + 横版封面 + 文案），发布者自己发布；发布提醒只是提醒，绝不替发布者发。见 `references/delivery.md`。
- 每支做完复盘一次，当天把一条规则写下来。
- 生成走内置视频能力；如果内置能力不可用，先说清楚再停下，不要悄悄换工具，也不要替发布者决定换。

## 文件

- `SKILL.md` — 总纲（本文件）
- `references/persona-v5.md` — 人物、服装、场景
- `references/script-rules.md` — 脚本规则、口播红线
- `references/prompt-template.md` — 六段式提示词模板
- `references/verification.md` — 验证清单
- `references/subtitles-and-covers.md` — 字幕与封面
- `references/delivery.md` — 交付与发布
- `scripts/check-script.py` — 脚本字数检查
- `scripts/check-segment.py` — 说话起止与停顿检查
- `scripts/make_cover_h.py` — 4:3 横版封面（每支加一条 EPISODES）

## 工具

- ffmpeg / ffprobe — 抽帧、量波形、剪辑、拼接。
- `scripts/` 里的三个脚本 — 字数、说话起止、横版封面。
