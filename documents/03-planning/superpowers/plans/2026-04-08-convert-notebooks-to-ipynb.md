# Convert Knowledge Notebooks to Jupyter (.ipynb) — Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Chuyển 25 knowledge notebooks từ Markdown sang Jupyter Notebook (.ipynb) với font tiếng Việt đẹp, có cells interactive.

**Architecture:** Viết Python script `convert_md_to_ipynb.py` để tự động convert tất cả .md → .ipynb. Script parse markdown theo heading structure, tách thành markdown cells + code cells. Thêm CSS styling cell đầu mỗi notebook cho font tiếng Việt đẹp. Xoá các file .md gốc sau khi convert thành công.

**Tech Stack:** Python 3.11, nbformat (tạo .ipynb), json (fallback nếu không có nbformat)

---

## File Structure

```
modules/knowledge/
├── scripts/
│   └── convert_md_to_ipynb.py    # Script convert .md → .ipynb (1 lần dùng)
├── 01-technical/
│   ├── 01-api-design.ipynb       # Thay thế .md
│   ├── 02-database-design.ipynb
│   ├── ...
│   └── 10-documentation-specs.ipynb
├── 02-professional/
│   ├── 01-project-planning.ipynb
│   ├── ...
│   └── 10-stakeholder-leadership.ipynb
├── 03-other/
│   ├── 01-japanese-communication.ipynb
│   ├── ...
│   └── 05-glossary-japanese.ipynb
├── README.md                      # Cập nhật hướng dẫn mở .ipynb
└── progress.yaml                  # Giữ nguyên
```

**Thay đổi:** 25 .md → 25 .ipynb + 1 script + README update

---

## Chunk 1: Script convert + CSS styling

### Task 1: Tạo script convert_md_to_ipynb.py

**Files:**
- Create: `modules/knowledge/scripts/convert_md_to_ipynb.py`

Script này:
1. Đọc từng file .md
2. Parse thành sections theo heading (## / ###)
3. Tách code blocks (```...```) thành code cells
4. Phần còn lại thành markdown cells
5. Inject CSS styling cell ở đầu notebook cho font tiếng Việt
6. Ghi ra file .ipynb cùng tên

- [ ] **Step 1: Tạo script convert**

```python
#!/usr/bin/env python3
"""Convert knowledge .md files to Jupyter notebooks with Vietnamese font styling."""

import json
import os
import re
import sys
from pathlib import Path

# Vietnamese font CSS - injected as first cell in every notebook
STYLE_CELL = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&family=JetBrains+Mono:wght@400;500&display=swap');

/* Main content font */
.jp-RenderedHTMLCommon, .jp-RenderedMarkdown,
div.text_cell_render, div.output_text {
    font-family: 'Be Vietnam Pro', 'Segoe UI', sans-serif !important;
    font-size: 15px !important;
    line-height: 1.7 !important;
    color: #2d3748 !important;
}

/* Headings */
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

/* Code blocks */
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

/* Tables */
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

/* Blockquotes - used for notebook metadata */
.jp-RenderedHTMLCommon blockquote, div.text_cell_render blockquote {
    border-left: 4px solid #3182ce !important;
    background: #ebf8ff !important;
    padding: 12px 16px !important;
    margin: 12px 0 !important;
    border-radius: 0 8px 8px 0 !important;
    font-style: normal !important;
}

/* Checkbox styling */
.jp-RenderedHTMLCommon li input[type="checkbox"],
div.text_cell_render li input[type="checkbox"] {
    margin-right: 8px !important;
}

/* Japanese text styling */
.jp-RenderedHTMLCommon ruby, div.text_cell_render ruby {
    font-size: 14px !important;
}
</style>
"""


def make_notebook(cells):
    """Create a minimal valid .ipynb structure."""
    nb = {
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
    return nb


def make_markdown_cell(source):
    """Create a markdown cell."""
    return {
        "cell_type": "markdown",
        "metadata": {},
        "source": source.splitlines(True)  # keep newlines
    }


def make_code_cell(source, language="python"):
    """Create a code cell."""
    # Add language comment at top if not python
    if language and language != "python":
        source = f"# Language: {language}\n# (Tham khảo — không chạy được trong Python kernel)\n\n{source}"
    return {
        "cell_type": "code",
        "metadata": {},
        "source": source.splitlines(True),
        "outputs": [],
        "execution_count": None
    }


def parse_md_to_cells(md_content):
    """Parse markdown content into notebook cells.

    Strategy:
    - Split by code fences (```...```)
    - Markdown sections become markdown cells (split at ## headings)
    - Code blocks become code cells
    - CSS styling injected as first cell
    """
    cells = []

    # First cell: CSS styling (HTML in markdown cell)
    cells.append(make_markdown_cell(STYLE_CELL))

    # Split content by code fences
    parts = re.split(r'(```\w*\n.*?```)', md_content, flags=re.DOTALL)

    for part in parts:
        part = part.strip()
        if not part:
            continue

        # Check if this is a code block
        code_match = re.match(r'```(\w*)\n(.*?)```', part, flags=re.DOTALL)
        if code_match:
            language = code_match.group(1) or "python"
            code = code_match.group(2).strip()
            cells.append(make_code_cell(code, language))
        else:
            # Split markdown by ## headings into separate cells
            sections = re.split(r'(?=^## )', part, flags=re.MULTILINE)
            for section in sections:
                section = section.strip()
                if section:
                    cells.append(make_markdown_cell(section))

    return cells


def convert_file(md_path, output_dir=None):
    """Convert a single .md file to .ipynb."""
    md_path = Path(md_path)
    if output_dir:
        out_path = Path(output_dir) / md_path.with_suffix('.ipynb').name
    else:
        out_path = md_path.with_suffix('.ipynb')

    with open(md_path, 'r', encoding='utf-8') as f:
        md_content = f.read()

    cells = parse_md_to_cells(md_content)
    nb = make_notebook(cells)

    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, ensure_ascii=False, indent=1)

    return out_path


def main():
    base = Path(__file__).parent.parent  # modules/knowledge/
    dirs = ['01-technical', '02-professional', '03-other']

    converted = 0
    errors = []

    for d in dirs:
        dir_path = base / d
        if not dir_path.exists():
            print(f"SKIP: {dir_path} not found")
            continue

        for md_file in sorted(dir_path.glob('*.md')):
            # Skip README files
            if md_file.name.lower() == 'readme.md':
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


if __name__ == '__main__':
    main()
```

- [ ] **Step 2: Chạy script convert**

```bash
mkdir -p modules/knowledge/scripts
# (save script to modules/knowledge/scripts/convert_md_to_ipynb.py)
python modules/knowledge/scripts/convert_md_to_ipynb.py
```

Expected output:
```
  OK: 01-api-design.md -> 01-api-design.ipynb
  OK: 02-database-design.md -> 02-database-design.ipynb
  ...
Converted: 25 files
Done!
```

- [ ] **Step 3: Verify .ipynb files valid**

```bash
python -c "
import json, pathlib
ok = fail = 0
for f in sorted(pathlib.Path('modules/knowledge').rglob('*.ipynb')):
    try:
        nb = json.load(open(f, encoding='utf-8'))
        assert nb['nbformat'] == 4
        assert len(nb['cells']) > 3
        ok += 1
        print(f'  OK: {f.name} ({len(nb[\"cells\"])} cells)')
    except Exception as e:
        fail += 1
        print(f'FAIL: {f.name}: {e}')
print(f'\nValid: {ok}, Failed: {fail}')
"
```

- [ ] **Step 4: Xoá .md gốc (chỉ notebooks, giữ README.md)**

```bash
find modules/knowledge/01-technical -name "*.md" -delete
find modules/knowledge/02-professional -name "*.md" -delete
find modules/knowledge/03-other -name "*.md" -delete
```

- [ ] **Step 5: Commit**

```bash
git add modules/knowledge/
git commit -m "feat(knowledge): convert 25 notebooks from .md to .ipynb with Vietnamese font styling"
```

---

## Chunk 2: Cập nhật README, gitignore, gitattributes

### Task 2: Cập nhật README và git config

**Files:**
- Modify: `modules/knowledge/README.md`
- Modify: `.gitignore` (thêm .ipynb_checkpoints)
- Modify: `.gitattributes` (nếu cần, cho ipynb diff)

- [ ] **Step 1: Cập nhật README.md**

Thay đổi:
- Hướng dẫn mở file: `jupyter notebook modules/knowledge/01-technical/01-api-design.ipynb`
- Hoặc dùng VS Code: cài extension Jupyter
- Lưu ý: cần kết nối internet lần đầu để load Google Fonts (Be Vietnam Pro)
- Nếu offline: fonts fallback sang Segoe UI / system sans-serif

- [ ] **Step 2: Thêm .ipynb_checkpoints vào .gitignore**

```
# Jupyter checkpoints
.ipynb_checkpoints/
```

- [ ] **Step 3: Commit**

```bash
git add modules/knowledge/README.md .gitignore
git commit -m "docs(knowledge): update README for .ipynb format, add jupyter gitignore"
```

---

## Chunk 3: Push và cập nhật PR

### Task 3: Push và update PR

- [ ] **Step 1: Push branch**

```bash
git push
```

- [ ] **Step 2: Verify trên GitHub**

Kiểm tra:
- 25 .ipynb files hiển thị render trên GitHub
- Không còn .md notebooks (chỉ README.md)
- CSS styling cell hiển thị ở đầu mỗi notebook

---

## Tổng kết

| Task | Nội dung | Files | Thời gian |
|------|---------|-------|----------|
| 1 | Script convert + chạy + xoá .md | 25 .ipynb + 1 script | ~15 phút |
| 2 | README + gitignore | 2 files | ~5 phút |
| 3 | Push + verify | — | ~5 phút |
| **Total** | | **28 files changed** | **~25 phút** |

## CSS Font Choice

**Be Vietnam Pro** (Google Fonts):
- Font tiếng Việt chuyên dụng, hỗ trợ đầy đủ dấu
- Thiết kế bởi người Việt, tối ưu cho tiếng Việt
- Weights: 300 (light), 400 (regular), 500 (medium), 600 (semibold), 700 (bold)
- Fallback: Segoe UI → system sans-serif

**JetBrains Mono** cho code blocks:
- Ligatures, clear distinction giữa 0/O, 1/l
- Monospace chuyên cho code
