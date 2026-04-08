# Process Improvement & Kaizen (Cải tiến Quy trình)

> **Mục tiêu:** Nắm vững quy trình CAR (Causal Analysis & Resolution), kỹ thuật phân tích nguyên nhân gốc rễ, quản lý cải tiến liên tục và PPQA audit trong tổ chức CMMI Level 3
> **Level:** L1 -> L2 -> L3
> **Thời gian đọc:** ~25 phút
> **Liên quan:** PM Competency #4 (品質管理), #8 (リーダーシップ), CMMI PA: PMG-CAR, PMG-OPF, PMG-PPQA

---

## 1. Khái niệm cơ bản (L1)

### 1.1 Tại sao cần cải tiến quy trình?

Trong dự án outsource Nhật Bản, khách hàng kỳ vọng "phòng bệnh hơn chữa bệnh." Lỗi lặp lại là dấu hiệu quy trình có lỗ hổng. PM phải:

- **Biết quy trình CAR:** Khi nào cần phân tích nguyên nhân gốc
- **Tham gia retrospective:** Góp ý cải tiến từ góc độ dự án
- **Báo cáo vấn đề quy trình:** Không im lặng khi thấy quy trình không hiệu quả

### 1.2 Quy trình CAR 5 bước (PRC-PMG-OPF-02)

```
BƯỚC 1: IDENTIFY & LOG INCIDENT
  |  Phát hiện vấn đề --> Đánh giá mức độ --> Tạo CAR record
  |
BƯỚC 2: ROOT CAUSE ANALYSIS
  |  Dùng 5-Whys / Fishbone --> Tìm nguyên nhân gốc (system gap)
  |
BƯỚC 3: DEFINE CAPA (Corrective & Preventive Actions)
  |  Hành động sửa lỗi + Hành động phòng ngừa (company-wide)
  |
BƯỚC 4: IMPLEMENT CAPA
  |  Triển khai --> Cập nhật PAL --> Đào tạo team
  |
BƯỚC 5: VERIFY EFFECTIVENESS (sau 3 tháng)
     Kiểm tra lỗi cũ có còn tái diễn không?
```

### 1.3 Khi nào phải thực hiện CAR?

| Mức độ | Tiêu chí trigger | CAR Team | Effort |
|--------|-----------------|----------|--------|
| **Critical** | Security breach, mất dữ liệu, tiến độ vượt >30% | 3-5 người (EPG + TL + QA + expert) | 8-16h |
| **Major** | Critical bug production, tiến độ vượt 20-30%, lỗi lặp lại >=3 lần | 2-3 người (EPG + PM/TL) | 4-8h |
| **Minor** (Tùy chọn) | Khách hàng phàn nàn, vấn đề chất lượng | 2 người (PM + TL) | 2-4h |

### 1.4 Phân biệt Triệu chứng và Nguyên nhân gốc

| Khía cạnh | Triệu chứng (Symptom) | Nguyên nhân gốc (Root Cause) |
|-----------|----------------------|------------------------------|
| Là gì? | Những gì bạn QUAN SÁT được | Lý do CĂN BẢN gây ra triệu chứng |
| Khi fix | Triệu chứng tạm thời biến mất | Triệu chứng KHÔNG tái diễn |
| Ví dụ | "Bug production" | "Process thiếu code review cho security" |

**Nguyên tắc vàng:** Root cause PHẢI chỉ vào **system/process gap**, KHÔNG chỉ vào cá nhân.

| Root Cause XẤU | Root Cause TỐT |
|----------------|----------------|
| "Developer careless" | "Code review checklist không có security section" |
| "Tester không test kỹ" | "Test template thiếu edge case section" |
| "Team không có thời gian" | "Planning process không allocate buffer cho QA" |
| "Người X làm sai" | "Training process thiếu module về [technical skill]" |

---

## 2. Thực hành nâng cao (L2)

### 2.1 Kỹ thuật 5-Whys (bắt buộc cho mọi CAR)

**Cách thực hiện:**

**BƯỚC 1 - Định nghĩa vấn đề rõ ràng:**
- SAI: "Hệ thống có lỗi"
- ĐÚNG: "Users không thể submit form khi nhấn Submit button (100% reproduce, 50 users affected, production)"

**BƯỚC 2 - Hỏi "Tại sao?" 5 lần:**

| # | Câu hỏi | Trả lời | Bằng chứng |
|---|---------|---------|------------|
| 1 | Tại sao [problem] xảy ra? | [Nguyên nhân cấp 1] | Data/logs |
| 2 | Tại sao [nguyên nhân 1]? | [Nguyên nhân cấp 2] | Data/logs |
| 3 | Tại sao [nguyên nhân 2]? | [Nguyên nhân cấp 3] | Data/logs |
| 4 | Tại sao [nguyên nhân 3]? | [Nguyên nhân cấp 4] | Data/logs |
| 5 | Tại sao [nguyên nhân 4]? | **[ROOT CAUSE]** | Process audit |

**Quy tắc:** Mỗi answer phải là FACT (không phải assumption), phải có evidence.

**BƯỚC 3 - Xác minh root cause:**
- "Nếu fix root cause này, problem sẽ không tái diễn?" --> YES = good
- "Root cause có phải lỗ hổng system/process không?" --> YES = good

**Ví dụ thực tế - Release Delay:**

| # | Why? | Answer | Evidence |
|---|------|--------|----------|
| 1 | Tại sao release delay 2 tuần? | 50 major bugs phát hiện ở UAT | UAT report |
| 2 | Tại sao 50 bugs ở UAT? | Bugs không được catch ở UT/IT phase | Metrics: chỉ 5 bugs ở UT/IT |
| 3 | Tại sao không catch ở UT/IT? | Test cases thiếu integration scenarios | Test review: 80% UT, 20% IT |
| 4 | Tại sao test cases thiếu? | Test template không có section cho IT | Template review |
| 5 | Tại sao template thiếu? | **Process không require IT plan trong planning** | PP process audit |

**Root Cause:** Project planning process không require integration test plan
**Preventive Action:** Update quy trình planning + Update test template + Training team

### 2.2 Kỹ thuật Fishbone (Ishikawa Diagram)

Dùng khi vấn đề phức tạp, có nhiều contributing factors. Phân loại nguyên nhân theo 6M:

| Category | Vietnamese | Ví dụ |
|----------|-----------|-------|
| **Man** (People) | Con người | Skills, training, experience, motivation |
| **Method** (Process) | Quy trình | Procedures, workflows, standards |
| **Machine** (Technology) | Công nghệ | Tools, automation, infrastructure |
| **Material** (Inputs) | Đầu vào | Requirements, data, dependencies |
| **Measurement** | Đo lường | Metrics, monitoring, quality gates |
| **Environment** | Môi trường | Conditions, constraints, external factors |

**Ví dụ: 15 bugs lọt ra production trong Q1 (target < 5)**

```
People:                              Process:
|- Thiếu testing skills              |- Không có security review bắt buộc
|- Không có security training        |- UAT checklist thiếu
|  +- Training program thiếu module  |- Code review không enforce
+- Turnover cao (3 testers nghỉ)     +- Review là tùy chọn cho "small changes"

Technology:                          Measurement:
|- Không có automated security scan  |- Không track bug leakage metric
|- Linter rules lỗi thời             |- Không có quality gate lúc release
+- CI pipeline thiếu tests           +- Code coverage không được monitor
```

### 2.3 Kỹ thuật Fault Tree Analysis (FTA)

Dùng cho vấn đề critical (security breach, data loss). Phân tích top-down từ "sự kiện không mong muốn" xuống các nguyên nhân:

```
           [Data Loss in Production]
                    |
            --------+--------
           |                 |
    [Backup Failed]    [DB Corruption]
         |                   |
    -----+-----         ----+----
   |           |       |         |
[No backup  [Storage  [Code bug  [No input
 schedule]   full]     in query]  validation]
```

### 2.4 Improvement Backlog và Ưu tiên hóa (Impact/Effort)

Sau khi thu thập feedback từ nhiều nguồn (PPQA audit, retrospective, CAR, metrics), ghi vào Improvement Backlog và ưu tiên:

**Ma trận Tác động/Effort:**

|  | **Effort Thấp** | **Effort Cao** |
|--|-----------------|---------------|
| **Tác động Lớn** | **THẮNG NHANH** (Ưu tiên cao) | **CHIẾN LƯỢC** (Ưu tiên trung bình) |
| **Tác động Nhỏ** | **TIỆN THỂ** (Ưu tiên thấp) | **TỪ CHỐI** (Không làm) |

**Tiêu chí đánh giá:**
- **Tác động Lớn:** Ảnh hưởng >50% dự án HOẶC giải quyết vấn đề lặp lại nghiêm trọng
- **Tác động Nhỏ:** Ảnh hưởng <20% dự án HOẶC cải thiện nhỏ
- **Effort Thấp:** <8h, 1 người
- **Effort Cao:** >40h, nhiều người, cần phối hợp

### 2.5 PPQA Audit và Quản lý Non-Conformance

**Quy trình audit PPQA:**
1. PPQA audit định kỳ theo lịch (Tier 1 cho dự án nhỏ = 10 items, 30 phút)
2. Phát hiện Non-Conformance (NC) --> Phân loại
3. Thông báo PM --> PM lập kế hoạch sửa lỗi
4. Theo dõi tiến độ sửa lỗi --> Xác nhận hoàn thành

**Phân loại NC và SLA:**

| Mức độ | SLA Fix | Ví dụ |
|--------|---------|-------|
| Critical | 3 ngày | Không có code review cho module critical |
| Major | 1 tuần | Thiếu test case cho requirement |
| Minor | 2 tuần | Format tài liệu không đúng template |

**Quy tắc escalation:**
- PM không fix đúng hạn --> QA Lead
- QA Lead không giải quyết --> PMO
- PMO không giải quyết --> Management
- NC lặp lại >= 3 lần cùng loại trong 3 tháng --> Trigger quy trình CAR

### 2.6 Chạy thử (Pilot Testing)

Khi có thay đổi lớn hoặc quy trình mới:
1. Chọn 1-2 dự án thử (diverse: 1 nhỏ + 1 trung bình)
2. Thời gian: 2-4 tuần
3. Thu thập feedback (survey + interview)
4. Đo kết quả (thời gian thực hiện, chất lượng, mức hài lòng)
5. Tinh chỉnh dựa trên feedback

**Tiêu chí thành công thử nghiệm:**
- Feedback tích cực >= 60%
- Không có vấn đề blocking
- Effort thực hiện trong phạm vi dự kiến (+/-20%)

---

## 3. Chiến lược & Dẫn dắt (L3)

### 3.1 Feedback Loop toàn tổ chức

PM cấp L3 hiểu và vận hành được vòng phản hồi đầy đủ:

```
PPQA Findings --> CAR Analysis --> OPF Improvement
       |                                 |
       v                                 v
  Audit phát hiện        Process Asset Library cập nhật
  vấn đề quy trình              |
                                v
                    OPD (Tailoring + Knowledge)
                                |
                                v
                    OT (Training --> Team áp dụng)
                                |
                                v
                    Dự án áp dụng --> PPQA audit lại
                    (Vòng lặp cải tiến liên tục)
```

### 3.2 PAL Maintenance và Versioning

**Process Asset Library (PAL)** gồm 242 tài liệu, 25 Practice Areas. PM L3 góp phần duy trì:

**Triết lý áp dụng:** Problem-First --> Solve with PA --> Prove Value --> Expand

**Chu trình AAME (Assess-Adopt-Measure-Expand):**
1. **ASSESS:** PM + TL + QA đánh giá Pain Point (12 vấn đề, điểm 1-5)
2. **ADOPT:** EPG hướng dẫn áp dụng Starter Kit (3-4 tài liệu tối thiểu)
3. **MEASURE:** Đo metric trước/sau (4-6 tuần)
4. **EXPAND:** Hiệu quả --> Quay lại Assess cho vấn đề tiếp

**Ví dụ dự án Alpha (10 người, 6 tháng):**

| Vòng | Tuần | Vấn đề TOP 1 | PA áp dụng | Kết quả mong đợi |
|------|------|-------------|-----------|-------------------|
| 1 | T1-T8 | Bug lọt KH nhiều | VER + MA | Bug density giảm 40% |
| 2 | T9-T16 | Yêu cầu đổi --> rework | REQM | Rework effort giảm 30% |
| 3 | T17-T24 | Trễ tiến độ | PMC + PP | SPI cải thiện 0.7 --> 0.9 |
| 4 | T25-T30 | Thiết kế sai | TS Design | Design defect giảm 50% |
| 5 | T31+ | Cải tiến liên tục | OPF/CAR | Retrospective hàng tháng |

**Kết quả:** Sau 5 vòng, dự án cover 7 PA một cách tự nhiên. Team hiểu TẠI SAO mỗi quy trình tồn tại.

### 3.3 Quy trình Cải tiến 5 bước (PRC-PMG-OPF-01)

| Bước | Hoạt động | Tần suất | Effort |
|------|-----------|---------|--------|
| 1. Thu thập feedback | Từ PPQA, CAR, retrospective, metrics, team | Liên tục | 1h/quý |
| 2. Đánh giá và ưu tiên | Phân tích, khả thi, tác động, ưu tiên | Hàng quý | 2-4h |
| 3. Triển khai cải tiến | Soạn thảo thay đổi, AI verify, peer review, pilot | Tùy phạm vi | 1-40h |
| 4. Deploy và communicate | Cập nhật PAL, truyền đạt, đào tạo, hỗ trợ | Khi có thay đổi | 2-4h |
| 5. Đánh giá hiệu quả | Adoption rate, compliance, metrics trước/sau | 1 quý sau deploy | 1-2h |

**Tiêu chí thành công:**
- Adoption rate >= 80% sau 3 tháng
- Compliance >= 90% sau 6 tháng
- Không có hậu quả ngoài ý muốn nghiêm trọng
- Feedback tích cực >= 60%

### 3.4 Governance và Chuẩn hóa toàn tổ chức

**Hệ thống chỉ số cấp tổ chức:**

| Cấp độ | Chỉ số | Tần suất | Nguồn |
|--------|--------|----------|-------|
| Tổ chức | Doanh thu, lợi nhuận, tăng trưởng | Hàng quý | Tài chính |
| Dự án | Tiến độ, chất lượng, chi phí, rủi ro | Hàng tháng | PMO |
| Quy trình | Tuân thủ, hiệu quả, defect density | Hàng tháng | QA/PPQA |
| Nhân sự | Năng lực, đào tạo, mức hài lòng | Hàng quý | HR |

**Ngưỡng Escalation cấp tổ chức:**

| Mức rủi ro | Điểm (PxI) | Xử lý |
|-----------|------------|-------|
| Thấp | 1-6 | PM tự quản lý |
| Trung bình | 7-14 | Báo cáo Department Head |
| Cao | 15-20 | Escalate Steering Committee |
| Nghiêm trọng | >20 | Họp khẩn CEO/Board |

### 3.5 Xử lý vấn đề "Không tuân thủ quy trình" (3 lớp)

**Lớp 1: HIỂU -- Giải quyết "không biết tại sao" (Soft)**
- Training tập trung vào WHY: mỗi quy trình giải quyết vấn đề gì thực tế
- Dùng ví dụ từ chính dự án: "Lần trước bug lọt KH vì KHÔNG review --> giờ có checklist"
- Member tự nhận diện vấn đề --> tự thấy cần quy trình --> buy-in tự nhiên

**Lớp 2: ĐƠN GIẢN HÓA -- Giải quyết "quy trình quá nặng" (Practical)**
- Tailoring quy trình theo size dự án (S/M/L) -- dự án nhỏ KHÔNG cần full process
- Tích hợp vào tool hiện tại: checklist trong PR template, CI/CD quality gates tự động
- Giảm overhead: tự động hóa những gì có thể

**Lớp 3: KIỂM TRA -- Giải quyết "không ai check" (Hard)**
- PPQA audit định kỳ, NC classification rõ ràng, escalation path
- Chỉ áp dụng khi Lớp 1+2 không đủ. **KHÔNG bắt đầu bằng "audit + phạt"**

---

## 4. Tự kiểm tra

### Bài tập 1: Phân tích 5-Whys (L1-L2)

**Tình huống:** Dự án của bạn vừa deploy lên staging. Khách hàng Nhật phát hiện 15 bugs mà QA team đã report "fixed" nhưng thực tế chưa fix xong. 3 features hoạt động khác với 詳細設計書.

**Yêu cầu:**
1. Thực hiện phân tích 5-Whys cho vấn đề "15 bugs chưa fix nhưng report là fixed"
2. Xác định root cause (PHẢI là system/process gap, KHÔNG phải lỗi cá nhân)
3. Đề xuất ít nhất 1 Corrective Action (fix ngay) và 1 Preventive Action (phòng ngừa)
4. Xác định scope: Preventive action áp dụng cho dự án hay toàn công ty?

### Bài tập 2: Thiết kế Pilot Plan (L2-L3)

**Tình huống:** EPG quyết định triển khai quy trình code review mới, yêu cầu mỗi PR phải có ít nhất 2 reviewers và sử dụng checklist 20 items.

**Yêu cầu:**
1. Chọn 2 dự án để pilot (giải thích lý do chọn)
2. Xác định metrics đo lường trước/sau (ít nhất 3 metrics)
3. Thiết kế timeline pilot (2-4 tuần)
4. Xác định tiêu chí thành công
5. Viết kế hoạch rollback nếu pilot thất bại

### Bài tập 3: Fishbone Analysis (L2)

**Tình huống:** Bug density của dự án là 8 bug/KLOC (ngưỡng trên là 5). Đã 3 sprint liên tiếp vượt ngưỡng.

**Yêu cầu:**
1. Vẽ Fishbone diagram với 6M categories
2. Xác định ít nhất 2 root causes
3. Với mỗi root cause, đề xuất preventive action cụ thể
4. Ước tính Impact/Effort cho mỗi action và ưu tiên

### Gợi ý đáp án Bài tập 1:

```
Vấn đề: 15 bugs report "fixed" nhưng thực tế chưa fix
Why 1: Tại sao bugs chưa fix nhưng status là "fixed"?
  --> Developer update status trước khi QA verify
Why 2: Tại sao developer tự update status?
  --> Quy trình không bắt buộc QA verify trước khi close
Why 3: Tại sao không có QA verify?
  --> Bug workflow chỉ có 2 trạng thái: Open --> Fixed
Why 4: Tại sao workflow thiếu trạng thái Verified?
  --> Bug management process không định nghĩa verification step
Why 5: Tại sao process thiếu?
  --> Bug management process chưa được review/update từ 2024

Root Cause: Bug management process thiếu verification step
Corrective: Fix 15 bugs + QA verify tất cả
Preventive: Update PRC-ENG-VER-04 thêm trạng thái "QA Verified"
Scope: Toàn công ty (vì là process gap trong standard process)
```

---

## 5. Tài liệu tham khảo

| Tài liệu | Vai trò |
|----------|---------|
| PRC-PMG-OPF-02 | Quy trình CAR 5 bước |
| RUL-PMG-CAR-01 | Quy định 5-Whys bắt buộc, preventive action company-wide, follow-up 3 tháng |
| GLN-PMG-CAR-01 | Hướng dẫn 5-Whys, Fishbone, Fault Tree với ví dụ chi tiết |
| TPL-PMG-CAR-01 | Mẫu bản ghi CAR |
| PRC-PMG-OPF-01 | Quy trình Cải tiến Quy trình 5 bước |
| GLN-PMG-OPF-01 | Hướng dẫn ưu tiên hóa (Impact/Effort), pilot testing, quản lý thay đổi |
| GLN-PMG-OPF-04 | Hướng dẫn áp dụng PAL (AAME cycle, Pain Point Assessment, Starter Kit) |
| GLN-PMG-OPF-02 | Governance Guide - OKR, dashboard, ra quyết định, escalation |
| PRC-PMG-PPQA-01 | Quy trình audit PPQA |
| RUL-PMG-PPQA-01 | Quy tắc audit, NC classification, escalation |
