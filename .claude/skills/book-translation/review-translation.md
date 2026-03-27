---
name: review-translation
description: Review translated chapters and learn from user feedback — use when user provides feedback on translation, says "review ban dich", approves/rejects a chapter, or has edited a translated file
---

# Review Translation

## Trigger
User provides feedback on a translation, says "review", "approve", "reject", edits a translated file, or comments on translation quality.

## Context to Load
1. **Always:** The translated section being reviewed from `projects/{slug}/translated/`
2. **Always:** The source section from `projects/{slug}/source/chapters/`
3. **If needed:** `projects/{slug}/style-guide.md`
4. **If needed:** `projects/{slug}/glossary.md`

## Handling Feedback

### Path A: Verbal feedback (big changes)
User says something like "this paragraph is too stiff" or "use a different term for X".

1. Understand the feedback — ask clarifying questions if ambiguous
2. Revise the section according to feedback
3. Show the revised version to user
4. Classify the feedback:
   - **Book-specific** (style choice for this book) → update `projects/{slug}/style-guide.md` or `glossary.md`
   - **Universal rule** (applies to all future books) → append to `modules/book-translation/memory/style-feedback.md`
   - **Good translation pattern** (reusable example) → append to `modules/book-translation/memory/translation-patterns.md`
5. Update `projects/{slug}/progress.yaml`: set chapter status to `reviewing`

### Path B: User edited file directly (small fixes)
User says "I edited ch03.md" or you notice the file changed.

1. Read the current translated file
2. Ask user what they changed and why (if not obvious)
3. Ask: "Should this change apply to all future translations, or just this section?"
4. Save to appropriate memory file if universal
5. Update progress.yaml status

### Path C: Combined A + B
Handle both verbal and file-edit feedback together.

## Approve Flow
When user says "approve", "LGTM", "ok", or explicitly approves:

1. Update `projects/{slug}/progress.yaml`: set chapter status to `approved`
2. Show next chapter to translate: read progress.yaml, find next `extracted` chapter
3. Ask: "Chapter X approved. Continue with chapter Y, or review something else?"

## Memory Classification Guide

**Save to `style-guide.md`** (per-book):
- Specific tone/voice choices for this book
- Book-specific terminology decisions
- Author-specific translation approaches

**Save to `memory/style-feedback.md`** (cross-book):
- General translation rules confirmed by user
- Anti-patterns user has rejected
- Format: rule + **Source:** book/chapter where confirmed

**Save to `memory/translation-patterns.md`** (cross-book):
- Specific EN→VI translation examples user approved
- Metaphor translations
- Complex sentence restructuring examples
- Format: EN original → VI translation + **Context:** where/why

## After Review
- If more chapters to review: ask user which to review next
- If all chapters reviewed: suggest running consistency check
