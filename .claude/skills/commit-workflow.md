# Skill: Commit Workflow for AI Agent Project

**Version:** 1.0
**Last Updated:** 2026-03-13
**Purpose:** Git commit workflow cho AI Agent Social Media Automation project

---

## 📋 Overview

Skill này định nghĩa quy trình commit chuẩn cho dự án AI Agent, bao gồm:
- Git configuration
- Conventional commit format
- Commit message templates
- Best practices

---

## 🎯 When to Use This Skill

**Use for ALL commits:**
- ✅ Adding new documentation
- ✅ Creating new strategies
- ✅ Updating tech stack analysis
- ✅ Adding automation workflows
- ✅ Creating templates/examples

---

## ⚙️ Git Configuration

### User Config

**ALWAYS use these credentials:**

```bash
# For this repository
git config user.name "VictorAurelius"
git config user.email "vankiet14491@gmail.com"

# Verify
git config user.name   # Should output: VictorAurelius
git config user.email  # Should output: vankiet14491@gmail.com
```

**Note:** This is local config (only for this repo), not global.

---

## 📝 Commit Message Format (Conventional Commits)

### Template

```
<type>(<scope>): <subject>

[optional body - explain WHAT and WHY]

[optional details - features, files, metrics]

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>
```

### Commit Types

| Type | When to Use | Example |
|------|------------|---------|
| `docs` | Documentation changes | `docs(linkedin): add content strategy` |
| `feat` | New features/workflows | `feat(automation): add Make.com workflow` |
| `fix` | Bug fixes | `fix(readme): correct tech stack pricing` |
| `refactor` | Restructuring | `refactor: organize documents by platform` |
| `chore` | Maintenance, configs | `chore: update .gitignore` |
| `style` | Formatting only | `style(docs): format markdown tables` |

### Scope Guidelines

**For this project:**
- `linkedin` - LinkedIn strategy files
- `facebook` - Facebook strategies (tech-page, chinese-page)
- `tech-stack` - Tech stack documentation
- `automation` - Workflow & automation configs
- `templates` - Content templates
- `readme` - Root README or project docs

---

## 💡 Commit Message Examples

### Example 1: Adding Documentation

```bash
git commit -m "$(cat <<'EOF'
docs(linkedin): add comprehensive LinkedIn AI agent strategy

Add detailed strategy for LinkedIn personal branding automation.

Key sections:
- Profile optimization checklist
- Content pillars (4 types: news, knowledge, product, engagement)
- AI workflow (RSS → Claude → Notion → LinkedIn)
- Monetization strategy
- 8-phase implementation roadmap

Metrics:
- Feasibility score: 7.2/10
- Target: 1000+ followers in 3 months
- Cost: $30-60/month

Files: documents/linkedin/strategy.md (663 lines)

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>
EOF
)"
```

### Example 2: Adding New Feature/Workflow

```bash
git commit -m "$(cat <<'EOF'
feat(automation): add Make.com workflow template for tech news

Add complete Make.com workflow template for automating tech news posts.

Workflow steps:
1. Fetch RSS feeds (Hacker News, Dev.to, TechCrunch)
2. AI filter & rank articles (Claude API)
3. Generate Facebook posts (Claude with prompt)
4. Save to Notion queue (review required)
5. Telegram notification

Configuration:
- Operations: ~19/day = 570/month (fits Make.com free tier)
- AI cost: ~$5-10/month (Claude Sonnet)
- Includes error handling & retries

Files: workflows/make-tech-news.json

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>
EOF
)"
```

### Example 3: Refactoring

```bash
git commit -m "$(cat <<'EOF'
refactor: organize documents into platform-specific folders

Restructure documents/ for better organization and discoverability.

New structure:
- documents/linkedin/ - LinkedIn strategies
- documents/facebook/tech-page/ - Tech page strategies
- documents/facebook/chinese-page/ - Chinese learning strategies
- documents/tech-stack/ - Tech stack overview
- documents/99-archived/ - Archived drafts

Changes:
- Moved 3 strategy files to appropriate folders
- Added README.md to each folder for quick navigation
- Archived combined Facebook strategy (no longer needed)

Files: 10 files moved, 4 READMEs added

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>
EOF
)"
```

### Example 4: Initial Commit

```bash
git commit -m "$(cat <<'EOF'
docs: initial commit - AI Agent social media automation strategies

Add comprehensive documentation for automating LinkedIn & Facebook content
using AI agents (Claude API, GPT-4o) with orchestration tools.

Documentation includes:
- LinkedIn strategy (personal branding, networking)
- Facebook Tech Page strategy (dev audience)
- Facebook Chinese Page strategy (language learning)
- Complete tech stack analysis (tools, costs, comparisons)

Features:
- AI automation workflows (Make.com/n8n + Claude API)
- Content templates & examples
- Monetization roadmaps (affiliate, products, courses)
- Week-by-week implementation guides
- Feasibility scores (7.2-8.1/10)

Tech stack:
- Orchestration: Make.com ($9/mo) / n8n (self-hosted)
- AI: Claude Sonnet 3.5 ($10-20/mo)
- Storage: Notion (free)
- Design: Canva Pro ($13/mo)
- Total: ~$32-50/month

Files: 13 markdown files, README.md, .gitignore

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>
EOF
)"
```

### Example 5: Small Fix

```bash
git commit -m "fix(tech-stack): correct Claude API pricing estimate

Update Claude Sonnet pricing from $10-30/mo to $5-10/mo based on
realistic usage calculation (90k tokens/month output).

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

---

## 🔄 Commit Workflow

### Standard Flow

```bash
# 1. Check status
git status

# 2. Stage files
git add <files>
# Or stage all: git add .

# 3. Check what's staged
git status

# 4. Commit with message
git commit -m "$(cat <<'EOF'
<type>(<scope>): <subject>

<body>

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>
EOF
)"

# 5. Verify commit
git log -1 --stat

# 6. Push (if ready)
git push origin <branch>
```

### Using HEREDOC (Recommended for Multi-line)

**Why HEREDOC?**
- ✅ Preserves formatting
- ✅ Allows multi-line messages
- ✅ No escaping issues
- ✅ Easy to read & edit

**Format:**
```bash
git commit -m "$(cat <<'EOF'
Your commit message here
Can be multiple lines
With proper formatting

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>
EOF
)"
```

**CRITICAL:** Always use `<<'EOF'` (with quotes) to prevent variable expansion.

---

## ✅ Commit Message Checklist

Before committing, verify:

- [ ] **Type is correct** (docs, feat, fix, refactor, chore, style)
- [ ] **Scope is appropriate** (linkedin, facebook, tech-stack, etc.)
- [ ] **Subject is clear** (<72 chars, imperative mood, no period)
- [ ] **Body explains WHAT and WHY** (not just WHAT)
- [ ] **Details included** (files changed, metrics, features)
- [ ] **Co-Authored-By line present**
- [ ] **No secrets/credentials** in commit message or files
- [ ] **Git config is correct** (VictorAurelius / vankiet14491@gmail.com)

---

## 🚫 Anti-Patterns (What NOT to Do)

❌ **Vague messages:**
```bash
git commit -m "update docs"  # Too vague
git commit -m "fix"          # What fix?
git commit -m "wip"          # Work in progress = not ready to commit
```

✅ **Better:**
```bash
git commit -m "docs(linkedin): add profile optimization checklist

Add 15-item checklist for optimizing LinkedIn profile including
photo guidelines, headline formula, and about section structure.

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

❌ **Mixing concerns:**
```bash
# Don't commit unrelated changes together
git add documents/linkedin/strategy.md
git add documents/facebook/tech-page/strategy.md
git commit -m "add strategies"  # Too broad
```

✅ **Better:**
```bash
# Commit related changes separately
git add documents/linkedin/
git commit -m "docs(linkedin): add strategy"

git add documents/facebook/tech-page/
git commit -m "docs(facebook): add tech page strategy"
```

❌ **Forgetting Co-Authored-By:**
```bash
git commit -m "docs: add readme"  # Missing Co-Authored-By
```

---

## 🎯 Special Cases

### Committing Archived Files

```bash
git commit -m "$(cat <<'EOF'
chore: archive outdated strategy drafts

Move previous draft versions to documents/99-archived/.

Archived files:
- facebook-ai-agent-strategy.md (combined version, now split)
- linkedin-ai-agent-strategy.md (moved from root)

Reason: These are superseded by new organized structure.
Kept for reference only.

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>
EOF
)"
```

### Committing Config Changes

```bash
git commit -m "$(cat <<'EOF'
chore: update .gitignore for AI Agent project

Add entries to exclude:
- Previous project artifacts (.claude/, .github/, .vscode/)
- Sensitive files (API keys, credentials)
- Temporary files (.log/, cache/)

Ensures only relevant AI Agent project files are tracked.

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>
EOF
)"
```

### Committing Multiple Files (Same Feature)

```bash
git commit -m "$(cat <<'EOF'
docs(facebook): add complete Facebook strategies for 2 pages

Add comprehensive strategies for Tech Page and Chinese Learning Page.

Tech Page (7.9/10 feasibility):
- Target: Vietnamese developers
- Content: News, tutorials, tools, career insights
- Revenue: $1000+/month by month 12

Chinese Page (8.1/10 feasibility):
- Target: Vietnamese learners (HSK 1-4)
- Content: Vocab, grammar, culture
- Revenue: $500-1500/month by month 12

Both include:
- Complete content templates
- AI automation workflows
- Growth strategies (0-10k followers)
- Monetization roadmaps

Files:
- documents/facebook/tech-page/strategy.md (1,033 lines)
- documents/facebook/tech-page/README.md
- documents/facebook/chinese-page/strategy.md (1,056 lines)
- documents/facebook/chinese-page/README.md

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>
EOF
)"
```

---

## 📊 Commit Hygiene Best Practices

### Frequency

- ✅ **Commit often** (small, logical chunks)
- ✅ **Each commit = one logical change**
- ✅ **Commit before switching context**

### Size

- ✅ **Keep commits focused** (1 feature/fix per commit)
- ⚠️ **Large commits OK if**:
  - Initial documentation setup
  - Major refactoring (well documented)
  - Multiple related files (same feature)

### Testing

- ✅ **Ensure files are correct** before committing
- ✅ **Check for typos** in commit message
- ✅ **Verify git config** before first commit

---

## 🔐 Security Checklist

Before committing, ensure:

- [ ] No API keys in files
- [ ] No passwords or tokens
- [ ] No `.env` files (should be in .gitignore)
- [ ] No personal/sensitive data
- [ ] Check with: `git diff --staged`

---

## 🛠️ Automation Opportunity

**Future enhancement:**
- Create pre-commit hook to check:
  - Git config is correct
  - Commit message follows format
  - No secrets in staged files
  - Co-Authored-By line present

**File:** `.git/hooks/pre-commit` (future)

---

## 📚 Related Skills

- `organize.md` - File organization guidelines
- `documentation-structure.md` - Documentation best practices

---

**Remember:** Good commits = good project history = easier collaboration & debugging

Last updated: 2026-03-13
