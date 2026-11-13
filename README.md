# Douyin AI Explainer — 抖音 AI 科普短视频生产线

一套用 Muse 内置视频做抖音 AI 科普口播的完整工作流：一支约 25 秒的竖版视频，由三段 10 秒视频拼接而成，同一位主播、同一套衣服、同一个场景；英文口播 + 定时中文字幕；封面竖版 + 4:3 横版。

这套线已经跑了 9 支，沉淀出来的规则都在这里。

## 生产线

选题 → 脚本 → 首尾帧 → 生成 → 抽帧验证 → 波形验证 → 剪辑烧字幕 → 人工审核 → 发布复盘

## 核心规则

- **人物锁死**：一位固定主播，一个系列一套衣服，场景固定。
- **每段 fresh 生成，不用 resume**：resume 链像复印的复印件，脸和取景一段比一段走样。
- **首尾帧锁定**：每段从第 1 段首帧开场，落到自己生成的尾帧定格（中性表情）；镜头全程固定在三脚架上。
- **脚本每段 25–28 字**，三段之间差 ≤2 字；任何换词后重跑 `scripts/check-script.py`。
- **每段生成完先验后拼**：分辨率、取景（0/2/4/7/8 秒 + 尾帧）、烧进去的字幕、底噪（超 100 直接重生成）、闭眼 / 笑场、脸部特写并排比对。
- **字幕定时烧**，只在说话时出现；封面只写“AI 科普”，不写期数。
- **口播里不提公众号**：有一支因为结尾提了公众号，被平台判“引导至风险不可控渠道”，直接减少推荐。
- **每支做完复盘一次**，当天把一条规则写下来。

## 目录

```
douyin-ai-explainer/
├── SKILL.md                  # 总纲
├── README.md                 # 本文件
├── LICENSE                   # MIT
├── references/               # 按需加载的领域知识
│   ├── persona-v5.md         # 人物、服装、场景
│   ├── script-rules.md       # 脚本规则、口播红线
│   ├── prompt-template.md    # 六段式提示词模板
│   ├── verification.md       # 验证清单
│   ├── subtitles-and-covers.md  # 字幕与封面
│   └── delivery.md           # 交付与发布
└── scripts/
    ├── check-script.py       # 脚本字数检查
    ├── check-segment.py      # 说话起止与停顿检查
    └── make_cover_h.py       # 4:3 横版封面
```

## 安装

通用 Agent Skills 格式，任何支持 skills 的 AI Agent 均可装载：

```
git clone <你的仓库地址>
# 放入所用 Agent 的 skills 目录，例如：
#   Claude Code → ~/.claude/skills/douyin-ai-explainer/
```

## 许可证

MIT © 2026 FishNineteenAI
