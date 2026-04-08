# Quality Management & Metrics (Quản lý Chất lượng & Chỉ số)

> **Mục tiêu:** Thiết lập, theo dõi và báo cáo chất lượng dự án với số liệu thuyết phục cho khách hàng Nhật
> **Level:** L1 -> L2 -> L3 -> L4
> **Thời gian đọc:** ~25 phút
> **Liên quan:** PM Competency #4 (品質管理), CMMI PA: PMC (Project Monitoring & Control), VER, VAL

---

## 1. Khái niệm cơ bản (L1)

### 1.1. Chất lượng là gì trong dự án Nhật?

**説明できる品質 (Setsumei dekiru hinshitsu)** = "Chất lượng có thể giải thích được"
- Không chỉ "ít bug" mà phải CHỨNG MINH bằng số liệu
- Khách hàng Nhật hỏi: "Tại sao bạn nói chất lượng tốt?" -> Phải trả lời bằng DATA

### 1.2. Bug Count & Review cơ bản

**Hành vi L1:**
- Theo dõi bug count: số bug mở, số bug đã fix, số bug critical
- Tham gia review meeting, ghi 指摘件数 (số lỗi chỉ ra)
- Theo dõi review checklist
- Chuẩn bị data khi được yêu cầu
- Hiểu quality target của dự án

**Bug Classification:**

| Severity | Định nghĩa | Ví dụ | SLA Fix |
|----------|-----------|-------|---------|
| **Critical** | Hệ thống không hoạt động | Crash, data loss, security breach | Fix trong 4h |
| **Major** | Chức năng chính lỗi | Login fail, calculation sai | Fix trong 1 ngày |
| **Minor** | Chức năng phụ lỗi | UI misalignment, typo | Fix trong 3 ngày |
| **Trivial** | Cosmetic, không ảnh hưởng | Color sai, spacing | Fix khi có thời gian |

### 1.3. Ngưỡng chất lượng cơ bản (GLN-PJM-PMC-01)

| Chỉ số | Xanh | Vàng | Đỏ |
|--------|------|------|-----|
| **Bug density (tổng thể)** | < 10 bugs/KLOC | 10-20 | > 20 |
| **Tiến độ** | Đúng hạn | Trễ 1-2 tuần | Trễ > 2 tuần |
| **Ngân sách** | Vượt <= 5% | Vượt 5-10% | Vượt > 10% |
| **Phạm vi** | Đúng 100% | 90-99% | < 90% |

---

## 2. Thực hành nâng cao (L2)

### 2.1. Quality Plan với GQM (Goal-Question-Metric)

**GQM Framework:**

```
GOAL (Mục tiêu):
  "Giao sản phẩm chất lượng cao, đạt tiêu chuẩn khách hàng Nhật"

QUESTION (Câu hỏi):
  Q1: Code có ít lỗi không?          -> Metric: Bug density
  Q2: Code có được review đầy đủ?    -> Metric: Review coverage
  Q3: Test có đầy đủ không?          -> Metric: Test coverage
  Q4: Defect có được xử lý kịp?      -> Metric: Defect fix rate
  Q5: Sản phẩm có ổn định không?     -> Metric: Regression bug rate

METRIC (Chỉ số):
  M1: Bug density <= 0.5 bugs/KLoC (tại system test)
  M2: Code review coverage = 100%
  M3: Unit test coverage >= 80%
  M4: Critical bug fix within 4h, Major within 1 day
  M5: Regression bug rate < 5% của tổng bug
```

### 2.2. Definition of Done (DoD) — 3 cấp

**Story-level DoD:**
```
[ ] Code hoàn thành, compile thành công
[ ] Unit test written & pass (coverage >= 80%)
[ ] Code review completed (0 critical comments)
[ ] PO accepted (demo + acceptance criteria met)
[ ] Documentation updated (nếu cần)
```

**Sprint-level DoD:**
```
[ ] Tất cả stories trong sprint được accepted
[ ] Sprint demo hoàn thành, khách hàng confirm
[ ] Không có critical/major bug open
[ ] Regression test pass
[ ] Sprint burndown chart updated
[ ] Sprint retrospective completed
```

**Release-level DoD:**
```
[ ] Tất cả features deployed thành công
[ ] System test completed, bug density <= target
[ ] UAT completed, khách hàng sign-off
[ ] Release documentation hoàn thành
[ ] Training materials chuẩn bị (nếu cần)
[ ] Không có L1 (critical) bug open
[ ] Performance test pass (response time <= target)
[ ] Security scan pass (0 critical vulnerabilities)
```

### 2.3. KPI Dashboard — 10 chỉ số chính

| # | KPI | Target | Công thức | Tần suất |
|---|-----|--------|-----------|----------|
| 1 | **Bug density** | <= 0.5 bugs/KLoC (ST) | Số bug / (Lines of code / 1000) | Sprint |
| 2 | **Code review coverage** | 100% | Số file reviewed / Tổng số file | Sprint |
| 3 | **Unit test coverage** | >= 80% | Lines tested / Total lines | Sprint |
| 4 | **Defect fix rate** | >= 95% | Bug fixed / Bug found | Sprint |
| 5 | **Critical bug turnaround** | <= 4 hours | Thời gian từ report đến fix | Realtime |
| 6 | **Regression bug rate** | < 5% | Regression bugs / Total bugs | Release |
| 7 | **Schedule variance (SV)** | <= 0 | Actual - Planned (ngày) | Weekly |
| 8 | **Velocity stability** | +/- 15% | (Current - Avg) / Avg | Sprint |
| 9 | **Review 指摘 density** | 5-15 per review | Số 指摘 / Số review sessions | Sprint |
| 10 | **Customer satisfaction** | >= 4/5 | Survey score | Monthly |

### 2.4. Quality Gates

**Gate tại mỗi milestone:**

| Gate | Tiêu chí | Ai kiểm tra | Fail Action |
|------|----------|-------------|-------------|
| **Design Gate** | Design review done, 指摘 resolved, NFR addressed | TL + PM | KHÔNG bắt đầu coding |
| **Code Gate** | Code review 100%, unit test >= 80%, 0 critical | TL + QA | KHÔNG chuyển sang IT |
| **IT Gate** | Integration test pass, API contract verified | QA + TL | KHÔNG chuyển sang ST |
| **ST Gate** | Bug density <= target, performance test pass | QA + PM | KHÔNG bắt đầu UAT |
| **Release Gate** | UAT sign-off, 0 critical bugs, docs complete | PM + Khách hàng | KHÔNG deploy production |

**Nguyên tắc:** Gate KHÔNG ĐƯỢC bypass. Nếu fail, fix rồi mới qua gate.

### 2.5. Review Process

**3 loại review:**

| Review | Ai review | Khi nào | Tiêu chí |
|--------|-----------|---------|----------|
| **Design review** | TL + Senior dev | Sau khi thiết kế xong | Logic đúng, NFR addressed, consistency |
| **Code review** | Peer dev + TL | Trước khi merge | Coding standard, no security issue, test coverage |
| **Test case review** | QA lead + Dev | Trước khi test | Coverage đầy đủ, edge case, acceptance criteria |

**Theo dõi 指摘件数 (chi-teki kensuu):**
```
Sprint 1: 45 指摘 (design review) — nhiều vì mới bắt đầu
Sprint 2: 38 指摘 — giảm nhẹ
Sprint 3: 25 指摘 — team hiểu quy trình
Sprint 4: 12 指摘 — CẢNH BÁO: giảm quá nhanh

Phân tích: 指摘 giảm CÓ THỂ là:
  TỐT: Team viết code tốt hơn, ít lỗi hơn
  XẤU: Reviewer không kỹ, skip review vì timeline pressure

Kiểm tra: Bug density ở phase sau có tăng không?
  Nếu tăng -> Review KHÔNG KỸ (bad sign)
  Nếu giảm -> Chất lượng thực sự cải thiện (good sign)
```

---

## 3. Chiến lược & Dẫn dắt (L3)

### 3.1. Quality Strategy Design

**Thiết kế quality strategy phù hợp khách hàng Nhật:**

```
Quality Strategy: "Prevention over Remediation"

Mục tiêu:
  1. Phát hiện > 80% lỗi TRƯỚC system test
  2. Bug density <= 0.5/KLoC tại system test
  3. 0 critical bug tại UAT
  4. Khách hàng rate quality >= 4/5

Chiến lược:
  Phase 1 (Design): Review kỹ, prototype mơ hồ, confirm với BrSE
  Phase 2 (Code): 100% code review, pair programming cho module phức tạp
  Phase 3 (Test): Unit 80%+, integration test cho mỗi API
  Phase 4 (Release): Regression full, performance test, security scan
```

### 3.2. 説明できる品質 — Giải thích chất lượng cho khách hàng Nhật

**Quality Report template cho khách hàng:**

```
== QUALITY REPORT — Sprint 6 ==

1. TỔNG QUAN
   Trạng thái: XANH (tất cả chỉ số trong ngưỡng)

2. CHỈ SỐ CHÍNH
   | Chỉ số              | Target    | Thực tế    | Trạng thái |
   |---------------------|-----------|------------|------------|
   | Bug density         | <= 0.5    | 0.3        | XANH       |
   | Code review         | 100%      | 100%       | XANH       |
   | Unit test coverage  | >= 80%    | 85%        | XANH       |
   | Critical bugs open  | 0         | 0          | XANH       |
   | Velocity            | 30 SP     | 28 SP      | VÀNG       |

3. XU HƯỚNG BUG
   Sprint 1: 12 bugs | Sprint 2: 15 | Sprint 3: 10 | Sprint 4: 8 | Sprint 5: 6 | Sprint 6: 5
   -> Xu hướng GIẢM -> Chất lượng CẢI THIỆN

4. PHÂN TÍCH
   - Velocity hơi thấp do 2 PG mới ramp-up, dự kiến ổn định từ sprint 7
   - Bug density giảm nhờ code review strict và unit test tăng từ 60% -> 85%

5. HÀNH ĐỘNG
   - Pair programming cho 2 PG mới (tương đương senior mentor 2h/ngày)
   - Dự kiến velocity đạt 30 SP từ sprint 8
```

### 3.3. Defect Trend Analysis

**Phân tích xu hướng defect để dự đoán chất lượng:**

```
Bug Found per Sprint:
  Sprint 1: 12 | Sprint 2: 15 | Sprint 3: 10 | Sprint 4: 8 | Sprint 5: 6

Bug Fixed per Sprint:
  Sprint 1: 10 | Sprint 2: 14 | Sprint 3: 11 | Sprint 4: 9 | Sprint 5: 7

Open Bug Trend:
  Sprint 1: +2 | Sprint 2: +3 | Sprint 3: +2 | Sprint 4: +1 | Sprint 5: 0

Nhận định:
  - Found trend GIẢM -> Chất lượng code tốt dần
  - Fixed >= Found từ Sprint 3 -> Team kiểm soát được bug
  - Open bug GIẢM VỀ 0 -> Sẵn sàng cho release

CẢNH BÁO nếu:
  - Found đột ngột TĂNG ở sprint cuối -> Tìm được nhiều bug nghĩa là còn nhiều bug ẩn
  - Open trend TĂNG -> Team không fix kịp, cần thêm nguồn lực
```

### 3.4. Prevention over Remediation Culture

**Xây dựng văn hóa phòng ngừa:**

| Giai đoạn | Phòng ngừa (Làm trước) | Xử lý (Làm sau) |
|-----------|----------------------|-----------------|
| **Design** | Prototype, review, confirm | Làm lại thiết kế |
| **Code** | Code review, pair programming | Debug, fix bug |
| **Test** | Test case review, automation | Manual re-test |
| **Release** | Regression, performance test | Hotfix, rollback |

**Chi phí fix bug theo giai đoạn:**
```
Design:     1x (fix requirement/design)
Code:       5x (fix code + unit test)
System Test: 10x (fix code + re-test + regression)
UAT:        20x (fix + re-test + re-UAT + khách hàng mất tin tưởng)
Production: 100x (hotfix + rollback + damage control + uy tín)

-> Mỗi lỗi phát hiện SỚM tiết kiệm 10-100 lần chi phí
```

---

## 4. Quản lý cấp tổ chức (L4)

### 4.1. Quality Dashboard Design

**Dashboard tự động cho toàn tổ chức:**

```
+------------------------------------------------------+
|  ORGANIZATION QUALITY DASHBOARD                       |
|------------------------------------------------------|
|  Project A: XANH  | Bug: 0.3/KLoC | Test: 87%       |
|  Project B: VÀNG  | Bug: 0.8/KLoC | Test: 72%       |
|  Project C: XANH  | Bug: 0.2/KLoC | Test: 91%       |
|  Project D: ĐỎ    | Bug: 1.5/KLoC | Test: 55%       |
|------------------------------------------------------|
|  Org Average:  Bug density: 0.7/KLoC                 |
|  Org Target:   Bug density: <= 0.5/KLoC              |
|  Trend:        Improving (giảm từ 0.9 -> 0.7)        |
+------------------------------------------------------+
```

### 4.2. Organizational Quality Baseline

**Xây dựng baseline từ dữ liệu nhiều dự án:**

| Metric | Baseline (trung bình) | Target (tốt) | Best Practice |
|--------|----------------------|-------------|---------------|
| Bug density (ST) | 0.7 bugs/KLoC | <= 0.5 | <= 0.3 |
| Code review coverage | 85% | 100% | 100% + pair review |
| Unit test coverage | 65% | >= 80% | >= 90% |
| Design review 指摘 | 10/session | 5-15/session | Consistent |
| Defect fix rate | 90% | >= 95% | >= 98% |
| UAT bug rate | 5% of total | <= 3% | <= 1% |

**Sử dụng baseline để:**
- So sánh dự án mới với baseline tổ chức
- Phát hiện dự án "bất thường" sớm (outlier detection)
- Thiết lập quality target cho dự án mới dựa trên lịch sử
- Báo cáo cho management về xu hướng chất lượng toàn tổ chức

### 4.3. Cross-project Quality Benchmarking

**So sánh giữa các dự án:**

| Dự án | Size | Bug Density | Test Coverage | Customer Sat | Note |
|-------|------|-------------|---------------|-------------|------|
| Prj A | 200 MD | 0.3 | 87% | 4.5/5 | Best in class |
| Prj B | 150 MD | 0.8 | 72% | 3.8/5 | Below baseline |
| Prj C | 300 MD | 0.2 | 91% | 4.7/5 | Excellent |
| Prj D | 100 MD | 1.5 | 55% | 3.2/5 | Need intervention |

**Phân tích: Tại sao Prj D kém?**
- Team mới, thiếu kinh nghiệm (RR)
- Skip code review do timeline pressure (process issue)
- Action: Assign mentor từ Prj A, enforce quality gate

---

## 5. Tự kiểm tra

### Bài tập: Xây dựng Quality Plan với 10 KPIs + RAG thresholds

**Bối cảnh:**
```
Dự án: Hệ thống quản lý vận hành (Boiler Operations)
8 modules, 12 sprints, 12 người
Quality target: Bug density <= 0.5/KLoC, khách hàng Nhật
```

**Yêu cầu:**
1. Định nghĩa 10 KPIs với target cụ thể
2. Thiết lập RAG threshold (Xanh/Vàng/Đỏ) cho từng KPI
3. Xác định Quality Gate tại 4 milestone (Design/Code/ST/Release)
4. Viết DoD 3 cấp (Story/Sprint/Release)
5. Thiết kế review process: ai review gì, khi nào, tiêu chí pass/fail
6. Viết Quality Report mẫu cho 1 sprint (format cho khách hàng Nhật)

**KPI Template:**

| # | KPI | Target | Xanh | Vàng | Đỏ | Tần suất | Công thức |
|---|-----|--------|------|------|-----|----------|-----------|
| 1 | Bug density (ST) | <= 0.5/KLoC | <= 0.5 | 0.5-1.0 | > 1.0 | Sprint | bugs/KLOC |
| 2 | Code review coverage | 100% | 100% | 90-99% | < 90% | Sprint | % files reviewed |
| 3 | Unit test coverage | >= 80% | >= 80% | 60-79% | < 60% | Sprint | % lines covered |
| 4 | ... | ... | ... | ... | ... | ... | ... |

**Tiêu chí đánh giá:**

| Level | Yêu cầu |
|-------|---------|
| L1 | Theo dõi bug count, hiểu DoD cơ bản, dùng review checklist |
| L2 | Quality Plan với GQM, 10 KPIs, DoD 3 cấp, quality gates, review process |
| L3 | Quality strategy design, 説明できる品質 report, defect trend analysis, prevention culture |
| L4 | Quality dashboard design, organizational baseline, cross-project benchmarking |

### Câu hỏi tự kiểm tra

1. **Bug density 1.0/KLoC ở sprint 5, target 0.5. Bạn làm gì?**
   - Root cause analysis: Tại sao bug nhiều? (code review skip? PG mới? Module phức tạp?)
   - Action plan: Enforce 100% review, pair programming, thêm QA resource
   - Báo khách hàng: Trình bày root cause + action + timeline đạt target
   - KHÔNG nói "sẽ cải thiện" mà nói "Làm A, B, C, dự kiến đạt target sprint 8"

2. **指摘件数 giảm 50% so với sprint đầu — tốt hay xấu?**
   - Kiểm tra bug density ở phase sau
   - Nếu bug density TĂNG -> Review không kỹ (BAD)
   - Nếu bug density GIẢM -> Chất lượng thực sự tốt lên (GOOD)

3. **Khách hàng Nhật hỏi: "Tại sao chất lượng tốt?" — bạn trả lời thế nào?**
   - Trình bày Quality Report với số liệu cụ thể
   - "Bug density 0.3/KLoC, thấp hơn target 0.5 và thấp hơn industry average 0.7"
   - "Code review coverage 100%, unit test 85%"
   - "Xu hướng bug GIẢM từ sprint 1 đến sprint 6"
   - "0 critical bugs còn open"

---

## 6. Tài liệu tham khảo

**Source gốc:**
- PM Competency #4: `khung-danh-gia-nang-luc-main/roles/pm/nang-luc.md`
- PM Levels (Quality section): `khung-danh-gia-nang-luc-main/roles/pm/levels.md`
- Planning Test (quality section): `khung-danh-gia-nang-luc-main/roles/pm/tests/planning.md`

**CMMI Documents:**
- PRC-PJM-PMC-01: Project Monitoring & Control Process (6 bước)
- GLN-PJM-PMC-01: Project Monitoring Guide (EVM, RAG, dashboard, quality tracking)
- RUL-PJM-PMC-01: Status Reporting Rule (ngưỡng sai lệch, công thức)
- RUL-PMG-MA-01: Metric Threshold Rule (Moving Average, auto-escalation)

**Nguyên tắc then chốt với khách hàng Nhật:**
- 説明できる品質 = Chất lượng giải thích được bằng SỐ LIỆU
- Prevention > Remediation — phát hiện lỗi sớm tiết kiệm 10-100x chi phí
- Quality gate KHÔNG ĐƯỢC bypass — fail thì fix rồi mới qua
- Báo cáo chất lượng PHẢI có: số liệu + xu hướng + phân tích + hành động
- "Nắm vững tình trạng bằng số liệu" (数字で品質を語る) — dùng data, không dùng cảm tính
