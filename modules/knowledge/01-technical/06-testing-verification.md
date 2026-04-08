# Testing & Verification

> **Mục tiêu:** Nắm vững kiểm thử phần mềm từ cơ bản đến thiết kế chiến lược test cho dự án Nhật Bản
> **Level:** L1 -> L2 -> L3
> **Thời gian đọc:** ~35 phút
> **Liên quan:** SE Competency #5 (Quality Mindset), CMMI PA: ENG-VER

---

## 1. Khái niệm cơ bản (L1)

### 1.1. Các cấp độ kiểm thử (Test Levels)

| Cấp độ | Ai thực hiện | Mục tiêu | Môi trường |
|--------|-------------|----------|-----------|
| **Unit Test** | Developer | Kiểm tra từng hàm/class độc lập | Local, mock dependencies |
| **Integration Test** | Developer/QA | Kiểm tra tương tác giữa các module | Staging, real DB |
| **System Test** | QA Team | Kiểm tra toàn bộ hệ thống theo requirement | Staging, production-like |
| **UAT** | Khách hàng/End user | Xác nhận hệ thống đáp ứng nhu cầu | Pre-production |

**V-Model (liên kết testing với từng giai đoạn phát triển):**

```
Requirement Analysis  <--->  UAT (User Acceptance Test)
        |                            |
   Basic Design      <--->  System Test
        |                            |
  Detail Design      <--->  Integration Test
        |                            |
      Coding         <--->  Unit Test
```

### 1.2. Format cơ bản của Test Case

Theo quy định **RUL-ENG-VER-01**, mỗi test case BẮT BUỘC có:

| Mục | Mô tả | Ví dụ |
|-----|-------|-------|
| **Mã test case** | Định danh duy nhất | TC-FUEL-001 |
| **Tên test case** | Mô tả ngắn gọn | Kiểm tra tạo nhiên liệu với dữ liệu hợp lệ |
| **Module/Tính năng** | Thuộc module nào | Fuel Management - Create |
| **Độ ưu tiên** | Cao / Trung bình / Thấp | Cao |
| **Loại kiểm thử** | Chức năng / Phi chức năng / Hồi quy | Chức năng |
| **Điều kiện tiên quyết** | Trạng thái trước khi test | User đã đăng nhập với role Admin |
| **Dữ liệu kiểm thử** | Giá trị cụ thể | fuel_name: "Than đá", fuel_type: "solid" |
| **Các bước** | Từng bước cụ thể | 1. Vào menu Fuel > 2. Click "Tạo mới" > ... |
| **Kết quả mong đợi** | Rõ ràng, đo lường được | Hệ thống hiển thị "Tạo thành công", dữ liệu xuất hiện trong danh sách |
| **Trạng thái** | Đạt / Không đạt / Bị chặn | Đạt |
| **Bằng chứng** | Screenshot/Video | TC-FUEL-001_Pass_2026-04-08.png |

**Ví dụ test case đầy đủ:**

```
TC-FUEL-001: Tạo nhiên liệu mới với dữ liệu hợp lệ

Module: Fuel Management - Create API
Độ ưu tiên: Cao
Loại: Chức năng
Điều kiện tiên quyết: User đã đăng nhập với role Admin, hệ thống ở trạng thái bình thường

Dữ liệu kiểm thử:
  - fuel_name: "Than đá Quảng Ninh"
  - fuel_type: "solid"
  - calorific_value: 5500
  - sulfur_content: 0.8
  - unit_price: 2500000

Các bước:
  1. Truy cập POST /api/v1/fuel-infos
  2. Gửi request body với dữ liệu kiểm thử ở trên
  3. Kiểm tra response

Kết quả mong đợi:
  - HTTP Status: 201 Created
  - Response body có fuel_info_id (UUID)
  - fuel_name = "Than đá Quảng Ninh"
  - created_at có giá trị thời gian hiện tại
  - Kiểm tra database: record mới đã được tạo đúng
```

### 1.3. Nguyên tắc FIRST cho Unit Test

| Nguyên tắc | Yêu cầu | Ví dụ |
|-----------|---------|-------|
| **F**ast | Mỗi test < 1 giây, suite < 5 phút | Mock external API, không gọi network |
| **I**ndependent | Không phụ thuộc thứ tự chạy | Mỗi test có setup/teardown riêng |
| **R**epeatable | Kết quả giống nhau mọi lần | Không dùng Date.now(), dùng mock time |
| **S**elf-validating | Tự động Pass/Fail | Dùng assertions, không cần kiểm tra thủ công |
| **T**imely | Viết test trước hoặc cùng lúc code | TDD: Red -> Green -> Refactor |

---

## 2. Thực hành nâng cao (L2)

### 2.1. Kỹ thuật thiết kế test case

#### 2.1.1. Equivalence Partitioning (Phân vùng tương đương)

Chia dữ liệu đầu vào thành các nhóm tương đương, chỉ cần test 1 giá trị đại diện.

**Ví dụ: Trường "tuổi" (hợp lệ: 1-120):**

| Nhóm | Đại diện | Mong đợi |
|------|---------|---------|
| Hợp lệ | 25, 50, 100 | Accept |
| Không hợp lệ (dưới) | 0, -1, -999 | Reject |
| Không hợp lệ (trên) | 121, 999, 9999 | Reject |
| Không hợp lệ (kiểu khác) | "abc", null, empty, ký tự đặc biệt | Reject |

**Sai lầm thường gặp:** Chỉ test giá trị hợp lệ mà quên test invalid input.

#### 2.1.2. Boundary Value Analysis (Phân tích giá trị biên)

Với mỗi biên, test 3 điểm: `n-1`, `n`, `n+1`

**Ví dụ: Trường "số lượng" (hợp lệ: 1-999):**

| Biên | Giá trị test | Mong đợi |
|------|-------------|---------|
| Biên dưới | 0 | Reject |
| Biên dưới | 1 | Accept |
| Biên dưới | 2 | Accept |
| Biên trên | 998 | Accept |
| Biên trên | 999 | Accept |
| Biên trên | 1000 | Reject |

**Sai lầm thường gặp:** Quên test biên của trường text (ví dụ: tên tối đa 100 ký tự -> test 99, 100, 101 ký tự).

#### 2.1.3. Decision Table (Bảng quyết định)

Áp dụng khi có nhiều điều kiện kết hợp.

**Ví dụ: Tính phí vận chuyển:**

| # | Khách VIP | Đơn > 500k | Nội thành | Phí ship |
|---|-----------|-----------|-----------|----------|
| 1 | Có | Có | Có | Miễn phí |
| 2 | Có | Có | Không | 15,000 |
| 3 | Có | Không | Có | 20,000 |
| 4 | Có | Không | Không | 30,000 |
| 5 | Không | Có | Có | 20,000 |
| 6 | Không | Có | Không | 30,000 |
| 7 | Không | Không | Có | 35,000 |
| 8 | Không | Không | Không | 50,000 |

#### 2.1.4. State Transition (Chuyển đổi trạng thái)

Áp dụng khi chức năng có nhiều trạng thái.

**Ví dụ: Đơn hàng (Order):**

```
  [Mới] ---> [Xác nhận] ---> [Đang giao] ---> [Hoàn thành]
    |                                              |
    +---------> [Hủy] <---------------------------+
```

| Test case | Transition | Kỳ vọng |
|-----------|-----------|---------|
| TC-01 | Mới -> Xác nhận | Thành công |
| TC-02 | Xác nhận -> Đang giao | Thành công |
| TC-03 | Mới -> Hoàn thành | **Bị từ chối** (không thể bỏ qua bước) |
| TC-04 | Hoàn thành -> Mới | **Bị từ chối** (không thể quay lại) |
| TC-05 | Đang giao -> Hủy | Thành công (return policy) |

### 2.2. Mục tiêu Coverage (theo RUL-ENG-VER-03)

| Loại kiểm thử | Đối tượng | Ngưỡng tối thiểu |
|--------------|----------|------------------|
| Unit test | Business logic | >= 80% |
| Unit test | Utility / Helper | >= 60% |
| Integration test | API endpoints | >= 70% |
| System test | Functional (requirement coverage) | >= 95% |
| Mọi cấp độ | Critical paths | **100%** |

**4 loại coverage:**

| Metric | Mô tả | Độ ưu tiên |
|--------|------|-----------|
| **Line Coverage** | % dòng code được execute | Cơ bản |
| **Branch Coverage** | % nhánh logic được test (if/else) | **Quan trọng nhất** |
| **Function Coverage** | % functions được gọi | Trung bình |
| **Statement Coverage** | % statements được execute | Cơ bản |

**Bug density target:** < 10 bugs / KLOC (1000 dòng code)

### 2.3. Quản lý Test Cycle

| Cycle | Mục đích | Nội dung |
|-------|---------|----------|
| **Cycle 1** | Functional test | Chạy toàn bộ test cases lần đầu |
| **Cycle 2** | Bug retest + Regression | Verify bug đã fix + test các chức năng liên quan |
| **Cycle 3** | Final verification | Chạy lại test cases Critical/High + smoke test toàn hệ thống |

**Khi nào cần thêm cycle:** Nếu Cycle 2 phát hiện regression bugs -> cần Cycle 3 hoặc thêm. Thông báo PM nếu effort vượt kế hoạch.

### 2.4. Ví dụ Unit Test (TypeScript)

```typescript
describe('FuelInfoService', () => {
  describe('createFuelInfo', () => {
    // Happy path
    it('should create fuel info when valid data provided', async () => {
      const input = createTestFuelInfo({ fuel_name: 'Than da' });
      const result = await service.create(input);

      expect(result.fuel_info_id).toBeDefined();
      expect(result.fuel_name).toBe('Than da');
    });

    // Boundary value
    it('should accept fuel_name with exactly 100 characters', async () => {
      const input = createTestFuelInfo({ fuel_name: 'A'.repeat(100) });
      const result = await service.create(input);
      expect(result.fuel_name.length).toBe(100);
    });

    it('should reject fuel_name with 101 characters', async () => {
      const input = createTestFuelInfo({ fuel_name: 'A'.repeat(101) });
      await expect(service.create(input))
        .rejects.toThrow(ValidationError);
    });

    // Equivalence partitioning - invalid type
    it('should reject non-string fuel_name', async () => {
      const input = createTestFuelInfo({ fuel_name: null });
      await expect(service.create(input))
        .rejects.toThrow(ValidationError);
    });

    // State transition - duplicate check
    it('should reject duplicate fuel_name in same tenant', async () => {
      await service.create(createTestFuelInfo({ fuel_name: 'Than da' }));
      await expect(service.create(createTestFuelInfo({ fuel_name: 'Than da' })))
        .rejects.toThrow(ConflictError);
    });
  });
});

// Test data factory
const createTestFuelInfo = (overrides = {}) => ({
  fuel_name: 'Test Fuel',
  fuel_type: 'solid',
  calorific_value: 5500,
  sulfur_content: 0.8,
  unit_price: 2500000,
  tenant_code: 'TENANT_01',
  ...overrides,
});
```

---

## 3. Chiến lược & Dẫn dắt (L3)

### 3.1. Thiết kế Test Strategy cho dự án

**Cấu trúc Test Strategy Document:**

1. **Scope:** Chức năng nào test, chức năng nào KHÔNG test
2. **Test Levels:** Unit -> Integration -> System -> UAT
3. **Entry/Exit Criteria** (xem 3.2)
4. **Test Environment:** Staging mirror production
5. **Test Data Strategy:** Cách tạo, quản lý, bảo mật dữ liệu test
6. **Risk-based Testing:** Ưu tiên test theo risk matrix
7. **Automation Strategy:** Ưu tiên automate smoke test và critical path
8. **Defect Management:** Quy trình báo lỗi, SLA
9. **Metrics & Reporting:** Các chỉ số theo dõi

**Risk-based Testing Matrix:**

| | Ảnh hưởng CAO | Ảnh hưởng THẤP |
|---|---|---|
| **Xác suất lỗi CAO** | Test đầy đủ + regression | Test cơ bản + edge cases |
| **Xác suất lỗi THẤP** | Test cơ bản + happy path | Smoke test hoặc exploratory |

### 3.2. Quality Gates (Entry/Exit Criteria)

**Entry Criteria (điều kiện bắt đầu test):**

| Giai đoạn | Điều kiện |
|-----------|----------|
| Unit Test | Code đã compile, coding standard pass |
| Integration Test | Unit test pass (>= 80% coverage) |
| System Test | Build stable trên staging >= 24h, không có blocker từ Integration Test |
| UAT | System test pass, không có bug Critical/High đang mở |

**Exit Criteria (điều kiện kết thúc test):**

| Giai đoạn | Điều kiện |
|-----------|----------|
| Unit Test | Coverage >= 80% business logic, 0 test fail |
| Integration Test | Coverage >= 70% API endpoints, 0 Critical bugs |
| System Test | Coverage >= 95% requirements, 0 Critical/High bugs mở, test report hoàn thành |
| UAT | Khách hàng sign-off, known issues đã được chấp thuận |

### 3.3. Phân tích xu hướng lỗi (Defect Trend Analysis)

**Các metric cần theo dõi:**

| Metric | Công thức | Target | Cảnh báo |
|--------|---------|--------|---------|
| Bug density | Bugs / KLOC | < 10 | > 15 = review process |
| Bug leakage rate | Bugs_UAT / Total_bugs | < 5% | > 10% = test strategy fail |
| Bug reopen rate | Reopened / Total_fixed | < 10% | > 20% = dev quality issue |
| Bug find rate | Bugs_found / Test_day | Stable hoặc giảm | Tăng đột biến = new risk area |
| Bug fix rate | Bugs_fixed / Bugs_found | >= 80% trong sprint | < 60% = resource issue |

**Khi bug leakage rate cao (> 10%):**
1. Phân tích escaped bugs theo category (module nào, loại lỗi nào)
2. Tìm pattern chung (ví dụ: thiếu test negative case)
3. Cập nhật test strategy để cover gap
4. Thêm test case vào regression suite

### 3.4. Root Cause Analysis (RCA) cho Escaped Bugs

Theo **GLN-ENG-VER-04**, áp dụng kỹ thuật 5 Whys:

**Ví dụ: Bug mất dữ liệu đơn hàng trên production:**

| # | Tại sao? | Trả lời | Bằng chứng |
|---|----------|---------|-----------|
| 1 | Tại sao dữ liệu bị mất? | Migration script xóa cột rồi tạo lại | Kiểm tra file migration |
| 2 | Tại sao script xóa cột? | Dev dùng DROP + ADD thay vì ALTER | Review code migration |
| 3 | Tại sao Dev chọn cách DROP? | Không biết ALTER giữ data | Phỏng vấn Dev |
| 4 | Tại sao không phát hiện khi review? | Code review không kiểm tra migration | Kiểm tra PR |
| 5 | **Tại sao review bỏ qua migration?** | **Checklist không có mục migration** | Kiểm tra checklist |

**Hành động phòng ngừa (PHẢI cụ thể):**

| Hành động MƠ HỒ (KHÔNG chấp nhận) | Hành động CỤ THỂ (Chấp nhận) |
|-------------------------------------|-------------------------------|
| "Cẩn thận hơn khi code" | "Thêm mục 'Kiểm tra migration script' vào CHK-ENG-TS-04" |
| "Test kỹ hơn" | "Bổ sung 5 test cases negative test cho module Order: TC-ORD-050 đến 054" |
| "Review code cẩn thận hơn" | "Thêm ESLint rule detect missing input sanitization" |

---

## 4. Tự kiểm tra

### Bài tập 1 (L1): Viết test case cơ bản

Cho API: `POST /api/v1/users/register`

Request body:
```json
{
  "email": "string (bắt buộc, max 255, format email)",
  "password": "string (bắt buộc, 8-50 ký tự, >= 1 uppercase, >= 1 number)",
  "full_name": "string (bắt buộc, max 100)",
  "phone": "string (không bắt buộc, format: 0xxxxxxxxx)"
}
```

Viết 5 test cases theo format chuẩn (TC-REG-001 đến 005), bao gồm:
- 1 happy path
- 2 boundary value (password length, email length)
- 2 negative case (email format sai, password yếu)

### Bài tập 2 (L2): Áp dụng 4 kỹ thuật

Cho cùng API User Registration, áp dụng tất cả 4 kỹ thuật:

**Equivalence Partitioning:** Liệt kê các nhóm tương đương cho từng trường (email, password, full_name, phone).

**Boundary Value Analysis:** Xác định giá trị biên cho password (8 và 50 ký tự) và email (255 ký tự).

**Decision Table:** Tạo bảng quyết định với 4 điều kiện: email hợp lệ, password mạnh, full_name có, phone format đúng.

**State Transition:** Vẽ sơ đồ trạng thái cho user account: Pending -> Active -> Suspended -> Deleted.

**Yêu cầu:** Tối thiểu 15 test cases, tỷ lệ: 30% happy path, 50% negative, 20% boundary.

### Bài tập 3 (L3): Thiết kế Test Strategy

Cho dự án Fuel Management System (6 tháng, team 5 dev + 2 QA):

1. Định nghĩa Entry/Exit Criteria cho 4 cấp độ test
2. Thiết kế Risk-based Testing matrix (xác định 3 module rủi ro cao nhất)
3. Xác định coverage targets cho từng module
4. Lập kế hoạch 3 test cycles với timeline
5. Định nghĩa 5 bug metrics cần theo dõi hàng sprint

---

## 5. Tài liệu tham khảo

### Từ tài liệu nội bộ (CMMI)
- **RUL-ENG-VER-01** -- Quy định Viết Test Case
- **RUL-ENG-VER-03** -- Mục tiêu Bao phủ Kiểm thử
- **RUL-ENG-VER-04** -- Chất lượng Unit Test
- **GLN-ENG-VER-01** -- Hướng dẫn Tổ chức Unit Test
- **GLN-ENG-VER-02** -- Hướng dẫn Quản lý Bug
- **GLN-ENG-VER-03** -- Hướng dẫn Kiểm thử Hệ thống
- **GLN-ENG-VER-04** -- Hướng dẫn Phân tích Nguyên nhân Gốc rễ

### Từ khung năng lực SE
- **Competency #5 (Quality Mindset):** Tính nhất quán, trường hợp ngoại lệ, NFR, self-review
- L1: Tuân thủ template, đúng naming convention
- L2: Kiểm tra nhất quán giữa các tài liệu, xem xét ngoại lệ đầy đủ
- L3: Đảm bảo nhất quán toàn hệ thống, định nghĩa quality gate cho team

### Sách & Tài liệu bên ngoài
- "Software Testing Techniques" -- Boris Beizer
- "Lessons Learned in Software Testing" -- Cem Kaner
- ISTQB Foundation Level Syllabus
- OWASP Testing Guide
