# Knowledge Notebook Module — Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Tao module `modules/knowledge/` chua cac notebook kien thuc tu hoc, du de dat tieu chuan SE (L1-L3) + PM (L1-L4) theo CMMI Level 3 va Khung Danh Gia Nang Luc.

**Architecture:** Module Markdown-based voi 3 danh muc chinh (technical, professional, other), moi notebook la 1 file .md co cau truc: ly thuyet + vi du + bai tap tu kiem tra. Tien do theo doi qua progress.yaml. Noi dung rut trich tu 2 bo tai lieu archived (CMMI PAL 250 docs + Khung Danh Gia 28 docs).

**Tech Stack:** Markdown notebooks, YAML progress tracker, no code dependencies.

**Source Material:**
- `documents/07-archived/cmmi-main/` — 250 docs (policies, processes, templates, rules, checklists, guidelines)
- `documents/07-archived/khung-danh-gia-nang-luc-main/` — 28 docs (SE 6 competencies, PM 8 competencies, tests, rubrics)

---

## File Structure

```
modules/knowledge/
├── README.md                           # Huong dan su dung module
├── progress.yaml                       # Theo doi tien do hoc
│
├── 01-technical/                       # Kien thuc ky thuat (SE-focused)
│   ├── 01-api-design.md               # RESTful API, request/response, status codes
│   ├── 02-database-design.md          # Schema, indexes, soft delete, multi-tenant
│   ├── 03-batch-processing.md         # Batch job design, async, idempotent
│   ├── 04-security-authentication.md  # JWT, RBAC, OWASP, multi-tenant isolation
│   ├── 05-architecture-patterns.md    # Monolithic, Microservices, Clean Architecture, C4
│   ├── 06-testing-verification.md     # Unit/Integration/System test, coverage, techniques
│   ├── 07-code-review-standards.md    # Review process, coding standards, Definition of Done
│   ├── 08-ui-frontend-design.md       # Screen specs, validation, state, components
│   ├── 09-common-design.md            # Shared utilities, naming conventions, logging
│   └── 10-documentation-specs.md      # API specs, design docs, traceability
│
├── 02-professional/                    # Kien thuc chuyen mon (PM-focused + CMMI)
│   ├── 01-project-planning.md         # WBS, estimation, EVM, scheduling
│   ├── 02-requirement-management.md   # Elicitation, traceability, change control
│   ├── 03-risk-management.md          # 7-step process, mitigation strategies
│   ├── 04-quality-management.md       # Metrics, GQM, quality gates, DoD
│   ├── 05-agile-scrum-kanban.md       # Scrum framework, Sprint 0, velocity, retrospective
│   ├── 06-cmmi-process-overview.md    # 25 PAs, maturity levels, PAL structure
│   ├── 07-config-management.md        # Git workflow, branching, CI/CD, baselines
│   ├── 08-measurement-analysis.md     # Metric thresholds, RAG status, trend analysis
│   ├── 09-process-improvement.md      # Kaizen, CAR, PPQA audit, improvement cycle
│   └── 10-stakeholder-leadership.md   # Stakeholder mapping, negotiation, team building
│
└── 03-other/                           # Kien thuc khac (soft skills + culture)
    ├── 01-japanese-communication.md   # Horenso, Keigo, email format, meeting etiquette
    ├── 02-japanese-business-culture.md # Nemawashi, Wa, hierarchy, quality mindset
    ├── 03-soft-skills.md              # Problem solving, time management, EQ
    ├── 04-business-acumen.md          # ROI, cost-benefit, customer perspective
    └── 05-glossary-japanese.md        # 60+ terms: Japanese-Vietnamese-English
```

**Total: 28 files (README + progress.yaml + 25 notebooks + 1 glossary)**

---

## Notebook Template Structure

Moi notebook theo cau truc chuan:

```markdown
# [Topic Title]

> **Muc tieu:** [Sau khi doc xong, ban se biet/lam duoc gi]
> **Level:** L1 (Co ban) → L2 (Tu chu) → L3 (Dan dat) [→ L4 cho PM]
> **Thoi gian doc:** ~X phut
> **Nguon:** [CMMI docs + Khung danh gia]

---

## 1. Khai niem co ban (L1)
[Ly thuyet nen tang]

## 2. Thuc hanh nang cao (L2)
[Vi du thuc te, case study]

## 3. Chien luoc & Dan dat (L3)
[System-level thinking, coaching]

## 4. Tu kiem tra
### Cau hoi ly thuyet
- [ ] [Question 1]
- [ ] [Question 2]

### Bai tap thuc hanh
- [ ] [Exercise 1]
- [ ] [Exercise 2]

### Tieu chi dat
- L1: Tra loi duoc 60%+ cau hoi ly thuyet
- L2: Hoan thanh bai tap thuc hanh
- L3: Giai quyet duoc case study phuc tap

## 5. Tai lieu tham khao
- [Link to CMMI docs]
- [Link to Khung danh gia docs]
```

---

## Chunk 1: Module Setup & Infrastructure

### Task 1: Tao cau truc module va README

**Files:**
- Create: `modules/knowledge/README.md`
- Create: `modules/knowledge/progress.yaml`

- [ ] **Step 1: Tao directory structure**

```bash
mkdir -p modules/knowledge/{01-technical,02-professional,03-other}
```

- [ ] **Step 2: Tao README.md**

Noi dung README gom:
- Gioi thieu module (muc dich: tu hoc dat SE L3 + PM L4)
- Bang tong hop 25 notebooks voi mapping toi nang luc SE/PM
- Huong dan su dung (doc theo thu tu, lam bai tap, cap nhat progress)
- Mapping: notebook → competency group → level target
- Uoc luong thoi gian hoc tong (~40-50 gio)

- [ ] **Step 3: Tao progress.yaml**

```yaml
# Knowledge Notebook Progress Tracker
# Updated: 2026-04-08
# Target: SE L3 + PM L4

technical:
  api-design: { status: not_started, level: null, last_reviewed: null }
  database-design: { status: not_started, level: null, last_reviewed: null }
  batch-processing: { status: not_started, level: null, last_reviewed: null }
  security-authentication: { status: not_started, level: null, last_reviewed: null }
  architecture-patterns: { status: not_started, level: null, last_reviewed: null }
  testing-verification: { status: not_started, level: null, last_reviewed: null }
  code-review-standards: { status: not_started, level: null, last_reviewed: null }
  ui-frontend-design: { status: not_started, level: null, last_reviewed: null }
  common-design: { status: not_started, level: null, last_reviewed: null }
  documentation-specs: { status: not_started, level: null, last_reviewed: null }

professional:
  project-planning: { status: not_started, level: null, last_reviewed: null }
  requirement-management: { status: not_started, level: null, last_reviewed: null }
  risk-management: { status: not_started, level: null, last_reviewed: null }
  quality-management: { status: not_started, level: null, last_reviewed: null }
  agile-scrum-kanban: { status: not_started, level: null, last_reviewed: null }
  cmmi-process-overview: { status: not_started, level: null, last_reviewed: null }
  config-management: { status: not_started, level: null, last_reviewed: null }
  measurement-analysis: { status: not_started, level: null, last_reviewed: null }
  process-improvement: { status: not_started, level: null, last_reviewed: null }
  stakeholder-leadership: { status: not_started, level: null, last_reviewed: null }

other:
  japanese-communication: { status: not_started, level: null, last_reviewed: null }
  japanese-business-culture: { status: not_started, level: null, last_reviewed: null }
  soft-skills: { status: not_started, level: null, last_reviewed: null }
  business-acumen: { status: not_started, level: null, last_reviewed: null }
  glossary-japanese: { status: not_started, level: null, last_reviewed: null }

# status: not_started | in_progress | completed
# level: null | L1 | L2 | L3 | L4
```

- [ ] **Step 4: Commit**

```bash
git add modules/knowledge/
git commit -m "feat(knowledge): scaffold module structure with README and progress tracker"
```

---

## Chunk 2: Technical Notebooks (01-technical/)

Noi dung rut trich tu:
- SE nang-luc.md (6 nhom nang luc: thiet ke co ban, thiet ke chi tiet, review, chat luong, tai lieu)
- SE tests (thiet-ke-co-ban.md, thiet-ke-chi-tiet.md, review.md)
- CMMI 600_guidelines/GLN-ENG-* (engineering guidelines)
- CMMI 400_rules/RUL-ENG-* (engineering rules & thresholds)

### Task 2: Technical Notebooks 1-3 (API, Database, Batch)

**Files:**
- Create: `modules/knowledge/01-technical/01-api-design.md`
- Create: `modules/knowledge/01-technical/02-database-design.md`
- Create: `modules/knowledge/01-technical/03-batch-processing.md`
- Source: `07-archived/khung-danh-gia-nang-luc-main/roles/se/nang-luc.md` (competency #2, #3)
- Source: `07-archived/khung-danh-gia-nang-luc-main/roles/se/tests/thiet-ke-co-ban.md`
- Source: `07-archived/khung-danh-gia-nang-luc-main/roles/se/tests/thiet-ke-chi-tiet.md`
- Source: `07-archived/cmmi-main/600_guidelines/GLN-ENG-TS-*`
- Source: `07-archived/cmmi-main/400_rules/RUL-ENG-TS-*`

**Noi dung moi notebook:**

**01-api-design.md:**
- L1: RESTful conventions, HTTP methods, status codes, request/response format
- L2: API list design cho 1 module (CRUD + actions + internal), common API (error codes, pagination, authentication), versioning
- L3: System-wide API strategy, naming convention policy, NFR (response time, rate limiting)
- Tu kiem tra: Thiet ke API list cho 1 module (vd: User Management) voi CRUD + search + batch

**02-database-design.md:**
- L1: Table design, data types, PK/FK, NOT NULL, indexes
- L2: Multi-tenant isolation (tenant_code), soft delete (delete_flag), audit columns, optimistic lock (updated_at), composite indexes
- L3: Partitioning strategy, query optimization, cross-module data consistency
- Tu kiem tra: Thiet ke schema cho module Fuel Management voi multi-tenant + soft delete

**03-batch-processing.md:**
- L1: Batch vs API, trigger types (scheduled, event), input/output
- L2: Batch flow design (sequential/parallel/conditional), error handling, retry, idempotent
- L3: Complex batch with intermediate interfaces, data consistency with concurrent API access
- Tu kiem tra: Thiet ke batch flow cho import CSV 10,000 records voi error handling

- [ ] **Step 1: Doc source docs va rut trich noi dung cho 01-api-design.md**
- [ ] **Step 2: Viet 01-api-design.md theo template structure**
- [ ] **Step 3: Doc source docs va rut trich noi dung cho 02-database-design.md**
- [ ] **Step 4: Viet 02-database-design.md theo template structure**
- [ ] **Step 5: Doc source docs va rut trich noi dung cho 03-batch-processing.md**
- [ ] **Step 6: Viet 03-batch-processing.md theo template structure**
- [ ] **Step 7: Commit**

```bash
git add modules/knowledge/01-technical/0{1,2,3}-*.md
git commit -m "feat(knowledge): add technical notebooks - API, Database, Batch design"
```

### Task 3: Technical Notebooks 4-6 (Security, Architecture, Testing)

**Files:**
- Create: `modules/knowledge/01-technical/04-security-authentication.md`
- Create: `modules/knowledge/01-technical/05-architecture-patterns.md`
- Create: `modules/knowledge/01-technical/06-testing-verification.md`
- Source: `07-archived/cmmi-main/600_guidelines/GLN-ENG-VER-*`
- Source: `07-archived/cmmi-main/400_rules/RUL-ENG-VER-*`
- Source: `07-archived/cmmi-main/400_rules/RUL-ENG-TS-*`

**Noi dung:**

**04-security-authentication.md:**
- L1: JWT flow, Bearer token, basic RBAC (Admin/Operator/Viewer)
- L2: Permission matrix design, multi-tenant data isolation, input validation (XSS, SQL injection)
- L3: Security architecture, OWASP Top 10, compliance, security audit

**05-architecture-patterns.md:**
- L1: Layered architecture, component decomposition
- L2: Clean Architecture, C4 Model (4 levels), ADR (Architecture Decision Records)
- L3: Microservices vs Monolith decision, scalability design, cloud strategy

**06-testing-verification.md:**
- L1: Test levels (unit/integration/system/UAT), test case format
- L2: Techniques (equivalence partitioning, boundary value, decision table), coverage targets (unit >=80%, system >=90%)
- L3: Test strategy design, quality gates, defect management, bug density analysis

- [ ] **Step 1-6: Viet 3 notebooks (tuong tu Task 2)**
- [ ] **Step 7: Commit**

```bash
git add modules/knowledge/01-technical/0{4,5,6}-*.md
git commit -m "feat(knowledge): add technical notebooks - Security, Architecture, Testing"
```

### Task 4: Technical Notebooks 7-10 (Review, UI, Common, Docs)

**Files:**
- Create: `modules/knowledge/01-technical/07-code-review-standards.md`
- Create: `modules/knowledge/01-technical/08-ui-frontend-design.md`
- Create: `modules/knowledge/01-technical/09-common-design.md`
- Create: `modules/knowledge/01-technical/10-documentation-specs.md`
- Source: `07-archived/khung-danh-gia-nang-luc-main/roles/se/tests/review.md`
- Source: `07-archived/cmmi-main/400_rules/RUL-ENG-TS-03-*` (Coding Standard)
- Source: `07-archived/cmmi-main/400_rules/RUL-ENG-TS-04-*` (Code Review)

**Noi dung:**

**07-code-review-standards.md:**
- L1: Coding standards (cyclomatic complexity <=10, function <=50 LOC, comment >=10%)
- L2: Review process (200 LOC/hour max), review checklist, evidence collection
- L3: Define quality gates, mentor team on review culture, Definition of Done

**08-ui-frontend-design.md:**
- L1: Screen layout (header/search/result/action), basic validation
- L2: Component design (Atoms/Molecules/Organisms), state management, event handling
- L3: Design system, i18n, accessibility, cross-module UI consistency

**09-common-design.md:**
- L1: Naming conventions (snake_case DB, kebab-case URL, camelCase JS)
- L2: Common utilities (date, string, validation), error code system, logging strategy
- L3: Shared library design, cross-module standards, common API patterns

**10-documentation-specs.md:**
- L1: Fill template correctly (API spec, DB spec, batch spec)
- L2: Write clear specs (developer can implement without questions), traceability
- L3: Design templates, define documentation guidelines for team

- [ ] **Step 1-8: Viet 4 notebooks**
- [ ] **Step 9: Commit**

```bash
git add modules/knowledge/01-technical/0{7,8,9}-*.md modules/knowledge/01-technical/10-*.md
git commit -m "feat(knowledge): add technical notebooks - Review, UI, Common, Documentation"
```

---

## Chunk 3: Professional Notebooks (02-professional/)

Noi dung rut trich tu:
- PM nang-luc.md (8 nhom nang luc)
- PM tests (planning.md, risk-management.md, communication.md)
- CMMI 200_process/PRC-PJM-* (project management processes)
- CMMI 600_guidelines/GLN-PJM-*, GLN-PMG-* (management guidelines)
- CMMI 400_rules/RUL-PJM-*, RUL-PMG-* (management rules)

### Task 5: Professional Notebooks 1-3 (Planning, Requirements, Risk)

**Files:**
- Create: `modules/knowledge/02-professional/01-project-planning.md`
- Create: `modules/knowledge/02-professional/02-requirement-management.md`
- Create: `modules/knowledge/02-professional/03-risk-management.md`
- Source: `07-archived/khung-danh-gia-nang-luc-main/roles/pm/nang-luc.md` (competency #1, #2, #3)
- Source: `07-archived/khung-danh-gia-nang-luc-main/roles/pm/tests/planning.md`
- Source: `07-archived/khung-danh-gia-nang-luc-main/roles/pm/tests/risk-management.md`
- Source: `07-archived/cmmi-main/600_guidelines/GLN-PJM-PP-*`
- Source: `07-archived/cmmi-main/200_process/PRC-PJM-PP-*`

**Noi dung:**

**01-project-planning.md:**
- L1: Update Gantt chart, basic WBS, man-hour tracking
- L2: Full WBS creation, multiple estimation methods (Story Point, Planning Poker, T-shirt), velocity-based scheduling, Sprint 0 planning
- L3: Multi-module WBS, challenge estimates, resource optimization, 12-step planning process
- L4 (PM only): Portfolio-level planning framework, organizational estimation baseline
- Tu kiem tra: Tao WBS + Release Plan cho du an 6 thang, 8 nguoi

**02-requirement-management.md:**
- L1: Track requirement status, basic classification
- L2: Product backlog management, MoSCoW prioritization, traceability matrix, change request 5-step
- L3: Full traceability (requirement → design → code → test → delivery), prototype-driven approach
- Tu kiem tra: Xay dung RTM cho 1 module voi 20 requirements

**03-risk-management.md:**
- L1: Identify risks when asked, basic risk register
- L2: Proactive 7-step risk process, 6 risk categories, Probability × Impact matrix, mitigation plans
- L3: Predictive risk assessment, contingency budget, risk framework for team
- Tu kiem tra: Giai quyet 4 crisis scenarios (spec ambiguity, resource loss, quality alert, compound crisis)

- [ ] **Step 1-6: Viet 3 notebooks (doc source → viet content)**
- [ ] **Step 7: Commit**

```bash
git add modules/knowledge/02-professional/0{1,2,3}-*.md
git commit -m "feat(knowledge): add professional notebooks - Planning, Requirements, Risk"
```

### Task 6: Professional Notebooks 4-6 (Quality, Agile, CMMI)

**Files:**
- Create: `modules/knowledge/02-professional/04-quality-management.md`
- Create: `modules/knowledge/02-professional/05-agile-scrum-kanban.md`
- Create: `modules/knowledge/02-professional/06-cmmi-process-overview.md`
- Source: `07-archived/khung-danh-gia-nang-luc-main/roles/pm/nang-luc.md` (competency #4, #6)
- Source: `07-archived/cmmi-main/600_guidelines/GLN-PMG-MA-*`, `GLN-PMG-PPQA-*`
- Source: `07-archived/cmmi-main/README.md`

**Noi dung:**

**04-quality-management.md:**
- L1: Monitor bug count, follow review checklist
- L2: Quality plan, GQM metrics, DoD (Story/Sprint/Release), bug density < 10/KLOC
- L3: Quality strategy design, explain metrics to customer (説明できる品質)
- Tu kiem tra: Xay dung Quality Plan voi 10 KPIs + nguong RAG

**05-agile-scrum-kanban.md:**
- L1: Attend ceremonies, update task board
- L2: Facilitate all Scrum events, velocity tracking, burn-down, Sprint 0 setup
- L3: Optimize sprint process, hybrid Waterfall+Agile balance, SAFe/LeSS awareness
- Tu kiem tra: Len ke hoach Sprint 0 + Release Plan cho du an hybrid

**06-cmmi-process-overview.md:**
- L1: Understand 6-tier document hierarchy (POL/PRC/TPL/RUL/CHK/GLN)
- L2: Know 25 Process Areas, tailoring by project size (S/M/L)
- L3: Process improvement governance, PAL versioning, pilot validation
- Tu kiem tra: Map 1 du an thuc te vao CMMI process areas

- [ ] **Step 1-6: Viet 3 notebooks**
- [ ] **Step 7: Commit**

```bash
git add modules/knowledge/02-professional/0{4,5,6}-*.md
git commit -m "feat(knowledge): add professional notebooks - Quality, Agile, CMMI"
```

### Task 7: Professional Notebooks 7-10 (CM, Metrics, Improvement, Leadership)

**Files:**
- Create: `modules/knowledge/02-professional/07-config-management.md`
- Create: `modules/knowledge/02-professional/08-measurement-analysis.md`
- Create: `modules/knowledge/02-professional/09-process-improvement.md`
- Create: `modules/knowledge/02-professional/10-stakeholder-leadership.md`
- Source: `07-archived/cmmi-main/600_guidelines/GLN-TOOL-*` (Git, Redmine)
- Source: `07-archived/cmmi-main/400_rules/RUL-PMG-MA-*`
- Source: `07-archived/cmmi-main/200_process/PRC-PMG-OPF-*`
- Source: `07-archived/khung-danh-gia-nang-luc-main/roles/pm/nang-luc.md` (competency #5, #7, #8)
- Source: `07-archived/khung-danh-gia-nang-luc-main/roles/pm/tests/communication.md`

**Noi dung:**

**07-config-management.md:**
- L1: Basic Git (add/commit/push), branch naming
- L2: Gitflow (main/develop/feature/release/hotfix), CI/CD, baseline management, semantic versioning
- L3: CM strategy design, audit procedures, release management framework

**08-measurement-analysis.md:**
- L1: Collect basic metrics (bug count, schedule status)
- L2: Metric thresholds (design review 0.25-0.5/page, code review 3-7/KLOC, test 70-100/KLOC), moving average, RAG zones
- L3: Trend analysis, predictive forecasting (EAC/ETC), metrics framework design

**09-process-improvement.md:**
- L1: Follow CAR process, participate in retrospective
- L2: Root cause analysis (5 Why, Fishbone), improvement backlog, pilot testing
- L3: Improvement governance, PAL maintenance, org-wide process standardization

**10-stakeholder-leadership.md:**
- L1: Understand stakeholder expectations, honest reporting
- L2: Stakeholder mapping, expectation management, conflict resolution 1-1, onboarding
- L3: Direct negotiation (win-win), build high-performing team, mentor juniors
- L4 (PM only): Strategic partner positioning, build PM capability across org

- [ ] **Step 1-8: Viet 4 notebooks**
- [ ] **Step 9: Commit**

```bash
git add modules/knowledge/02-professional/0{7,8,9}-*.md modules/knowledge/02-professional/10-*.md
git commit -m "feat(knowledge): add professional notebooks - CM, Metrics, Improvement, Leadership"
```

---

## Chunk 4: Other Notebooks + Final Integration

### Task 8: Other Notebooks (03-other/)

**Files:**
- Create: `modules/knowledge/03-other/01-japanese-communication.md`
- Create: `modules/knowledge/03-other/02-japanese-business-culture.md`
- Create: `modules/knowledge/03-other/03-soft-skills.md`
- Create: `modules/knowledge/03-other/04-business-acumen.md`
- Create: `modules/knowledge/03-other/05-glossary-japanese.md`
- Source: `07-archived/cmmi-main/600_guidelines/GLN-PJM-PMC-02-*` (Japanese Communication Guide)
- Source: `07-archived/khung-danh-gia-nang-luc-main/docs/thuat-ngu.md` (60+ terms)
- Source: `07-archived/khung-danh-gia-nang-luc-main/roles/se/tests/communication.md`
- Source: `07-archived/khung-danh-gia-nang-luc-main/roles/pm/tests/communication.md`

**Noi dung:**

**01-japanese-communication.md:**
- Horenso (報連相): Report-Liaison-Consult protocol
- Email format: Greeting → Context → Request → Closing (敬語)
- Meeting minutes (議事録): Format, bilingual, <=24h delivery
- Escalation rules: Red status → report within 4 hours
- Bad news delivery: Report early, propose solution, never hide

**02-japanese-business-culture.md:**
- Nemawashi (根回し): Pre-meeting consensus building
- Wa (和): Group harmony, avoid direct confrontation
- Keishiki (形式): Formal structure in everything
- Kuuki wo Yomu (空気を読む): Read the atmosphere
- Quality mindset: Prevention > remediation, 説明できる品質

**03-soft-skills.md:**
- Problem solving (root cause analysis, trade-off analysis)
- Time management (priority, deadline, workload balancing)
- Emotional intelligence (self-awareness, empathy, stress management)
- Professional ethics (honesty, accountability, confidentiality)

**04-business-acumen.md:**
- ROI & cost-benefit analysis
- Customer perspective & business process understanding
- MVP identification & scope management
- Success criteria definition

**05-glossary-japanese.md:**
- 60+ terms: Japanese → Romaji → Vietnamese → English
- Categories: Process (要件定義, 基本設計, ...), Design (共通化, 排他制御, ...), Management (見積, 品質, リスク, ...)

- [ ] **Step 1-10: Viet 5 notebooks**
- [ ] **Step 11: Commit**

```bash
git add modules/knowledge/03-other/
git commit -m "feat(knowledge): add other notebooks - Japanese comm, culture, soft skills, glossary"
```

### Task 9: Final Integration & Documentation

**Files:**
- Update: `modules/knowledge/README.md` (final version with all notebooks listed)
- Update: `modules/knowledge/progress.yaml` (verify all entries match actual files)
- Update: `CLAUDE.md` (add knowledge module to project structure)

- [ ] **Step 1: Cap nhat README.md voi bang mapping day du**

Bang mapping notebook → SE competency → PM competency → CMMI PA:

| Notebook | SE Competency | PM Competency | CMMI PA |
|----------|--------------|---------------|---------|
| 01-tech/01-api-design | #2 基本設計力, #3 詳細設計力 | — | ENG-TS |
| 01-tech/06-testing | — | #4 品質管理 | ENG-VER, ENG-VAL |
| 02-prof/01-planning | — | #1 計画・見積力 | PJM-PP |
| 02-prof/03-risk | — | #3 リスク管理 | PJM-RSKM |
| 03-other/01-japanese-comm | #4 コミュニケーション | #5 コミュニケーション | PJM-IPM |
| ... | ... | ... | ... |

- [ ] **Step 2: Cap nhat CLAUDE.md**

Them vao Project Structure:
```
├── modules/
│   ├── social/                     # Social automation (8 workflows)
│   ├── novel/                      # Novel translation (1 workflow)
│   └── knowledge/                  # Knowledge notebooks (25 topics)
```

- [ ] **Step 3: Verify file count**

```bash
find modules/knowledge -name "*.md" | wc -l  # Expected: 26 (README + 25 notebooks)
find modules/knowledge -name "*.yaml" | wc -l  # Expected: 1
```

- [ ] **Step 4: Commit & push**

```bash
git add modules/knowledge/ CLAUDE.md
git commit -m "feat(knowledge): finalize module with README mapping and CLAUDE.md update"
```

---

## Execution Summary

| Chunk | Tasks | Notebooks | Estimated Time |
|-------|-------|-----------|---------------|
| 1. Setup | Task 1 | 0 (infra) | 10 min |
| 2. Technical | Tasks 2-4 | 10 notebooks | 60-90 min |
| 3. Professional | Tasks 5-7 | 10 notebooks | 60-90 min |
| 4. Other + Final | Tasks 8-9 | 5 notebooks + integration | 30-45 min |
| **Total** | **9 tasks** | **25 notebooks** | **~3-4 hours** |

## Learning Path Recommendation

**Giai doan 1 — Foundation (SE L1 + PM L1):** ~15h
- 01-tech/01 → 02 → 03 → 09 (API, DB, Batch, Common)
- 02-prof/06 (CMMI overview)
- 03-other/01 → 02 → 05 (Japanese comm, culture, glossary)

**Giai doan 2 — Independent (SE L2 + PM L2):** ~15h
- 01-tech/04 → 05 → 06 → 07 (Security, Architecture, Testing, Review)
- 02-prof/01 → 02 → 03 → 04 → 05 (Planning, Req, Risk, Quality, Agile)

**Giai doan 3 — Leadership (SE L3 + PM L3/L4):** ~15h
- 01-tech/08 → 10 (UI, Documentation)
- 02-prof/07 → 08 → 09 → 10 (CM, Metrics, Improvement, Leadership)
- 03-other/03 → 04 (Soft skills, Business acumen)
