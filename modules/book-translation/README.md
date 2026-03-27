# Book Translation Module

Công cụ tự động hóa dịch sách từ PDF/EPUB sang DOCX với hỗ trợ glossary, style feedback, và translation patterns.

## Quick Start

```bash
# 1. Install dependencies
pip install -r scripts/requirements.txt

# 2. Initialize a translation project
python scripts/manage.py init --name "my-book" --source path/to/book.pdf

# 3. Define translation style
python scripts/manage.py define-style --project my-book

# 4. Translate sections
python scripts/manage.py translate --project my-book --section 1

# 5. Merge and render output
python scripts/manage.py merge --project my-book --output my-book-translated.docx
```

## Skills

| Skill | Purpose |
|-------|---------|
| `init-project` | Initialize new translation project with source file |
| `define-style` | Define translation style and tone for consistency |
| `translate-section` | Translate single section with memory integration |

## Scripts

| Script | Purpose |
|--------|---------|
| `manage.py` | Main CLI for project management and translation |
| `lib/config_loader.py` | Load and validate project configuration |
| `lib/extractor.py` | Extract text from PDF/EPUB files |
| `lib/merger.py` | Merge translated sections into DOCX |
| `lib/renderer.py` | Render final formatted output |

## Memory

- `glossary-global.md` — Global terminology dictionary
- `style-feedback.md` — Common style issues and solutions
- `translation-patterns.md` — Recurring translation patterns

## Project Structure

```
projects/
├── my-book/
│   ├── config.yaml          # Project configuration
│   ├── style.md             # Translation style guide
│   ├── source/
│   │   └── original.pdf     # Source file
│   ├── sections/
│   │   ├── 1-intro.txt
│   │   ├── 2-chapter1.txt
│   │   └── ...
│   └── output/
│       └── my-book-translated.docx
```
