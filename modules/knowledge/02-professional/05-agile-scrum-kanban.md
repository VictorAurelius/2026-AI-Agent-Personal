# Agile / Scrum / Kanban Practices

> **Mục tiêu:** Nắm vững framework Agile/Scrum/Kanban để áp dụng vào dự án outsource Nhật Bản (Hybrid Waterfall + Agile)
> **Level:** L1 -> L2 -> L3
> **Thời gian đọc:** ~25 phút
> **Liên quan:** PM Competency #6 (Agile/Scrum/Kanban実践力) / CMMI PA: PP, PMC, IPM

---

## 1. Khái niệm cơ bản (L1)

### 1.1 Agile Manifesto — 4 giá trị cốt lõi

| Giá trị | Ý nghĩa thực tế |
|---------|----------------|
| Individuals & interactions > processes & tools | Giao tiếp trực tiếp với team, không chỉ dựa vào tool |
| Working software > comprehensive documentation | Demo sản phẩm chạy được, không chỉ tạo tài liệu |
| Customer collaboration > contract negotiation | Hợp tác chặt với khách hàng Nhật qua BrSE |
| Responding to change > following a plan | Linh hoạt khi khách thay đổi yêu cầu giữa chừng |

### 1.2 Scrum Framework — 3-4-3

**3 Roles:**

```
+------------------+     +------------------+     +------------------+
|   Product Owner  |     |   Scrum Master   |     |  Development     |
|                  |     |                  |     |  Team            |
| - Quản lý       |     | - Facilitate     |     | - Cross-         |
|   Product        |     |   ceremonies     |     |   functional     |
|   Backlog        |     | - Remove         |     | - Tự tổ chức    |
| - Ưu tiên hóa   |     |   blockers       |     | - 3-9 người     |
|   business value |     | - Coach team     |     |                  |
+------------------+     +------------------+     +------------------+
```

**4 Ceremonies:**

| Ceremony | Mục đích | Thời gian (Sprint 2 tuần) |
|----------|---------|--------------------------|
| Sprint Planning | Chọn công việc cho Sprint | 2-4 giờ |
| Daily Standup | Đồng bộ hàng ngày: Đã làm / Sẽ làm / Blocker | 15 phút |
| Sprint Review | Demo sản phẩm cho PO và stakeholders | 1-2 giờ |
| Sprint Retrospective | Nhìn lại quy trình: tốt / cần cải thiện | 1-1.5 giờ |

**3 Artifacts:**

| Artifact | Người sở hữu | Mô tả |
|----------|-------------|-------|
| Product Backlog | Product Owner | Danh sách tất cả yêu cầu, ưu tiên theo business value |
| Sprint Backlog | Development Team | Các item được chọn cho Sprint hiện tại + kế hoạch |
| Increment (+ Burn-down) | Team | Sản phẩm "Done" có thể release + biểu đồ tiến độ |

### 1.3 Vai trò PM trong Scrum tại công ty outsource Nhật

Trong mô hình outsource Nhật Bản, PM thường kiêm nhiệm vai trò Scrum Master:
- Tham dự đầy đủ các ceremonies
- Cập nhật task board (Redmine/Jira) hàng ngày
- Báo cáo tiến độ cho khách hàng Nhật theo 報連相 (Hou-Ren-Sou)
- Đảm bảo team hiểu DOD (Definition of Done) tại mọi cấp

---

## 2. Thực hành nâng cao (L2)

### 2.1 Sprint 0 — Khởi động dự án

Sprint 0 là sprint đặc biệt trước khi bắt đầu phát triển. Checklist:

```
Sprint 0 Checklist (2-4 tuần)
================================
[ ] Business Case        — Hiểu rõ bài toán kinh doanh, QCD target
[ ] Environment Setup    — Dev/Staging/Prod, CI/CD pipeline
[ ] Architecture         — HLD, technology stack, integration points
[ ] Team Setup           — Assign members, xác định skill gaps
[ ] Team Norms           — Working agreement, DOD, coding standards
[ ] Training             — Onboard tool (Redmine/Git), quy trình CMMI
[ ] Release Planning     — Roadmap, milestones, baseline schedule
```

**Sprint 0 Output:**

```
+-----------------+     +------------------+     +------------------+
| Release Plan    |---->| Initial Product  |---->| Sprint 1 Ready   |
| (Roadmap)       |     | Backlog          |     | (Env + Team +    |
|                 |     | (Prioritized)    |     |  Architecture)   |
+-----------------+     +------------------+     +------------------+
```

### 2.2 Facilitate All Scrum Events

**Sprint Planning (2 parts):**

| Part | Câu hỏi | Người dẫn | Output |
|------|---------|----------|--------|
| WHAT | Làm gì trong Sprint này? | PO trình bày items | Sprint Goal + Selected items |
| HOW | Làm như thế nào? | Team phân ra tasks | Task breakdown + estimates |

**Daily Standup — 3 câu hỏi:**

```
Mỗi thành viên trả lời (< 2 phút):
  1. Hôm qua tôi đã làm gì?
  2. Hôm nay tôi sẽ làm gì?
  3. Có blocker nào không?

=> PM ghi nhận blocker, xử lý NGAY SAU standup (không giải quyết trong standup)
```

**Sprint Retrospective — Format:**

```
+-----------------------------------+-----------------------------------+
|      WHAT WENT WELL               |     WHAT COULD BE IMPROVED        |
|  (Giữ lại, phát huy)              |  (Cần cải thiện Sprint sau)       |
+-----------------------------------+-----------------------------------+
|  - CI/CD pipeline ổn định         |  - Daily report gửi trễ           |
|  - Code review kỹ lưỡng           |  - Unit test coverage thấp        |
|  - Giao tiếp với BrSE tốt         |  - Sprint goal không rõ ràng      |
+-----------------------------------+-----------------------------------+
                    |
                    v
+-----------------------------------+
|        ACTION ITEMS               |
| (Cụ thể, có owner, có deadline)   |
+-----------------------------------+
| 1. [Tuân] Setup code coverage     |
|    report trong CI — deadline T4  |
| 2. [PM] Viết Sprint Goal rõ hơn   |
|    vào Sprint Planning — ongoing  |
+-----------------------------------+
```

### 2.3 Velocity Tracking & Burn-down Chart

**Velocity** = Tổng Story Points hoàn thành trong 1 Sprint

```
Velocity Chart (6 Sprints)
SP |
40 |
35 |          *
30 |    *           *     *
25 | *                          *
20 |
   +---+----+----+----+----+----+
     S1   S2   S3   S4   S5   S6

Avg Velocity = (25+30+35+30+30+25) / 6 = 29.2 SP/Sprint
=> Dự báo: Còn 120 SP => 120/29.2 ~ 4.1 Sprints
```

**Burn-down Chart:**

```
SP |
60 | *
50 |   *  Ideal line
40 |     *  .
30 |       * .  * Actual line (trễ 2 ngày)
20 |         . *
10 |        .    *
 0 |       .       *
   +---+---+---+---+---+---+
   D1  D2  D3  D4  D5  D6...D10
```

### 2.4 Capacity Calculation

**Công thức tính capacity Sprint (2 tuần = 10 ngày làm việc):**

```
Capacity = (Số người x Ngày làm việc) - Nghỉ phép - Buffer(20%)

Ví dụ: Team 5 người, Sprint 2 tuần
  Tổng man-days = 5 x 10 = 50 MD
  Nghỉ phép     = 2 MD (1 người nghỉ 2 ngày)
  Buffer 20%    = (50 - 2) x 0.2 = 9.6 MD
  ------------------------------------------
  Available     = 50 - 2 - 9.6 = 38.4 MD

=> Chọn công việc ~ 38 MD cho Sprint
```

**Buffer 20% bao gồm:** meeting, support, bug từ Sprint trước, unplanned work.

### 2.5 Kanban — Hệ thống Pull

**Kanban Board:**

```
| TO DO (WIP:8) | IN PROGRESS (WIP:3) | REVIEW (WIP:2) | DONE     |
|---------------|---------------------|-----------------|----------|
| [Task-7]      | [Task-4] @Tuan      | [Task-2] @Linh  | [Task-1] |
| [Task-8]      | [Task-5] @Minh      | [Task-3] @Hoa   |          |
| [Task-9]      | [Task-6] @Nam       |                 |          |
| [Task-10]     |                     |                 |          |
```

**Nguyên tắc Kanban:**

| Nguyên tắc | Mô tả | Ví dụ |
|-----------|-------|-------|
| Pull system | Chỉ kéo việc mới khi có capacity | Không push task vào column đã đầy |
| WIP limit | Giới hạn công việc đang làm | IN PROGRESS max 3 items |
| Flow optimization | Tối ưu hóa lead time | Giảm thời gian chờ review |
| Visual management | Mọi người thấy trạng thái | Board cập nhật real-time |
| Continuous delivery | Không có Sprint cố định | Release khi sẵn sàng |

**Metrics Kanban:**

| Metric | Công thức | Mục tiêu |
|--------|----------|---------|
| Lead Time | Ngày tạo item -> Ngày Done | Giảm dần qua mỗi tuần |
| Cycle Time | Ngày bắt đầu làm -> Ngày Done | < Lead Time |
| Throughput | Số item Done / Tuần | Ổn định hoặc tăng |
| WIP compliance | Số lần vi phạm WIP limit | 0 vi phạm |

### 2.6 Release Planning — 6 bước

```
B1: Hiểu mục tiêu Release (Business goal)
    |
B2: Hiểu danh sách yêu cầu (Product Backlog items)
    |
B3: Ưu tiên & Ước lượng Backlog (MoSCoW + Story Points)
    |
B4: Tính Velocity dự kiến (Avg 3-4 Sprint gần nhất)
    |
B5: Tạo Release Plan (Map items vào Sprints)
    |
B6: Truyền đạt & Cập nhật thường xuyên

Release Plan:
+--------+--------+--------+--------+--------+--------+
|Sprint 0|Sprint 1|Sprint 2|Sprint 3|Sprint 4|Sprint 5|
| Setup  | Login  | Search | Cart   | Payment| UAT    |
|        | Signup | Filter | Order  | Report | Fix    |
+--------+--------+--------+--------+--------+--------+
                    Release 1.0             Release 1.1
```

### 2.7 Definition of Done (DOD) — 3 cấp

| Cấp | Tiêu chí | Ví dụ cụ thể |
|-----|---------|-------------|
| Story-level | Code + Unit Test + Review + PO Accept | Code push, UT >= 80%, CR approved, PO demo OK |
| Sprint-level | All stories accepted + Demo + No critical bugs | Sprint Review done, 0 L1 bugs open |
| Release-level | Deploy + Docs + Training + No L1 bugs | Production deploy, user guide updated, training done |

---

## 3. Chiến lược & Dẫn dắt (L3)

### 3.1 Hybrid Waterfall + Agile — Mô hình outsource Nhật Bản

Đây là mô hình mặc định cho dự án outsource Nhật Bản (theo khung năng lực PM):

```
Phase 1: WATERFALL (Fixed scope, Fixed deliverables)
+------------+----------+
| Req Gather | Design   |    <- Khách hàng Nhật ký duyệt deliverables
| (SRS)      | (HLD/LLD)|    <- 報連相 formal, tài liệu song ngữ JP/VN
+------------+----------+

Phase 2: AGILE/SCRUM (Fixed time/team, Flexible scope)
+--------+--------+--------+--------+
|Sprint 1|Sprint 2|Sprint 3|Sprint 4|    <- 2-week sprints
| Coding | Coding | Coding | Fix    |    <- Demo mỗi Sprint
| UT     | UT     | IT     | ST     |    <- Velocity tracking
+--------+--------+--------+--------+

Phase 3: WATERFALL (Controlled release)
+--------+--------+
| UAT    | Release|    <- Khách hàng kiểm thử
| Bug fix| Deploy |    <- Handover tài liệu 納品物
+--------+--------+
```

**Tại sao Hybrid?**
- Khách hàng Nhật cần deliverables rõ ràng ở phase đầu và cuối (văn hóa 説明できる品質)
- Team offshore cần linh hoạt trong coding phase
- QCD balance: Waterfall = fixed scope, Scrum = fixed time/team

### 3.2 SAFe / LeSS — Nhận biết khi nào cần

| Framework | Khi nào dùng | Đặc điểm |
|-----------|-------------|---------|
| Scrum | 1 team (3-9 người) | Đơn giản, đủ cho hầu hết dự án |
| LeSS | 2-8 teams cùng 1 sản phẩm | 1 Product Backlog, nhiều teams |
| SAFe | > 50 người, nhiều streams | ART (Agile Release Train), PI Planning |

### 3.3 Continuous Improvement — Muda / Muri / Mura

Từ Lean Manufacturing (Toyota), áp dụng vào phát triển phần mềm:

| Loại lãng phí | Định nghĩa | Ví dụ trong phát triển PM |
|---------------|-----------|--------------------------|
| **Muda** (無駄) — Lãng phí | Hoạt động không tạo giá trị | Meeting không có agenda, tài liệu không ai đọc |
| **Muri** (無理) — Quá tải | Yêu cầu vượt capacity | Sprint planning nhồi 120% capacity |
| **Mura** (斑) — Bất đều | Không nhất quán, biến động | Sprint 1: 40SP, Sprint 2: 15SP, Sprint 3: 45SP |

**Cách phát hiện và xử lý:**

```
Muda: Giá trị nhỏ -> Loại bỏ hoặc giảm
  Ví dụ: Báo cáo hàng ngày 2 trang -> Rút gọn còn 5 dòng
         Meeting 1 giờ -> Timebox 30 phút

Muri: Vượt tải -> Cân bằng lại
  Ví dụ: Sprint velocity 40SP nhưng plan 55SP -> Giảm còn 38SP
         1 người on-call + dev -> Tách role

Mura: Biến động -> Ổn định hóa
  Ví dụ: Velocity dao động 15-45 -> Tìm nguyên nhân, target 25-35
         Task size khác nhau lớn -> Story splitting đều hơn
```

### 3.4 Sprint 0 giữa các Release

Giữa Release 1 và Release 2, tổ chức Sprint 0 để:

```
Inter-Release Sprint 0 (1-2 tuần)
===================================
[ ] Architecture Review   — Refactoring technical debt
[ ] Retrospective tổng hợp — Review toàn bộ Release 1
[ ] Team rotation/training — Xoay vai, đào tạo kỹ năng mới
[ ] QA Audit              — PPQA audit cho Release 1
[ ] Process improvement   — Áp dụng bài học từ Retro
[ ] Release Planning 2    — Cập nhật roadmap cho Release 2
```

### 3.5 Tối ưu quy trình Sprint

**Phát hiện vấn đề qua metrics:**

| Metric | Vấn đề | Hành động |
|--------|--------|----------|
| Velocity giảm 3 Sprint liên | Team gặp khó khăn | Root cause analysis, hỗ trợ team |
| Sprint Goal < 70% | Scope không rõ | Cải thiện Sprint Planning, DOD |
| Defect Escape Rate tăng | Chất lượng giảm | Tăng code review, tăng UT coverage |
| Lead Time tăng | Bottleneck trong flow | Kiểm tra WIP, tối ưu Review step |

---

## 4. Tự kiểm tra

### Bài tập 1: Sprint 0 + Release Plan (L2)

**Tình huống:** Bạn nhận dự án mới từ khách hàng Nhật. Dự án phát triển module quản lý đơn hàng, 6 tháng, team 7 người (1 PM, 1 BrSE, 3 Dev, 1 QA, 1 Designer). Mô hình Hybrid Waterfall+Agile.

**Yêu cầu:**
1. Lập Sprint 0 checklist cụ thể (ai làm gì, bao lâu)
2. Tính capacity cho Sprint 1 (biết 1 dev nghỉ 3 ngày, 2-week sprint)
3. Với velocity dự kiến 25 SP/Sprint, lập Release Plan cho 120 SP backlog
4. Xác định DOD 3 cấp cho dự án này

### Bài tập 2: Xử lý vấn đề Sprint (L2-L3)

**Tình huống:** Sprint 4, velocity giảm từ 30 xuống 18 SP. Defect Escape Rate tăng từ 3% lên 12%. Khách hàng Nhật bắt đầu lo lắng.

**Yêu cầu:**
1. Phân tích nguyên nhân sử dụng 5-Whys
2. Đề xuất hành động khắc phục (ngắn hạn + dài hạn)
3. Thiết kế Retrospective cho Sprint này (format, câu hỏi, action items)
4. Chuẩn bị báo cáo cho khách hàng (報告 format)

### Bài tập 3: Thiết kế quy trình Hybrid cho dự án mới (L3)

**Tình huống:** Dự án mới, Size L (>500 MD), 15 người, 12 tháng. Khách hàng yêu cầu Waterfall cho Requirement/Design nhưng muốn linh hoạt trong Implementation.

**Yêu cầu:**
1. Thiết kế mô hình Hybrid (phase nào Waterfall, phase nào Agile, phase nào Kanban)
2. Xác định metrics cho từng phase
3. Lập kế hoạch Continuous Improvement (Retrospective frequency, KPI targets)
4. Đề xuất cách balance giữa yêu cầu 説明できる品質 của khách và tính linh hoạt của Agile

---

## 5. Tài liệu tham khảo

### Từ kho CMMI PAL
- **PRC-PJM-PP-01** — Project Planning Process (Sprint Planning, Release Planning)
- **PRC-PJM-PMC-01** — Project Monitoring & Control (Velocity, Burn-down)
- **GLN-PMG-OPD-01** — Tailoring Guidelines (Hybrid/Agile/Waterfall selection)
- **GLN-PMG-MA-01** — Metrics Selection Guide (GQM, Agile metrics)
- **RUL-PMG-MA-01** — Metric Threshold Rule (RAG status, Moving Average)

### Từ khung năng lực PM
- **Competency #6** — Agile/Scrum/Kanban実践力 (10% trọng số)
- **SYP02** — SDLC & Agile/Scrum Training
- **SYP03 Phần 5+6** — Kanban, DOD, Velocity

### Sách & Tài liệu ngoài
- Scrum Guide 2020, SAFe 6.0, Kanban (Anderson 2010), Toyota Production System (Ohno 1988)
