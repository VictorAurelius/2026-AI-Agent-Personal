# Code Review & Quality Standards

> **Mục tiêu:** Nắm vững quy trình code review, tiêu chuẩn chất lượng, và cách dẫn dắt văn hóa review trong dự án Nhật Bản
> **Level:** L1 -> L2 -> L3
> **Thời gian đọc:** ~30 phút
> **Liên quan:** SE Competency #5 (Quality Mindset), CMMI PA: ENG-TS, ENG-VER

---

## 1. Khái niệm cơ bản (L1)

### 1.1. Coding Standards -- Ngưỡng bắt buộc (RUL-ENG-TS-03)

| Chỉ số | Ngưỡng | Mô tả |
|--------|--------|-------|
| **Độ phức tạp vòng (Cyclomatic complexity)** | <= 10 | Nếu vượt quá, BẮT BUỘC phân tách thành hàm con |
| **Độ dài hàm** | <= 50 dòng | Không tính comment/dòng trống |
| **Độ dài lớp (class)** | <= 500 dòng | Quá lớn -> tách class |
| **Tỷ lệ bình luận** | >= 10% | Phải giải thích logic nghiệp vụ, KHÔNG mô tả cú pháp |
| **Số tham số hàm** | <= 4 | Quá nhiều -> dùng object/DTO |
| **Độ lồng (nesting depth)** | <= 3 cấp | if/for/while lồng > 3 cấp -> refactor |

**Ví dụ vi phạm và cách sửa:**

```python
# XAU - Cyclomatic complexity = 12, nesting = 4
def process_order(order, user, config):
    if order is not None:
        if order.is_valid():
            if user.is_active:
                if config.allow_discount:
                    if order.total > 500000:
                        discount = 0.1
                    else:
                        discount = 0.05
                else:
                    discount = 0
                # ... xu ly tiep
            else:
                raise ValueError("User inactive")
        else:
            raise ValueError("Invalid order")
    else:
        raise ValueError("Order is None")

# TOT - Dung early return, tach ham
def process_order(order, user, config):
    validate_order_input(order, user)
    discount = calculate_discount(order, config)
    return apply_order(order, discount)

def validate_order_input(order, user):
    if order is None:
        raise ValueError("Order is None")
    if not order.is_valid():
        raise ValueError("Invalid order")
    if not user.is_active:
        raise ValueError("User inactive")

def calculate_discount(order, config):
    if not config.allow_discount:
        return 0
    return 0.1 if order.total > 500000 else 0.05
```

### 1.2. Review Checklist cơ bản

Khi review code, kiểm tra theo 7 khía cạnh (theo GLN-ENG-TS-03):

**1. Functionality (Chức năng):**
- Code làm đúng việc được yêu cầu?
- Edge cases đã xử lý? (null, empty, giá trị âm, giá trị cực lớn)
- Happy path và error path đều hoạt động?

**2. Design (Thiết kế):**
- Tuân thủ SOLID?
  - **S**: Mỗi class/function chỉ làm 1 việc
  - **O**: Mở rộng bằng cách thêm mới, không sửa code cũ
  - **L**: Class con thay thế được class cha
  - **I**: Interface nhỏ, chuyên biệt
  - **D**: Phụ thuộc vào abstraction, không phụ thuộc implementation
- Vi phạm DRY (code lặp lại)?
- Vi phạm KISS (giải pháp phức tạp quá mức)?

**3. Naming (Đặt tên):**

| Tên xấu | Tên tốt | Lý do |
|---------|---------|-------|
| `d` | `elapsedDays` | Mô tả rõ giá trị |
| `process()` | `calculateMonthlyRevenue()` | Cụ thể mục đích |
| `data` | `userProfiles` | Cho biết nội dung |
| `flag` | `isEmailVerified` | Cho biết ý nghĩa boolean |
| `temp` | `sortedUserList` | Cho biết vai trò biến |

**4. Security (Bảo mật):**
- SQL injection: Dùng parameterized queries?
- XSS: Output được escape/sanitize?
- Hardcoded credentials: TUYỆT ĐỐI KHÔNG có password/API key trong code?
- Input validation: Tất cả đầu vào từ user được validate?

**5. Performance (Hiệu năng):**
- N+1 queries?
- Missing pagination?
- Blocking operations trên main thread?

**6. Testing:**
- Có unit test cho code mới?
- Coverage >= 80%?
- Test cover happy path + error cases + edge cases?

**7. Complexity:**
- Hàm dài hơn 50 dòng?
- Nesting > 3 cấp?
- Cyclomatic complexity > 10?

### 1.3. Công cụ Phân tích Tĩnh (BẮT BUỘC theo RUL-ENG-TS-03)

100% code PHẢI đi qua công cụ phân tích tĩnh TRƯỚC khi yêu cầu code review:

| Ngôn ngữ | Công cụ | Lưu ý |
|----------|--------|-------|
| TypeScript/JS | ESLint + Prettier | Bắt buộc trong CI/CD |
| Python | Pylint + Black + MyPy | Type checking với MyPy |
| Java | Checkstyle + SpotBugs | Tích hợp SonarQube |
| C# | StyleCop + Roslyn Analyzers | Tích hợp vào .csproj |
| Tất cả | SonarQube | Server-side analysis |

**KHÔNG ĐƯỢC có lỗi mức "Critical" hoặc "Major" từ công cụ phân tích tĩnh.**

---

## 2. Thực hành nâng cao (L2)

### 2.1. Quy trình Review hiệu quả (RUL-ENG-TS-04)

**Giới hạn hiệu suất:**

| Quy định | Ngưỡng | Lý do |
|----------|--------|-------|
| Tốc độ review | **<= 200 dòng/giờ** | Vượt quá -> chất lượng review bị nghi ngờ |
| Thời lượng liên tục | **<= 60 phút** | Phải nghỉ >= 10 phút trước khi tiếp |
| Kích thước PR tối đa | **<= 400 dòng** | Vượt -> BẮT BUỘC chia nhỏ |
| Thời gian phản hồi | **<= 2 giờ làm việc** | Author phản hồi comment của reviewer |
| Review lại | **<= 2 giờ làm việc** | Reviewer review lại sau khi author sửa |

**Kích thước PR và chất lượng review:**

| Kích thước PR | Thời gian review | Chất lượng | Khuyến nghị |
|---------------|-----------------|------------|-------------|
| < 200 dòng | 15-30 phút | Cao | Lý tưởng |
| 200-400 dòng | 30-60 phút | Tốt | Chấp nhận |
| 400-800 dòng | 1-2 giờ | Trung bình | Cân nhắc chia nhỏ |
| > 800 dòng | > 2 giờ | Thấp | **PHẢI chia nhỏ** |

**Cách chia nhỏ PR:**
- Tách theo layer: database migration -> backend API -> frontend UI
- Tách theo tính năng con: authentication -> authorization -> session
- Tách refactor riêng: PR refactor trước, PR tính năng sau
- Tách config/dependency ra PR riêng

### 2.2. Review Density Metrics

| Metric | Công thức | Target | Ý nghĩa |
|--------|---------|--------|---------|
| Review density | Issues_found / KLOC | 3-7 | Quá thấp = review qua loa, quá cao = code quality kém |
| False positive rate | False_issues / Total_issues | < 10% | Reviewer phát hiện "lỗi" không phải lỗi |
| Review effectiveness | Bugs_found_review / Total_bugs | >= 60% | % bugs được phát hiện qua review (không phải testing) |
| Review turnaround | Time_submit_to_approve | < 1 ngày | Thời gian từ tạo PR đến được approve |

**Khi review density < 3 issues/KLOC:**
- Reviewer có thể review quá nhanh (> 200 LOC/giờ)
- Code có thể quá đơn giản (không cần review sâu)
- Cần kiểm tra lại chất lượng review

**Khi review density > 7 issues/KLOC:**
- Code quality kém -> cần training cho developer
- Coding standard không rõ ràng -> cập nhật RUL-ENG-TS-03
- Developer mới chưa quen quy trình -> cần mentor

### 2.3. Thu thập Bằng chứng (Evidence) -- BẮT BUỘC

Theo **RUL-ENG-TS-04 Mục 2.5**, PR KHÔNG CÓ bằng chứng sẽ bị TỪ CHỐI:

| Loại thay đổi | Bằng chứng bắt buộc |
|---------------|-------------------|
| Code mới/sửa đổi | Screenshot kết quả test + Coverage report |
| UI changes | Screenshot trước/sau |
| Database migration | Screenshot schema change + test data |
| Bug fix | Screenshot lỗi trước + sau khi fix |
| Performance | Benchmark trước/sau |

**PR Description BẮT BUỘC có các mục (RUL-ENG-TS-04 Mục 5):**

```markdown
## Tóm tắt
[Mô tả ngắn gọn 2-3 câu]

## Tham chiếu Nhiệm vụ
- Redmine/Jira: #ISSUE-123
- Loại: Feature / Bugfix / Refactor / Hotfix

## Các thay đổi chính
### What (Thay đổi gì)
- [Thay đổi 1]: [Mô tả]

### Why (Tại sao)
- [Lý do, bối cảnh nghiệp vụ]

## Bằng chứng Kiểm thử
- Coverage: XX%
- Unit test: Đạt
- Ảnh chụp: [đính kèm]

## Danh mục Kiểm tra
- [ ] Self-review đã thực hiện
- [ ] Unit test đã viết và đạt
- [ ] Không có hardcoded credentials
- [ ] Đã xử lý edge cases
```

### 2.4. Definition of Done (DoD)

Một task/story chỉ được coi là HOÀN THÀNH khi đạt TẤT CẢ tiêu chí:

| # | Tiêu chí | Kiểm tra bởi |
|---|---------|-------------|
| 1 | Code đã viết và compile thành công | Developer |
| 2 | Unit test đã viết (>= 80% coverage cho code mới) | Developer |
| 3 | Phân tích tĩnh pass (0 Critical/Major) | CI/CD |
| 4 | Code review được approve (>= 1 reviewer) | Reviewer/TL |
| 5 | 0 thảo luận chưa giải quyết trên PR | Developer + Reviewer |
| 6 | CI/CD pipeline pass (build, test, lint, security) | CI/CD |
| 7 | Bằng chứng test đính kèm | Developer |
| 8 | Acceptance criteria được verify | QA/PO |

### 2.5. Cách đưa feedback hiệu quả

**Phân loại mức độ feedback:**

| Prefix | Ý nghĩa | Ví dụ |
|--------|---------|-------|
| `[MUST]` | Bắt buộc sửa | `[MUST] SQL injection: dùng parameterized query` |
| `[SHOULD]` | Nên sửa | `[SHOULD] Function này nên tách thành 2 hàm nhỏ hơn` |
| `[NIT]` | Nit-pick, không bắt buộc | `[NIT] Có thể dùng const thay vì let ở đây` |
| `[QUESTION]` | Câu hỏi, cần giải thích | `[QUESTION] Tại sao chọn approach này thay vì dùng cache?` |

**Feedback tốt vs xấu:**

| Feedback XẤU | Feedback TỐT |
|-------------|-------------|
| "Code này xấu" | "[MUST] Hàm processOrder có cyclomatic complexity = 15, vượt ngưỡng 10. Đề nghị tách thành 3 hàm: validateOrder, calculateDiscount, applyOrder" |
| "Sai rồi" | "[MUST] Thiếu check tenant_code trong WHERE clause -> vi phạm multi-tenant security. Thêm AND tenant_code = :tenant_code" |
| "Không hiểu" | "[QUESTION] Logic ở dòng 45-52: Tại sao cần gọi API 2 lần? Có thể batch thành 1 call được không?" |

---

## 3. Chiến lược & Dẫn dắt (L3)

### 3.1. Định nghĩa Quality Gates cho team

| Gate | Tiêu chí | Người phê duyệt | Tool |
|------|---------|-----------------|------|
| **Gate 1: Pre-commit** | Lint pass, format pass | Developer (tự động) | ESLint, Prettier |
| **Gate 2: Pre-review** | Unit test pass, coverage >= 80%, phân tích tĩnh 0 Critical | CI/CD (tự động) | Jest, SonarQube |
| **Gate 3: Code Review** | Review approve, 0 thảo luận chưa giải quyết | Reviewer (thủ công) | GitLab/GitHub |
| **Gate 4: Integration** | Integration test pass, API contract verified | CI/CD + QA | Postman, CI |
| **Gate 5: Pre-release** | System test pass, 0 Critical/High bugs, coverage >= 95% | QA Lead + PM | Test report |
| **Gate 6: Production** | Smoke test pass, monitoring OK, rollback plan ready | TL + PM | Monitoring |

### 3.2. Xây dựng văn hóa Review

**Nguyên tắc dẫn dắt:**
1. **Review là học hỏi, không phải phê phán** -- Tạo môi trường an toàn để team sẵn sàng nhận feedback
2. **Lead by example** -- Senior/TL review trước, để junior quan sát cách review
3. **Pair review cho người mới** -- Ghép junior + senior cùng review 1 PR
4. **Celebrate good code** -- Nhận xét tích cực khi thấy code tốt, không chỉ chỉ ra lỗi
5. **Review là trách nhiệm chung** -- Reviewer cũng chịu trách nhiệm về chất lượng code được merge

**Chương trình mentor review:**

| Tuần | Hoạt động | Mục tiêu |
|------|---------|---------|
| 1-2 | Junior quan sát Senior review | Hiểu quy trình, học cách đọc code |
| 3-4 | Junior review với Senior guide | Bắt đầu tự phát hiện lỗi cơ bản |
| 5-6 | Junior review độc lập, Senior kiểm tra | Tự tin review, giảm false positive |
| 7-8 | Junior review + mentor người mới hơn | Củng cố kiến thức, nhận trách nhiệm |

### 3.3. Design Review Checklists (theo loại artifact)

**Architecture Review (CHK-ENG-TS-01):**

| # | Kiểm tra | Lý do |
|---|---------|-------|
| 1 | Architecture pattern phù hợp với requirements? | Tránh over-engineering hoặc under-engineering |
| 2 | Components đủ để cover 100% requirements? | Không miss requirement |
| 3 | Không có Single Point of Failure (SPOF)? | Reliability |
| 4 | Scale được khi load tăng 10x? | Scalability |
| 5 | Data flow không có lỗ hổng bảo mật? | Security |
| 6 | Caching strategy hợp lý? | Performance |
| 7 | ADR ghi nhận đầy đủ quyết định? | Traceability |

**Basic Design Review (CHK-ENG-TS-02):**

| # | Kiểm tra | Lý do |
|---|---------|-------|
| 1 | API naming nhất quán (RESTful)? | Consistency |
| 2 | DB schema có index strategy? | Performance |
| 3 | Error codes đầy đủ (400/401/403/404/409/500)? | Completeness |
| 4 | Exclusive check (optimistic lock)? | Data integrity |
| 5 | Multi-tenant isolation? | Security |
| 6 | Audit columns (created_at/by, updated_at/by)? | Traceability |
| 7 | Log strategy định nghĩa? | Operability |

**Detail Design Review (CHK-ENG-TS-03):**

| # | Kiểm tra | Lý do |
|---|---------|-------|
| 1 | Flowchart đầy đủ (Auth -> Validate -> Check exist -> Exclusive -> Process)? | No missing steps |
| 2 | Transaction boundaries rõ ràng? | Data consistency |
| 3 | Validation 3 tầng (đơn mục, tương quan, nghiệp vụ)? | Data quality |
| 4 | Pseudo code cover tất cả nhánh? | Implementation clarity |
| 5 | Nhất quán với Basic Design (API list <-> API spec <-> DB schema)? | Consistency |

### 3.4. AI-Assisted Review (RUL-ENG-TS-04 Mục 2.6)

**BẮT BUỘC có AI Review Summary khi:**
- Logic nghiệp vụ phức tạp (>= 3 nhánh quyết định)
- Code liên quan đến bảo mật (auth, encryption, input validation)
- Code quan trọng về hiệu năng (loop > 1000, DB query, cache)
- Công nghệ/library mới chưa sử dụng trong dự án

**Tiêu chí từ chối PR thiếu AI Review:**
- PR thuộc tình huống bắt buộc nhưng KHÔNG có AI Review Summary
- AI Review Summary quá sơ sài (< 3 dòng)
- AI phát hiện vấn đề nhưng không có giải thích tại sao không sửa

---

## 4. Tự kiểm tra

### Bài tập 1 (L1): Review code và phát hiện lỗi

Cho đặc tả API "update_fuel_info" (từ đề thi SE Review Test -- xem file gốc: `roles/se/tests/review.md`).

Đặc tả gồm: Endpoint POST /api/v1/fuel-info/{id}, Method POST, Quyền Admin+Operator, Request body có calorificValue (camelCase), unit_price (số thực), max 200 ký tự cho fuel_name. Response chỉ có data (không có result). DB UPDATE chỉ WHERE fuel_info_id. Error chỉ có 400 và 500. Flowchart: Nhận request -> Validation -> Update DB -> Trả response.

**Yêu cầu:** Tìm tối thiểu 10 lỗi, phân loại mức độ (Critical/Major/Minor), đề xuất sửa.

**Gợi ý (đáp án có 18 lỗi, trong đó 7 Critical):**
- Kiểm tra: HTTP method, naming convention, quyền truy cập, validation, exclusive check
- Kiểm tra: DB operation (tenant_code, delete_flag, audit columns)
- Kiểm tra: Error codes (401, 403, 404, 409), flowchart (auth, exclusive, transaction)

**Rubric chấm điểm:**
- L1 (>= 30%): Tìm >= 5 lỗi, bao gồm >= 2 Critical
- L2 (>= 56%): Tìm >= 10 lỗi, bao gồm >= 4 Critical, phân loại đúng phần lớn
- L3 (>= 77%): Tìm >= 15 lỗi, phân loại chính xác, đề xuất sửa chất lượng cao

### Bài tập 2 (L2): Thực hành review một đoạn code

Review đoạn code sau và phát hiện vấn đề:

```typescript
// OrderService.ts
class OrderService {
  async createOrder(data) {
    var order = new Order();
    order.items = data.items;
    order.total = 0;
    for (let i = 0; i < data.items.length; i++) {
      let item = data.items[i];
      let product = await db.query(
        "SELECT * FROM products WHERE id = '" + item.productId + "'"
      );
      if (product) {
        order.total = order.total + product.price * item.quantity;
      }
    }
    if (order.total > 0) {
      await db.query(
        "INSERT INTO orders (user_id, total, status) VALUES ('" +
        data.userId + "', " + order.total + ", 'new')"
      );
      console.log("Order created: " + order.total);
      sendEmail(data.userEmail, "Order confirmed");
      return { success: true };
    }
  }
}
```

**Gợi ý:** SQL injection (2 chỗ), N+1 queries, thiếu validation, thiếu error handling, không return khi total <= 0, console.log, var thay vì const, thiếu types, sendEmail không await, thiếu transaction, không idempotency.

### Bài tập 3 (L3): Thiết kế Quality Gates

Cho dự án Fuel Management System (team 5 dev, 2 QA, CMMI Level 3): Định nghĩa 6 Quality Gates, review checklists cho 3 loại artifact, kế hoạch mentor 8 tuần, 5 review metrics.

---

## 5. Tài liệu tham khảo

### Từ tài liệu nội bộ (CMMI)
- **RUL-ENG-TS-03** -- Tiêu chuẩn Lập trình (Coding Standard Rule)
- **RUL-ENG-TS-04** -- Quy định Rà soát Mã nguồn (Code Review Rule)
- **GLN-ENG-TS-03** -- Hướng dẫn Code Review Best Practices
- **CHK-ENG-TS-04** -- Danh mục Kiểm tra Code Review (Checklist)
- **RUL-ENG-TS-05** -- Tiêu chuẩn Hoàn thành (Definition of Done)

### Từ khung năng lực SE
- **Competency #5 (Quality Mindset):**
  - L1: Tuân thủ template, không lỗi format
  - L2: Self-review pass, xem xét ngoại lệ đầy đủ
  - L3: Định nghĩa quality gate cho team, mentor review culture

### Từ đề thi SE Review Test
- 18 lỗi cài sẵn trong API spec "update_fuel_info"
- 7 Critical: Quyền truy cập, exclusive check, unique check, tenant isolation, delete_flag, 409 Conflict, flowchart thiếu bước
- 11 Major: HTTP method, naming, validation, audit columns, error codes, transaction

### Sách & Tài liệu bên ngoài
- "Code Complete" -- Steve McConnell
- "Clean Code" -- Robert C. Martin
- Google Engineering Practices: https://google.github.io/eng-practices/review/
- OWASP Code Review Guide: https://owasp.org/www-project-code-review-guide/
