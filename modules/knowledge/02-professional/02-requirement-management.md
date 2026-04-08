# Requirement Management (Quản lý Yêu cầu)

> **Mục tiêu:** Quản lý yêu cầu từ thu thập, phân loại, ưu tiên, theo dõi trạng thái đến kiểm soát thay đổi
> **Level:** L1 -> L2 -> L3
> **Thời gian đọc:** ~25 phút
> **Liên quan:** PM Competency #2 (要件管理), CMMI PA: REQM (Requirements Management)

---

## 1. Khái niệm cơ bản (L1)

### 1.1. Requirement là gì?

Requirement = Nhu cầu của stakeholder được diễn đạt cụ thể, có thể kiểm chứng.

**3 loại requirement:**

| Loại | Định nghĩa | Ví dụ |
|------|------------|-------|
| **Nhu cầu (Needs)** | Lưu thông tin, xử lý, báo cáo | "Hệ thống cần lưu thông tin khách hàng" |
| **Mong đợi (Expectations)** | Nhanh, tiết kiệm, dễ dùng | "Response time < 3 giây" |
| **Ràng buộc (Constraints)** | Hạ tầng, kết nối, quy định | "Phải chạy trên AWS, tương thích IE11" |

**Phân loại chính:**

| Phân loại | Mô tả | Ví dụ |
|-----------|-------|-------|
| **Functional (Chức năng)** | Hệ thống làm gì | "Người dùng đăng ký tài khoản bằng email" |
| **Non-functional (Chất lượng)** | Hệ thống làm tốt như thế nào | "Response time <= 3s, uptime 99.9%" |
| **Communication (Giao tiếp)** | Cách tương tác với hệ thống | "Giao diện hỗ trợ tiếng Nhật và tiếng Việt" |

### 1.2. Theo dõi trạng thái requirement

**6 trạng thái cơ bản:**

```
Đặt tác -> Xác nhận -> Thiết kế -> Code -> Test -> Bàn giao
  [New]    [Confirmed]  [Designed] [Coded] [Tested] [Delivered]
```

**Hành vi L1:**
- Hiểu danh sách yêu cầu đã có
- Cập nhật trạng thái khi được giao
- Báo khi phát hiện scope creep
- Phân biệt được functional vs non-functional

### 1.3. Requirement Attributes (Thuộc tính yêu cầu)

Mỗi requirement phải có tối thiểu các thuộc tính sau:

| Thuộc tính | Mô tả | Ví dụ |
|------------|-------|-------|
| **ID** | Mã định danh duy nhất | REQ-001 |
| **Tên** | Tên ngắn gọn | "Đăng ký tài khoản" |
| **Nội dung chi tiết** | Mô tả đầy đủ | "Người dùng nhập email, mật khẩu..." |
| **Ưu tiên** | Mức độ quan trọng | Must / Should / Could / Won't |
| **Trạng thái** | Vị trí trong quy trình | Confirmed / Designed / Coded / Tested |
| **Độ lớn** | Kích thước ước lượng | 5 Story Points / 3 man-day |
| **Phê duyệt** | Ai đã xác nhận | PO sign-off 2026-01-15 |

---

## 2. Thực hành nâng cao (L2)

### 2.1. Quy trình 8 bước quản lý yêu cầu

```
Bước 1: Xác định stakeholder
         |-- Khách hàng, end-user, BrSE, dev/QA lead, ops
         v
Bước 2: Tìm hiểu yêu cầu
         |-- Interview, workshop, document analysis
         v
Bước 3: Lập danh sách yêu cầu (Product Backlog)
         |-- User stories, acceptance criteria
         v
Bước 4: Phân ưu tiên
         |-- MoSCoW, Kano, Business Value matrix
         v
Bước 5: Quản lý trạng thái
         |-- Tracking trên Jira/Excel: 6 trạng thái
         v
Bước 6: Quản lý thay đổi (Change Control)
         |-- 5-step CR process
         v
Bước 7: Kiểm soát ăn khớp kế hoạch — yêu cầu
         |-- Mỗi sprint: review scope vs plan
         v
Bước 8: Quản lý quan hệ yêu cầu — sản phẩm
         |-- Traceability Matrix
```

### 2.2. Product Backlog Management

**Product Backlog** = Danh sách tất cả yêu cầu, sắp xếp theo ưu tiên.

**Nguyên tắc:**
- PO owned, PM hỗ trợ ưu tiên hóa
- Prioritized by business value
- "Chỉ cho phép thay đổi yêu cầu định kỳ sau mỗi sprint"
- Mục tiêu: "Xây 20% tính năng, giao 80% giá trị"

**User Story format:**
```
As a [vai trò],
I want [mục tiêu],
So that [giá trị].

Acceptance Criteria:
- Given [điều kiện], When [hành động], Then [kết quả]
```

### 2.3. MoSCoW Prioritization

| Phân loại | Ý nghĩa | Tỉ lệ khuyến nghị | Ví dụ |
|-----------|---------|-------|-------|
| **Must** | Bắt buộc, không có thì dự án thất bại | 60% effort | Login, Core business logic |
| **Should** | Quan trọng nhưng có workaround | 20% effort | Advanced search, Export CSV |
| **Could** | Mong muốn, giao thêm được thì tốt | 15% effort | Dark mode, Dashboard widget |
| **Won't** | Loại bỏ (đợt này), làm sau | 5% (defer) | Mobile app, AI recommendation |

### 2.4. Kano Model

```
Satisfaction (hài lòng)
    ^
    |        /  Delighter (Excitement)
    |       /     "Không ai yêu cầu nhưng sẽ wow"
    |      /
    |-----/---- Performance (Mong đợi)
    |    /        "Càng tốt thì càng hài lòng"
    |   /
    |  /
    |----- Basic (Cơ bản)
    |        "Không có thì thất bại, có thì không ai khen"
    +-------------------------------------------> Functionality
```

| Loại | Ví dụ | Chiến lược |
|------|-------|------------|
| **Basic** | Login, save data, error handling | PHẢI có, không được thiếu |
| **Performance** | Response time, search accuracy | Càng tốt càng được đánh giá cao |
| **Delighter** | Auto-suggest, smart notification | Surprise factor, tăng customer satisfaction |

### 2.5. Change Request — Quy trình 5 bước

```
Bước 1: GHI NHẬN
  |-- CR ID, mô tả, người yêu cầu, ngày
  v
Bước 2: ĐÁNH GIÁ IMPACT
  |-- Size (SP), Effort (man-day), Cost, Time, Quality
  |-- "Module nào bị ảnh hưởng? Cần sửa gì?"
  v
Bước 3: PHÊ DUYỆT
  |-- PM + PO + Khách hàng
  |-- Approved / Rejected / Deferred
  v
Bước 4: XỬ LÝ
  |-- Update backlog, schedule, resource plan
  |-- Thực hiện development
  v
Bước 5: BÀN GIAO
  |-- Test, review, deploy
  |-- Cập nhật Traceability Matrix
```

**Quy tắc với dự án Nhật:**
- "Chỉ cho phép thay đổi yêu cầu định kỳ sau mỗi sprint" (không giữa sprint)
- CR tăng effort > 10% -> bắt buộc lập lại kế hoạch (RUL-PJM-PP-01)
- Mỗi CR phải có impact analysis bằng văn bản

### 2.6. Traceability Matrix (RTM) — 1 chiều

**RTM** đảm bảo mỗi yêu cầu được thiết kế, code, và test.

| Req ID | Requirement | Design | Code Module | Test Case | Status |
|--------|-------------|--------|-------------|-----------|--------|
| REQ-001 | User Registration | DD-001 | auth/register.ts | TC-001, TC-002 | Tested |
| REQ-002 | Login with email | DD-002 | auth/login.ts | TC-003 | Coded |
| REQ-003 | Password reset | DD-003 | auth/reset.ts | TC-004 | Designed |
| REQ-004 | Export report PDF | DD-010 | report/export.ts | TC-020 | Confirmed |

**Kiểm tra:**
- Có requirement nào chưa có design? -> GAP
- Có requirement nào chưa có test case? -> RISK
- Có code nào không link về requirement? -> SCOPE CREEP

---

## 3. Chiến lược & Dẫn dắt (L3)

### 3.1. Full 2-way Traceability

**2 chiều:**
- **Forward:** Requirement -> Design -> Code -> Test -> Delivery
- **Backward:** Delivery -> Test -> Code -> Design -> Requirement

```
Requirement  <-->  Design Doc  <-->  Code Module  <-->  Test Case  <-->  Deliverable
  REQ-001          DD-001           auth/*.ts          TC-001~002      Release 1.0
  REQ-002          DD-002           auth/login.ts      TC-003          Release 1.0
```

**Lợi ích:**
- **Impact Analysis:** Khi requirement thay đổi, biết ngay code và test nào bị ảnh hưởng
- **Coverage Check:** Đảm bảo không sót requirement, không thừa code
- **Audit Trail:** Khách hàng Nhật có thể trace bất kỳ tính năng nào từ yêu cầu đến sản phẩm

### 3.2. Prototype-driven Requirement Clarification

**Quy trình:**
```
Requirement mơ hồ (tiếng Nhật)
    |
    v
Prototype/Mockup (2-3 ngày)
    |
    v
Demo cho khách hàng + BrSE
    |
    v
Feedback & chỉnh sửa
    |
    v
Requirement được confirm (sign-off)
    |
    v
Development bắt đầu
```

**Tại sao quan trọng với dự án Nhật?**
- Spec tiếng Nhật thường có nhiều điểm mơ hồ (暗黙の了解 — hiểu ngầm)
- Prototype giúp "thấy" thay vì "đọc"
- Giảm risk hiểu sai spec — risk lớn nhất trong dự án Nhật

### 3.3. Non-Functional Requirements (NFR) Specification

**4 loại NFR chính:**

| NFR | Metric | Target ví dụ | Cách đo |
|-----|--------|-------------|---------|
| **Performance** | Response time | <= 3s (bình thường), <= 5s (cao điểm) | Load test (JMeter) |
| **Security** | OWASP compliance | Top 10 vulnerabilities = 0 | Penetration test |
| **Scalability** | Concurrent users | 1000 users đồng thời | Stress test |
| **Availability** | Uptime | 99.9% (8.7h downtime/năm) | Monitoring (Grafana) |

**NFR Template:**
```
ID: NFR-001
Category: Performance
Description: Thời gian phản hồi của API không quá 3 giây
  trong điều kiện bình thường (< 100 concurrent users)
Measurement: Response time P95 <= 3000ms
Test Method: Load test với 100 concurrent users trong 30 phút
Acceptance: 95% requests có response time <= 3s
Priority: Must
```

### 3.4. Kiểm soát CR hiệu quả

**Nguyên tắc L3:**
- Trade-off analysis cho mỗi CR: scope vs time vs cost vs quality
- "Chỉ cho phép thay đổi sau mỗi sprint" — enforce nghiêm ngặt
- Giữ scope baseline, mọi thay đổi phải approved trước khi thực hiện
- Protect team khỏi scope creep: PM là "bộ lọc" giữa khách hàng và team

**Báo cáo CR cho khách hàng Nhật:**
```
CR-005: Thêm tính năng Data Export

Impact Analysis:
- Effort: +15 man-day
- Timeline: +1 sprint (2 tuần)
- Cost: +15 man-day x đơn giá
- Quality: Không ảnh hưởng (thêm test case tương ứng)
- Risk: Chưa đủ resource -> cần thêm 1 PG

Đề xuất:
  Phương án A: Accept CR, dịch deadline 2 tuần, budget tăng 15 MD
  Phương án B: Accept CR, cắt module Reporting (defer), giữ deadline
  Phương án C: Reject CR, làm ở phase 2

Khuyến nghị: Phương án B — giữ deadline, defer Reporting vì ưu tiên thấp hơn
```

---

## 4. Tự kiểm tra

### Bài tập: Xây dựng RTM cho 1 module với 20 requirement

**Bối cảnh:**
```
Module: User Management (hệ thống quản lý vận hành)
20 requirements bao gồm:
- 12 Functional: CRUD user, role assignment, permission, login, logout,
  password policy, 2FA, audit log, bulk import, search, filter, export
- 5 Non-functional: Response time, concurrent users, password encryption,
  session timeout, audit retention
- 3 Communication: Error messages tiếng Nhật, email notification, help tooltip
```

**Yêu cầu:**
1. Lập danh sách 20 requirements với đầy đủ thuộc tính (ID, tên, ưu tiên, độ lớn)
2. Phân ưu tiên bằng MoSCoW
3. Xây dựng Traceability Matrix 2 chiều (Req -> Design -> Code -> Test -> Delivery)
4. Xác định 3 CR tiềm năng và viết impact analysis
5. Xác định requirement nào cần prototype trước khi phát triển

**Tiêu chí đánh giá:**

| Level | Yêu cầu |
|-------|---------|
| L1 | Danh sách 20 req với trạng thái, phân loại functional/non-functional |
| L2 | Đầy đủ thuộc tính, MoSCoW, RTM 1 chiều, CR process 5 bước |
| L3 | RTM 2 chiều, NFR có metric cụ thể, prototype cho req phức tạp, trade-off analysis |

### Câu hỏi tự kiểm tra

1. **Khi khách hàng Nhật yêu cầu thêm tính năng giữa sprint, bạn xử lý thế nào?**
   - Ghi nhận CR, đánh giá impact, trình bày phương án (accept/defer/reject)
   - KHÔNG thêm vào sprint hiện tại -> đợi sprint tiếp theo
   - Nếu urgent: negotiate scope trade-off

2. **指摘件数 (số lỗi chỉ ra) tại design review giảm 50% — dấu hiệu tốt hay xấu?**
   - Có thể TỐT: thiết kế tốt hơn, ít lỗi hơn
   - Có thể XẤU: review không kỹ, bỏ sót lỗi
   - Cần kiểm tra kèm: bug density ở phase sau có tăng không?

3. **Làm sao đảm bảo không sót requirement?**
   - RTM 2 chiều: forward + backward traceability
   - Review RTM hàng sprint
   - Kiểm tra: có code nào không link về requirement? Có requirement nào chưa có test?

---

## 5. Tài liệu tham khảo

**Source gốc:**
- PM Competency #2: `khung-danh-gia-nang-luc-main/roles/pm/nang-luc.md`
- PM Levels (Requirement section): `khung-danh-gia-nang-luc-main/roles/pm/levels.md`
- Planning Test (requirement phần): `khung-danh-gia-nang-luc-main/roles/pm/tests/planning.md`

**CMMI Documents:**
- CMMI PA: REQM (Requirements Management)
- PRC-PJM-PP-02: Project Planning Process (Bước 1 — Xác định scope)
- GLN-PJM-PP-01: Project Planning Guide

**Nguyên tắc với khách hàng Nhật:**
- Prototype để xác nhận yêu cầu trước khi dev (tránh hiểu sai spec)
- RTM trình bày cho khách hàng để chứng minh "không sót"
- CR phải có impact analysis bằng văn bản, khách hàng phê duyệt trước khi thực hiện
- 暗黙の了解 (hiểu ngầm) là rủi ro lớn — luôn confirm bằng văn bản hoặc prototype
