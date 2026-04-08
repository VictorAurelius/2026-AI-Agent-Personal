#!/usr/bin/env python3
"""Convert knowledge .md files to Jupyter notebooks with Vietnamese font styling."""

import json
import re
import sys
from pathlib import Path

STYLE_CELL = """\
<style>
@import url('https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&family=JetBrains+Mono:wght@400;500&display=swap');

.jp-RenderedHTMLCommon, .jp-RenderedMarkdown,
div.text_cell_render, div.output_text {
    font-family: 'Be Vietnam Pro', 'Segoe UI', sans-serif !important;
    font-size: 15px !important;
    line-height: 1.7 !important;
    color: #2d3748 !important;
}

.jp-RenderedHTMLCommon h1, div.text_cell_render h1 {
    font-family: 'Be Vietnam Pro', sans-serif !important;
    font-weight: 700 !important;
    font-size: 28px !important;
    color: #1a365d !important;
    border-bottom: 3px solid #3182ce !important;
    padding-bottom: 8px !important;
    margin-top: 24px !important;
}

.jp-RenderedHTMLCommon h2, div.text_cell_render h2 {
    font-family: 'Be Vietnam Pro', sans-serif !important;
    font-weight: 600 !important;
    font-size: 22px !important;
    color: #2c5282 !important;
    border-bottom: 1px solid #bee3f8 !important;
    padding-bottom: 4px !important;
    margin-top: 20px !important;
}

.jp-RenderedHTMLCommon h3, div.text_cell_render h3 {
    font-family: 'Be Vietnam Pro', sans-serif !important;
    font-weight: 600 !important;
    font-size: 18px !important;
    color: #2b6cb0 !important;
}

.jp-RenderedHTMLCommon code, div.text_cell_render code {
    font-family: 'JetBrains Mono', 'Consolas', monospace !important;
    font-size: 13px !important;
    background: #edf2f7 !important;
    padding: 2px 6px !important;
    border-radius: 4px !important;
}

.jp-RenderedHTMLCommon pre, div.text_cell_render pre {
    font-family: 'JetBrains Mono', 'Consolas', monospace !important;
    font-size: 13px !important;
    background: #1a202c !important;
    color: #e2e8f0 !important;
    padding: 16px !important;
    border-radius: 8px !important;
    line-height: 1.5 !important;
}

.jp-RenderedHTMLCommon table, div.text_cell_render table {
    border-collapse: collapse !important;
    width: 100% !important;
    margin: 12px 0 !important;
}

.jp-RenderedHTMLCommon th, div.text_cell_render th {
    background: #2c5282 !important;
    color: white !important;
    font-weight: 600 !important;
    padding: 10px 14px !important;
    text-align: left !important;
}

.jp-RenderedHTMLCommon td, div.text_cell_render td {
    padding: 8px 14px !important;
    border-bottom: 1px solid #e2e8f0 !important;
}

.jp-RenderedHTMLCommon tr:nth-child(even), div.text_cell_render tr:nth-child(even) {
    background: #f7fafc !important;
}

.jp-RenderedHTMLCommon blockquote, div.text_cell_render blockquote {
    border-left: 4px solid #3182ce !important;
    background: #ebf8ff !important;
    padding: 12px 16px !important;
    margin: 12px 0 !important;
    border-radius: 0 8px 8px 0 !important;
    font-style: normal !important;
}
</style>
"""


def make_notebook(cells):
    return {
        "nbformat": 4,
        "nbformat_minor": 5,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "name": "python",
                "version": "3.11.0"
            }
        },
        "cells": cells
    }


def md_cell(source):
    return {
        "cell_type": "markdown",
        "metadata": {},
        "source": source.splitlines(True)
    }


def code_cell(source, language="python"):
    if language and language not in ("python", "py"):
        source = f"# Language: {language}\n# (Tham khảo — không chạy được trong Python kernel)\n\n{source}"
    return {
        "cell_type": "code",
        "metadata": {},
        "source": source.splitlines(True),
        "outputs": [],
        "execution_count": None
    }


def parse_md(content):
    """Parse markdown into notebook cells."""
    cells = [md_cell(STYLE_CELL)]

    # Split by code fences
    parts = re.split(r"(```\w*\n.*?```)", content, flags=re.DOTALL)

    for part in parts:
        part = part.strip()
        if not part:
            continue

        fence = re.match(r"```(\w*)\n(.*?)```", part, flags=re.DOTALL)
        if fence:
            lang = fence.group(1) or "python"
            code = fence.group(2).strip()
            cells.append(code_cell(code, lang))
        else:
            # Split at ## headings for cleaner cells
            sections = re.split(r"(?=^## )", part, flags=re.MULTILINE)
            for sec in sections:
                sec = sec.strip()
                if sec:
                    cells.append(md_cell(sec))

    return cells


def convert_file(md_path):
    out_path = md_path.with_suffix(".ipynb")

    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()

    cells = parse_md(content)
    nb = make_notebook(cells)

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(nb, f, ensure_ascii=False, indent=1)

    return out_path


def main():
    base = Path(__file__).resolve().parent.parent  # modules/knowledge/
    dirs = ["01-technical", "02-professional", "03-other"]

    converted = 0
    errors = []

    for d in dirs:
        dir_path = base / d
        if not dir_path.exists():
            print(f"SKIP: {dir_path}")
            continue

        for md_file in sorted(dir_path.glob("*.md")):
            if md_file.name.lower() == "readme.md":
                continue
            try:
                out = convert_file(md_file)
                print(f"  OK: {md_file.name} -> {out.name}")
                converted += 1
            except Exception as e:
                print(f"FAIL: {md_file.name} -> {e}")
                errors.append((md_file.name, str(e)))

    print(f"\nConverted: {converted} files")
    if errors:
        print(f"Errors: {len(errors)}")
        for name, err in errors:
            print(f"  {name}: {err}")
        sys.exit(1)
    print("Done!")


if __name__ == "__main__":
    main()
