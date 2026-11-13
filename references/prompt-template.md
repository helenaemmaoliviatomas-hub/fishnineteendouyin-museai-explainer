# 六段式提示词模板

每段生成提示词按六段写：时长画幅 / 人物 / 场景 / 节拍时间轴 / 镜头语言 / 声音 / 对白 / 限制清单。

## 锁死的写法

- 时长画幅：10 秒，竖版 9:16。
- 人物：按 `references/persona-v5.md` 写全（年龄、混血、黑长发、无雀斑、当批服装），每段都写，不要只写“同上”。
- 镜头语言（逐字用）：“completely static and locked off on a tripod, no zoom/pan/tilt, framing identical first to last frame”。
- 首尾帧：第一张图就是首帧（第 1 段已验过的帧 0），第二张图就是尾帧；视频从首帧动到尾帧。
- 尾帧定格：同姿势同取景，只变结尾表情；用嘴闭、无表情的中性脸，不要微笑——微笑会被模型放大成结尾笑场。尾帧上手放腿上、保持静止。
- 声音：“no background noise or hum at any time”，“全程不要呼吸声、喘气声”。
- 画面干净：“no text, no captions, no subtitles, no words on screen at any time”——写一遍不够就加重写明，模型自己烧进去的字幕只能重生成，不能后期盖。
- 对白：只写本段英文台词，不要加中文解释，不要夹英文词（除 "outline"）。

## 生成方式

- 每段 fresh 生成，不用 resume：resume 链像复印的复印件，脸和取景一段比一段走样，还会锁死中文语音。
- 后段 key 在前段已验过的尾帧定格 + 脸锚点 + 人物参考图上，不用 resume 操作。
- 一段只试第 1 段先行：先过第 1 段再开后两段。
- 如果工具不能从参考图 fresh 生成，先说清楚再停下，不要悄悄退回 resume 链。
