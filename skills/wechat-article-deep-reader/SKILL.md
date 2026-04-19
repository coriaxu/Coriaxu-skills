---
name: wechat-article-deep-reader
description: 稳定抓取微信公众号文章并输出“主旨-论证-细节”三级阅读笔记。适用于用户提供 mp.weixin.qq.com 链接并要求提炼大纲、结构化阅读、总结要点、整理三级笔记等场景。
---

# WeChat Article Deep Reader

## Overview

执行微信文章双引擎抓取，并直接产出固定结构的三级阅读笔记。
默认输出中文，不包含国内版海外版对比，也不输出证据分级章节。

## Workflow

1. 执行脚本抓取文章正文并完成字段归一化。
2. 按“主旨-论证-细节”模板生成三级阅读笔记。
3. 输出 Markdown，可选同时输出 JSON。

## Quick Start

```bash
python3 ~/.codex/skills/wechat-article-deep-reader/scripts/wechat_reader.py \
  --url "https://mp.weixin.qq.com/s/xxxx"
```

```bash
python3 ~/.codex/skills/wechat-article-deep-reader/scripts/wechat_reader.py \
  --url "https://mp.weixin.qq.com/s/xxxx" \
  --note-output /tmp/wechat_note.md \
  --json /tmp/wechat_note.json
```

## Script Interface

- `--url` 必填，微信公众号文章链接。
- `--note-output` 可选，三级笔记 Markdown 文件路径。
- `--json` 可选，结构化 JSON 文件路径。
- `--force-fallback` 可选，跳过直连抓取并直接走回退引擎。

## Output Contract

JSON 固定字段：

- `success`
- `engine_used`
- `article`
  - `title`
  - `account_name`
  - `publish_time`
  - `content_text`
  - `source_url`
- `three_level_note`
  - `level1_main_thesis`
  - `level2_argument_chain`
  - `level3_key_details`

Markdown 固定结构：

- `# 一级 主旨与框架`
- `# 二级 论证链条`
- `# 三级 关键细节与原文表达`

## Writing Rules

- 严格按三级结构输出，不追加其他章节。
- 保留原文关键词和关键表达，避免过度改写。
- 仅做内容提炼和结构化整理，不主动给行动建议。

## References

- 三级模板与风格约束见 `references/three-level-template.md`
