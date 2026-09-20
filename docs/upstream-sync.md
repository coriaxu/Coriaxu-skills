# Upstream Sync

This file records the latest verified upstream snapshot used to refresh third-party skills in this repository.

Last checked: 2026-09-21

> Baseline note: the `Updated from` refs below describe the working-tree content each sync replaced, not the
> previously committed content. Several 2026-08 syncs ran but were never committed, so a single commit can
> change more skills than this table marks as updated in the current round.

| Local skill | Upstream | Ref used | Status / notes |
|---|---|---|---|
| `aihot` | https://aihot.virxact.com/aihot-skill/ | fetched 2026-09-14, sha256 `d063d465` | Found upstream update: sha256 `5b2861bb` (v1.7.1), adds compression and stable query URL guidance. NOT synced or installed: `/Users/surfin/.agent/skills/aihot/SKILL.md` has a locally customized description; retained repository baseline and local customization. Fixed-rule SKILL.md-only mapping still omits linked references |
| `darwin-skill` | https://github.com/alchaincyf/darwin-skill | `55395164` | Found upstream update: `8a8b6625`, excludes quoted examples and scan commands from runtime-drift false positives. NOT synced or installed: `/Users/surfin/.agent/skills/darwin-skill/SKILL.md` is a locally rewritten Astra edition; retained recorded baseline |
| `dbs` | https://github.com/dontbesilent2025/dbskill | `8b8e33f1` | Checked; no upstream change; existing attribution and license boundaries retained |
| `dbs-content` | https://github.com/dontbesilent2025/dbskill | `8b8e33f1` | Checked; no upstream change; existing attribution and license boundaries retained |
| `dbs-diagnosis` | https://github.com/dontbesilent2025/dbskill | `8b8e33f1` | Checked; no upstream change; existing attribution and license boundaries retained |
| `dbskill-knowledge` | https://github.com/dontbesilent2025/dbskill | `8b8e33f1` | Checked; no upstream change; existing attribution and license boundaries retained |
| `luban-skill` | https://github.com/LearnPrompt/luban-skill | `cea2da33` | Checked; no upstream change; existing attribution and license boundaries retained |
| `nuwa-skill` | https://github.com/alchaincyf/nuwa-skill | `fe037468` | Checked; no upstream change; existing attribution and license boundaries retained |
| `obsidian-bases` | https://github.com/kepano/obsidian-skills | `3ccff533` | Upstream advanced from `8ccef29`; managed content and LICENSE unchanged; no installation needed |
| `obsidian-markdown` | https://github.com/kepano/obsidian-skills | `3ccff533` | Upstream advanced from `8ccef29`; managed content and LICENSE unchanged; no installation needed |
| `qiaomu-epub-book-generator` | https://github.com/joeseesun/qiaomu-epub-book-generator | `c558598b` | Checked; no upstream change; existing attribution and license boundaries retained |
| `shuorenhua` | https://github.com/MrGeDiao/shuorenhua | `5a9eafe` | Checked; no upstream change; existing attribution and license boundaries retained |
| `web-access` | https://github.com/eze-is/web-access | `33eef84a` | Checked; no upstream change; existing attribution and license boundaries retained |
| `yao-meta-skill` | https://github.com/yaojingang/yao-meta-skill | `f5d8f681` | Checked; no upstream change; existing attribution and license boundaries retained |

Still missing a verified upstream URL: `guizang-html-ppt`, `guizang-social-card-skill`, `huashu-design`, `yao-expert-skill`, `yao-gametheory-skill`, `yao-tutorial-skill`, `agent-review`, `devils-advocate`, `dws`, `fund-investment-strategy`, `getnote`, `hv-analysis`, `khazix-writer`, `xray-book`, `naval-perspective`, `taleb-perspective`, `x-mastery-mentor`.

## 2026-09-21 verification

- All 14 managed skills and the sole rules-card pending-source entry `agent-review` exist. All 10 first-party sources were reachable.
- Found content updates in `aihot` and `darwin-skill`; neither was synced because installation would overwrite the local customizations identified above. Repository skill files and local installations were left unchanged.
- Obsidian source advanced, but both managed skill trees and the root LICENSE match the recorded content.
- No install or dry run was performed; there are no updated skills to install. Existing shared entries remain readable.
- Repository started on `main`, even with `origin/main`, with unrelated local edits preserved. This run changes only this ledger.
