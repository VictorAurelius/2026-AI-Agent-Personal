# modules/book-translation/scripts/tests/test_manage_cli.py
"""Tests for manage.py CLI commands."""
import pytest
from pathlib import Path
from click.testing import CliRunner

import sys
sys.path.insert(0, str(Path(__file__).parent.parent))
from manage import cli

FIXTURES_DIR = Path(__file__).parent / "fixtures"


@pytest.fixture
def runner():
    return CliRunner()


@pytest.fixture
def sample_pdf():
    path = FIXTURES_DIR / "sample.pdf"
    if not path.exists():
        pytest.skip("sample.pdf fixture not created yet")
    return path


@pytest.fixture
def initialized_project(runner, sample_pdf, tmp_path, monkeypatch):
    """Create an initialized project for testing."""
    import manage
    monkeypatch.setattr(manage, "PROJECTS_DIR", tmp_path)
    result = runner.invoke(cli, ["init", "Test Book", "--author", "Author", "--source", str(sample_pdf)])
    assert result.exit_code == 0, f"Init failed: {result.output}"
    return tmp_path / "test-book"


class TestInitCommand:
    def test_creates_project(self, runner, sample_pdf, tmp_path, monkeypatch):
        import manage
        monkeypatch.setattr(manage, "PROJECTS_DIR", tmp_path)
        result = runner.invoke(cli, ["init", "My Book", "--author", "Author", "--source", str(sample_pdf)])
        assert result.exit_code == 0
        assert "created" in result.output.lower() or "my-book" in result.output.lower()
        assert (tmp_path / "my-book").exists()

    def test_duplicate_project_fails(self, runner, sample_pdf, tmp_path, monkeypatch):
        import manage
        monkeypatch.setattr(manage, "PROJECTS_DIR", tmp_path)
        runner.invoke(cli, ["init", "My Book", "--author", "A", "--source", str(sample_pdf)])
        result = runner.invoke(cli, ["init", "My Book", "--author", "A", "--source", str(sample_pdf)])
        assert "already exists" in result.output.lower()


class TestStatusCommand:
    def test_shows_status(self, runner, initialized_project, monkeypatch):
        import manage
        monkeypatch.setattr(manage, "PROJECTS_DIR", initialized_project.parent)
        runner.invoke(cli, ["extract", "test-book"])
        result = runner.invoke(cli, ["status", "test-book"])
        assert result.exit_code == 0

    def test_missing_project(self, runner, tmp_path, monkeypatch):
        import manage
        monkeypatch.setattr(manage, "PROJECTS_DIR", tmp_path)
        result = runner.invoke(cli, ["status", "nonexistent"])
        assert "not found" in result.output.lower()


class TestValidateCommand:
    def test_validate_missing_translations(self, runner, initialized_project, monkeypatch):
        import manage
        monkeypatch.setattr(manage, "PROJECTS_DIR", initialized_project.parent)
        runner.invoke(cli, ["extract", "test-book"])
        result = runner.invoke(cli, ["validate", "test-book"])
        assert "error" in result.output.lower() or "missing" in result.output.lower()
