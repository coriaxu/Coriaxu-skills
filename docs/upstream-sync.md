# Upstream Sync

This file records the latest verified upstream snapshot used to refresh third-party skills in this repository.

Last checked: 2026-09-26

> Baseline note: the `Updated from` refs below describe the working-tree content each sync replaced, not the
> previously committed content. Several 2026-08 syncs ran but were never committed, so a single commit can
> change more skills than this table marks as updated in the current round.

| Local skill | Upstream | Ref used | Status / notes |
|---|---|---|---|
| `aihot` | https://aihot.virxact.com/aihot-skill/ | fetched 2026-09-14, sha256 `d063d465` | NOT re-checked on 2026-09-26: the run environment's network policy blocked `aihot.virxact.com` and `aihot.news`. The 2026-09-21 finding still stands: upstream v1.7.1 (sha256 `5b2861bb`) exists but was not synced; `/Users/surfin/.agent/skills/aihot/SKILL.md` has a locally customized description. Fixed-rule SKILL.md-only mapping still omits linked references |
| `darwin-skill` | https://github.com/alchaincyf/darwin-skill | `8a8b6625` | Updated from `55395164`; runtime-drift scan no longer flags quoted examples and scan commands inside a skill's own rules as P0 (self-reference false positive). Repository copy only; NOT installed: `/Users/surfin/.agent/skills/darwin-skill/SKILL.md` is a locally rewritten Astra edition that `./install.sh darwin-skill` would overwrite |
| `dbs` | https://github.com/dontbesilent2025/dbskill | `3ec74054` | Updated from `8b8e33f1`; v2.18.42 adds numbered hidden prompts (`/dbs <三位编号>`) and a hidden-prompt catalog query, fetched at runtime from the upstream GitHub repo with SHA-256 checks (adds `numbered-prompts/` and `scripts/numbered-prompts.py`); local wrapper `README.md` / `LICENSE` retained; CC BY-NC 4.0 boundary retained |
| `dbs-content` | https://github.com/dontbesilent2025/dbskill | `3ec74054` | Checked at new ref; no change; CC BY-NC 4.0 boundary retained |
| `dbs-diagnosis` | https://github.com/dontbesilent2025/dbskill | `3ec74054` | Checked at new ref; no change; CC BY-NC 4.0 boundary retained |
| `dbskill-knowledge` | https://github.com/dontbesilent2025/dbskill | `3ec74054` | Checked at new ref; knowledge-pack content unchanged; local wrapper `README.md` / `LICENSE` / `SKILL.md` retained |
| `luban-skill` | https://github.com/LearnPrompt/luban-skill | `cea2da33` | Checked; no upstream change; existing attribution and license boundaries retained |
| `nuwa-skill` | https://github.com/alchaincyf/nuwa-skill | `fe037468` | Checked; no upstream change; existing attribution and license boundaries retained |
| `obsidian-bases` | https://github.com/kepano/obsidian-skills | `3ccff533` | Checked; no upstream change; existing attribution and license boundaries retained |
| `obsidian-markdown` | https://github.com/kepano/obsidian-skills | `3ccff533` | Checked; no upstream change; existing attribution and license boundaries retained |
| `qiaomu-epub-book-generator` | https://github.com/joeseesun/qiaomu-epub-book-generator | `c558598b` | Checked; no upstream change; existing attribution and license boundaries retained |
| `shuorenhua` | https://github.com/MrGeDiao/shuorenhua | `cd681637` | Updated from `5a9eafe`; eval runner makes the Grok judge truly tool-free and isolates local skills in code (with tests); README documents the known gap of light cleanup on long texts. Also restores upstream trailing line breaks in `evals/results-v2.1.0.md` |
| `web-access` | https://github.com/eze-is/web-access | `33eef84a` | Checked; no upstream change; existing attribution and license boundaries retained |
| `yao-meta-skill` | https://github.com/yaojingang/yao-meta-skill | `f5d8f681` | Checked; no upstream change; existing attribution and license boundaries retained |

Still missing a verified upstream URL: `guizang-html-ppt`, `guizang-social-card-skill`, `huashu-design`, `yao-expert-skill`, `yao-gametheory-skill`, `yao-tutorial-skill`, `agent-review`, `devils-advocate`, `dws`, `fund-investment-strategy`, `getnote`, `hv-analysis`, `khazix-writer`, `xray-book`, `naval-perspective`, `taleb-perspective`, `x-mastery-mentor`.

## 2026-09-26 verification

- Run in a cloud session on branch `claude/skill-upgrade-latest-0o2dyg`; all nine GitHub sources were cloned and diffed against the repository copies. `aihot` could not be reached (egress policy), so it was not re-checked.
- Synced `darwin-skill`, `dbs` and `shuorenhua`; every synced tree now matches its upstream source (except the retained local wrapper files). `shuorenhua` eval tests pass (38/38, `python3 -m unittest discover -s automation/eval -p 'test_*.py'`); `dbs/scripts/numbered-prompts.py list` reads the live catalog.
- New runtime network behavior: `/dbs <编号>` downloads prompt text from `raw.githubusercontent.com/dontbesilent2025/dbskill` and executes it in the session. The SHA-256 check compares the prompt with a catalog from the same repository, so it guards consistency, not authorship.
- `nuwa-skill` and `yao-meta-skill` still differ from upstream only by trailing whitespace in a few files; left unchanged.
- No local installation was performed. Before running `./install.sh darwin-skill` (or a bare `./install.sh`), back up the local Astra edition of `darwin-skill`.

## 2026-09-21 verification

- All 14 managed skills and the sole rules-card pending-source entry `agent-review` exist. All 10 first-party sources were reachable.
- Found content updates in `aihot` and `darwin-skill`; neither was synced because installation would overwrite the local customizations identified above. Repository skill files and local installations were left unchanged.
- Obsidian source advanced, but both managed skill trees and the root LICENSE match the recorded content.
- No install or dry run was performed; there are no updated skills to install. Existing shared entries remain readable.
- Repository started on `main`, even with `origin/main`, with unrelated local edits preserved. This run changes only this ledger.
