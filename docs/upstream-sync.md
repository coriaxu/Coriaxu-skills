# Upstream Sync

This file records the latest verified upstream snapshot used to refresh third-party skills in this repository.

Last checked: 2026-10-05

> Baseline note: the `Updated from` refs below describe the working-tree content each sync replaced, not the
> previously committed content. Several 2026-08 syncs ran but were never committed, so a single commit can
> change more skills than this table marks as updated in the current round.

| Local skill | Upstream | Ref used | Status / notes |
|---|---|---|---|
| `aihot` | https://aihot.virxact.com/aihot-skill/ | fetched 2026-09-14, sha256 `d063d465` | Found upstream update: sha256 `1fe3b86d` (v2.0.0; previously `e15bd52f` / v1.7.2). NOT synced or installed: installed `SKILL.md` retains a locally customized description; fixed SKILL.md-only mapping remains unchanged |
| `darwin-skill` | https://github.com/alchaincyf/darwin-skill | `8a8b6625` | Updated from `55395164` and installed after the user explicitly requested the latest upstream version. Runtime scan now requires context review to exclude false positives. Previous local Astra rewrite was backed up outside the Skill hub |
| `dbs` | https://github.com/dontbesilent2025/dbskill | `8b8e33f1` | Found upstream update: `a0e6fa35` (v2.18.45; previous pending `a97797b9`), adds routing distinctions for related content skills. NOT synced or installed: installed `SKILL.md`, `references/composition-contract.md`, and `references/official-skill-names.txt` contain local customizations |
| `dbs-content` | https://github.com/dontbesilent2025/dbskill | `a0e6fa35` | Upstream advanced from `a97797b9`; managed content unchanged; no installation needed; CC BY-NC 4.0 and attribution retained |
| `dbs-diagnosis` | https://github.com/dontbesilent2025/dbskill | `a0e6fa35` | Upstream advanced from `a97797b9`; managed content unchanged; no installation needed; CC BY-NC 4.0 and attribution retained |
| `dbskill-knowledge` | https://github.com/dontbesilent2025/dbskill | `a0e6fa35` | Upstream advanced from `a97797b9`; managed knowledge content unchanged; README/LICENSE/SKILL wrappers and CC BY-NC 4.0 retained |
| `luban-skill` | https://github.com/LearnPrompt/luban-skill | `cea2da33` | Checked; no upstream change; existing attribution and license boundaries retained |
| `nuwa-skill` | https://github.com/alchaincyf/nuwa-skill | `fe037468` | Checked; no upstream change; existing attribution and license boundaries retained |
| `obsidian-bases` | https://github.com/kepano/obsidian-skills | `3ccff533` | Checked; no upstream change; no installation needed |
| `obsidian-markdown` | https://github.com/kepano/obsidian-skills | `3ccff533` | Checked; no upstream change; no installation needed |
| `qiaomu-epub-book-generator` | https://github.com/joeseesun/qiaomu-epub-book-generator | `c558598b` | Checked; no upstream change; existing attribution and license boundaries retained |
| `shuorenhua` | https://github.com/MrGeDiao/shuorenhua | `e7c2b867` | Updated from `9e6400d5` to v2.5.1 and installed to the shared hub. Twelve managed metadata/docs files changed; three runtime rule files remain unchanged. `.github` is excluded |
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

## 2026-10-05 verification

- All 14 managed skills and `agent-review` exist; all 10 confirmed first-party sources were reachable.
- Newly observed upstream content: `aihot` sha256 `1fe3b86d` (v2.0.0), `dbs` at dbskill `a0e6fa35` (v2.18.45), and `shuorenhua` `e7c2b867` (v2.5.1). The previously pending `darwin-skill` update at `8a8b6625` remains unsynced.
- Synced and installed only `shuorenhua`; its three runtime rule files are unchanged. Backups are in `/tmp/coriaxu-upstreams-20261005/backup`. The local customizations in `aihot`, `darwin-skill`, and `dbs` remain untouched.
- `git diff --check`, updated Skill frontmatter, targeted `./install.sh --dry-run shuorenhua`, actual install, checksum-aware repository-to-hub comparison, and all three shared entry readbacks passed.
- Repository started on `main`, even with fetched `origin/main` at `96c7181e8b20349b489ee40376e8320786677401`; unrelated working-tree changes were left untouched. No attribution or license changes were needed; dbskill CC BY-NC 4.0 boundaries remain intact.

## 2026-10-05 darwin follow-up

- On explicit user request, synced `darwin-skill` from official `55395164` to `8a8b6625` and installed it to the shared hub. Only upstream `SKILL.md` and `references/runtime-neutrality.md` changed; no other managed skills were reinstalled.
- The installed Astra rewrite of `SKILL.md` was saved byte-for-byte at `/Users/surfin/.codex/automations/coriaxu-skills/backups/darwin-skill-astra-20261005/SKILL.md` before replacement. The earlier weekly-run note above records its status at that time.
- `git diff --check`, updated Skill frontmatter, targeted install dry run, actual install, official changed-file equality, checksum-aware repository-to-hub equality, and three shared entry readbacks passed. No broader runtime evaluation was run.
