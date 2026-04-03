---
name: translate-section
description: Core translation skill — translate a chapter/section using 3-pass method (Translate, Reflect, Improve). Use when user says "dich chapter X", "tiep tuc dich", or "translate next"
---

# Translate Section

## Trigger
User says "dich chapter X", "tiep tuc dich", "translate next", or "dich tiep".

## Context to Load (Priority Order)
1. **Always:** `projects/{slug}/style-guide.md`
2. **Always:** `projects/{slug}/glossary.md`
3. **Always:** Source section from `projects/{slug}/source/chapters/{chapter}.md`
4. **If exists:** Last 1-2 translated sections (for voice consistency)
5. **If exists:** `modules/book-translation/memory/translation-patterns.md` (top 10 examples)

## Determine What to Translate

1. Read `projects/{slug}/progress.yaml`
2. If user specified a chapter: use that chapter
3. If user said "tiep tuc dich": find the next chapter with status `extracted` or `translating`
4. If chapter has multiple sections: translate the next untranslated section

## 3-Pass Translation

### Pass 1: TRANSLATE
- Read the source section completely
- Read style-guide.md rules
- Read glossary.md terms
- Translate the entire section following the style guide
- Preserve paragraph structure from source
- Apply glossary terms consistently
- Use Vietnamese idioms where appropriate

### Pass 2: REFLECT
Self-review checklist:
- [ ] No content omitted from source?
- [ ] All glossary terms used consistently?
- [ ] No word-by-word translation patterns?
- [ ] No word repetition within 3 consecutive sentences?
- [ ] Paragraph structure matches source?
- [ ] Formatting preserved (bold, italic, headings)?
- [ ] QC 3 layers: logic content -> aesthetic style -> grammar correctness

### Pass 3: IMPROVE
- Fix all issues found in reflection
- Read the full translation aloud (mentally) for flow
- Polish final version

## After Translation

1. **Write file:** Save to `projects/{slug}/translated/{chapter}.md` with frontmatter:
   ```yaml
   ---
   chapter: {N}
   section: {S or null}
   source: "source/chapters/{chapter}.md"
   status: draft
   translated_at: "{date}"
   pass: 3
   ---
   ```

2. **Update progress:** Edit `projects/{slug}/progress.yaml`:
   - Set chapter/section status to `draft`
   - Update `last_updated`

3. **Report to user:**
   - Word count (source vs translated, ratio)
   - Number of glossary terms applied
   - Any new terms encountered (suggest adding to glossary)
   - Any passages that were particularly challenging

4. **Git commit:** Stage and commit the translated chapter:
   ```bash
   git add projects/{slug}/translated/{chapter}.md projects/{slug}/progress.yaml projects/{slug}/glossary.md
   git commit -m "translate({slug}): complete {chapter}"
   ```
   Push periodically (every 2-3 chapters or end of session):
   ```bash
   git push
   ```

5. **Mid-translation fixes:** If you discover a bug in scripts or skills during translation:
   - Stash or commit current work on `translate/{slug}`
   - Create `fix/xxx` branch from main, fix, PR, merge to main
   - Return to `translate/{slug}` and rebase: `git rebase main`
   - Do NOT mix tooling fixes with book content commits

6. **Ask:** "Ban muon review chapter nay, hay tiep tuc dich chapter tiep theo?"
