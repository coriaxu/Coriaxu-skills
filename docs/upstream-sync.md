# Upstream Sync

This file records the latest verified upstream snapshot used to refresh third-party skills in this repository.

Last checked: 2026-07-27

| Local skill | Upstream | Ref used | Status / notes |
|---|---|---|---|
| `aihot` | https://aihot.virxact.com/aihot-skill/ | fetched 2026-07-27, sha256 `4f5837b0` | Updated from `e9576960`; v1.1.2 strengthens API routing, caching, and safe handling of untrusted returned content |
| `darwin-skill` | https://github.com/alchaincyf/darwin-skill | `7c7b7909` | Checked; no upstream change |
| `dbs` | https://github.com/dontbesilent2025/dbskill | `b862fa83` | Updated from `daca0716`; adds the cross-Skill handoff contract and standard-answer routing; CC BY-NC 4.0 boundary retained |
| `dbs-content` | https://github.com/dontbesilent2025/dbskill | `b862fa83` | Updated handoff guidance to return to `/dbs`; CC BY-NC 4.0 boundary retained |
| `dbs-diagnosis` | https://github.com/dontbesilent2025/dbskill | `b862fa83` | Updated boundary and handoff guidance to preserve diagnosis context; CC BY-NC 4.0 boundary retained |
| `dbskill-knowledge` | https://github.com/dontbesilent2025/dbskill | `b862fa83` | Updated upstream `原子库/README.md`; local wrapper `README.md` / `LICENSE` / `SKILL.md` retained |
| `luban-skill` | https://github.com/LearnPrompt/luban-skill | `cea2da3` | Upstream advanced from `89b1f0dd`; checked its relocated `skills/luban/` source and found no change to the included skill files |
| `nuwa-skill` | https://github.com/alchaincyf/nuwa-skill | `72857dc` | Updated from `550a8e1`; added community contribution docs, fidelity scorecards, English triggers, cost-tier guidance, and failure/checkpoint safeguards |
| `obsidian-bases` | https://github.com/kepano/obsidian-skills | `a1dc48e6` | Checked; no upstream change; local attribution README retained |
| `obsidian-markdown` | https://github.com/kepano/obsidian-skills | `a1dc48e6` | Checked; no upstream change |
| `qiaomu-epub-book-generator` | https://github.com/joeseesun/qiaomu-epub-book-generator | `c558598b` | Checked; no upstream change |
| `shuorenhua` | https://github.com/MrGeDiao/shuorenhua | `6318b703` | Updated from `bbcb0062`; strengthens fact, relation, and protected-span preservation during rewrites |
| `web-access` | https://github.com/eze-is/web-access | `7af34af6` | Checked; no upstream change |
| `yao-meta-skill` | https://github.com/yaojingang/yao-meta-skill | `e15472e1` | Updated from `4eb11f9`; updates evaluation, registry, reports and governance tooling |

Still missing a verified upstream URL: `guizang-html-ppt`, `guizang-social-card-skill`, `huashu-design`, `yao-expert-skill`, `yao-gametheory-skill`, `yao-tutorial-skill`, `agent-review`, `career-skill-planner`, `ljg-card`, `ljg-roundtable`, `三级笔记`, `devils-advocate`, `dws`, `fund-investment-strategy`, `getnote`, `hv-analysis`, `khazix-writer`, `xray-book`, `naval-perspective`, `taleb-perspective`, `x-mastery-mentor`.
