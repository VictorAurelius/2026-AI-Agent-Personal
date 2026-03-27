# modules/book-translation/scripts/tests/test_consistency_scanner.py
"""Tests for consistency scanner module."""
import pytest
from pathlib import Path
from lib.consistency_scanner import (
    scan_glossary_consistency, scan_heading_counts, scan_word_count_ratios, generate_report,
)

@pytest.fixture
def project_with_translations(tmp_path):
    source_dir = tmp_path / "source" / "chapters"
    source_dir.mkdir(parents=True)
    translated_dir = tmp_path / "translated"
    translated_dir.mkdir()
    (source_dir / "ch01.md").write_text(
        "# Chapter 1: Beginning\n\nThe inferiority complex is a common issue.\n\nThe style of life determines behavior.\n", encoding="utf-8")
    (source_dir / "ch02.md").write_text(
        "# Chapter 2: Middle\n\n## Section A\n\nThe inferiority complex grows over time.\n\nThe style of life can change.\n", encoding="utf-8")
    (translated_dir / "ch01.md").write_text(
        "---\nchapter: 1\nstatus: approved\n---\n\n# Chuong 1: Khoi dau\n\nMac cam tu ti la van de pho bien.\n\nNep song quyet dinh hanh vi.\n", encoding="utf-8")
    (translated_dir / "ch02.md").write_text(
        "---\nchapter: 2\nstatus: approved\n---\n\n# Chuong 2: Giua\n\n## Phan A\n\nPhuc cam tu ti phat trien theo thoi gian.\n\nPhong cach song co the thay doi.\n", encoding="utf-8")
    (tmp_path / "glossary.md").write_text(
        "# Glossary\n\n| English | Vietnamese | Context | Notes |\n|---------|-----------|---------|-------|\n| inferiority complex | mac cam tu ti | psychology | |\n| style of life | nep song | core concept | |\n", encoding="utf-8")
    return tmp_path

class TestScanGlossaryConsistency:
    def test_finds_inconsistent_terms(self, project_with_translations):
        results = scan_glossary_consistency(project_with_translations / "glossary.md", project_with_translations / "translated")
        assert len(results) > 0
        terms_found = [r["term_vi"] for r in results]
        assert "mac cam tu ti" in terms_found or "nep song" in terms_found

    def test_reports_which_chapters_have_issues(self, project_with_translations):
        results = scan_glossary_consistency(project_with_translations / "glossary.md", project_with_translations / "translated")
        for r in results:
            assert "chapters_with_term" in r
            assert "chapters_without_term" in r
            assert "status" in r

    def test_empty_glossary_returns_empty(self, tmp_path):
        glossary = tmp_path / "glossary.md"
        glossary.write_text("# Glossary\n\n| English | Vietnamese | Context | Notes |\n|---|---|---|---|\n", encoding="utf-8")
        translated_dir = tmp_path / "translated"
        translated_dir.mkdir()
        results = scan_glossary_consistency(glossary, translated_dir)
        assert results == []

class TestScanHeadingCounts:
    def test_compares_heading_counts(self, project_with_translations):
        results = scan_heading_counts(project_with_translations / "source" / "chapters", project_with_translations / "translated")
        for r in results:
            assert "chapter" in r
            assert "source_headings" in r
            assert "translated_headings" in r

    def test_flags_mismatch(self, tmp_path):
        source_dir = tmp_path / "source" / "chapters"
        source_dir.mkdir(parents=True)
        translated_dir = tmp_path / "translated"
        translated_dir.mkdir()
        (source_dir / "ch01.md").write_text("# Ch1\n\n## Sec A\n\n## Sec B\n", encoding="utf-8")
        (translated_dir / "ch01.md").write_text("# Ch1\n\nContent without section headings.\n", encoding="utf-8")
        results = scan_heading_counts(source_dir, translated_dir)
        mismatches = [r for r in results if r["source_headings"] != r["translated_headings"]]
        assert len(mismatches) >= 1

class TestScanWordCountRatios:
    def test_calculates_ratios(self, project_with_translations):
        results = scan_word_count_ratios(project_with_translations / "source" / "chapters", project_with_translations / "translated")
        for r in results:
            assert "chapter" in r
            assert "source_words" in r
            assert "translated_words" in r
            assert "ratio" in r
            assert r["ratio"] > 0

    def test_flags_outlier_ratio(self, tmp_path):
        source_dir = tmp_path / "source" / "chapters"
        source_dir.mkdir(parents=True)
        translated_dir = tmp_path / "translated"
        translated_dir.mkdir()
        (source_dir / "ch01.md").write_text("# Ch1\n\n" + "word " * 100, encoding="utf-8")
        (translated_dir / "ch01.md").write_text("# Ch1\n\n" + "tu " * 30, encoding="utf-8")
        results = scan_word_count_ratios(source_dir, translated_dir)
        assert results[0]["is_outlier"] is True

class TestGenerateReport:
    def test_produces_text_report(self, project_with_translations):
        report = generate_report(project_with_translations)
        assert isinstance(report, str)
        assert "Glossary" in report or "glossary" in report
        assert "Heading" in report or "heading" in report
