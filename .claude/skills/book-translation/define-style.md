---
name: define-style
description: Brainstorm and define the translation style guide for a book — use after init-project or when user wants to adjust style
---

# Define Translation Style Guide

## Trigger
After init-project completes, or user says "dinh nghia van phong", "adjust style guide".

## Context to Load
- Read 2-3 sample paragraphs from `projects/{slug}/source/chapters/ch01.md`
- Read `modules/book-translation/memory/style-feedback.md` (cross-book rules if any)

## Steps

### 1. Analyze source text
Read the first 2-3 paragraphs of chapter 1. Identify:
- Genre (philosophical, literary, technical, self-help, etc.)
- Author's voice (formal, conversational, academic, poetic)
- Target audience
- Complexity level

### 2. Ask clarifying questions (one at a time)
- **Target reader:** Who will read the translation? (general public / academics / students)
- **Han-Viet level:** How much Sino-Vietnamese vocabulary? (heavy / moderate / light)
- **Tone:** What feeling should the translation convey? (formal-elegant / accessible-warm / neutral)
- **Pronouns:** How should toi/ban or other forms be used?
- **Technical terms:** Translate fully / translate with EN in parentheses first time / keep EN?

### 3. Apply cross-book feedback
Check `modules/book-translation/memory/style-feedback.md` for rules from previous books.
Apply relevant rules, skip irrelevant ones.

### 4. Draft style guide
Write a complete style-guide.md based on answers. Include:
- Voice description
- Pronoun rules
- Terminology approach
- Translation rules (no word-by-word, no repetition in 3 sentences, etc.)
- Anti-patterns
- Reference: DICH_PROMPT_1.txt and DICH_PROMPT_2.txt patterns in `documents/07-archived/legacy/`

### 5. User approval
Present the draft. User approves or requests changes.
Save to `projects/{slug}/style-guide.md`.

### 6. Initialize glossary
If the book has specialized terms, start populating `projects/{slug}/glossary.md` with the first set of terms.

### 7. Transition
Tell user: "Style guide saved. You can now start translating with 'dich chapter 1' or 'tiep tuc dich'."
