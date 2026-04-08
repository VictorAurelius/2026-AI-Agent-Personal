# Project Planning & Estimation (Lập kế hoạch & Ước lượng)

> **Mục tiêu:** Nắm vững quy trình lập kế hoạch dự án và kỹ thuật ước lượng trong dự án outsource Nhật Bản
> **Level:** L1 -> L2 -> L3 -> L4
> **Thời gian đọc:** ~25 phút
> **Liên quan:** PM Competency #1 (計画・見積力), CMMI PA: PP (Project Planning)

---

## 1. Khái niệm cơ bản (L1)

### 1.1. WBS là gì?

**Work Breakdown Structure (WBS)** = Cấu trúc phân ra công việc thành các task nhỏ để quản lý.

**3 quy tắc bắt buộc (RUL-PJM-PP-01):**
- **Quy tắc 100%:** Tổng task con = 100% công việc của task cha, không thừa không thiếu
- **Kích thước gói công việc:** Mỗi task nhỏ nhất từ 4h đến 40h. Lớn hơn 40h phải phân ra tiếp
- **Độ sâu tối thiểu:** 3 cấp (Phase -> Module -> Task)

**Cấu trúc 4 cấp khuyến nghị cho dự án Nhật:**
```
Cấp 1: Phase (Giai đoạn) — VD: 要件定義, 基本設計, 開発, テスト
  Cấp 2: Module/Feature — VD: User Management, Reporting
    Cấp 3: Sub-feature — VD: Login screen, Password reset
      Cấp 4: Task cụ thể — VD: Backend API development (8h)
```

### 1.2. Gantt Chart & theo dõi tiến độ

**Gantt chart** hiển thị tiến độ trực quan theo thời gian:
```
Task                Week 1  Week 2  Week 3  Week 4  Week 5
Requirements        ████████
Design                      ████████████████
Development                         ████████████████████████
Testing                                      ████████████████
Deployment                                           ████
```

**Hành vi L1:**
- Cập nhật Gantt chart hàng tuần
- Báo delay khi phát hiện
- Theo dõi man-hour thực tế vs kế hoạch
- Hiểu scope module được giao

### 1.3. Tam giác QCD (Quality - Cost - Delivery)

| Framework | Scope | Time | Cost | Quality |
|-----------|-------|------|------|---------|
| **Waterfall** | Fixed scope | Balance khi thực hiện | Balance | Phụ thuộc scope |
| **Scrum** | Flexible (backlog) | Fixed (sprint) | Fixed (team) | Velocity tuning |
| **Kanban** | Optimize flow | WIP limit | Optimize | Continuous |

---

## 2. Thực hành nâng cao (L2)

### 2.1. Tạo WBS hoàn chỉnh

**Với mỗi feature, luôn bao gồm các task sau:**
```
Feature X
+-- Phân tích & Thiết kế
|   +-- Phân tích requirements chi tiết
|   +-- Thiết kế database
|   +-- Thiết kế API
|   +-- Review thiết kế với TL
+-- Phát triển (Development)
|   +-- Backend development
|   +-- Frontend development
|   +-- API integration
|   +-- Unit test
+-- Kiểm thử (Testing)
|   +-- Viết test case
|   +-- Thực hiện test
|   +-- Sửa bug
+-- Các hoạt động khác (THƯỜNG BỊ QUÊN — chiếm 15-25% effort)
    +-- Code review
    +-- Documentation
    +-- Deployment support
```

### 2.2. Kỹ thuật ước lượng

**5 kỹ thuật được phép sử dụng (RUL-PJM-PP-01):**

| Kỹ thuật | Cốt lõi | Phù hợp khi | Độ chính xác |
|----------|---------|-------------|--------------|
| **WBS Bottom-Up** | Phân ra -> estimate từng task -> cộng tổng | Dự án Size M/L, sau khi có SRS | +/- 10-15% |
| **PERT (3-point)** | Best/Most/Worst -> trung bình có trọng số | Task rủi ro cao, công nghệ mới | +/- 15-20% |
| **Planning Poker** | Team đồng thuận qua bỏ phiếu độc lập | Dự án Agile, Sprint Planning | +/- 15-20% |
| **T-shirt Sizing** | Phân loại nhanh S/M/L/XL | Proposal, Roadmap sơ bộ | +/- 50% |
| **Expert Judgment** | Dựa trên kinh nghiệm + dữ liệu lịch sử | Dự án Size S, CR nhỏ | +/- 25-30% |

### 2.3. Công thức PERT chi tiết

```
E = (O + 4M + P) / 6

Trong đó:
  O = Optimistic (Lạc quan) — mọi thứ suôn sẻ
  M = Most Likely (Khả thi nhất) — bình thường, có vài vấn đề nhỏ
  P = Pessimistic (Bi quan) — gặp nhiều khó khăn

Độ lệch chuẩn: SD = (P - O) / 6
Khoảng tin cậy 95%: E +/- 2 x SD
```

**Ví dụ: Estimation tích hợp Payment Gateway**

| Task | O (ngày) | M (ngày) | P (ngày) | PERT | SD |
|------|----------|----------|----------|------|-----|
| Nghiên cứu API | 1 | 2 | 5 | 2.3 | 0.67 |
| Thiết kế integration | 1 | 2 | 3 | 2.0 | 0.33 |
| Phát triển backend | 3 | 5 | 10 | 5.5 | 1.17 |
| Phát triển frontend | 2 | 3 | 5 | 3.2 | 0.50 |
| Test integration | 2 | 3 | 7 | 3.5 | 0.83 |
| Sửa bug & hoàn thiện | 1 | 2 | 5 | 2.3 | 0.67 |
| **Tổng** | **10** | **17** | **35** | **18.8** | — |

**Trình bày cho khách hàng:** "Chúng tôi estimate 19 man-day, trường hợp xấu nhất không quá 23 man-day"

### 2.4. Planning Poker — Quy trình từng vòng

```
Bước 1: SM/PM đọc mô tả user story
         |
Bước 2: Team thảo luận (3-5 phút) — KHÔNG đưa ra con số
         |
Bước 3: Mọi người ĐỒNG THỜI lật thẻ Fibonacci (1,2,3,5,8,13,21)
         |
Bước 4: Kiểm tra kết quả
         - Chênh lệch <= 2 bậc (VD: 5 và 8) -> Lấy giá trị cao hơn
         - Chênh lệch > 2 bậc (VD: 3 và 13) -> Thảo luận thêm
         |
Bước 5: Người có số CAO NHẤT và THẤP NHẤT giải thích lý do
         |
Bước 6: Lật thẻ lại (vòng 2) — thường đạt consensus sau 2-3 vòng
```

### 2.5. Velocity-based Scheduling & Sprint 0

**Tính toán capacity cho 1 sprint (2 tuần):**
```
Capacity = Số người x Số ngày làm việc x Hệ số hiệu dụng
         = 5 PG x 10 ngày x 0.8 (trừ meeting, review, unexpected)
         = 40 man-day / sprint

Velocity (sau 3 sprint): Trung bình Story Point hoàn thành = 30 SP/sprint
```

**Sprint 0 — Sprint khởi động:**
- Business case review
- Environment setup (dev, staging, CI/CD)
- Architecture decision
- Team norms & Definition of Done
- Training (công nghệ mới, quy trình khách hàng)
- Initial Release Planning

### 2.6. Quy trình lập kế hoạch 7 bước (PRC-PJM-PP-02)

| Bước | Hoạt động | Người thực hiện | Effort |
|------|-----------|-----------------|--------|
| 1 | Xác định scope chi tiết (WBS) | PM + BA | 4-8h |
| 2 | Ước lượng effort và duration | TL + Team | 4-8h |
| 3 | Lập schedule và milestones | PM | 2-4h |
| 4 | Phân bổ nguồn lực | PM | 1-2h |
| 5 | Lập subordinate plans (Risk, Test, Communication) | PM + TL + QA | 4-8h |
| 6 | Tổng hợp Project Plan | PM | 2h |
| 7 | AI Quality Check, Review & Baseline | PM + Management | 2-4h |

**Bắt buộc có buffer:**
- Development buffer: 10-15%
- Management reserve: 5-10%
- Risk-based adjustment: theo mức độ rủi ro

**Điều kiện lập lại kế hoạch (RUL-PJM-PP-01):**
- Change request tăng effort > 10%
- Sai lệch thực tế vs kế hoạch > 15% liên tục 2 tuần

---

## 3. Chiến lược & Dẫn dắt (L3)

### 3.1. Multi-module WBS

**Dự án 8 modules, 12 sprint (test Planning):**

| Sprint | Module chính | Lý do ưu tiên |
|--------|-------------|---------------|
| S1-S2 | Authentication + User Management | Foundation, mọi module phụ thuộc |
| S3-S4 | Fuel Management + System Settings | Core data, ít dependency |
| S5-S7 | Optimization Calculation | Phức tạp nhất, cần nhiều thời gian |
| S6-S8 | Boiler Monitoring | Phức tạp, parallel với Optimization |
| S9-S10 | Alert Management + Reporting | Phụ thuộc Monitoring data |
| S11-S12 | Integration testing + UAT prep | Hoàn thiện, regression |

### 3.2. Challenge estimation của team

**Kỹ thuật phát hiện estimation sai:**
- So sánh với dự án tương tự (historical data)
- Kiểm tra từng task có vượt quy tắc 4/40 không
- Hỏi: "Đã bao gồm effort cho code review, bug fixing, rework chưa?"
- PERT cho task rủi ro cao thay vì single-point estimate
- Đề nghị team estimate độc lập trước khi thảo luận (tránh anchoring bias)

### 3.3. Buffer Management nâng cao

```
Method: Project Buffer (Critical Chain)
  Task estimate tổng: 50 ngày (aggressive, không buffer riêng lẻ)
  Project buffer: 50% = 25 ngày
  Tổng timeline: 75 ngày

-> Task riêng lẻ: aggressive
-> Buffer tập trung cuối dự án
-> Tiêu thụ buffer khi cần (linh hoạt)
```

**KHÔNG nói team về buffer** -> Tránh Parkinson's Law ("công việc tự giãn ra để lấp đầy thời gian có sẵn")

### 3.4. Recovery Plan khi dự án gặp vấn đề

**Ví dụ: Velocity thực tế = 60%, Bug density = 1.2/KLoC (target 0.5)**

| Phương án | Pros | Cons |
|-----------|------|------|
| Tăng nguồn lực (thêm 2 PG) | Tăng capacity | Ramp-up time, cost tăng |
| Thu hẹp scope (defer module) | Giữ deadline | Cần negotiate với khách hàng |
| Tăng giờ làm thêm | Nhanh, không cost thêm | Chỉ ngắn hạn, burnout risk |
| Cải thiện quy trình (review, pair) | Tăng quality + velocity | Mất thời gian đầu |

---

## 4. Quản lý cấp tổ chức (L4)

### 4.1. Estimation Framework cho tổ chức

- Xây dựng **historical database** từ tất cả dự án: effort thực tế vs estimate
- Định nghĩa **estimation baseline** theo loại dự án (web app, mobile, migration)
- Benchmark cross-project: cost/function point, defect density, velocity range

### 4.2. Portfolio-level Resource Optimization

```
Project A (15 người, 6 tháng): Cần senior BE Sprint 3-8
Project B (8 người, 4 tháng): Cần senior BE Sprint 1-4
Project C (10 người, 3 tháng): Cần senior FE Sprint 1-6

-> Chia sẻ senior BE: Project B Sprint 1-4 -> Project A Sprint 5-8
-> Tránh thiếu nguồn lực, tối ưu chi phí
```

### 4.3. Xây dựng Hybrid Methodology chuẩn

- Định nghĩa khi nào dùng Waterfall, khi nào Agile, khi nào Kanban
- Template WBS chuẩn cho từng loại dự án
- Training PM khác về estimation và planning

---

## 5. Tự kiểm tra

### Bài tập: Lập WBS + Release Plan cho dự án 6 tháng, 8 người

**Bối cảnh:**
```
Dự án: Hệ thống quản lý vận hành (8 modules)
Team: 1 PM, 1 BrSE, 2 SE, 3 PG, 1 Tester
Model: Hybrid (Phase 1 Waterfall 2 tháng, Phase 2 Agile 4 tháng)
Budget: 80 man-month
```

**Yêu cầu:**
1. Tạo WBS cho Phase 2 (8 modules x 3 activities: Design/Dev/Test)
2. Ước lượng effort bằng PERT cho 2 module phức tạp nhất
3. Lập Sprint Roadmap (phân bổ 8 modules vào 8 sprint)
4. Xác định MVP — module nào làm trước? Giải thích lý do
5. Phân bổ 3 PG + 1 Tester cho 8 modules (lưu ý 1 PG mới cần ramp-up)
6. Xác định Critical Path và buffer strategy

**Tiêu chí đánh giá:**

| Level | Yêu cầu |
|-------|---------|
| L1 | WBS đủ 8 modules, effort hợp lý, format đúng |
| L2 | Sprint roadmap có MVP, resource allocation xét ramp-up, PERT cho module phức tạp |
| L3 | Recovery plan khi velocity thấp, hybrid process design, reporting framework |
| L4 | Cross-project resource optimization, estimation accuracy improvement plan |

---

## 6. Tài liệu tham khảo

**Source gốc:**
- PM Competency #1: `khung-danh-gia-nang-luc-main/roles/pm/nang-luc.md`
- PM Levels: `khung-danh-gia-nang-luc-main/roles/pm/levels.md`
- Planning Test: `khung-danh-gia-nang-luc-main/roles/pm/tests/planning.md`

**CMMI Documents:**
- PRC-PJM-PP-02: Project Planning Process (7 bước)
- PRC-PJM-PP-03: Estimation Process (6 bước)
- RUL-PJM-PP-01: Project Planning Rule (WBS, estimation, buffer)
- GLN-PJM-PP-01: Project Planning Guide (techniques, case study)
- GLN-PJM-PP-02: Estimation Best Practices Guide (PERT, Planning Poker, WBS phân ra)

**Đặc thù khách hàng Nhật:**
- Deadline = 約束 (lời hứa) — vi phạm gây tổn hại nghiêm trọng
- Re-estimation làm giảm mức độ tin tưởng
- Estimation sai lệch > 15% có thể bị yêu cầu giải trình bằng văn bản
- Đầu tư thời gian cho estimation = bảo vệ uy tín công ty
