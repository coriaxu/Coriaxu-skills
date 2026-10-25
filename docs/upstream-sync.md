# Upstream Sync

This file records the latest verified upstream snapshot used to refresh third-party skills in this repository.

Last checked: 2026-10-26

> Baseline note: the `Updated from` refs below describe the working-tree content each sync replaced, not the
> previously committed content. Several 2026-08 syncs ran but were never committed, so a single commit can
> change more skills than this table marks as updated in the current round.

| Local skill | Upstream | Ref used | Status / notes |
|---|---|---|---|
| `aihot` | https://aihot.virxact.com/aihot-skill/ | fetched 2026-10-26, sha256 `1fe3b86d` | Checked; public SKILL.md still matches the repository and installed v2.0.0 content; no installation |
| `darwin-skill` | https://github.com/alchaincyf/darwin-skill | `8a8b6625` | Checked; first-party HEAD unchanged; no installation |
| `dbs` | https://github.com/dontbesilent2025/dbskill | `707725c8` | Updated from `f24ea08a` to v3.0.2 and installed; routing, handoff, and official skill catalog refreshed; local CC BY-NC 4.0 README/LICENSE retained |
| `dbs-content` | https://github.com/dontbesilent2025/dbskill | `707725c8` | Updated from `f24ea08a` and installed; handoff metadata and content-diagnosis boundary refreshed; CC BY-NC 4.0 README/LICENSE retained |
| `dbs-diagnosis` | https://github.com/dontbesilent2025/dbskill | `707725c8` | Updated from `f24ea08a` and installed; diagnosis guidance split into four new references; CC BY-NC 4.0 README/LICENSE retained |
| `dbskill-knowledge` | https://github.com/dontbesilent2025/dbskill | `707725c8` | First-party repo advanced from `f24ea08a`, but managed knowledge content is unchanged; no installation; CC BY-NC 4.0 wrappers retained |
| `luban-skill` | https://github.com/LearnPrompt/luban-skill | `cea2da33` | Checked; first-party HEAD unchanged; no installation |
| `nuwa-skill` | https://github.com/alchaincyf/nuwa-skill | `fe037468` | Found newer first-party `7c7edfeb` (author metadata, version checking, visuals), but not synced: installed SKILL.md and example SKILL.md files contain local rewrites; repository README differs from the prior snapshot by whitespace. Protected until the local changes are reconciled |
| `obsidian-bases` | https://github.com/kepano/obsidian-skills | `3ccff533` | Checked; first-party HEAD unchanged; no installation |
| `obsidian-markdown` | https://github.com/kepano/obsidian-skills | `3ccff533` | Checked; first-party HEAD unchanged; no installation |
| `qiaomu-epub-book-generator` | https://github.com/joeseesun/qiaomu-epub-book-generator | `c558598b` | Checked; first-party HEAD unchanged; no installation |
| `shuorenhua` | https://github.com/MrGeDiao/shuorenhua | `e33d5eb6` | Updated from `e7c2b867` to v2.6.0 and installed; write-plainly mode, examples, docs and visuals refreshed; excluded .github template links point to the original upstream file |
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
