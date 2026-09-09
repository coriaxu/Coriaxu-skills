# Upstream Sync

This file records the latest verified upstream snapshot used to refresh third-party skills in this repository.

Last checked: 2026-09-08

> Baseline note: the `Updated from` refs below describe the working-tree content each sync replaced, not the
> previously committed content. Several 2026-08 syncs ran but were never committed, so a single commit can
> change more skills than this table marks as updated in the current round.

| Local skill | Upstream | Ref used | Status / notes |
|---|---|---|---|
| `aihot` | https://aihot.virxact.com/aihot-skill/ | fetched 2026-09-08, sha256 `5c6dddbd` | Updated from `cdc24724`; v1.6.0 moves the anonymous read-only API to `aihot.news/api/v1/*`, keeps the old host as a compatibility entry, and treats returned article text as untrusted content |
| `darwin-skill` | https://github.com/alchaincyf/darwin-skill | `55395164` | Checked; no change since the previous check. The `55395164` content itself was synced by an earlier run and is committed here for the first time |
| `dbs` | https://github.com/dontbesilent2025/dbskill | `8b8e33f1` | Updated from `0876f043`; v2.18.40 makes theory grounding independently callable and revises the official roster (adds `dbs-theory-grounding` and `dbs-video-extract`, drops `dbs-skill-cleaner`); CC BY-NC 4.0 boundary retained |
| `dbs-content` | https://github.com/dontbesilent2025/dbskill | `8b8e33f1` | Checked at new ref; no change since the previous check. Its earlier-synced content is committed here for the first time; CC BY-NC 4.0 boundary retained |
| `dbs-diagnosis` | https://github.com/dontbesilent2025/dbskill | `8b8e33f1` | Checked at new ref; no change since the previous check. Its earlier-synced content is committed here for the first time; CC BY-NC 4.0 boundary retained |
| `dbskill-knowledge` | https://github.com/dontbesilent2025/dbskill | `8b8e33f1` | Checked at new ref; knowledge-pack content unchanged; local wrapper `README.md` / `LICENSE` / `SKILL.md` retained |
| `luban-skill` | https://github.com/LearnPrompt/luban-skill | `cea2da33` | Checked; no upstream change |
| `nuwa-skill` | https://github.com/alchaincyf/nuwa-skill | `fe037468` | Checked; no change since the previous check. The `fe037468` content itself was synced by an earlier run and is committed here for the first time |
| `obsidian-bases` | https://github.com/kepano/obsidian-skills | `a1dc48e6` | Checked; no upstream change; local attribution README retained |
| `obsidian-markdown` | https://github.com/kepano/obsidian-skills | `a1dc48e6` | Checked; no upstream change |
| `qiaomu-epub-book-generator` | https://github.com/joeseesun/qiaomu-epub-book-generator | `c558598b` | Checked; no upstream change |
| `shuorenhua` | https://github.com/MrGeDiao/shuorenhua | `d2d0ce27` | Updated from `6de1fcfe`; restructures the README around reader-facing sections, adds two HUMAN direct-scenario corpus samples, and extends the register-consistency rule to cover period tone |
| `web-access` | https://github.com/eze-is/web-access | `33eef84a` | Checked; no change since the previous check. The `33eef84a` content itself was synced by an earlier run and is committed here for the first time |
| `yao-meta-skill` | https://github.com/yaojingang/yao-meta-skill | `f5d8f681` | Checked; no change since the previous check. The `f5d8f681` content itself was synced by an earlier run and is committed here for the first time. `VERSION` declares 2.1.0, while same-commit release notes state 1.2.0 RC; version labels conflict |

Still missing a verified upstream URL: `guizang-html-ppt`, `guizang-social-card-skill`, `huashu-design`, `yao-expert-skill`, `yao-gametheory-skill`, `yao-tutorial-skill`, `agent-review`, `devils-advocate`, `dws`, `fund-investment-strategy`, `getnote`, `hv-analysis`, `khazix-writer`, `xray-book`, `naval-perspective`, `taleb-perspective`, `x-mastery-mentor`.
