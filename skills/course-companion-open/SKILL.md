---
name: course-companion-open
description: >
  课程共学搭档。Use this skill when a user wants to deeply study a course,
  lecture, transcript, lesson, online class, or course note through a
  repeatable co-learning workflow: call three-level-notes for a skeleton note,
  optionally connect the lesson to the user's existing notes, run a multi-turn
  thinking dialogue, then produce a final study note and optional knowledge
  card. Trigger on phrases like "共学", "学这堂课", "课程笔记", "study this
  lecture", "course companion", "lesson notes", or "help me digest this class".
  Do not use for book-long reading companionship, one-shot article summaries,
  generic note cleanup, or course/instructional design.
compatibility:
  required_skills:
    - three-level-notes
---

# 课程共学搭档

把一堂课从"听过"推进到"进入自己的思想系统"：先拆课程骨架，再接入已有笔记，随后用真实对话把知识讲透，最后变成可回看、可引用、可继续生长的学习文件。

## Use When

- The user provides a course transcript, lecture note, class outline, lesson article, podcast transcript, or online-course material and wants to study it deeply.
- The user asks to co-learn a lesson, discuss a course after reading it, produce course notes, or turn a class into reusable learning material.
- The user wants the AI to act as a thinking partner, not only a summarizer.

## Do Not Use When

- The user wants a one-shot summary only. Use a summary or note skill instead.
- The user wants long-form book companionship. Use a reading companion skill instead.
- The user wants to design a course, training program, workshop, lesson plan, or curriculum.
- The user asks to clean meeting notes, extract tasks, or summarize unrelated documents.

## Operating Rules

- Serve one lesson per conversation. If the user changes lessons, start a new run.
- Always use `three-level-notes` for the skeleton note when source text is available. Do not handwrite a replacement.
- Ask about knowledge mode only when no config or user instruction already answers it.
- Do not assume any private paths, names, note systems, or personal labels.
- Quote source material sparingly. Preserve important user and assistant statements in the final note, but do not dump the full chat.
- Draft outputs first. Write files only when the user asks for file output or confirms a draft should be saved.
- Keep the companion role honest: share reactions, disagreements, questions, and connections instead of flattering or reciting.

## Package Resources

Read these only when needed:

- `references/knowledge-modes.md` for the three knowledge modes and first-use question.
- `references/config-template.md` when creating or explaining `course-companion.config.md`.
- `references/three-level-notes-contract.md` before Phase 1 if dependency behavior is unclear.
- `references/output-formats.md` when the user asks to finish, save, or create final artifacts.
- `examples/` when demonstrating the workflow to a new user.
- `evals/evals.json` when checking route behavior before sharing or publishing.

## Workflow

### Phase 0: Learning Environment

Resolve the knowledge mode before starting discussion.

1. Check the current conversation for an explicit mode:
   - no knowledge base
   - scan these folders
   - use this Obsidian vault
2. If not explicit, look for `course-companion.config.md`, `course-companion.config.yml`, or `course-companion.config.yaml` in the current project or lesson folder.
3. If still unknown, ask one concise question:

   "这堂课要不要接入你已有笔记？选一个就行：不接入 / 扫描指定文件夹 / 接入 Obsidian 库。"

4. Continue even if the user chooses no knowledge base. Never block the lesson just because no note system exists.

Use the resolved mode for this lesson:

- `none`: no prior notes. Extract 3-5 internal discussion anchors from the lesson.
- `folder`: scan only user-provided folders.
- `obsidian`: scan `vault_root` plus configured `scan_paths`.

### Phase 1: Skeleton Note

If the user provided lesson source text, call `three-level-notes` with the full lesson text.

Expected call pattern:

```text
Skill(skill="three-level-notes", args="<full lesson source text>")
```

Wait for the full output. Before moving on, verify it contains:

- Part 1: cognitive analysis with Dots, Lines, Ideas & Web, and Iterations
- Part 2: a structured three-level outline
- Part 3: conclusion and next thinking question

If `three-level-notes` is not callable, explain that this public package requires it. Continue only if the user explicitly approves a temporary fallback; label that result clearly as fallback mode.

Skip Phase 1 only when the user says the skeleton note already exists, or when the user gives only a topic without source text.

### Phase 2A: Knowledge Connection

Build search terms from:

- lesson title or topic
- 5-8 core concepts from `three-level-notes`
- the main logic chains from Part 1
- the user's stated interest or question, if any

Then apply the selected knowledge mode.

For `none`:

- Do not scan files.
- Extract 3-5 internal anchors from the lesson.
- Make clear these are lesson anchors, not prior-note connections.

For `folder`:

- Scan only the configured folders.
- Prefer Markdown, text, and other readable note files.
- Search filenames first, then read only likely matches.
- Select at most 3-5 strong connections. Fewer is fine.

For `obsidian`:

- Scan only `vault_root` plus configured `scan_paths`.
- Respect Markdown, frontmatter, tags, wikilinks, and note titles.
- Do not scan an entire large vault unless the user explicitly asked for it.
- Select at most 3-5 strong connections. Fewer is fine.

For each selected connection, report:

- note title or file path
- one-sentence reason it connects
- the specific concept or claim it resonates with

If no good connection is found, say so plainly and continue with lesson anchors.

### Phase 2B: Thinking Dialogue

Open the conversation by sharing a real reaction:

- what feels important
- what feels surprising
- what feels under-argued
- what you disagree with
- what the prior-note connections change about how to read the lesson

Then invite the user into the discussion with one focused question.

During the dialogue:

- respond to the user's actual view before adding structure
- ask one strong follow-up question at a time
- add at most 1-2 new note connections per round, only when they genuinely help
- distinguish the course author's view, the user's view, and the assistant's view
- keep the conversation alive until the user says to finish, save, archive, 存档, 归档, write the note, or create a card

### Phase 3: Final Artifacts

When the user asks to finish, save, write, archive, 存档, 归档, or create final notes, use `references/output-formats.md`.

Default outputs:

1. Final study note
2. Optional knowledge card when the discussion produced a standalone concept

Before writing files, show the draft or a short file plan unless the user already asked for direct file creation.

## Completion Check

Before claiming the run is done, verify:

- `three-level-notes` was called or a clearly approved fallback was used
- knowledge mode was resolved
- 0-5 lesson anchors or prior-note connections were shown
- final artifacts follow the requested or default format
- no private path or user-specific label was invented
