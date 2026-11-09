# Upstream Sync

This file records the latest verified upstream snapshot used to refresh third-party skills in this repository.

Last checked: 2026-11-09

> Baseline note: the `Updated from` refs below describe the working-tree content each sync replaced, not the
> previously committed content. Several 2026-08 syncs ran but were never committed, so a single commit can
> change more skills than this table marks as updated in the current round.

| Local skill | Upstream | Ref used | Status / notes |
|---|---|---|---|
| `aihot` | https://aihot.virxact.com/aihot-skill/ | fetched 2026-11-09, sha256 `dfa82adb` | Updated public SKILL.md contact address and installed; service/data terms remain separate from the MIT Skill file |
| `darwin-skill` | https://github.com/alchaincyf/darwin-skill | `8a8b6625` | Checked; first-party HEAD unchanged; no installation |
| `dbs` | https://github.com/dontbesilent2025/dbskill | `bab93c03` | First-party HEAD `69e6fab2` has v3.3.0 content, but not synced: the new 2026-11-02 license bars redistribution/packaging without written permission; repository and installed pre-change CC BY-NC 4.0 snapshot retained |
| `dbs-content` | https://github.com/dontbesilent2025/dbskill | `bab93c03` | Checked; first-party HEAD `69e6fab2` has no managed content change; pre-change CC BY-NC 4.0 snapshot retained; no installation |
| `dbs-diagnosis` | https://github.com/dontbesilent2025/dbskill | `bab93c03` | Checked; first-party HEAD `69e6fab2` has no managed content change; pre-change CC BY-NC 4.0 snapshot retained; no installation |
| `dbskill-knowledge` | https://github.com/dontbesilent2025/dbskill | `bab93c03` | Checked; first-party HEAD `69e6fab2` has no managed content change; pre-change CC BY-NC 4.0 knowledge wrappers retained; no installation |
| `luban-skill` | https://github.com/LearnPrompt/luban-skill | `cea2da33` | Checked; first-party HEAD unchanged; no installation |
| `nuwa-skill` | https://github.com/alchaincyf/nuwa-skill | `fe037468` | First-party HEAD `5bb9b659` has newer content; not synced because installed SKILL.md and examples contain local rewrites. Repository snapshot and local customizations protected |
| `obsidian-bases` | https://github.com/kepano/obsidian-skills | `3ccff533` | Checked; first-party HEAD unchanged; no installation |
| `obsidian-markdown` | https://github.com/kepano/obsidian-skills | `3ccff533` | Checked; first-party HEAD unchanged; no installation |
| `qiaomu-epub-book-generator` | https://github.com/joeseesun/qiaomu-epub-book-generator | `c558598b` | Checked; first-party HEAD unchanged; no installation |
| `shuorenhua` | https://github.com/MrGeDiao/shuorenhua | `9b91ed94` | Updated and installed from first-party runtime directory `skills/shuorenhua/`: three runtime files plus unchanged root MIT LICENSE; prior development files remain available in the first-party repo and the run backup |
| `web-access` | https://github.com/eze-is/web-access | `d173a759` | Updated from `2c8bf0e1` to v2.6.0 and installed; browser data-path support and frame handling added; local-only config.env preserved, first-use data migration not run |
| `yao-meta-skill` | https://github.com/yaojingang/yao-meta-skill | `f5d8f681` | Checked; first-party HEAD unchanged; no installation |

Weekly managed pending-source item: `agent-review` (the Skill exists in this repository; a verified first-party URL is still missing).

Historical source leads outside this weekly automation: `guizang-html-ppt`, `guizang-social-card-skill`, `huashu-design`, `yao-expert-skill`, `yao-gametheory-skill`, `yao-tutorial-skill`, `devils-advocate`, `dws`, `fund-investment-strategy`, `getnote`, `hv-analysis`, `khazix-writer`, `xray-book`, `naval-perspective`, `taleb-perspective`, `x-mastery-mentor`. These entries are retained for historical context and are not part of this check.

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

## 2026-10-12 verification

- All 14 managed skills and the sole rules-card pending-source entry `agent-review` exist. All 10 confirmed first-party sources were reachable.
- New first-party refs: dbskill `a0e6fa35` -> `f24ea08a` (v2.18.50), with managed changes in `dbs`, `dbs-content`, and `dbs-diagnosis`; web-access `33eef84a` -> `2c8bf0e1`. The aihot page remains at pending sha256 `1fe3b86d` (v2.0.0). Other first-party refs are unchanged; dbskill-knowledge managed content is unchanged.
- No Skill content was synced or installed. The installed aihot, dbs, dbs-content, dbs-diagnosis, and web-access targets differ from the prior official snapshots or repository copies. The repository dbs also has local changes on upstream-overlapping paths. The installed web-access directory contains a local-only `config.env`, which the current installer would remove. All were protected from overwrite.
- The repository started on `main` even with fetched `origin/main` at `efa899acfa0b200d3886d72de2037da1f18d1c14`. Existing out-of-scope working-tree edits were untouched. No attribution or license change was required.

## 2026-10-12 user-requested follow-up

- On explicit user request after the weekly check, refreshed `aihot`, `dbs`, `dbs-content`, `dbs-diagnosis`, and `web-access` from the confirmed first-party versions above. No new Skill was added to the weekly managed list.
- Before writing, backed up the old repository and installed trees plus this ledger to `/Users/surfin/.codex/automations/coriaxu-skills/backups/20261012-requested-sync/`; verified every backup against its source. The previous custom files remain recoverable there.
- Preserved the dbskill README/LICENSE attribution wrappers and their CC BY-NC 4.0 boundary. The repository and installed managed files match. The installed web-access `config.env` remains byte-for-byte unchanged and outside the public repository.
- `git diff --check`, all five SKILL frontmatter checks, targeted `./install.sh --dry-run`, and installation of four targets through `./install.sh` passed. `web-access` was installed with an equivalent targeted rsync excluding `config.env`, because the installer would delete that user configuration. All five managed installed trees match the repository; all three existing shared entries are readable.
- Updated dbs helper Python files passed syntax checks. The web-access loopback unit tests passed all 135 cases when run with localhost access; the initial sandbox-only run could not bind `127.0.0.1`. No live browser session was started.

## 2026-10-26 verification

- All 14 managed Skill entries and the weekly pending-source entry exist. All 10 confirmed first-party sources were reachable. The aihot page SHA-256 is unchanged.
- Found managed content changes in `dbs`, `dbs-content`, `dbs-diagnosis`, `nuwa-skill`, `shuorenhua`, and `web-access`. Synced and installed the five conflict-free entries; `nuwa-skill` remains at the prior repository ref because its installed copy contains local rewrites. The dbskill knowledge directory is unchanged at the new upstream ref.
- Backed up the previous repository and installed trees for the five updated entries and this ledger under `/Users/surfin/.codex/automations/coriaxu-skills/backups/20261026-weekly-sync/`, with byte-level verification. Existing out-of-scope working-tree changes were left untouched.
- `git diff --check`, five basic YAML frontmatter checks, the targeted installer dry run for four entries, and a protected web-access rsync dry run passed. Installed the four entries through `install.sh`; installed web-access with `config.env` excluded and confirmed unchanged. All five installed trees match repository content (aside from that protected config), and the three shared skill entry links can read them.
- `shuorenhua` structure check passed (123 cases, 60 links) after two links to the excluded `.github` issue template were redirected to its pinned first-party GitHub file; two upstream trailing-space instances were removed mechanically. Eight web-access Node test files passed. The dbs helper Python syntax and targeted handoff discovery check passed. No live browser or model evaluation was run.
- Existing source and license attributions remain current; dontbesilent CC BY-NC 4.0 files were preserved. The repository started on `main`, even with fetched `origin/main`, with no historical unpushed commits.

## 2026-11-02 verification

- All 14 confirmed managed Skill entries and `agent-review` exist. All 10 first-party sources were reachable; the public aihot SKILL.md SHA-256 is unchanged.
- dbskill advanced from `707725c8` to `bab93c03`; managed content changed only in `dbs` and `dbs-diagnosis`. `dbs-content` and `dbskill-knowledge` were checked and left uninstalled. shuorenhua advanced from `e33d5eb6` to `0a001940`; its evaluation tools and documentation changed, while its SKILL.md stayed the same.
- Synced and installed `dbs`, `dbs-diagnosis`, and `shuorenhua` only. Backed up their previous repository and installed trees and this ledger under `/tmp/coriaxu-upstreams-20261102/backup`, with file-level verification before writing. Existing out-of-scope working-tree edits were preserved.
- `nuwa-skill` remains unsynced at repository ref `fe037468`: first-party HEAD `7c7edfeb` is newer, but installed local rewrites still conflict. No automatic replacement or installation was attempted.
- `git diff --check`, three updated-Skill frontmatter checks, targeted `install.sh --dry-run`, actual installation, repository-to-hub tree equality, and all three shared entry readbacks passed. shuorenhua structure check passed (123 cases, 60 links), and 78 relevant unit tests passed; dbs Python helpers compiled. Two excluded issue-template links were pinned to the new upstream ref, and two upstream trailing-space instances were removed mechanically.
- Existing source/license attributions remain current; dontbesilent CC BY-NC 4.0 README/LICENSE wrappers were retained.

## 2026-11-09 verification

- All 14 confirmed managed Skill entries and the existing pending-source entry exist. All 10 first-party sources were reachable. The run began on `main`, aligned with `origin/main`, with no historical unpushed commit.
- Found first-party updates in aihot (SHA-256 `1fe3b86d` -> `dfa82adb`), dbskill (`bab93c03` -> `69e6fab2`), nuwa-skill (`7c7edfeb` -> `5bb9b659` since the prior check), and shuorenhua (`0a001940` -> `9b91ed94`). dbskill managed content changed only in `dbs`; its new license forbids redistribution and packaging without written permission, so the repository and installed pre-change CC BY-NC 4.0 snapshot remain. nuwa-skill remains unsynced because installed local rewrites conflict.
- Synced and installed `aihot` and `shuorenhua` only. shuorenhua now uses the author's three-file runtime directory plus its unchanged root MIT LICENSE; prior development files remain in first-party Git, local Git history and the verified run backup at `/tmp/coriaxu-upstreams-20261109/backup`. Existing out-of-scope working-tree changes were preserved.
- `git diff --check`, two frontmatter checks, targeted `install.sh --dry-run`, actual targeted installation, first-party content equality, repository-to-hub equality, and readback through all three shared entries passed. The author's full-source `automation/check_repo.py` passed 123 cases and 65 links before packaging; no model evaluation was run.
- Updated README, CREDITS and origin-audit to distinguish the retained CC BY-NC 4.0 snapshot from the newly restricted dbskill upstream license.
