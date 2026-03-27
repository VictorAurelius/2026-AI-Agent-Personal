# modules/book-translation/scripts/lib/consistency_scanner.py
"""Scan translated files for consistency issues."""
import re
from pathlib import Path

def _parse_glossary(glossary_path: Path) -> list[dict]:
    if not glossary_path.exists():
        return []
    text = glossary_path.read_text(encoding="utf-8")
    terms = []
    for line in text.split("\n"):
        line = line.strip()
        if not line.startswith("|") or line.startswith("|---") or line.startswith("| English"):
            continue
        parts = [p.strip() for p in line.split("|")]
        parts = [p for p in parts if p]
        if len(parts) >= 2 and parts[0] and parts[1]:
            terms.append({
                "term_en": parts[0],
                "term_vi": parts[1],
                "context": parts[2] if len(parts) > 2 else "",
                "notes": parts[3] if len(parts) > 3 else "",
            })
    return terms

def _strip_frontmatter(text: str) -> str:
    if text.startswith("---"):
        end = text.find("---", 3)
        if end != -1:
            return text[end + 3:].strip()
    return text.strip()

def _count_headings(text: str) -> int:
    return len(re.findall(r"^#{1,6}\s+", text, re.MULTILINE))

def _count_words(text: str) -> int:
    clean = re.sub(r"^#{1,6}\s+", "", text, flags=re.MULTILINE)
    clean = re.sub(r"[*_`>]", "", clean)
    return len(clean.split())

def scan_glossary_consistency(glossary_path: Path, translated_dir: Path) -> list[dict]:
    """Check that glossary terms appear consistently across all translated chapters."""
    terms = _parse_glossary(glossary_path)
    if not terms:
        return []
    translated_files = sorted(translated_dir.glob("ch*.md"))
    if not translated_files:
        return []
    results = []
    for term in terms:
        vi = term["term_vi"].lower()
        with_term = []
        without_term = []
        for f in translated_files:
            content = _strip_frontmatter(f.read_text(encoding="utf-8")).lower()
            if vi in content:
                with_term.append(f.stem)
            else:
                without_term.append(f.stem)
        if without_term:
            results.append({
                "term_en": term["term_en"],
                "term_vi": term["term_vi"],
                "chapters_with_term": with_term,
                "chapters_without_term": without_term,
                "status": "missing" if not with_term else "inconsistent",
            })
    return results

def scan_heading_counts(source_dir: Path, translated_dir: Path) -> list[dict]:
    """Compare heading counts between source and translated chapters."""
    results = []
    for source_file in sorted(source_dir.glob("ch*.md")):
        chapter_id = source_file.stem
        translated_file = translated_dir / f"{chapter_id}.md"
        if not translated_file.exists():
            continue
        source_text = source_file.read_text(encoding="utf-8")
        translated_text = _strip_frontmatter(translated_file.read_text(encoding="utf-8"))
        results.append({
            "chapter": chapter_id,
            "source_headings": _count_headings(source_text),
            "translated_headings": _count_headings(translated_text),
        })
    return results

def scan_word_count_ratios(
    source_dir: Path,
    translated_dir: Path,
    outlier_low: float = 0.5,
    outlier_high: float = 2.0,
) -> list[dict]:
    """Compare word counts and flag chapters with unusual translation ratios."""
    results = []
    for source_file in sorted(source_dir.glob("ch*.md")):
        chapter_id = source_file.stem
        translated_file = translated_dir / f"{chapter_id}.md"
        if not translated_file.exists():
            continue
        source_words = _count_words(source_file.read_text(encoding="utf-8"))
        translated_words = _count_words(
            _strip_frontmatter(translated_file.read_text(encoding="utf-8"))
        )
        ratio = translated_words / source_words if source_words > 0 else 0
        results.append({
            "chapter": chapter_id,
            "source_words": source_words,
            "translated_words": translated_words,
            "ratio": round(ratio, 2),
            "is_outlier": ratio < outlier_low or ratio > outlier_high,
        })
    return results

def generate_report(project_dir: Path) -> str:
    """Generate a full consistency report for a project directory."""
    glossary_path = project_dir / "glossary.md"
    source_dir = project_dir / "source" / "chapters"
    translated_dir = project_dir / "translated"

    lines = ["# Consistency Report\n"]

    lines.append("## Glossary Consistency\n")
    glossary_results = scan_glossary_consistency(glossary_path, translated_dir)
    if glossary_results:
        for r in glossary_results:
            lines.append(
                f"- **{r['term_en']}** ({r['term_vi']}): {r['status']} "
                f"- found in {r['chapters_with_term']}, missing in {r['chapters_without_term']}"
            )
    else:
        lines.append("No glossary inconsistencies found.")

    lines.append("")
    lines.append("## Heading Counts\n")
    heading_results = scan_heading_counts(source_dir, translated_dir)
    mismatches = [r for r in heading_results if r["source_headings"] != r["translated_headings"]]
    if mismatches:
        for r in mismatches:
            lines.append(
                f"- **{r['chapter']}**: source={r['source_headings']}, "
                f"translated={r['translated_headings']}"
            )
    else:
        lines.append("All heading counts match.")

    lines.append("")
    lines.append("## Word Count Ratios\n")
    ratio_results = scan_word_count_ratios(source_dir, translated_dir)
    outliers = [r for r in ratio_results if r["is_outlier"]]
    if outliers:
        for r in outliers:
            lines.append(
                f"- **{r['chapter']}**: {r['source_words']} -> {r['translated_words']} "
                f"(ratio {r['ratio']}) OUTLIER"
            )
    else:
        lines.append("All word count ratios within normal range.")

    lines.append("")
    total_issues = len(glossary_results) + len(mismatches) + len(outliers)
    lines.append(f"## Summary: {total_issues} issue(s) found\n")

    return "\n".join(lines)
