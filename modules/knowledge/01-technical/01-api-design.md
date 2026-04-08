# RESTful API Design

> **Mục tiêu:** Nắm vững thiết kế API theo chuẩn RESTful cho dự án outsourcing Nhật Bản (CMMI Level 3)
> **Level:** L1 -> L2 -> L3
> **Thời gian đọc:** ~30 phút
> **Liên quan:** SE Competency #2 (基本設計力), #3 (詳細設計力), CMMI PA: ENG-TS

---

## 1. Khái niệm cơ bản (L1)

### 1.1. HTTP Methods

| Method | Mục đích | Idempotent | Safe | Ví dụ |
|--------|----------|------------|------|-------|
| GET | Lấy dữ liệu | Có | Có | `GET /api/v1/fuel-infos` |
| POST | Tạo mới resource | Không | Không | `POST /api/v1/fuel-infos` |
| PUT | Cập nhật toàn bộ | Có | Không | `PUT /api/v1/fuel-infos/{id}` |
| PATCH | Cập nhật một phần | Không | Không | `PATCH /api/v1/fuel-infos/{id}` |
| DELETE | Xoá resource | Có | Không | `DELETE /api/v1/fuel-infos/{id}` |

**Lưu ý quan trọng:**
- GET không được thay đổi dữ liệu phía server
- PUT gửi toàn bộ object, PATCH chỉ gửi fields cần thay đổi
- DELETE trong dự án Nhật thường là soft delete (cập nhật delete_flag)

### 1.2. HTTP Status Codes

| Code | Ý nghĩa | Khi nào dùng |
|------|---------|--------------|
| 200 | OK | GET thành công, PUT/PATCH thành công |
| 201 | Created | POST tạo mới thành công |
| 204 | No Content | DELETE thành công |
| 400 | Bad Request | Validation lỗi (sai kiểu, thiếu trường bắt buộc) |
| 401 | Unauthorized | Token hết hạn hoặc không có |
| 403 | Forbidden | Không có quyền truy cập |
| 404 | Not Found | Resource không tồn tại |
| 409 | Conflict | Exclusive error (optimistic lock), duplicate data |
| 500 | Internal Server Error | Lỗi hệ thống |

**Lưu ý:** Khi danh sách trả về 0 kết quả -> vẫn trả HTTP 200 với `data: []`, KHÔNG phải 404.

### 1.3. URL Conventions

**Quy tắc naming:**
- Dùng **kebab-case** cho URL path: `/api/v1/fuel-infos` (KHÔNG phải `/api/v1/fuelInfos`)
- Dùng **danh từ số nhiều** cho resource: `/users`, `/fuel-infos`
- Dùng **snake_case** cho query parameters: `?fuel_name=abc&sort_by=name`
- Versioning trong URL: `/api/v1/...`

```
# Đúng
GET  /api/v1/fuel-infos
GET  /api/v1/fuel-infos/{fuel_info_id}
POST /api/v1/fuel-infos
PUT  /api/v1/fuel-infos/{fuel_info_id}

# Sai
GET  /api/v1/getFuelInfoList        # Không dùng động từ
GET  /api/v1/fuel_info              # Không dùng underscore trong path
GET  /api/v1/FuelInfo               # Không dùng PascalCase
```

### 1.4. Request/Response Common Format

Mọi response trong dự án PHẢI tuân theo format chung:

```json
// Response thành công (GET list)
{
  "data": [
    {
      "fuel_info_id": "550e8400-e29b-41d4-a716-446655440000",
      "fuel_name": "Than đá A",
      "fuel_type": "solid",
      "unit_price": 15000
    }
  ],
  "result": {
    "code": "success",
    "message": null,
    "total_count": 150,
    "total_pages": 8,
    "current_page": 1
  }
}

// Response lỗi
{
  "data": null,
  "result": {
    "code": "invalid_parameter",
    "message": "fuel_name is required"
  }
}
```

---

## 2. Thực hành nâng cao (L2)

### 2.1. Thiết kế API List cho 1 Module

Khi nhận module "Quản lý thông tin nhiên liệu", cần liệt kê ĐẦY ĐỦ các API:

| No | Resource | Tên API | Quyền | Endpoint | Method | Tổng quan |
|----|----------|---------|-------|----------|--------|-----------|
| 1 | auth | get_login_user_info | All | /api/v1/auth/me | GET | Lấy thông tin user đăng nhập (role, tenant) |
| 2 | fuel_info | get_fuel_info_list | Admin, Operator, Viewer | /api/v1/fuel-infos | GET | Danh sách + phân trang + tìm kiếm |
| 3 | fuel_info | get_fuel_info | Admin, Operator, Viewer | /api/v1/fuel-infos/{fuel_info_id} | GET | Chi tiết 1 nhiên liệu |
| 4 | fuel_info | create_fuel_info | Admin | /api/v1/fuel-infos | POST | Đăng ký nhiên liệu mới |
| 5 | fuel_info | update_fuel_info | Admin | /api/v1/fuel-infos/{fuel_info_id} | PUT | Cập nhật thông tin |
| 6 | fuel_info | delete_fuel_info | Admin | /api/v1/fuel-infos/{fuel_info_id} | DELETE | Xoá logic (soft delete) |
| 7 | fuel_info | export_fuel_info_csv | Admin, Operator | /api/v1/fuel-infos/export | GET | Export CSV theo điều kiện |

**Checklist khi liệt kê API:**
- [ ] Đủ CRUD (Create, Read list, Read detail, Update, Delete)?
- [ ] Có API action đặc biệt (export, import, approve)?
- [ ] Có API internal (hệ thống gọi nhau, không expose ra ngoài)?
- [ ] Quyền hạn đúng theo role requirement?

### 2.2. Pagination Pattern

```
GET /api/v1/fuel-infos?page=1&size=20&sort_by=fuel_name&sort_order=asc

Query Parameters:
- page: integer >= 1 (default: 1)
- size: integer 1-100 (default: 20)
- sort_by: IN ('fuel_name', 'unit_price', 'calorific_value')
- sort_order: IN ('asc', 'desc'), default: 'asc'
```

**Response pagination info:**

```json
{
  "result": {
    "code": "success",
    "total_count": 150,
    "total_pages": 8,
    "current_page": 1
  }
}
```

**SQL tương ứng:**

```sql
SELECT fuel_info_id, fuel_name, fuel_type, unit_price
FROM fuel_info
WHERE tenant_code = :login_tenant   -- Từ login info, KHÔNG từ request
  AND delete_flag = false
ORDER BY fuel_name ASC
LIMIT 20 OFFSET 0;

-- Count riêng cho total_count
SELECT COUNT(*) FROM fuel_info
WHERE tenant_code = :login_tenant AND delete_flag = false;
```

### 2.3. Error Code Design

| HTTP Status | Error Code | Điều kiện | Message |
|-------------|------------|-----------|---------|
| 400 | invalid_parameter | Validation lỗi | "{field} is invalid" |
| 400 | missing_required | Thiếu trường bắt buộc | "{field} is required" |
| 401 | unauthorized | Token không hợp lệ | "Authentication required" |
| 403 | forbidden | Không đủ quyền | "Access denied" |
| 404 | not_found | Resource không tồn tại | "{resource} not found" |
| 409 | conflict | Trùng dữ liệu | "{field} already exists" |
| 409 | optimistic_lock_error | Exclusive check fail | "Data has been updated by another user" |
| 500 | internal_error | Lỗi hệ thống | "Internal server error" |

### 2.4. Authentication Bearer JWT

```
Request Header:
Authorization: Bearer eyJhbGciOiJIUzI1NiIs...

JWT Payload chứa:
{
  "sub": "user_id_123",
  "tenant_code": "company_a",
  "role": "admin",
  "exp": 1735689600
}
```

**Flow xử lý mỗi request:**

```
1. Client gửi request với header: Authorization: Bearer {token}
2. Server verify JWT signature
3. Server kiểm tra token hết hạn chưa (exp)
4. Server lấy tenant_code, role từ token payload
5. Server kiểm tra role có quyền gọi API này không
6. Nếu OK -> xử lý business logic
7. Nếu fail -> trả 401 (token) hoặc 403 (role)
```

### 2.5. Versioning

```
# URL versioning (phổ biến nhất trong dự án JP)
/api/v1/fuel-infos
/api/v2/fuel-infos

# Khi nào tăng version?
- Thay đổi breaking: đổi kiểu dữ liệu response, xoá field
- KHÔNG tăng version khi: thêm field mới vào response, thêm API mới
```

---

## 3. Chiến lược & Dẫn dắt (L3)

### 3.1. Chiến lược API toàn hệ thống

**Phân chia module (DDD/Feature-based):**

```
/api/v1/fuel-infos/...       # Module Quản lý nhiên liệu
/api/v1/boilers/...          # Module Quản lý nồi hơi
/api/v1/combustion-logs/...  # Module Nhật ký đốt
/api/v1/reports/...          # Module Báo cáo
/api/v1/users/...            # Module Quản lý người dùng
/api/v1/auth/...             # Module Xác thực (common)
```

**Phân biệt API nội bộ vs API hệ thống ngoài:**

| Tiêu chí | API nội bộ (FE -> BE) | API hệ thống ngoài |
|----------|----------------------|-------------------|
| Xác thực | JWT Bearer Token | API Key + IP whitelist |
| Error format | Common format (data + result) | Theo spec của hệ thống ngoài |
| Rate limit | Cao (1000 req/min) | Thấp (100 req/min) |
| Timeout | 3-5 giây | 10-30 giây |
| Versioning | /api/v1/ | /external/v1/ |

### 3.2. Non-Functional Requirements (NFR)

| NFR | Mục tiêu | Biện pháp |
|-----|---------|-----------|
| Response time | Bình thường <= 3s, cao điểm <= 5s | Index DB, caching, server-side pagination |
| Rate limiting | 1000 req/min/user | API Gateway rate limiter |
| Payload limit | Request body <= 1MB | Middleware check Content-Length |
| Concurrent users | 50 user/tenant, 100 tenant | Connection pooling, horizontal scaling |
| CSV export | <= 10,000 records | Nếu vượt -> batch async |
| Timeout | API: 30s, Batch: tuỳ cấu hình | Circuit breaker pattern |

### 3.3. Đảm bảo tính nhất quán cross-module

**Naming convention thống nhất:**

| Thành phần | Convention | Ví dụ |
|-----------|------------|-------|
| URL path | kebab-case | /fuel-infos |
| Query param | snake_case | fuel_name, sort_by |
| Request/Response body | snake_case | fuel_info_id |
| DB column | snake_case | tenant_code |
| Frontend JS variable | camelCase | fuelInfoId |
| Date/Time format | ISO 8601 | 2026-03-28T10:00:00+09:00 |

**Common API design bắt buộc:**
1. Tất cả API đều trả response format chung (data + result)
2. Error code naming nhất quán toàn hệ thống
3. Audit columns tự động fill: created_by, created_at, updated_by, updated_at
4. Multi-tenant filter: tenant_code lấy từ JWT, KHÔNG từ request param
5. Optimistic lock: so sánh updated_at trước khi update

### 3.4. API Security Headers

```
# Response headers bắt buộc
Content-Type: application/json; charset=utf-8
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
X-XSS-Protection: 1; mode=block
Strict-Transport-Security: max-age=31536000; includeSubDomains
Cache-Control: no-store
```

---

## 4. Tự kiểm tra

### Câu hỏi lý thuyết

1. **L1:** Phân biệt PUT và PATCH? Khi nào dùng GET, khi nào dùng POST?
2. **L1:** Tại sao danh sách trả về 0 kết quả là HTTP 200 chứ không phải 404?
3. **L2:** Giải thích optimistic lock bằng updated_at hoạt động thế nào?
4. **L2:** Tại sao tenant_code phải lấy từ JWT token chứ không từ request param?
5. **L3:** Khi CSV export 10,000 records có thể timeout, bạn thiết kế giải pháp thế nào?
6. **L3:** Làm thế nào đảm bảo naming convention nhất quán giữa 5 module do 5 team khác nhau làm?

### Bài tập thực hành

**Đề bài:** Thiết kế API list cho module "Quản lý người dùng" (User Management) với:
- CRUD người dùng
- Tìm kiếm theo tên, email, role
- Phân trang, sắp xếp
- Gán role cho người dùng
- Reset mật khẩu
- Multi-tenant
- 3 roles: Admin (toàn quyền), Manager (xem + sửa), Viewer (chỉ xem)

**Yêu cầu:**
1. Liệt kê API theo bảng: No | Resource | Tên API | Quyền | Endpoint | Method | Tổng quan
2. Viết response format cho API lấy danh sách users
3. Thiết kế error codes cho module này
4. Xem xét: Reset mật khẩu nên là API đồng bộ hay gửi email bất đồng bộ?

### Tiêu chí đạt

| Level | Tiêu chí |
|-------|---------|
| L1 | Liệt kê đúng CRUD API, endpoint đúng RESTful, hiểu HTTP methods/status codes |
| L2 | Đủ các API (CRUD + action + internal), có pagination, error codes đầy đủ, có auth design |
| L3 | Phân chia module rõ ràng, có NFR (rate limit, timeout), phân biệt API nội bộ vs ngoài, naming nhất quán |

---

## 5. Tài liệu tham khảo

- **SE Competency:** nang-luc.md - Nhóm #2 (基本設計力): "Danh sách API", "Thiết kế common API"
- **Bài test tham khảo:** thiet-ke-co-ban.md - Phần A (Danh sách API), Phần B (Common design)
- **CMMI Guide:** GLN-ENG-TS-01 - Basic Design Documentation Guide
- **CMMI Rule:** RUL-ENG-TS-01 - Design Standard Rule (Section 2.3: Interface Design)
- **CMMI Guide:** GLN-ENG-TS-02 - Detail Design Documentation Guide (Section 6: API Contracts)
