# Knowledge Notebooks

Module tu hoc kien thuc de dat tieu chuan **SE L3 + PM L4** theo CMMI Level 3 va Khung Danh Gia Nang Luc.

## Tong quan

| Danh muc | So notebook | Noi dung chinh |
|----------|-------------|----------------|
| **01-technical/** | 10 | Ky thuat: API, DB, Batch, Security, Architecture, Testing, Review, UI, Common, Docs |
| **02-professional/** | 10 | Chuyen mon: Planning, Requirements, Risk, Quality, Agile, CMMI, CM, Metrics, Improvement, Leadership |
| **03-other/** | 5 | Khac: Japanese comm, Culture, Soft skills, Business acumen, Glossary |

## Mapping: Notebook → Nang luc SE/PM → CMMI

### Technical (SE-focused)

| # | Notebook | SE Competency | CMMI PA | Level Target |
|---|----------|--------------|---------|-------------|
| 1 | api-design | #2 基本設計力, #3 詳細設計力 | ENG-TS | L1→L3 |
| 2 | database-design | #2 基本設計力, #3 詳細設計力 | ENG-TS | L1→L3 |
| 3 | batch-processing | #2 基本設計力, #3 詳細設計力 | ENG-TS | L1→L3 |
| 4 | security-authentication | #3 詳細設計力, #5 品質意識 | ENG-TS, SUP-SEC | L1→L3 |
| 5 | architecture-patterns | #2 基本設計力 | ENG-TS, ENG-PI | L1→L3 |
| 6 | testing-verification | #5 品質意識 | ENG-VER, ENG-VAL | L1→L3 |
| 7 | code-review-standards | #5 品質意識 | ENG-VER | L1→L3 |
| 8 | ui-frontend-design | #3 詳細設計力 | ENG-TS | L1→L3 |
| 9 | common-design | #2 基本設計力 | ENG-TS, PMG-OPD | L1→L3 |
| 10 | documentation-specs | #6 ドキュメント作成力 | ENG-TS | L1→L3 |

### Professional (PM-focused + CMMI)

| # | Notebook | PM Competency | CMMI PA | Level Target |
|---|----------|--------------|---------|-------------|
| 1 | project-planning | #1 計画・見積力 | PJM-PP | L1→L4 |
| 2 | requirement-management | #2 要件管理 | ENG-REQM, ENG-RD | L1→L3 |
| 3 | risk-management | #3 リスク管理 | PJM-RSKM | L1→L3 |
| 4 | quality-management | #4 品質管理 | PMG-MA, PMG-PPQA | L1→L4 |
| 5 | agile-scrum-kanban | #6 Agile実践力 | PJM-IPM | L1→L3 |
| 6 | cmmi-process-overview | — | PMG-OPF, PMG-OPD | L1→L3 |
| 7 | config-management | — | SUP-CM | L1→L3 |
| 8 | measurement-analysis | #4 品質管理 | PMG-MA | L1→L3 |
| 9 | process-improvement | — | PMG-OPF, PMG-CAR | L1→L3 |
| 10 | stakeholder-leadership | #7 ステークホルダー管理, #8 リーダーシップ | PJM-IPM | L1→L4 |

### Other (Soft skills + Culture)

| # | Notebook | SE/PM Competency | CMMI PA | Level Target |
|---|----------|-----------------|---------|-------------|
| 1 | japanese-communication | SE #4, PM #5 コミュニケーション | PJM-IPM | L1→L3 |
| 2 | japanese-business-culture | SE #4, PM #5 | PJM-IPM | L1→L3 |
| 3 | soft-skills | PM #8 リーダーシップ | — | L1→L3 |
| 4 | business-acumen | PM #7 ステークホルダー管理 | — | L1→L3 |
| 5 | glossary-japanese | SE #4, PM #5 | — | Reference |

## Lo trinh hoc

### Giai doan 1 — Foundation (SE L1 + PM L1) ~15h

1. `03-other/05-glossary-japanese` — Thuat ngu co ban
2. `01-technical/01-api-design` — API co ban
3. `01-technical/02-database-design` — Database co ban
4. `01-technical/03-batch-processing` — Batch co ban
5. `01-technical/09-common-design` — Naming conventions, utilities
6. `02-professional/06-cmmi-process-overview` — CMMI overview
7. `03-other/01-japanese-communication` — Horenso co ban
8. `03-other/02-japanese-business-culture` — Van hoa Nhat

### Giai doan 2 — Independent (SE L2 + PM L2) ~15h

1. `01-technical/04-security-authentication` — Security & RBAC
2. `01-technical/05-architecture-patterns` — Architecture
3. `01-technical/06-testing-verification` — Testing techniques
4. `01-technical/07-code-review-standards` — Code review
5. `02-professional/01-project-planning` — WBS, estimation
6. `02-professional/02-requirement-management` — Traceability
7. `02-professional/03-risk-management` — 7-step risk process
8. `02-professional/04-quality-management` — GQM, metrics
9. `02-professional/05-agile-scrum-kanban` — Scrum, Sprint 0

### Giai doan 3 — Leadership (SE L3 + PM L3/L4) ~15h

1. `01-technical/08-ui-frontend-design` — UI specs
2. `01-technical/10-documentation-specs` — Doc guidelines
3. `02-professional/07-config-management` — CM strategy
4. `02-professional/08-measurement-analysis` — Trend analysis, RAG
5. `02-professional/09-process-improvement` — CAR, Kaizen
6. `02-professional/10-stakeholder-leadership` — Negotiation, team building
7. `03-other/03-soft-skills` — EQ, problem solving
8. `03-other/04-business-acumen` — ROI, customer perspective

## Cach su dung

1. Doc theo lo trinh (Giai doan 1 → 2 → 3)
2. Moi notebook: doc ly thuyet → lam bai tap tu kiem tra → tu cham diem
3. Cap nhat `progress.yaml` sau moi notebook:
   - `status`: not_started → in_progress → completed
   - `level`: L1 / L2 / L3 (level dat duoc)
   - `last_reviewed`: ngay doc gan nhat

## Nguon tai lieu

- `documents/07-archived/cmmi-main/` — CMMI Level 3 PAL (250 docs)
- `documents/07-archived/khung-danh-gia-nang-luc-main/` — Khung Danh Gia Nang Luc (28 docs)
