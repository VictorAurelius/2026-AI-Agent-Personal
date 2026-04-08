# Database Design & SQL

> **Mục tiêu:** Nắm vững thiết kế database vật lý cho dự án outsourcing Nhật Bản (CMMI Level 3)
> **Level:** L1 -> L2 -> L3
> **Thời gian đọc:** ~35 phút
> **Liên quan:** SE Competency #2 (基本設計力) - "Database", CMMI PA: ENG-TS

---

## 1. Khái niệm cơ bản (L1)

### 1.1. Thiết kế bảng (Table Design)

Mỗi bảng trong dự án JP PHẢI có đầy đủ: cột nghiệp vụ + audit columns + soft delete.

**Ví dụ bảng fuel_info:**

```sql
CREATE TABLE fuel_info (
    fuel_info_id    UUID         NOT NULL DEFAULT gen_random_uuid(),
    tenant_code     VARCHAR(50)  NOT NULL,
    fuel_name       VARCHAR(100) NOT NULL,
    fuel_type       VARCHAR(20)  NOT NULL,  -- 'solid', 'liquid', 'gas'
    calorific_value DECIMAL(7,2) NOT NULL,
    sulfur_content  DECIMAL(5,3),            -- nullable
    ash_content     DECIMAL(5,3),            -- nullable
    unit_price      INTEGER      NOT NULL,
    supplier_name   VARCHAR(200),
    delete_flag     BOOLEAN      NOT NULL DEFAULT false,
    created_by      VARCHAR(100) NOT NULL,
    created_at      TIMESTAMPTZ  NOT NULL DEFAULT NOW(),
    updated_by      VARCHAR(100) NOT NULL,
    updated_at      TIMESTAMPTZ  NOT NULL DEFAULT NOW(),

    CONSTRAINT pk_fuel_info PRIMARY KEY (fuel_info_id),
    CONSTRAINT fk_fuel_info_tenant FOREIGN KEY (tenant_code)
        REFERENCES tenant(tenant_code)
);
```

### 1.2. Kiểu dữ liệu thường dùng

| Kiểu | Khi nào dùng | Ví dụ |
|------|-------------|-------|
| UUID | Primary key (không dùng serial) | fuel_info_id |
| VARCHAR(n) | Chuỗi có giới hạn | fuel_name VARCHAR(100) |
| TEXT | Chuỗi không giới hạn | description |
| INTEGER | Số nguyên | unit_price |
| DECIMAL(p,s) | Số thập phân chính xác | calorific_value DECIMAL(7,2) |
| BOOLEAN | Có/không | delete_flag |
| TIMESTAMPTZ | Ngày giờ có timezone | created_at |
| DATE | Chỉ ngày | birth_date |
| JSONB | Dữ liệu bán cấu trúc | metadata |

**Tại sao dùng UUID thay vì SERIAL?**
- Không lo trùng khi merge data từ nhiều tenant
- Không lo leak thông tin (từ serial id có thể đoán số lượng records)
- Phù hợp với distributed system

**Tại sao dùng TIMESTAMPTZ thay vì TIMESTAMP?**
- Dự án JP thao tác ở timezone JST (+09:00)
- Server có thể ở UTC
- TIMESTAMPTZ lưu kèm timezone, tránh nhầm lẫn

### 1.3. PK, FK, NOT NULL, Constraints

```sql
-- Primary Key: mỗi bảng PHẢI có PK
CONSTRAINT pk_fuel_info PRIMARY KEY (fuel_info_id)

-- Foreign Key: đảm bảo tham chiếu data integrity
CONSTRAINT fk_fuel_info_tenant FOREIGN KEY (tenant_code)
    REFERENCES tenant(tenant_code)

-- NOT NULL: trường bắt buộc
fuel_name VARCHAR(100) NOT NULL

-- CHECK constraint: ràng buộc giá trị
CONSTRAINT chk_fuel_type CHECK (fuel_type IN ('solid', 'liquid', 'gas'))
CONSTRAINT chk_calorific_positive CHECK (calorific_value > 0)
CONSTRAINT chk_unit_price_positive CHECK (unit_price > 0)
```

### 1.4. Index cơ bản

```sql
-- Index cho cột thường dùng trong WHERE, ORDER BY, JOIN
CREATE INDEX idx_fuel_info_tenant
    ON fuel_info (tenant_code, delete_flag);

-- Index trên các trường tìm kiếm cơ bản
CREATE INDEX idx_fuel_info_name
    ON fuel_info (tenant_code, fuel_name, delete_flag);
```

**Nguyên tắc:** Tạo index cho cột xuất hiện trong WHERE, JOIN, ORDER BY nhiều nhất.
Không tạo index tràn lan vì làm chậm INSERT/UPDATE.

---

## 2. Thực hành nâng cao (L2)

### 2.1. Multi-tenant Isolation (tenant_code)

Mỗi bảng chứa dữ liệu nghiệp vụ PHẢI có cột `tenant_code`:

```sql
-- Mỗi query PHẢI filter theo tenant_code
SELECT * FROM fuel_info
WHERE tenant_code = :login_tenant   -- Lấy từ JWT, KHÔNG từ request
  AND delete_flag = false;

-- Khi INSERT, phải set tenant_code
INSERT INTO fuel_info (fuel_info_id, tenant_code, fuel_name, ...)
VALUES (gen_random_uuid(), :login_tenant, :fuel_name, ...);
```

**QUAN TRỌNG:** tenant_code KHÔNG BAO GIỜ lấy từ request parameter. Luôn lấy từ JWT token của user đăng nhập. Điều này ngăn chặn user truy cập data của tenant khác.

### 2.2. Soft Delete (delete_flag)

```sql
-- Xoá logic: KHÔNG xoá thật, chỉ cập nhật flag
UPDATE fuel_info
SET delete_flag = true,
    updated_by = :current_user,
    updated_at = NOW()
WHERE fuel_info_id = :id
  AND tenant_code = :login_tenant
  AND delete_flag = false;

-- Tất cả query SELECT phải có điều kiện:
WHERE delete_flag = false
```

**Tại sao soft delete?**
- Dự án JP yêu cầu audit trail đầy đủ
- Khả năng phục hồi dữ liệu khi cần
- Liên kết với các bảng khác không bị gãy

### 2.3. Audit Columns

Mỗi bảng PHẢI có 4 cột audit:

| Cột | Kiểu | Mục đích | Khi nào fill |
|-----|------|---------|-------------|
| created_by | VARCHAR(100) | Người tạo | INSERT |
| created_at | TIMESTAMPTZ | Ngày tạo | INSERT (DEFAULT NOW()) |
| updated_by | VARCHAR(100) | Người cập nhật | INSERT và UPDATE |
| updated_at | TIMESTAMPTZ | Ngày cập nhật | INSERT và UPDATE (DEFAULT NOW()) |

```sql
-- Khi INSERT
INSERT INTO fuel_info (..., created_by, created_at, updated_by, updated_at)
VALUES (..., :current_user, NOW(), :current_user, NOW());

-- Khi UPDATE
UPDATE fuel_info
SET fuel_name = :new_name,
    updated_by = :current_user,
    updated_at = NOW()
WHERE fuel_info_id = :id;
```

**Common function (xử lý chung):** Viết hàm common_db_update tự động fill audit columns:

```python
def common_db_update(table_name: str, data: dict, user_info: dict):
    """Auto-fill audit columns trước khi UPDATE."""
    data["updated_by"] = user_info["user_id"]
    data["updated_at"] = datetime.now(timezone.utc)

    # Exclusive check
    current = db.query(f"SELECT updated_at FROM {table_name} WHERE id = :id", data["id"])
    if current.updated_at != data["original_updated_at"]:
        raise OptimisticLockError("Data has been updated by another user")

    db.update(table_name, data)
```

### 2.4. Optimistic Lock (Exclusive Control)

Ngăn chặn 2 người sửa cùng 1 record đồng thời:

```
Luồng xử lý:
1. User A lấy dữ liệu (updated_at = 2026-03-28 10:00:00)
2. User B lấy dữ liệu (updated_at = 2026-03-28 10:00:00)
3. User A gửi UPDATE với updated_at = 2026-03-28 10:00:00
   -> Server so sánh: DB updated_at == request updated_at -> OK, update thành công
   -> DB updated_at thành 2026-03-28 10:05:00
4. User B gửi UPDATE với updated_at = 2026-03-28 10:00:00
   -> Server so sánh: DB updated_at (10:05:00) != request updated_at (10:00:00) -> REJECT
   -> Trả HTTP 409, code: "optimistic_lock_error"
```

```sql
-- Pseudo SQL cho update với optimistic lock
UPDATE fuel_info
SET fuel_name = :new_name,
    updated_by = :current_user,
    updated_at = NOW()
WHERE fuel_info_id = :id
  AND tenant_code = :login_tenant
  AND delete_flag = false
  AND updated_at = :original_updated_at;  -- Exclusive check

-- Kiểm tra số rows affected
-- Nếu 0 rows -> data đã bị người khác update -> raise OptimisticLockError
```

### 2.5. Composite Index và Conditional UNIQUE

```sql
-- Composite index: query filter chính (tenant + delete_flag)
CREATE INDEX idx_fuel_info_tenant
    ON fuel_info (tenant_code, delete_flag);

-- Index cho tìm kiếm (tenant + search column + delete_flag)
CREATE INDEX idx_fuel_info_name
    ON fuel_info (tenant_code, fuel_name, delete_flag);

CREATE INDEX idx_fuel_info_type
    ON fuel_info (tenant_code, fuel_type, delete_flag);

-- Conditional UNIQUE: tên nhiên liệu không trùng TRONG CÙNG tenant (chỉ xét record chưa xoá)
CREATE UNIQUE INDEX uq_fuel_info_name_tenant
    ON fuel_info (tenant_code, fuel_name)
    WHERE delete_flag = false;
```

**Tại sao cần conditional UNIQUE (WHERE delete_flag = false)?**
- Cho phép tạo lại record có cùng tên sau khi đã soft delete
- Nếu không có điều kiện, record đã xoá vẫn chiếm chỗ UNIQUE

### 2.6. Entity Relationships

```
tenant (1) ----< (N) fuel_info
tenant (1) ----< (N) user_role
fuel_info (1) ----< (N) fuel_usage
boiler (1) ----< (N) fuel_usage

Giải thích:
- 1 tenant có nhiều fuel_info
- 1 fuel_info được sử dụng ở nhiều boiler (qua bảng fuel_usage)
- 1 boiler sử dụng nhiều loại fuel (qua bảng fuel_usage)
```

---

## 3. Chiến lược & Dẫn dắt (L3)

### 3.1. Partitioning Strategy

Khi bảng có > 10 triệu records, cần xem xét partitioning:

```sql
-- Range partitioning theo thời gian (cho bảng log, transaction)
CREATE TABLE combustion_log (
    log_id          UUID NOT NULL DEFAULT gen_random_uuid(),
    tenant_code     VARCHAR(50) NOT NULL,
    recorded_at     TIMESTAMPTZ NOT NULL,
    -- ... other columns
) PARTITION BY RANGE (recorded_at);

CREATE TABLE combustion_log_2026_q1
    PARTITION OF combustion_log
    FOR VALUES FROM ('2026-01-01') TO ('2026-04-01');

CREATE TABLE combustion_log_2026_q2
    PARTITION OF combustion_log
    FOR VALUES FROM ('2026-04-01') TO ('2026-07-01');

-- List partitioning theo tenant (khi tenant có data rất lớn)
CREATE TABLE fuel_info_partitioned (
    -- ... columns
) PARTITION BY LIST (tenant_code);
```

### 3.2. Query Optimization

**Kiểm tra execution plan:**

```sql
EXPLAIN ANALYZE
SELECT fuel_info_id, fuel_name, fuel_type, unit_price
FROM fuel_info
WHERE tenant_code = 'company_a'
  AND delete_flag = false
  AND fuel_name LIKE '%than%'
ORDER BY fuel_name ASC
LIMIT 20 OFFSET 0;
```

**Các vấn đề thường gặp:**

| Vấn đề | Nguyên nhân | Giải pháp |
|--------|------------|-----------|
| Seq Scan trên bảng lớn | Thiếu index | Tạo composite index |
| LIKE '%abc%' chậm | Full scan, index không hiệu quả | pg_trgm extension + GIN index |
| COUNT(*) chậm | Scan toàn bảng | Lưu total_count trong cache hoặc bảng riêng |
| JOIN nhiều bảng | Cartesian product | Kiểm tra ON clause, dùng INNER JOIN thay LEFT JOIN khi có thể |
| Offset lớn (OFFSET 10000) | Scan quá nhiều rows | Keyset pagination (WHERE id > last_id) |

**Keyset pagination thay cho OFFSET khi cần performance cao:**

```sql
-- Thay vì: OFFSET 10000 LIMIT 20 (chậm)
-- Dùng: WHERE id > last_seen_id LIMIT 20 (nhanh)

SELECT fuel_info_id, fuel_name, unit_price
FROM fuel_info
WHERE tenant_code = :tenant
  AND delete_flag = false
  AND fuel_info_id > :last_fuel_info_id   -- cursor
ORDER BY fuel_info_id ASC
LIMIT 20;
```

### 3.3. Cross-module Data Consistency

```
Vấn đề: Module A (fuel_info) và Module B (fuel_usage) cùng truy cập.
Khi xoá fuel_info, cần kiểm tra fuel_usage có đang tham chiếu không?

Giải pháp 1: FK constraint (tự động báo lỗi khi xoá)
Giải pháp 2: Application-level check (linh hoạt hơn)

-- Application-level check trước khi soft delete
SELECT COUNT(*) FROM fuel_usage
WHERE fuel_info_id = :id
  AND delete_flag = false;

-- Nếu > 0: trả lời "Cannot delete: fuel is in use by X boilers"
-- Nếu = 0: cho phép soft delete
```

### 3.4. Transaction Handling

```python
# Pattern xử lý transaction trong dự án JP
async def update_fuel_with_usage(fuel_data, usage_data, user_info):
    async with db.transaction():  # BEGIN
        # 1. Update fuel_info
        fuel = await db.query("SELECT * FROM fuel_info WHERE id = :id FOR UPDATE", fuel_data["id"])
        if fuel.updated_at != fuel_data["original_updated_at"]:
            raise OptimisticLockError()

        await db.update("fuel_info", fuel_data)

        # 2. Update fuel_usage (cùng transaction)
        await db.update("fuel_usage", usage_data)

        # Nếu bất kỳ bước nào lỗi -> tự động ROLLBACK
    # COMMIT tự động khi thoát block
```

**Quy tắc transaction:**
- Giữ transaction ngắn nhất có thể (tránh lock lâu)
- SELECT ... FOR UPDATE khi cần exclusive lock cấp row
- KHÔNG gọi API ngoài trong transaction
- Log trước khi commit, log kết quả sau commit

### 3.5. Schema Design cho toàn hệ thống

```
Nguyên tắc:
1. Mỗi bảng có: PK (UUID), tenant_code, delete_flag, 4 audit columns
2. Naming: snake_case, prefix theo domain (fuel_, boiler_, user_)
3. Kiểu dữ liệu nhất quán toàn hệ thống (UUID cho PK, TIMESTAMPTZ cho datetime)
4. Index strategy: composite index (tenant_code, delete_flag, search_columns)
5. UNIQUE constraint: luôn có điều kiện WHERE delete_flag = false
6. FK: chỉ dùng khi 2 bảng cùng module. Cross-module dùng application check.
```

---

## 4. Tự kiểm tra

### Câu hỏi lý thuyết

1. **L1:** Tại sao dùng UUID thay vì SERIAL cho PK? Khi nào dùng TIMESTAMPTZ?
2. **L1:** NOT NULL khác gì với DEFAULT? Cột nào nên NOT NULL, cột nào cho phép NULL?
3. **L2:** Giải thích cách optimistic lock bằng updated_at hoạt động. Khi nào xảy ra conflict?
4. **L2:** Tại sao conditional UNIQUE (WHERE delete_flag = false) cần thiết?
5. **L3:** Khi bảng có 10 triệu records, OFFSET 50000 LIMIT 20 có vấn đề gì? Giải pháp?
6. **L3:** Khi 2 module cùng truy cập 1 bảng, làm sao đảm bảo data consistency?

### Bài tập thực hành

**Đề bài:** Thiết kế schema cho module "Quản lý nhiên liệu" (Fuel Management) với yêu cầu:

1. Thiết kế bảng `fuel_info` với đầy đủ cột (data columns + multi-tenant + soft delete + audit)
2. Thiết kế bảng `fuel_usage` (liên kết fuel_info với boiler)
3. Định nghĩa index strategy (composite index, conditional UNIQUE)
4. Viết SQL cho các thao tác:
   - Tìm kiếm danh sách có phân trang và filter
   - Tạo mới với audit columns
   - Cập nhật với optimistic lock
   - Soft delete với kiểm tra tham chiếu

**Format output:**

```
| Tên cột | Kiểu | Nullable | Default | PK | FK | Mô tả |
```

### Tiêu chí đạt

| Level | Tiêu chí |
|-------|---------|
| L1 | Đúng kiểu dữ liệu, đủ PK/FK, hiểu NOT NULL và constraints cơ bản |
| L2 | Có tenant_code, delete_flag, 4 audit columns, composite index, conditional UNIQUE, optimistic lock |
| L3 | Partitioning strategy, keyset pagination, cross-module consistency, transaction handling |

---

## 5. Tài liệu tham khảo

- **SE Competency:** nang-luc.md - Nhóm #2 (基本設計力): "Database" - thiết kế bảng vật lý
- **Bài test tham khảo:** thiet-ke-co-ban.md - Phần A (DB Schema), Phần B (Common API - audit, exclusive)
- **Bài test tham khảo:** thiet-ke-chi-tiet.md - Phần A, Mục 5 (Thao tác DB - pseudo SQL)
- **CMMI Rule:** RUL-ENG-TS-01 - Section 3.4: "Database Schema PHẢI có column types, constraints, indexes"
- **CMMI Guide:** GLN-ENG-TS-02 - Section 3: Data Structures
