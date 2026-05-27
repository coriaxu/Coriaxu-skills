# Output Risk Profile

## Main Risks

1. **Skipping `three-level-notes`**
   - The assistant may handwrite a simpler outline because it is faster.
   - Guard: Phase 1 requires a dependency check and a three-Part self-check.

2. **Over-asking during first use**
   - The assistant may turn setup into a long questionnaire.
   - Guard: ask one mode question first, then only ask for paths if needed.

3. **Weak note connections**
   - The assistant may show five files even when only one is truly relevant.
   - Guard: fewer strong connections are better than five weak ones.

4. **Private-path leakage**
   - A public package may accidentally inherit the author's personal note paths.
   - Guard: no default private paths; all paths come from user config.

5. **Final note becomes a chat dump**
   - The assistant may paste the whole conversation.
   - Guard: preserve important statements, not every turn.

## Review Checks

- Does `SKILL.md` require `three-level-notes`?
- Does Phase 0 support `none`, `folder`, and `obsidian`?
- Does no-knowledge mode still continue the lesson?
- Are file writes confirmation-based by default?
- Are all examples free of private personal data?
