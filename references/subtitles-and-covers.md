# 字幕与封面

## 定时中文字幕

- 从 .ass 烧，短语窗口按 CUT 文件的细 RMS 量，不要按原片量。
- 每个短语只在说话时出现；停顿是干净画面。成品要在说话处和停顿处都验一遍。
- 样式：Noto Sans CJK SC，86px（PlayRes 1080x1920），白字 + 50% 黑底框（BorderStyle 3），底部居中，MarginV 120。
- 字体文件是 .ttc，在 `/usr/share/fonts/opentype/noto/`（NotoSansCJK-Bold.ttc / -Regular.ttc），不在 truetype/ 下找 .otf。
- 写 .ass 用 muse.write，别用 heredoc（heredoc 可能丢第一行）。
- 剪辑又烧字幕时，把 scale+ass 也写进 filter_complex 的视频链里；`-vf` 和 `-filter_complex` 不能同时用在同一个流上。

## 封面

- 从原片里量过的静帧取：嘴闭、中性表情，不要说话中途的帧。
- 徽章只写“AI 科普”，不写期数；文字放底部，不要放顶部，也不要超过桌线。
- 竖版 1080x1920 和 4:3 横版 1440x1080 各一张，同一张底图；做竖版的同时做横版。
- 横版用 `scripts/make_cover_h.py`：每支在 EPISODES 里加一条（源静帧、标题两行、输出路径）；源静帧是 1080x1920 的图，脚本取 y 150–960 的带子。
- 改过的封面用新文件名重发，不要覆盖旧文件——旧图会在聊天里缓存。
- 封面发 JPG，不要发 webp。
