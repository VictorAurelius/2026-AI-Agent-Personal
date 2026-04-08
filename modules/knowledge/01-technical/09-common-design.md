# Common Design & Shared Utilities (共通設計)

> **Mục tiêu:** Nắm vững thiết kế các thành phần dùng chung (共通設計) — naming convention, error code, logging, utility functions — theo chuẩn dự án Nhật Bản
> **Level:** L1 (tuân thủ convention) -> L2 (thiết kế common cho module) -> L3 (thiết kế common toàn hệ thống)
> **Thời gian đọc:** ~25 phút
> **Liên quan:** SE Competency #2 (基本設計力), #5 (品質意識), CMMI PA: ENG-TS (PRC-ENG-TS-02)

---

## 1. Khái niệm cơ bản (L1)

### 1.1. Naming Convention — Quy tắc đặt tên

Trong dự án Nhật Bản, naming convention là bắt buộc và được kiểm tra nghiêm ngặt khi review.

**Quy tắc theo context:**

| Context | Convention | Ví dụ | Lý do |
|---------|-----------|-------|-------|
| **DB column** | snake_case | `fuel_name`, `created_at`, `delete_flag` | SQL standard |
| **Python variable/function** | snake_case | `get_fuel_list()`, `total_count` | PEP 8 |
| **URL path** | kebab-case | `/api/v1/fuel-infos`, `/user-profiles` | HTTP convention |
| **JavaScript variable** | camelCase | `fuelName`, `totalCount`, `isLoading` | JS convention |
| **JavaScript component** | PascalCase | `SearchForm`, `DataTable`, `FuelList` | React/Vue convention |
| **CSS class** | kebab-case | `.search-area`, `.btn-primary` | CSS convention |
| **Constant** | UPPER_SNAKE | `MAX_PAGE_SIZE`, `DEFAULT_SORT` | Common practice |
| **JSON request/response** | snake_case | `{ "fuel_name": "...", "unit_price": 100 }` | Match BE convention |

**Quy tắc đặt tên API endpoint:**

```
Pattern: /api/v{version}/{resource-plural}[/{id}][/{sub-resource}]

Ví dụ:
  GET    /api/v1/fuel-infos              — Lấy danh sách
  GET    /api/v1/fuel-infos/{id}         — Lấy chi tiết
  POST   /api/v1/fuel-infos              — Tạo mới
  PUT    /api/v1/fuel-infos/{id}         — Cập nhật toàn phần
  PATCH  /api/v1/fuel-infos/{id}         — Cập nhật 1 phần
  DELETE /api/v1/fuel-infos/{id}         — Xóa (soft delete)
  GET    /api/v1/fuel-infos/export       — Action đặc biệt

Sai:
  /api/v1/getFuelInfo         ← Không dùng động từ trong URL
  /api/v1/fuel_info           ← snake_case (phải là kebab-case)
  /api/v1/fuelInfo            ← camelCase (phải là kebab-case)
```

### 1.2. Message ID Format

Message ID được dùng để quản lý tất cả các thông báo hiển thị cho người dùng, không phụ thuộc ngôn ngữ.

**Format:** `MSG_{MODULE}_{SEQUENCE}`

```
| Message ID   | Nội dung (ja)                                      | Loại    |
|------------- |----------------------------------------------------|---------|
| MSG_COM_001  | システムエラーが発生しました                            | Error   |
| MSG_COM_002  | 権限がありません                                      | Error   |
| MSG_COM_003  | 入力内容に誤りがあります                                | Warning |
| MSG_COM_004  | 保存しました                                          | Success |
| MSG_COM_005  | 削除しました                                          | Success |
| MSG_FUEL_001 | 検索条件に一致するデータがありません                      | Info    |
| MSG_FUEL_002 | 削除してもよろしいですか？                               | Confirm |
| MSG_FUEL_003 | 削除が完了しました                                     | Success |
| MSG_FUEL_004 | データが更新されています。再度読み込んでください。           | Error   |
| MSG_FUEL_005 | エクスポート件数が上限(10,000件)を超えています            | Error   |
```

**Quy tắc:**
- `MSG_COM_xxx`: Message dùng chung toàn hệ thống (001-099)
- `MSG_{MODULE}_xxx`: Message riêng của module (001-999)
- Không hardcode message text trong code — luôn tham chiếu bằng Message ID
- Message có thể chứa placeholder: `MSG_COM_010 = "{0}件のデータが見つかりました"` → format với số lượng thực tế

### 1.3. Common API Format

Tất cả API trong hệ thống phải tuân theo chung 1 format:

**Response thành công:**

```json
{
  "data": { ... },
  "result": {
    "code": "success",
    "message": null
  }
}
```

**Response thành công (list có phân trang):**

```json
{
  "data": [ ... ],
  "result": {
    "code": "success",
    "total_count": 150,
    "total_pages": 8,
    "current_page": 1
  }
}
```

**Response lỗi:**

```json
{
  "data": null,
  "result": {
    "code": "invalid_parameter",
    "message": "fuel_type must be one of: solid, liquid, gas",
    "errors": [
      { "field": "fuel_type", "message": "Invalid value: 'xyz'" }
    ]
  }
}
```

---

## 2. Thực hành nâng cao (L2)

### 2.1. Common Utilities Design

Khi thiết kế common cho 1 module, cần phân loại rõ Backend vs Frontend:

**Backend Utilities:**

| Utility | Function | Input | Output | Ví dụ |
|---------|----------|-------|--------|-------|
| **date-util** | `format_datetime(dt, fmt)` | datetime, format string | string | `format_datetime(now, "YYYY-MM-DD")` → `"2026-04-08"` |
| | `parse_datetime(s, fmt)` | string, format string | datetime | `parse_datetime("2026/04/08", "YYYY/MM/DD")` |
| | `to_jst(utc_dt)` | UTC datetime | JST datetime | UTC+9 conversion |
| **string-util** | `truncate(s, max_len)` | string, int | string | `truncate("abcdef", 4)` → `"abc..."` |
| | `sanitize_input(s)` | string | string | Remove SQL injection, XSS |
| | `to_half_width(s)` | string | string | Full-width → Half-width (日本語特有) |
| **number-util** | `format_number(n, decimals)` | number, int | string | `format_number(12345.6, 2)` → `"12,345.60"` |
| | `round_half_up(n, decimals)` | number, int | number | Python banker's rounding fix |
| **validation-util** | `validate_required(val, field)` | any, string | Error\|None | |
| | `validate_max_length(val, max)` | string, int | Error\|None | |
| | `validate_in_list(val, choices)` | any, list | Error\|None | |
| **db-access** | `build_where_clause(params)` | dict | SQL + params | Dynamic WHERE builder |
| | `apply_pagination(query, page, size)` | query, int, int | query | Add LIMIT/OFFSET |

**Frontend Utilities:** `date-util` (formatDate, formatDatetime), `validate-util` (isRequired, isMaxLength, isEmail, isNumeric), `data-util` (buildQueryString, downloadFile), `api-util` (handleApiError, withAuth)

### 2.2. Error Code System

**Cấu trúc Error Code:**

```
Format: E{CATEGORY}{MODULE}{SEQUENCE}

Category:
  A = Authentication/Authorization
  V = Validation
  B = Business logic
  S = System/Infrastructure
  D = Data (not found, conflict)

Ví dụ:
  EA_COM_001 = Token expired
  EA_COM_002 = Insufficient permissions
  EV_FUEL_001 = fuel_type invalid
  EV_FUEL_002 = page must be >= 1
  EB_FUEL_001 = Cannot delete fuel in use
  ES_COM_001 = Database connection failed
  ES_COM_002 = External service timeout
  ED_FUEL_001 = Fuel info not found
  ED_FUEL_002 = Data has been updated (exclusive error)
```

**Mapping Error Code → HTTP Status → Message:**

| Error Code | HTTP Status | Message ID | Xử lý Frontend |
|------------|-------------|------------|----------------|
| EA_COM_001 | 401 | - | Redirect login |
| EA_COM_002 | 403 | MSG_COM_002 | Modal error |
| EV_FUEL_001 | 400 | (inline) | Inline error per field |
| EB_FUEL_001 | 409 | MSG_FUEL_006 | Modal error |
| ES_COM_001 | 500 | MSG_COM_001 | Modal error |
| ED_FUEL_001 | 404 | MSG_FUEL_007 | Toast warning |
| ED_FUEL_002 | 409 | MSG_FUEL_004 | Modal + reload |

### 2.3. Logging Strategy

**4 mức log và khi nào dùng:**

| Level | Khi nào | Ví dụ | Lưu ý |
|-------|---------|-------|-------|
| **ERROR** | Lỗi cần điều tra | DB connection fail, unhandled exception | PHẢI có stack trace, PHẢI alert |
| **SECURITY** | Event bảo mật | Login fail, unauthorized access, suspicious input | Không log password/token value |
| **INFO** | Kết quả xử lý bình thường | API called, batch completed, record count | Log chi tiết vừa đủ |
| **DEBUG** | Chi tiết cho developer | SQL query, request/response body, variable values | TẮT trong production |

**JSON Log Format (chuẩn cho dự án Nhật):**

```json
{
  "timestamp": "2026-04-08T10:30:00.123+09:00",
  "level": "INFO",
  "logger": "api.fuel_info",
  "message": "get_fuel_info_list completed",
  "keyword": "FUEL_SEARCH",
  "tenant_code": "TENANT_001",
  "user_id": "user_123",
  "trace_id": "abc-123-def-456",
  "request_id": "req-789",
  "duration_ms": 45,
  "record_count": 150,
  "extra": {
    "search_params": { "fuel_type": "solid" },
    "page": 1,
    "size": 20
  }
}
```

**Keyword cho monitoring:** `FUEL_SEARCH`, `FUEL_DELETE`, `FUEL_EXPORT`, `AUTH_LOGIN`, `AUTH_FAIL`, `BATCH_START`, `BATCH_END`

### 2.4. Exclusive Control (Optimistic Lock)

Trong dự án Nhật, exclusive check (排他制御) là bắt buộc để tránh 2 người cùng sửa 1 record.

**Cơ chế:**
1. Khi GET data → trả về `updated_at` trong response
2. Khi PUT/DELETE → client gửi kèm `updated_at` đã nhận
3. Server so sánh `updated_at` trong request vs DB
4. Nếu khác nhau → trả 409 Conflict + `ED_xxx_002`

```python
# Pseudo code for exclusive check
def update_fuel_info(fuel_id, data, client_updated_at):
    # Step 1: Get current record
    current = db.get("fuel_info", fuel_id)
    if current is None:
        raise NotFoundException("ED_FUEL_001")

    # Step 2: Exclusive check
    if current.updated_at != client_updated_at:
        raise ConflictException("ED_FUEL_002")  # MSG_FUEL_004

    # Step 3: Update with audit columns
    data["updated_at"] = datetime.now()
    data["updated_by"] = login_user.user_id
    db.update("fuel_info", fuel_id, data)
```

---

## 3. Chiến lược & Dẫn dắt (L3)

### 3.1. Shared Library Architecture

Khi thiết kế common cho toàn hệ thống (nhiều module), cần phân tầng rõ ràng:

```
shared/
├── core/                    — Không phụ thuộc framework
│   ├── constants/           — Error codes, message IDs, enums
│   ├── exceptions/          — Custom exception classes
│   ├── utils/               — Pure functions (date, string, number)
│   └── validators/          — Validation rules
├── infrastructure/          — Phụ thuộc framework/library
│   ├── database/            — DB access layer, connection pool
│   ├── cache/               — Redis wrapper
│   ├── logging/             — Log formatter, log config
│   └── http/                — HTTP client wrapper
├── middleware/               — Cross-cutting concerns
│   ├── auth/                — JWT validation, role check
│   ├── error_handler/       — Global error → response mapping
│   ├── request_logger/      — Log request/response
│   └── tenant_filter/       — Multi-tenant WHERE injection
└── frontend-common/          — Frontend shared
    ├── components/          — Atoms, Molecules (design system)
    ├── hooks/               — useAuth, usePagination, useApiCall
    ├── utils/               — date-util, validate-util, data-util
    └── locales/             — i18n files (ja, en)
```

**Nguyên tắc:**
- `core/` không import từ `infrastructure/` (dependency inversion)
- Mỗi module import từ `shared/` — không import từ module khác
- Common化 (chung hóa) không quá mức: chỉ common khi >= 2 module dùng
- Viết unit test cho TOÀN BỘ shared library (coverage >= 90%)

### 3.2. Cross-Module Standards

**Định nghĩa các chuẩn cho toàn hệ thống:**

| Hạng mục | Standard | Áp dụng |
|----------|----------|---------|
| **Date/Time format** | ISO 8601: `2026-04-08T10:30:00+09:00` | API request/response |
| **Date display** | `YYYY/MM/DD` (ja), `DD/MM/YYYY` (vi) | Frontend |
| **Timezone** | Store UTC, display JST (+09:00) | DB và API |
| **Pagination** | page-based (page + size), max size = 100 | Tất cả list API |
| **Soft delete** | `delete_flag: boolean`, không xóa vật lý | Tất cả table |
| **Audit columns** | `created_by, created_at, updated_by, updated_at` | Tất cả table |
| **Multi-tenant** | `tenant_code` trong mỗi table, filter từ login info | Tất cả query |
| **API versioning** | URL path: `/api/v1/...` | Tất cả API |

### 3.3. Common API Patterns

**Pattern 1: Pagination Response**

```json
{
  "data": [...],
  "result": {
    "code": "success",
    "total_count": 150,
    "total_pages": 8,
    "current_page": 1,
    "page_size": 20
  }
}
```

**Pattern 2: Error Response**

```json
{
  "data": null,
  "result": {
    "code": "invalid_parameter",
    "message": "Validation failed",
    "errors": [
      { "field": "fuel_type", "code": "EV_FUEL_001", "message": "Must be: solid, liquid, gas" },
      { "field": "page", "code": "EV_COM_001", "message": "Must be >= 1" }
    ]
  }
}
```

**Pattern 3: Audit Trail**

```sql
-- Mỗi thao tác CUD (Create/Update/Delete) phải ghi nhận:
-- Auto-fill bởi common_db_update utility

INSERT INTO fuel_info (
  fuel_info_id, fuel_name, ...,
  tenant_code,              -- Từ login info
  delete_flag,              -- Default: false
  created_by, created_at,   -- Từ login info + system time
  updated_by, updated_at    -- Từ login info + system time
) VALUES (...);

UPDATE fuel_info SET
  fuel_name = :fuel_name, ...,
  updated_by = :login_user_id,   -- Auto-fill
  updated_at = CURRENT_TIMESTAMP  -- Auto-fill
WHERE fuel_info_id = :id
  AND tenant_code = :login_tenant  -- Multi-tenant filter
  AND delete_flag = false;

-- Soft delete
UPDATE fuel_info SET
  delete_flag = true,
  updated_by = :login_user_id,
  updated_at = CURRENT_TIMESTAMP
WHERE fuel_info_id = :id
  AND tenant_code = :login_tenant;
```

### 3.4. Cross-Module API Design Nâng cao

**API nội bộ vs API hệ thống ngoài:**

| Hạng mục | API nội bộ (internal) | API hệ thống ngoài (external) |
|----------|----------------------|-------------------------------|
| **Auth** | JWT token (internal issuer) | API Key + HMAC signature |
| **Error format** | Chi tiết (field-level errors) | Tổng quát (không expose internal) |
| **Rate limit** | Cao (10,000 req/min) | Thấp (100 req/min per key) |
| **Versioning** | Relaxed (backward compatible) | Strict (v1, v2 song song) |
| **Logging** | Full request/response | Redact sensitive fields |

---

## 4. Tự kiểm tra

### Bài tập: Thiết kế common utility library và error code system cho dự án 5 module

**Đề bài:** Dự án quản lý nhà máy gồm 5 module: fuel (nhiên liệu), emission (khí thải), report (báo cáo), master (dữ liệu chủ), user (quản lý người dùng).

**Yêu cầu:**

1. **Naming Convention Document** — Quy tắc đặt tên: DB, API, Request/Response, Frontend, Message IDs
2. **Error Code System** — Format, danh sách theo category (Auth/Validation/Business/System/Data), mapping → HTTP → Message → Frontend
3. **Common Utility List** — BE (date/string/number/validate/db-access) + FE (date/validate/data/api) với function name, I/O, exception
4. **Logging Strategy** — JSON format, log level, keyword list, rotation/retention policy
5. **Shared Library Structure** — Cấu trúc folder + trách nhiệm từng phần

**Tiêu chí đánh giá:**

| Tiêu chí | L1 | L2 | L3 |
|----------|-----|-----|-----|
| Naming convention | Tuân thủ có sẵn | Nhất quán trong module | Định nghĩa cho toàn hệ thống |
| Error code | Hiểu và dùng error code | Thiết kế cho module | Hệ thống 5 module đầy đủ |
| Utilities | Dùng utility có sẵn | Thiết kế utility cho module | Shared library architecture |
| Logging | Biết 3 loại log | Thiết kế log cho API/Batch | Chiến lược log toàn hệ thống |

---

## 5. Tài liệu tham khảo

| Tài liệu | Nội dung |
|----------|---------|
| SE năng-lực.md #2 (基本設計力) | Tiêu chí thiết kế common API, common màn hình, naming convention, log |
| SE năng-lực.md #2 — "Thiết kế common API" | Standardization, common化, exclusive, date/time format |
| SE năng-lực.md #2 — "Danh sách Xử lý chung" | BE vs FE common utilities, scope common |
| SE năng-lực.md #2 — "Log" | 4 loại log, keyword, JSON format, log level |
| SE năng-lực.md #2 — "Naming convention" | snake_case, kebab-case, camelCase theo context |
| GLN-ENG-TS-01 | Architecture patterns, RTM, component design |
| RUL-ENG-TS-01 Section 2 | Nội dung bắt buộc trong Basic Design |
| RUL-ENG-TS-03 | Tiêu chuẩn lập trình — liên quan đến naming/comment |
| SE test thiết-kế-chi-tiết.md Phần C | Thiết kế xử lý chung common_db_update |
