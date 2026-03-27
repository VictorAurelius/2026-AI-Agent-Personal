# modules/book-translation/scripts/tests/test_validator.py
"""Tests for comprehensive project validator."""
import pytest
from pathlib import Path
import yaml

from lib.validator import validate_project, ValidationResult


def _make_project(tmp_path, source_chapters=None, translated_chapters=None,
                  has_progress=True, translated_empty=False):
    """Helper to build a minimal project structure for testing."""
    project_dir = tmp_path / "test-project"
    source_dir = project_dir / "source"
    translated_dir = project_dir / "translated"
    source_dir.mkdir(parents=True)
    translated_dir.mkdir(parents=True)

    # Default: 2 source chapters
    if source_chapters is None:
        source_chapters = {
            "ch01.md": "# Chapter 1\n\nFirst chapter content.\n",
            "ch02.md": "# Chapter 2\n\nSecond chapter content.\n",
        }
    for name, content in source_chapters.items():
        (source_dir / name).write_text(content, encoding="utf-8")

    # Default: matching translated chapters
    if translated_chapters is None:
        translated_chapters = {
            "ch01.md": "---\nchapter: 1\nstatus: draft\n---\n\n# Chuong 1\n\nNoi dung.\n",
            "ch02.md": "---\nchapter: 2\nstatus: draft\n---\n\n# Chuong 2\n\nNoi dung 2.\n",
        }
    for name, content in translated_chapters.items():
        if translated_empty:
            (translated_dir / name).write_text("", encoding="utf-8")
        else:
            (translated_dir / name).write_text(content, encoding="utf-8")

    # progress.yaml
    if has_progress:
        progress = {
            "chapters": [
                {"id": "ch01", "status": "draft"},
                {"id": "ch02", "status": "draft"},
            ]
        }
        (project_dir / "progress.yaml").write_text(
            yaml.dump(progress), encoding="utf-8"
        )

    return project_dir


class TestValidProjectNoErrors:
    def test_valid_project_returns_no_errors(self, tmp_path):
        """A well-formed project should validate with no errors."""
        project_dir = _make_project(tmp_path)
        result = validate_project(project_dir)
        assert isinstance(result, ValidationResult)
        assert result.is_valid is True
        assert len(result.errors) == 0


class TestMissingTranslatedFile:
    def test_missing_translated_file_raises_error(self, tmp_path):
        """When a source chapter has no corresponding translated file, an error is added."""
        project_dir = _make_project(tmp_path, translated_chapters={
            "ch01.md": "---\nchapter: 1\nstatus: draft\n---\n\n# Ch1\n\nContent.\n",
            # ch02.md is missing
        })
        result = validate_project(project_dir)
        assert result.is_valid is False
        assert any("ch02" in e for e in result.errors)


class TestEmptyTranslatedFile:
    def test_empty_translated_file_raises_error(self, tmp_path):
        """An empty translated file should produce an error."""
        project_dir = _make_project(tmp_path, translated_empty=True)
        result = validate_project(project_dir)
        assert result.is_valid is False
        assert any("empty" in e.lower() for e in result.errors)


class TestHeadingCountMismatch:
    def test_heading_mismatch_adds_warning(self, tmp_path):
        """Different heading count between source and translated should add a warning."""
        source_chapters = {
            "ch01.md": "# Chapter 1\n\n## Section A\n\n## Section B\n\nContent.\n",
        }
        translated_chapters = {
            "ch01.md": "---\nchapter: 1\nstatus: draft\n---\n\n# Chuong 1\n\nContent only.\n",
        }
        progress = {"chapters": [{"id": "ch01", "status": "draft"}]}
        project_dir = _make_project(
            tmp_path,
            source_chapters=source_chapters,
            translated_chapters=translated_chapters,
        )
        result = validate_project(project_dir)
        # heading mismatch should add at least a warning
        assert len(result.warnings) >= 1 or any("heading" in e.lower() for e in result.errors)


class TestEncodingCheck:
    def test_valid_utf8_passes(self, tmp_path):
        """Valid UTF-8 files should not raise encoding errors."""
        source_chapters = {
            "ch01.md": "# Chương 1\n\nNội dung tiếng Việt.\n",
        }
        translated_chapters = {
            "ch01.md": "---\nchapter: 1\nstatus: draft\n---\n\n# Chương 1\n\nDịch thuật.\n",
        }
        project_dir = _make_project(
            tmp_path,
            source_chapters=source_chapters,
            translated_chapters=translated_chapters,
        )
        result = validate_project(project_dir)
        encoding_errors = [e for e in result.errors if "encoding" in e.lower() or "utf" in e.lower()]
        assert len(encoding_errors) == 0


class TestMissingProgressYaml:
    def test_missing_progress_yaml_adds_error(self, tmp_path):
        """Missing progress.yaml should add an error to validation result."""
        project_dir = _make_project(tmp_path, has_progress=False)
        result = validate_project(project_dir)
        assert result.is_valid is False
        assert any("progress" in e.lower() for e in result.errors)
