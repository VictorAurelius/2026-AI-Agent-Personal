# Documentation & Specification Writing (ドキュメント作成力)

> **Mục tiêu:** Thảo luận kỹ năng viết tài liệu thiết kế theo chuẩn dự án Nhật Bản — từ điền template đến thiết kế template cho team
> **Level:** L1 (điền đúng template) -> L2 (viết spec implementable) -> L3 (thiết kế template & guideline)
> **Thời gian đọc:** ~25 phút
> **Liên quan:** SE Competency #6 (ドキュメント作成力), #5 (品質意識), CMMI PA: ENG-TS (PRC-ENG-TS-02, PRC-ENG-TS-03)

---

## 1. Khái niệm cơ bản (L1)

### 1.1. Các loại tài liệu thiết kế trong dự án Nhật

| Tài liệu | Tên Nhật | Phase | Người viết | Output |
|----------|----------|-------|-----------|--------|
| **Basic Design** | 基本設計書 | Basic Design | SE (L2-L3) | System overview, API list, DB schema, screen design |
| **Detail Design - API** | API詳細設計書 | Detail Design | SE (L1-L3) | Request/Response/Validation/DB/Error/Flowchart |
| **Detail Design - Screen** | 画面詳細設計書 | Detail Design | SE (L2-L3) | Layout/I-O items/Events/Validation/Messages |
| **Detail Design - Batch** | バッチ設計書 | Detail Design | SE (L2-L3) | Input/Output/Flow/Log/Error/Re-run |
| **Common Design** | 共通設計書 | Basic Design | SE (L2-L3) | Naming/Error code/Logging/Utilities |
| **DB Spec** | DB定義書 | Basic Design | SE (L1-L3) | Table/Column/Type/Constraint/Index |

### 1.2. Điền template đúng — API Spec

Mẫu template API spec và cách điền đúng:

```
===========================================================
API SPECIFICATION (API詳細設計書)
===========================================================

1. THÔNG TIN CƠ BẢN
-----------------------------------------------------------
  API Name:        [tên_api]
  Endpoint:        [HTTP_METHOD] /api/v1/[resource]
  Overview:        [Mô tả ngắn gọn 1 dòng]
  Used by:         [Màn hình/Batch nào gọi API này]
  Permissions:     [Roles được phép: Admin, Operator, Viewer]

2. REQUEST
-----------------------------------------------------------
  2.1 Path Parameters:
  | Param  | Type   | Required | Description     | Example |
  |--------|--------|----------|-----------------|---------|
  | id     | UUID   | Yes      | Fuel info ID    | 550e... |

  2.2 Query Parameters:
  | Param     | Type    | Required | Description          | Example    |
  |-----------|---------|----------|----------------------|------------|
  | fuel_name | string  | No       | Search keyword (LIKE)| "石炭"     |
  | page      | integer | No       | Page number (def: 1) | 1          |
  | size      | integer | No       | Page size (def: 20)  | 20         |

  2.3 Request Header:
  | Header        | Required | Description          |
  |---------------|----------|----------------------|
  | Authorization | Yes      | Bearer {access_token}|
  | Content-Type  | Yes (POST/PUT) | application/json |

  2.4 Request Body (POST/PUT only):
  | Field      | Type    | Required | Validation         | Description |
  |------------|---------|----------|--------------------|-------------|
  | fuel_name  | string  | Yes      | max: 100           | Fuel name   |
  | fuel_type  | string  | Yes      | in: solid,liquid,gas| Fuel type  |

3. RESPONSE
-----------------------------------------------------------
  3.1 Success (HTTP 200):
  {
    "data": { ... },
    "result": { "code": "success" }
  }

  3.2 Error Responses:
  | HTTP | Error Code        | Condition              | Message ID  |
  |------|-------------------|------------------------|-------------|
  | 400  | invalid_parameter | Validation fail        | (per field) |
  | 401  | unauthorized      | Token invalid/expired  | -           |
  | 403  | forbidden         | Role không đủ quyền    | MSG_COM_002 |
  | 404  | not_found         | Resource không tồn tại | MSG_xxx_xxx |
  | 409  | conflict          | Exclusive error        | MSG_xxx_xxx |
  | 500  | internal_error    | System error           | MSG_COM_001 |

4. VALIDATION
-----------------------------------------------------------
  4.1 Role Check:
  - [Roles được phép]

  4.2 Đơn mục (単項目チェック):
  | Field     | Check             | Error code    |
  |-----------|-------------------|---------------|
  | fuel_name | max_length: 100   | EV_FUEL_001   |
  | page      | integer, >= 1     | EV_COM_001    |

  4.3 Tương quan (相関チェック):
  | Fields           | Check                        | Error code  |
  |------------------|------------------------------|-------------|
  | date_from, date_to | date_from <= date_to       | EV_FUEL_010 |

  4.4 Nghiệp vụ (業務チェック):
  | Check                              | Error code  |
  |------------------------------------|-------------|
  | Fuel đang được sử dụng → không xóa | EB_FUEL_001 |

5. DB OPERATIONS
-----------------------------------------------------------
  Table: fuel_info
  Join: (nếu có)

  Pseudo SQL:
  SELECT fuel_info_id, fuel_name, fuel_type, ...
  FROM fuel_info
  WHERE tenant_code = :login_tenant
    AND delete_flag = false
    AND (:fuel_name IS NULL OR fuel_name LIKE '%' || :fuel_name || '%')
  ORDER BY :sort_by :sort_order
  LIMIT :size OFFSET (:page - 1) * :size

6. XỬ LÝ LỖI
-----------------------------------------------------------
  Tuân theo common error handling.
  Kết quả 0 rows → trả data = [], total_count = 0 (KHÔNG phải 404)

7. FLOWCHART
-----------------------------------------------------------
  Nhận request
  → Xác thực token (401 nếu fail)
  → Check role (403 nếu fail)
  → Validate params (400 nếu fail)
  → Lấy tenant_code từ login info
  → Build SQL → Execute
  → Format response → Trả HTTP 200
===========================================================
```

### 1.3. Điền template đúng — DB Spec

```
===========================================================
DB SPECIFICATION (DB定義書)
===========================================================

Table: fuel_info
Description: Lưu trữ thông tin nhiên liệu
Module: fuel

| #  | Column          | Type         | PK | FK | Not Null | Default | Index | Description          |
|----|-----------------|------------- |----|-----|----------|---------|-------|----------------------|
| 1  | fuel_info_id    | UUID         | Yes| -   | Yes      | gen_uuid| -     | Primary key          |
| 2  | tenant_code     | VARCHAR(20)  | -  | Yes | Yes      | -       | idx_1 | Tenant identifier    |
| 3  | fuel_name       | VARCHAR(100) | -  | -   | Yes      | -       | idx_2 | Fuel name            |
| 4  | fuel_type       | VARCHAR(10)  | -  | -   | Yes      | -       | -     | solid/liquid/gas     |
| 5  | calorific_value | DECIMAL(10,2)| -  | -   | No       | -       | -     | Kcal/kg              |
| 6  | unit_price      | INTEGER      | -  | -   | No       | -       | -     | Yen/unit             |
| 7  | supplier_name   | VARCHAR(200) | -  | -   | No       | -       | -     | Supplier company     |
| 8  | delete_flag     | BOOLEAN      | -  | -   | Yes      | false   | -     | Soft delete flag     |
| 9  | created_by      | VARCHAR(50)  | -  | -   | Yes      | -       | -     | Creator user ID      |
| 10 | created_at      | TIMESTAMP    | -  | -   | Yes      | NOW()   | -     | Created datetime     |
| 11 | updated_by      | VARCHAR(50)  | -  | -   | Yes      | -       | -     | Updater user ID      |
| 12 | updated_at      | TIMESTAMP    | -  | -   | Yes      | NOW()   | idx_3 | Updated datetime     |

Indexes:
  idx_1: tenant_code — Filter performance (mỗi query đều có tenant_code)
  idx_2: tenant_code + fuel_name — Search performance
  idx_3: updated_at — Sort performance + exclusive check

Constraints:
  FK: tenant_code → tenant_master.tenant_code
  CHECK: fuel_type IN ('solid', 'liquid', 'gas')
===========================================================
```

### 1.4. Traceability cơ bản (Requirement → Design)

Mỗi thiết kế phải trace ngược về requirement:

```
| Requirement ID | Requirement              | Design Document      | Design ID    |
|----------------|--------------------------|----------------------|------------- |
| REQ-FUEL-001   | Hiển thị danh sách NL    | API Spec             | API-FUEL-001 |
| REQ-FUEL-001   | Hiển thị danh sách NL    | Screen Spec          | SCR-FUEL-001 |
| REQ-FUEL-002   | Tìm kiếm NL theo tên    | API Spec             | API-FUEL-001 |
| REQ-FUEL-003   | Xóa NL                   | API Spec             | API-FUEL-003 |
| REQ-FUEL-003   | Xóa NL                   | Screen Spec          | SCR-FUEL-001 |
| REQ-FUEL-004   | Export CSV                | API Spec             | API-FUEL-005 |
| REQ-FUEL-004   | Export CSV                | Batch Spec           | BAT-FUEL-001 |
```

**Quy tắc:** 100% requirement phải có ít nhất 1 design mapping. Không được có orphan requirement.

---

## 2. Thực hành nâng cao (L2)

### 2.1. Viết spec "Implementable" — Developer đọc xong code được ngay

**Tiêu chí "implementable":**

| Tiêu chí | Ví dụ Tốt | Ví dụ Xấu |
|----------|-----------|-----------|
| **Cụ thể** | "fuel_name: LIKE search, case-insensitive" | "Search by name" |
| **Có ví dụ** | `GET /api/v1/fuel-infos?fuel_name=石炭&page=1` | "Call search API" |
| **Có boundary** | "size: integer, 1-100, default 20" | "Page size parameter" |
| **Có error case** | "0 rows → empty array [], NOT 404" | "Handle no data" |
| **Có SQL** | `WHERE tenant_code = :login_tenant AND delete_flag = false` | "Filter by tenant" |
| **Có message ID** | "Show MSG_FUEL_001 when data empty" | "Show no data message" |

**Anti-patterns (cách viết xấu):**
- "Please refer to common design" — Mà không ghi rõ refer CÁI GÌ
- "Same as other API" — Mà không ghi rõ API NÀO
- "Handle error appropriately" — Không rõ là handle NHƯ THẾ NÀO
- "Validate input" — Không ghi rõ validate CÁI GÌ với ĐIỀU KIỆN GÌ

### 2.2. Structured Documentation Flow

Khi viết tài liệu cho 1 module, thứ tự như sau:

```
Step 1: API List (danh sách API)
  → Liệt kê tất cả API của module: endpoint, method, overview
  → Output: API-LIST-{MODULE}

Step 2: DB Spec (định nghĩa DB)
  → Thiết kế table, column, constraint, index
  → Output: DB-{MODULE}

Step 3: Common Design (thiết kế chung)
  → Naming convention, error code, utilities cho module này
  → Output: COM-{MODULE}

Step 4: API Detail Spec (đặc tả API chi tiết)
  → Viết chi tiết từng API: request/response/validation/DB/error
  → Output: API-{MODULE}-{SEQ} (vd: API-FUEL-001)
  → PHẢI reference đến DB spec và common design

Step 5: Screen Spec (đặc tả màn hình chi tiết)
  → Viết chi tiết từng màn hình: layout/event/validation/message
  → Output: SCR-{MODULE}-{SEQ}
  → PHẢI reference đến API spec và message list

Step 6: Batch Spec (nếu có)
  → Input/Output/Flow/Log/Error
  → Output: BAT-{MODULE}-{SEQ}

Step 7: RTM Update
  → Map tất cả requirement → design document
  → Kiểm tra 100% coverage
```

### 2.3. Version Control cho tài liệu

**Lịch sử thay đổi (改訂履歴):**

```
| Version | Date       | Author      | Reviewer    | Changes                |
|---------|------------|-------------|-------------|------------------------|
| 1.0     | 2026-03-01 | Nguyen V.K  | Tanaka-san  | Initial version        |
| 1.1     | 2026-03-15 | Nguyen V.K  | Tanaka-san  | Add CSV export API     |
| 2.0     | 2026-04-01 | Nguyen V.K  | Suzuki-san  | Redesign error handling|
```

**Quy tắc version:**
- **1.0** → First baseline (đã review và approve)
- **1.1, 1.2** → Minor changes (thêm field, sửa validation)
- **2.0** → Major changes (thay đổi structure, thêm/xóa API)
- Mỗi thay đổi phải ghi: nội dung thay đổi, ngày, người sửa, lý do
- Baseline mới chỉ được tạo sau khi review và approve

**Change Request tracking:** Mỗi CR ghi: CR ID, ngày, người yêu cầu, nội dung thay đổi, impact (DB/API/Screen), status (Pending/Approved/Rejected).

### 2.4. Bilingual Documentation (Vietnamese + Japanese)

**Nguyên tắc song ngữ cho dự án offshore:**
- Section headers song ngữ: `## 1. Tổng quan / 概要`, `## 2. Đặc tả API / API仕様`
- Field names ghi kèm tên Nhật: `fuel_name (燃料名)`, `unit_price (単価)`
- Technical terms giữ nguyên: 画面, API, バッチ, 排他制御
- Logic mô tả tiếng Việt (team VN hiểu), heading tiếng Nhật (team JP review)
- Code samples và SQL giữ tiếng Anh

---

## 3. Chiến lược & Dẫn dắt (L3)

### 3.1. Thiết kế Documentation Template cho team

Khi làm L3 (Senior SE), cần tạo template để team sử dụng nhất quán.

**Template API Spec — Cấu trúc bắt buộc:**

```
Sections bắt buộc (KHÔNG được bỏ):
  [ ] 1. Thông tin cơ bản (tên, endpoint, method, overview, permission)
  [ ] 2. Request (path/query/header/body với type + validation)
  [ ] 3. Response (success + error, có JSON sample)
  [ ] 4. Validation (role + đơn mục + tương quan + nghiệp vụ)
  [ ] 5. DB Operations (table, join, WHERE, ORDER BY, pseudo SQL)
  [ ] 6. Error Handling (error code → HTTP status → message ID)
  [ ] 7. Flowchart hoặc Pseudo code

Sections tùy chọn:
  [ ] 8. NFR (response time target, rate limit)
  [ ] 9. External system integration (IF spec)
  [ ] 10. Notes / Restrictions
```

**Template Screen Spec — Cấu trúc bắt buộc:**

```
Sections bắt buộc:
  [ ] 1. Layout màn hình (phân vùng, wireframe)
  [ ] 2. Mục nhập/xuất (tên, control, format, data source, default)
  [ ] 3. Event xử lý (tối thiểu: initial, search, action)
  [ ] 4. Validation (client vs server, đơn mục + tương quan)
  [ ] 5. Message list (ID, nội dung, điều kiện hiển thị)

Mỗi event phải có:
  [ ] a. Trigger (cái gì kích hoạt event)
  [ ] b. Xử lý (logic chi tiết)
  [ ] c. API call (endpoint + params)
  [ ] d. Response handling (success + error)
  [ ] e. UI update (data binding, enable/disable, show/hide)
```

### 3.2. Documentation Guidelines cho team

**Guideline document bao gồm 5 phần:**
1. **Mục đích** — Tại sao cần, áp dụng cho ai
2. **Quy tắc chung** — Format (Markdown/Excel), ngôn ngữ (song ngữ), naming ({TYPE}-{MODULE}-{SEQ}.md), encoding (UTF-8)
3. **Quy tắc viết** — Cụ thể + có ví dụ, ghi rõ document ID, không TODO/TBD, dùng Message ID
4. **Quy tắc review** — Self-review → Peer review (logic + nhất quán) → TL review (architecture + cross-module)
5. **Version control** — Draft → Review → Baseline, Change Request cho mỗi thay đổi sau baseline

### 3.3. Quality Gates cho Document Review

**Gate 1: Self-Review Checklist (trước khi gửi review)**

```
Format & Template:
  [ ] Đúng template (tất cả sections bắt buộc đã điền)
  [ ] Không còn TODO/TBD
  [ ] Lịch sử thay đổi đã cập nhật
  [ ] Version number đúng

Nội dung:
  [ ] Request/Response có JSON sample
  [ ] Validation đầy đủ: đơn mục + tương quan + nghiệp vụ
  [ ] Error handling cover: 400, 401, 403, 404, 409, 500
  [ ] Pseudo SQL có tenant_code filter và delete_flag check
  [ ] Flowchart/Pseudo code logic đúng

Tham chiếu:
  [ ] Reference đến common design (error code, message ID)
  [ ] Reference đến DB spec (table, column names nhất quán)
  [ ] Reference đến requirement (REQ-xxx)
  [ ] Naming convention nhất quán (snake_case, kebab-case)
```

**Gate 2: Peer Review** — Kiểm tra logic (SQL, validation, error handling), nhất quán (API ↔ Screen ↔ DB ↔ Message), và tính implementable (developer đọc xong code được không?)

**Gate 3: TL Review** — Kiểm tra architecture fit, cross-module consistency (naming, error code, API design), và quality (0 Critical/Major, RTM = 100%, không orphan)

### 3.4. Metrices cho Document Quality

| Metric | Ngưỡng | Đo như thế nào |
|--------|--------|---------------|
| **Template Compliance** | >= 95% sections filled | Count filled sections / total required sections |
| **Review Turnaround** | <= 2 ngày làm việc | Date submitted → Date reviewed |
| **Revision Count** | <= 3 revisions | Số lần phải sửa lại sau review |
| **Defect Density** | <= 5 issues / 10 pages | Số issues tìm thấy / số trang tài liệu |
| **Rework Rate** | <= 20% | Thời gian sửa / Thời gian viết ban đầu |
| **RTM Coverage** | = 100% | Requirements mapped / Total requirements |

---

## 4. Tự kiểm tra

### Bài tập: Viết API Specification đầy đủ cho 1 endpoint

**Đề bài:** Viết đặc tả API đầy đủ cho endpoint sau:

```
API: create_fuel_info
Endpoint: POST /api/v1/fuel-infos
Mục đích: Tạo mới thông tin nhiên liệu
Quyền: Admin, Operator (Viewer KHÔNG được)
```

**Yêu cầu viết đầy đủ:**

1. Thông tin cơ bản (tên, endpoint, method, overview, permission)
2. Request body với tất cả fields (fuel_name, fuel_type, calorific_value, sulfur_content, ash_content, unit_price, supplier_name)
3. Response (success: 201 Created, error: 400/401/403/409/500)
4. Validation:
   - Role check (Admin, Operator only)
   - Đơn mục: required, type, max_length, range, format
   - Tương quan: (tự suy nghĩ thêm)
   - Nghiệp vụ: Kiểm tra trùng tên nhiên liệu trong cùng tenant
5. DB Operations: INSERT statement với audit columns
6. Error handling: Đầy đủ mapping
7. Flowchart

**Tự chấm điểm (tổng 47 điểm):** Request params (/4) + Response format (/4) + Validation (/4) + Error response (/3) + SQL logic (/5) + Multi-tenant (/3) + Flowchart (/4) + Implementable (/5) + JSON sample (/3) + Tham chiếu chéo (/2) + Common format (/4) + Error handling (/3) + Naming (/3). Pass: L1 >= 28 (60%), L2 >= 33 (70%), L3 >= 38 (80%)

---

## 5. Tài liệu tham khảo

| Tài liệu | Nội dung |
|----------|---------|
| SE nang-luc.md #6 (ドキュメント作成力) | Tiêu chí: cấu trúc, mức độ chi tiết, tham chiếu chéo, quản lý phiên bản |
| SE nang-luc.md #5 (品質意識) | Tính nhất quán, trường hợp ngoại lệ, NFR, self-review |
| SE test thiet-ke-chi-tiet.md | Đề thi mẫu + đáp án API spec + Screen spec + Rubric chấm điểm |
| GLN-ENG-TS-01 | Hướng dẫn viết Basic Design: RTM, diagram, format dự án Nhật |
| GLN-ENG-TS-02 | Hướng dẫn viết Detail Design: code comments, formal document template |
| RUL-ENG-TS-01 | Tiêu chuẩn thiết kế: nội dung bắt buộc, diagram bắt buộc, RTM |
| RUL-ENG-TS-02 | Design Review Rule: tốc độ review, tiêu chí từ chối, ngưỡng phê duyệt |
| RUL-ENG-TS-05 | Definition of Done: tiêu chuẩn hoàn thành cho thiết kế và tài liệu |
| RUL-ENG-TS-03 | Tiêu chuẩn lập trình: độ phức tạp, độ dài hàm, comment |
