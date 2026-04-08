# Security & Authentication

> **Mục tiêu:** Nắm vững thiết kế bảo mật và xác thực cho dự án outsourcing Nhật Bản (CMMI Level 3)
> **Level:** L1 -> L2 -> L3
> **Thời gian đọc:** ~30 phút
> **Liên quan:** SE Competency #2 (基本設計力) - "Authentication & Security", CMMI PA: ENG-TS

---

## 1. Khái niệm cơ bản (L1)

### 1.1. JWT Token Flow

JWT (JSON Web Token) là phương thức xác thực phổ biến trong dự án JP:

```
[Client]                              [Server]

1. POST /api/v1/auth/login
   { "email": "user@company.com", "password": "***" }
                    ------>
                                      2. Verify credentials
                                      3. Tạo JWT token
                    <------
   { "access_token": "eyJhbG...", "refresh_token": "eyJhbG...", "expires_in": 3600 }

4. Lưu token (LocalStorage hoặc cookie)

5. GET /api/v1/fuel-infos
   Header: Authorization: Bearer eyJhbG...
                    ------>
                                      6. Verify JWT signature
                                      7. Check token expiry
                                      8. Lấy user info từ payload
                                      9. Check role permission
                                      10. Xử lý business logic
                    <------
   { "data": [...], "result": { "code": "success" } }
```

**Cấu trúc JWT:**

```
Header.Payload.Signature

Header: { "alg": "HS256", "typ": "JWT" }
Payload: {
  "sub": "user_123",              // User ID
  "tenant_code": "company_a",     // Tenant
  "role": "admin",                // Role
  "iat": 1735689600,              // Issued at
  "exp": 1735693200               // Expires at (1 giờ sau)
}
Signature: HMACSHA256(base64(header) + "." + base64(payload), secret_key)
```

**Lưu ý quan trọng:**
- KHÔNG lưu thông tin nhạy cảm trong JWT payload (mật khẩu, số thẻ tín dụng)
- JWT KHÔNG được thay đổi sau khi tạo (stateless)
- access_token ngắn hạn (15 phút - 1 giờ), refresh_token dài hạn (7-30 ngày)

### 1.2. Bearer Token

```
# Mỗi request API đều phải gửi token trong header
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...

# Server kiểm tra:
1. Header có "Authorization" không? -> 401 nếu không
2. Format có đúng "Bearer {token}" không? -> 401 nếu sai
3. JWT signature hợp lệ? -> 401 nếu sai
4. Token hết hạn? -> 401 nếu hết hạn
5. Token đã bị revoke? (kiểm tra blacklist) -> 401 nếu bị revoke
```

### 1.3. Basic RBAC (Role-Based Access Control)

Dự án JP thường có 3 role cơ bản:

| Role | Tiếng Nhật | Quyền |
|------|-----------|-------|
| Admin (管理者) | かんりしゃ | Toàn quyền: CRUD + export + quản lý user |
| Operator (操作者) | そうさしゃ | Xem + tìm kiếm + export (KHÔNG tạo/sửa/xóa) |
| Viewer (閲覧者) | えつらんしゃ | Chỉ xem (KHÔNG export) |

**Áp dụng vào API:**

```
GET  /api/v1/fuel-infos          -> Admin, Operator, Viewer  (tất cả được xem)
GET  /api/v1/fuel-infos/{id}     -> Admin, Operator, Viewer
POST /api/v1/fuel-infos          -> Admin only
PUT  /api/v1/fuel-infos/{id}     -> Admin only
DELETE /api/v1/fuel-infos/{id}   -> Admin only
GET  /api/v1/fuel-infos/export   -> Admin, Operator (Viewer không được export)
```

---

## 2. Thực hành nâng cao (L2)

### 2.1. Permission Matrix Design cho Module

Khi thiết kế cho 1 module, cần tạo Permission Matrix đầy đủ:

**Module: Quản lý thông tin nhiên liệu**

| Chức năng | API | Admin | Operator | Viewer |
|-----------|-----|-------|----------|--------|
| Xem danh sách | GET /fuel-infos | O | O | O |
| Xem chi tiết | GET /fuel-infos/{id} | O | O | O |
| Tìm kiếm | GET /fuel-infos?search | O | O | O |
| Tạo mới | POST /fuel-infos | O | X | X |
| Cập nhật | PUT /fuel-infos/{id} | O | X | X |
| Xóa | DELETE /fuel-infos/{id} | O | X | X |
| Export CSV | GET /fuel-infos/export | O | O | X |
| Import CSV | POST /fuel-infos/import | O | X | X |

(O = có quyền, X = không có quyền)

**Cách implement permission check:**

```python
# Middleware check role
PERMISSION_MAP = {
    ("GET", "/api/v1/fuel-infos"): ["admin", "operator", "viewer"],
    ("POST", "/api/v1/fuel-infos"): ["admin"],
    ("PUT", "/api/v1/fuel-infos/{id}"): ["admin"],
    ("DELETE", "/api/v1/fuel-infos/{id}"): ["admin"],
    ("GET", "/api/v1/fuel-infos/export"): ["admin", "operator"],
}

def check_permission(method, path, user_role):
    allowed_roles = PERMISSION_MAP.get((method, path), [])
    if user_role not in allowed_roles:
        raise ForbiddenError("Access denied")  # HTTP 403
```

### 2.2. Multi-tenant Data Isolation

```
NGUYÊN TẮC VÀNG:
tenant_code LUÔN lấy từ JWT token, KHÔNG BAO GIỜ từ request parameter.

Lý do: Nếu lấy từ request, user có thể gửi tenant_code của công ty khác
và truy cập data trái phép.
```

**Các tầng isolation:**

```
Tầng 1: Application-level (bắt buộc)
  - Mỗi query SELECT đều có WHERE tenant_code = :jwt_tenant
  - Mỗi INSERT đều set tenant_code = :jwt_tenant
  - Middleware tự động inject tenant_code vào mỗi query

Tầng 2: Database-level (khuyến nghị cho L3)
  - Row Level Security (RLS) trong PostgreSQL
  - Tự động filter theo tenant khi truy cập bảng

Tầng 3: Infrastructure-level (cho enterprise)
  - Database riêng cho mỗi tenant
  - Schema riêng cho mỗi tenant
```

```sql
-- PostgreSQL Row Level Security (RLS)
ALTER TABLE fuel_info ENABLE ROW LEVEL SECURITY;

CREATE POLICY tenant_isolation ON fuel_info
    USING (tenant_code = current_setting('app.current_tenant'));

-- Trước mỗi request, set tenant context
SET app.current_tenant = 'company_a';

-- Tự động, mỗi query chỉ thấy data của tenant đó
SELECT * FROM fuel_info;  -- Chỉ trả về data của company_a
```

### 2.3. Input Validation (Chống XSS, SQL Injection)

**SQL Injection Prevention:**

```python
# SAI - Vulnerable to SQL Injection
query = f"SELECT * FROM fuel_info WHERE fuel_name = '{user_input}'"
# Nếu user_input = "'; DROP TABLE fuel_info; --"
# -> SELECT * FROM fuel_info WHERE fuel_name = ''; DROP TABLE fuel_info; --'

# ĐÚNG - Parameterized query
query = "SELECT * FROM fuel_info WHERE fuel_name = :fuel_name"
params = {"fuel_name": user_input}
db.execute(query, params)
```

**XSS Prevention:**

```python
# Server-side: Escape HTML trước khi lưu hoặc trả về
import html

def sanitize_input(value: str) -> str:
    """Escape HTML special characters."""
    return html.escape(value)
    # "<script>alert('xss')</script>"
    # -> "&lt;script&gt;alert('xss')&lt;/script&gt;"

# Client-side (React/Vue): Tự động escape khi render
# React: {userInput} tự động escape
# NGUY HIỂM: dangerouslySetInnerHTML - KHÔNG DÙNG với user input
```

**Validation layers:**

| Tầng | Loại | Ví dụ |
|------|------|-------|
| Client-side | Format, bắt buộc | Email format, trường không được trống |
| Server-side đơn mục | Kiểu, độ dài, range | fuel_name <= 100 ký tự, unit_price > 0 |
| Server-side tương quan | 2+ trường liên quan | end_date > start_date |
| Server-side nghiệp vụ | Business rule | fuel_name không trùng trong cùng tenant |

### 2.4. OWASP Top 10 Cơ bản

| # | Rủi ro | Giải pháp trong dự án |
|---|--------|----------------------|
| A01 | Broken Access Control | RBAC + tenant isolation + permission check mỗi API |
| A02 | Cryptographic Failures | HTTPS bắt buộc, hash password (bcrypt), encrypt sensitive data |
| A03 | Injection | Parameterized queries, ORM, input validation |
| A04 | Insecure Design | Threat modeling trong basic design phase |
| A05 | Security Misconfiguration | Tắt debug mode production, remove default credentials |
| A06 | Vulnerable Components | Cập nhật dependencies thường xuyên, scan CVE |
| A07 | Auth Failures | JWT expiry ngắn, rate limit login, MFA cho admin |
| A08 | Data Integrity Failures | Verify JWT signature, checksum cho file upload |
| A09 | Logging & Monitoring | Log security events, alert trên bất thường |
| A10 | SSRF | Validate URL input, whitelist domain cho API call |

---

## 3. Chiến lược & Dẫn dắt (L3)

### 3.1. Security Architecture

```
                    [Internet]
                        |
                    [WAF / CDN]          -- Web Application Firewall
                        |
                    [Load Balancer]      -- SSL Termination
                        |
              +----+----+----+
              |              |
          [API Gateway]  [Static Files]
              |              |
              |          [CloudFront/S3]
              |
      +-------+-------+
      |               |
  [Auth Service]  [App Services]
      |               |
  [Cognito/        [PostgreSQL]    -- Encryption at rest
   Keycloak]       [Redis]         -- Encryption in transit
```

**Security layers:**
1. **Network:** WAF chống DDoS, IP whitelist cho admin
2. **Transport:** TLS 1.2+ bắt buộc, HSTS header
3. **Application:** JWT auth, RBAC, input validation, rate limiting
4. **Data:** Encryption at rest (AES-256), encryption in transit (TLS)
5. **Monitoring:** Security audit log, anomaly detection

### 3.2. Security Audit Process

```
Quy trình audit bảo mật (theo CMMI):

1. Pre-deployment Review
   - Static code analysis (SonarQube) - không có Critical/Major
   - Dependency scan (OWASP Dependency Check)
   - Secret scan (git-secrets, truffleHog)

2. Design Review
   - Kiểm tra RBAC matrix đầy đủ
   - Kiểm tra multi-tenant isolation
   - Kiểm tra sensitive data handling
   - Kiểm tra error message không expose internal info

3. Penetration Testing (trước go-live)
   - SQL Injection test
   - XSS test
   - Authentication bypass test
   - Authorization escalation test
   - CSRF test

4. Post-deployment Monitoring
   - Security log review hàng tuần
   - Failed login attempts alert
   - Unusual API pattern detection
   - Certificate expiry monitoring
```

### 3.3. Compliance (ISMS)

Dự án JP thường yêu cầu tuân thủ ISMS (Information Security Management System):

| Yêu cầu ISMS | Implementation |
|-------------|----------------|
| Access control policy | RBAC matrix + permission per API |
| Data classification | Phân loại: Public, Internal, Confidential, Secret |
| Audit trail | 4 audit columns + security event log |
| Password policy | Min 8 chars, complexity, expire 90 ngày, không reuse 5 lần |
| Session management | JWT expire 1h, refresh token 7d, concurrent session limit |
| Data retention | Quy định lưu trữ data theo loại (transaction: 7 năm, log: 1 năm) |
| Incident response | Quy trình xử lý sự cố bảo mật (phát hiện -> báo cáo -> xử lý -> review) |

### 3.4. API Security Headers

```python
# Middleware set security headers cho mỗi response
SECURITY_HEADERS = {
    "X-Content-Type-Options": "nosniff",
    "X-Frame-Options": "DENY",
    "X-XSS-Protection": "1; mode=block",
    "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
    "Content-Security-Policy": "default-src 'self'",
    "Cache-Control": "no-store",
    "Pragma": "no-cache",
    "Referrer-Policy": "strict-origin-when-cross-origin",
}

# Rate limiting
RATE_LIMITS = {
    "/api/v1/auth/login": "5 req/min",     # Chống brute force
    "/api/v1/auth/reset-password": "3 req/hour",
    "/api/v1/*": "1000 req/min/user",       # API thông thường
    "/external/v1/*": "100 req/min/apikey",  # API ngoài
}
```

### 3.5. Encryption at Rest / in Transit

```
Encryption in Transit:
- HTTPS (TLS 1.2+) bắt buộc cho mọi API endpoint
- Internal service-to-service: mutual TLS (mTLS)
- Database connection: SSL mode = require

Encryption at Rest:
- Database: PostgreSQL encryption (pgcrypto hoặc AWS RDS encryption)
- File storage: S3 server-side encryption (SSE-S3 hoặc SSE-KMS)
- Backup: Encrypted backup

Sensitive Data Handling:
- Password: bcrypt hash (cost factor >= 12), KHÔNG BAO GIỜ lưu plaintext
- API Key: sha256 hash, chỉ hiển thị lần đầu
- PII (Personal Info): Encrypt column-level hoặc mask khi hiển thị
  VD: email "user@company.com" -> "u***@company.com" trong log
```

---

## 4. Tự kiểm tra

### Câu hỏi lý thuyết

1. **L1:** Mô tả JWT token flow từ login đến gọi API. Token lưu ở đâu phía client?
2. **L1:** Phân biệt 401 Unauthorized và 403 Forbidden. Cho ví dụ cụ thể.
3. **L2:** Tại sao tenant_code phải lấy từ JWT, không từ request? Hậu quả nếu làm sai?
4. **L2:** Parameterized query chống SQL Injection thế nào? Cho ví dụ code SAI và ĐÚNG.
5. **L3:** Hệ thống có 100 tenant, mỗi tenant 50 user. Thiết kế authentication và data isolation thế nào?
6. **L3:** Liệt kê 5 security headers bắt buộc và mục đích của từng header.

### Bài tập thực hành

**Đề bài:** Thiết kế RBAC matrix cho hệ thống ERP với:

**5 roles:**
- System Admin: Quản lý toàn bộ hệ thống, cấu hình, user management
- Company Admin: Quản lý data của công ty mình, gán role cho nhân viên
- Manager: Xem báo cáo, duyệt yêu cầu, quản lý nhóm
- Operator: Nhập liệu, tạo yêu cầu, export
- Viewer: Chỉ xem dữ liệu được cho phép

**3 modules:**
- User Management: CRUD users, gán role, reset password, lock/unlock
- Fuel Management: CRUD nhiên liệu, import/export CSV, xem báo cáo nhiên liệu
- Report: Xem báo cáo, tạo báo cáo, tải báo cáo, xóa báo cáo

**Yêu cầu output:**

1. Tạo Permission Matrix (bảng như mục 2.1)
2. Định nghĩa data scope cho mỗi role:
   - System Admin: xem data tất cả tenant
   - Company Admin: chỉ xem data của tenant mình
   - Các role khác: chỉ xem data thuộc phòng ban mình
3. Thiết kế xử lý khi:
   - User chưa login truy cập API
   - User có role Viewer truy cập POST API
   - User của tenant A truy cập data tenant B
   - Token hết hạn giữa khi đang thao tác
4. Thiết kế security log:
   - Đăng nhập thành công/thất bại
   - Truy cập trái phép (403)
   - Thay đổi quyền

### Tiêu chí đạt

| Level | Tiêu chí |
|-------|---------|
| L1 | Hiểu JWT flow, Bearer token, phân biệt 3 role cơ bản, biết 401 vs 403 |
| L2 | Permission matrix đầy đủ, multi-tenant isolation, input validation (XSS, SQL injection), OWASP cơ bản |
| L3 | Security architecture, audit process, compliance ISMS, encryption at rest/transit, security headers |

---

## 5. Tài liệu tham khảo

- **SE Competency:** nang-luc.md - Nhóm #2: "Authentication & Security"
- **Bài test tham khảo:** thiet-ke-co-ban.md - Role trong đề bài (Admin/Operator/Viewer), Phần B (Common API - authen)
- **CMMI Rule:** RUL-ENG-TS-03 - Section 3: "Bảo mật và An toàn - 100% input phải sanitize"
- **CMMI Guide:** GLN-ENG-TS-01 - Section 8: Cross-cutting Concerns (Security)
- **CMMI Guide:** GLN-ENG-TS-02 - Section 9: Security Considerations
- **CMMI Rule:** RUL-ENG-TS-01 - Section 1.4: "NFR PHẢI quantified"
