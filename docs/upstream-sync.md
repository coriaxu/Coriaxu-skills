# Upstream Sync

This file records the latest verified upstream snapshot used to refresh third-party skills in this repository.

Last checked: 2026-09-28

> Baseline note: the `Updated from` refs below describe the working-tree content each sync replaced, not the
> previously committed content. Several 2026-08 syncs ran but were never committed, so a single commit can
> change more skills than this table marks as updated in the current round.

| Local skill | Upstream | Ref used | Status / notes |
|---|---|---|---|
| `aihot` | https://aihot.virxact.com/aihot-skill/ | fetched 2026-09-14, sha256 `d063d465` | Found upstream update: sha256 `e15bd52f` (v1.7.2; last check saw `5b2861bb` / v1.7.1), adds HTTP compression and stable query URL guidance and clarifies reset wording. NOT synced or installed: `/Users/surfin/.agent/skills/aihot/SKILL.md` retains a locally customized description. Fixed-rule SKILL.md-only mapping still omits linked references |
| `darwin-skill` | https://github.com/alchaincyf/darwin-skill | `55395164` | Found upstream update remains `8a8b6625` (same as last check): runtime scan false-positive handling. NOT synced or installed: `/Users/surfin/.agent/skills/darwin-skill/SKILL.md` retains a locally rewritten Astra edition |
| `dbs` | https://github.com/dontbesilent2025/dbskill | `8b8e33f1` | Found upstream update: `a97797b9` (v2.18.44), adds numbered prompts and catalog queries. NOT synced or installed: local customizations in `/Users/surfin/.agent/skills/dbs/SKILL.md`, `references/composition-contract.md`, and `references/official-skill-names.txt`; repository baseline retained |
| `dbs-content` | https://github.com/dontbesilent2025/dbskill | `a97797b9` | Upstream advanced from `8b8e33f1`; managed content unchanged; no installation needed; CC BY-NC 4.0 and attribution retained |
| `dbs-diagnosis` | https://github.com/dontbesilent2025/dbskill | `a97797b9` | Upstream advanced from `8b8e33f1`; managed content unchanged; no installation needed; CC BY-NC 4.0 and attribution retained |
| `dbskill-knowledge` | https://github.com/dontbesilent2025/dbskill | `a97797b9` | Upstream advanced from `8b8e33f1`; managed knowledge content unchanged; README/LICENSE/SKILL wrappers and CC BY-NC 4.0 retained |
| `luban-skill` | https://github.com/LearnPrompt/luban-skill | `cea2da33` | Checked; no upstream change; existing attribution and license boundaries retained |
| `nuwa-skill` | https://github.com/alchaincyf/nuwa-skill | `fe037468` | Checked; no upstream change; existing attribution and license boundaries retained |
| `obsidian-bases` | https://github.com/kepano/obsidian-skills | `3ccff533` | Checked; no upstream change; no installation needed |
| `obsidian-markdown` | https://github.com/kepano/obsidian-skills | `3ccff533` | Checked; no upstream change; no installation needed |
| `qiaomu-epub-book-generator` | https://github.com/joeseesun/qiaomu-epub-book-generator | `c558598b` | Checked; no upstream change; existing attribution and license boundaries retained |
| `shuorenhua` | https://github.com/MrGeDiao/shuorenhua | `9e6400d5` | Updated from `5a9eafe` and installed to the shared hub. Four files changed: Grok evaluation tool/context isolation and offline tests, plus README and contribution guidance. Skill entry remains v2.5.0 |
| `web-access` | https://github.com/eze-is/web-access | `33eef84a` | Checked; no upstream change; existing attribution and license boundaries retained |
| `yao-meta-skill` | https://github.com/yaojingang/yao-meta-skill | `f5d8f681` | Checked; no upstream change; existing attribution and license boundaries retained |

Still missing a verified upstream URL: `guizang-html-ppt`, `guizang-social-card-skill`, `huashu-design`, `yao-expert-skill`, `yao-gametheory-skill`, `yao-tutorial-skill`, `agent-review`, `devils-advocate`, `dws`, `fund-investment-strategy`, `getnote`, `hv-analysis`, `khazix-writer`, `xray-book`, `naval-perspective`, `taleb-perspective`, `x-mastery-mentor`.

## 2026-09-28 verification

- All 14 managed skills and the sole rules-card pending-source entry `agent-review` exist. All 10 first-party sources were reachable.
- Found content updates relative to repository baselines in `aihot`, `darwin-skill`, `dbs`, and `shuorenhua`. Only `shuorenhua` was synced and installed; the other three retain the local customizations identified above.
- Backed up the updated repository and installed tree plus metadata in `/tmp/coriaxu-upstreams-20260928/backup`; symlinks are preserved. No user files were deleted. Existing unrelated working-tree edits were left untouched.
- `git diff --check`, updated-Skill basic YAML frontmatter, targeted `./install.sh --dry-run shuorenhua`, and `./install.sh shuorenhua` passed. All 103 installed files/symlinks match the repository, and the three existing shared entries are readable without link changes.
- The complete first-party source passed `automation/check_repo.py` (123 cases). The synced repository passed 92 evaluation unit tests plus 12 runtime tests; no live model evaluation was run.
- Corrected stale Darwin license descriptions in `CREDITS.md` and `docs/origin-audit.md` after checking the existing MIT LICENSE. Other source and license boundaries remain unchanged.
- Repository started on `main`, even with fetched `origin/main` at `2c967c1aab9eaad2d84e3cc617a18d21bc084bfa`. Only this run's four Skill files and three metadata files are eligible for its commit and push.
