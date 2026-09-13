# Upstream Sync

This file records the latest verified upstream snapshot used to refresh third-party skills in this repository.

Last checked: 2026-09-14

> Baseline note: the `Updated from` refs below describe the working-tree content each sync replaced, not the
> previously committed content. Several 2026-08 syncs ran but were never committed, so a single commit can
> change more skills than this table marks as updated in the current round.

| Local skill | Upstream | Ref used | Status / notes |
|---|---|---|---|
| `aihot` | https://aihot.virxact.com/aihot-skill/ | fetched 2026-09-14, sha256 `d063d465` | Updated from `5c6dddbd`; v1.7.0 adds Codex reset-event queries and explicit handling of unknown reset times. Fixed-rule SKILL.md-only sync; linked references are not included in this source mapping |
| `darwin-skill` | https://github.com/alchaincyf/darwin-skill | `55395164` | Checked; no upstream change; existing attribution and license boundaries retained |
| `dbs` | https://github.com/dontbesilent2025/dbskill | `8b8e33f1` | Checked; no upstream change; existing attribution and license boundaries retained |
| `dbs-content` | https://github.com/dontbesilent2025/dbskill | `8b8e33f1` | Checked; no upstream change; existing attribution and license boundaries retained |
| `dbs-diagnosis` | https://github.com/dontbesilent2025/dbskill | `8b8e33f1` | Checked; no upstream change; existing attribution and license boundaries retained |
| `dbskill-knowledge` | https://github.com/dontbesilent2025/dbskill | `8b8e33f1` | Checked; no upstream change; existing attribution and license boundaries retained |
| `luban-skill` | https://github.com/LearnPrompt/luban-skill | `cea2da33` | Checked; no upstream change; existing attribution and license boundaries retained |
| `nuwa-skill` | https://github.com/alchaincyf/nuwa-skill | `fe037468` | Checked; no upstream change; existing attribution and license boundaries retained |
| `obsidian-bases` | https://github.com/kepano/obsidian-skills | `8ccef29` | Upstream advanced from `a1dc48e6`; managed content and LICENSE unchanged; no installation needed |
| `obsidian-markdown` | https://github.com/kepano/obsidian-skills | `8ccef29` | Upstream advanced from `a1dc48e6`; managed content and LICENSE unchanged; no installation needed |
| `qiaomu-epub-book-generator` | https://github.com/joeseesun/qiaomu-epub-book-generator | `c558598b` | Checked; no upstream change; existing attribution and license boundaries retained |
| `shuorenhua` | https://github.com/MrGeDiao/shuorenhua | `5a9eafe` | Updated from `d2d0ce27`; v2.5.0 consolidates editing rules into three runtime files, archives legacy rules, and rebuilds evaluations |
| `web-access` | https://github.com/eze-is/web-access | `33eef84a` | Checked; no upstream change; existing attribution and license boundaries retained |
| `yao-meta-skill` | https://github.com/yaojingang/yao-meta-skill | `f5d8f681` | Checked; no upstream change; existing attribution and license boundaries retained |

Still missing a verified upstream URL: `guizang-html-ppt`, `guizang-social-card-skill`, `huashu-design`, `yao-expert-skill`, `yao-gametheory-skill`, `yao-tutorial-skill`, `agent-review`, `devils-advocate`, `dws`, `fund-investment-strategy`, `getnote`, `hv-analysis`, `khazix-writer`, `xray-book`, `naval-perspective`, `taleb-perspective`, `x-mastery-mentor`.
