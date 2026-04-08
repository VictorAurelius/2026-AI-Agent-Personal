# Risk Management (Quản lý Rủi ro)

> **Mục tiêu:** Nhận diện, đánh giá, phòng ngừa và xử lý rủi ro chủ động trong dự án outsource Nhật Bản
> **Level:** L1 -> L2 -> L3
> **Thời gian đọc:** ~25 phút
> **Liên quan:** PM Competency #3 (リスク管理), CMMI PA: RSKM (Risk Management)

---

## 1. Khái niệm cơ bản (L1)

### 1.1. Risk vs Issue

| | Risk (Rủi ro) | Issue (Vấn đề) |
|---|---------------|----------------|
| **Thời điểm** | Chưa xảy ra (tương lai) | Đã xảy ra (hiện tại) |
| **Xử lý** | Phòng ngừa, giảm thiểu | Xử lý, khắc phục |
| **Ví dụ** | "Key dev CÓ THỂ nghỉ việc" | "Key dev ĐÃ nghỉ việc" |
| **Theo dõi** | Risk Register | Issue Tracker |

**Khi risk xảy ra** -> Chuyển từ Risk Register sang Issue Tracker

### 1.2. Risk Register cơ bản

**Mỗi risk cần có tối thiểu:**

| Thuộc tính | Mô tả |
|------------|-------|
| Risk ID | Mã định danh duy nhất (R-001) |
| Mô tả | Mô tả rủi ro cụ thể |
| Category | Phân loại (Technical, Resource, Schedule...) |
| Probability | Khả năng xảy ra (H/M/L) |
| Impact | Mức độ ảnh hưởng (H/M/L) |
| Owner | Người chịu trách nhiệm |
| Status | Trạng thái (Active / Mitigated / Closed) |

**Hành vi L1:**
- Nhận diện risk khi được hỏi hoặc khi risk đã hiện hữu
- Thực hiện mitigation action được giao
- Báo cho PM khi gặp vấn đề lớn
- Biết rằng "hiểu sai spec" là risk lớn nhất trong dự án Nhật

---

## 2. Thực hành nâng cao (L2)

### 2.1. Quy trình 7 bước quản lý rủi ro

**Từ nang-luc.md, SYP03:**

```
Bước 1: XÁC ĐỊNH NGUỒN RỦI RO
  |-- Rà quét 7 nguồn (xem 2.2)
  v
Bước 2: XÁC ĐỊNH RỦI RO
  |-- Brainstorming, checklist, lessons learned
  |-- Ghi nhận vào Risk Register
  v
Bước 3: ĐÁNH GIÁ RỦI RO
  |-- Probability x Impact = Risk Score
  v
Bước 4: LỰA CHỌN CHIẾN LƯỢC XỬ LÝ
  |-- Reduce / Avoid / Transfer / Accept
  v
Bước 5: KẾ HOẠCH PHÒNG CHỐNG (Mitigation)
  |-- Hành động chủ động: owner, deadline, action cụ thể
  v
Bước 6: KẾ HOẠCH KHẮC PHỤC (Contingency)
  |-- Hành động phản ứng NẾU risk xảy ra
  |-- Trigger condition cụ thể
  v
Bước 7: CẬP NHẬT KẾ HOẠCH & LỊCH
  |-- Tích hợp vào project plan
  |-- Rà soát định kỳ (hàng tuần)
```

### 2.2. 7 nguồn rủi ro (RUL-PJM-RSKM-01)

| Mã | Nguồn | Ví dụ cụ thể |
|----|-------|-------------|
| **TR** | Kỹ thuật (Technical) | Công nghệ mới, hiệu năng, kiến trúc phức tạp |
| **RR** | Nguồn lực (Resource) | Thiếu nhân sự, thiếu kỹ năng, key person nghỉ |
| **SR** | Tiến độ (Schedule) | Deadline gấp, phụ thuộc chặt, ước lượng sai |
| **CR** | Khách hàng (Customer) | Chậm phản hồi, thay đổi yêu cầu đột ngột, UAT delay |
| **ER** | Bên ngoài (External) | Third-party delay, quy định pháp lý |
| **CCR** | Văn hóa & Giao tiếp | Rào cản ngôn ngữ JP-VN, hiểu sai văn hóa, timezone |
| **FR** | Tài chính (Financial) | Vượt budget fixed-price, biến động tỷ giá JPY/VND |

### 2.3. Ma trận Probability x Impact

**Ma trận đánh giá:**

| Probability / Impact | **Low** | **Medium** | **High** |
|---------------------|---------|------------|----------|
| **High (>50%)** | Medium (3) | High (6) | Critical (9) |
| **Medium (20-50%)** | Low (2) | Medium (4) | High (6) |
| **Low (<20%)** | Low (1) | Low (2) | Medium (3) |

**Mức độ Impact:**

| Level | Schedule | Cost | Quality |
|-------|----------|------|---------|
| **High** | Trễ > 2 tuần | Vượt > 10% | Lỗi nghiêm trọng, rework lớn |
| **Medium** | Trễ 1-2 tuần | Vượt 5-10% | Lỗi lớn, workaround |
| **Low** | Trễ < 1 tuần | Vượt < 5% | Lỗi nhỏ, chấp nhận được |

**Hành động theo Risk Score:**
- **Critical (9):** Hành động NGAY LẬP TỨC, báo trong 2h (RUL-PJM-RSKM-01)
- **High (6):** Action plan trong 1 ngày
- **Medium (3-4):** Theo dõi, chuẩn bị mitigation
- **Low (1-2):** Chấp nhận, giám sát tối thiểu

### 2.4. 4 chiến lược xử lý rủi ro

| Chiến lược | Khi nào dùng | Ví dụ |
|-----------|-------------|-------|
| **Reduce (Giảm thiểu)** | Giảm khả năng xảy ra HOẶC mức độ ảnh hưởng | Cross-training để giảm bus factor, thêm buffer |
| **Avoid (Né tránh)** | Thay đổi approach để loại bỏ risk | Dùng công nghệ đã proven thay vì experimental |
| **Transfer (Chuyển)** | Chuyển risk cho bên thứ ba | Fixed-price vendor contract, insurance |
| **Accept (Chấp nhận)** | Risk thấp, mitigation quá đắt | Ghi nhận risk, giám sát, có contingency plan |

### 2.5. Risk Register đầy đủ — Ví dụ 10 risks

| ID | Risk | Cat | Prob | Impact | Score | Mitigation | Owner |
|----|------|-----|------|--------|-------|-----------|-------|
| R-001 | Spec ambiguity (tiếng Nhật) | CCR | H | H | 9 | Review spec với BrSE trước dev, Q&A log | PM |
| R-002 | Key SE nghỉ việc | RR | M | H | 6 | Knowledge transfer, pair work, document | PM |
| R-003 | Module phức tạp hơn estimate | TR | H | M | 6 | PERT estimate, POC 1 sprint, buffer 20% | TL |
| R-004 | 2 PG mới ramp-up chậm | RR | H | M | 6 | Pair programming, mentor, giảm task phức tạp | TL |
| R-005 | Timezone delay (JP-VN) | CCR | M | M | 4 | Batch Q&A, async communication tool | BrSE |
| R-006 | Bug density vượt target | TR | M | H | 6 | Enforce code review 100%, unit test coverage 80% | QA |
| R-007 | Scope creep từ CR | CR | H | H | 9 | Strict CR process, baseline, sprint gate | PM |
| R-008 | Integration phức tạp | TR | M | M | 4 | API contract, mock/stub, integration sprint | TL |
| R-009 | UAT delay từ khách hàng | CR | M | M | 4 | UAT plan sớm, test data chuẩn bị trước | PM |
| R-010 | Environment không ổn định | ER | L | M | 2 | DevOps backup, monitoring, staging env | DevOps |

### 2.6. Thời hạn báo cáo rủi ro (RUL-PJM-RSKM-01)

| Risk Score | Thời hạn báo cáo |
|------------|-----------------|
| >= 15 (Critical) | Báo trong **2 giờ** |
| 9-14 (High) | Báo trong **1 ngày** |
| < 9 (Medium/Low) | Báo trong báo cáo tuần |
| Rủi ro tiềm ẩn | PHẢI báo với ghi chú "Tiềm ẩn" |

**Tần suất rà soát:**
- Hàng ngày: PM rà soát sổ rủi ro
- Hàng tuần: Cuộc họp rà soát rủi ro với team
- Đột xuất: Báo ngay khi có rủi ro mới hoặc mức độ tăng

---

## 3. Chiến lược & Dẫn dắt (L3)

### 3.1. Predictive Risk Assessment

**Dự đoán risk trước khi dự án bắt đầu:**
- Review lessons learned từ dự án trước
- Kiểm tra risk checklist đặc thù dự án Nhật
- Risk assessment cho cả upstream (Waterfall) và downstream (Agile)
- Pre-mortem exercise: "Giả sử dự án thất bại sau 6 tháng, tại sao?"

**Risk từ kinh nghiệm dự án Nhật (Japan-specific):**

| Risk | Probability | Tại sao đặc thù | Mitigation |
|------|-------------|-----------------|------------|
| Spec ambiguity | HIGH | Tiếng Nhật mơ hồ, 暗黙の了解 | Review spec với BrSE, prototype, confirm meeting |
| Cultural gap | MEDIUM | Khác biệt cách làm việc, 報連相 | Training cross-cultural, BrSE bridge |
| Quality expectation gap | HIGH | Khách Nhật kỳ vọng chất lượng rất cao | 説明できる品質, quality gate strict |
| Timezone delay | MEDIUM | 2h chênh lệch, response chậm | Batch Q&A, overlap hours, async tools |
| Re-estimation shame | MEDIUM | Re-estimate = mất uy tín | Invest estimation quality, PERT, buffer |

### 3.2. Contingency Budget Planning

**Tính contingency reserve:**
```
EMV (Expected Monetary Value) = Probability x Cost Impact

Ví dụ:
  R-001 Spec ambiguity:  60% x 20 MD = 12 MD
  R-002 Key person leave: 30% x 30 MD = 9 MD
  R-003 Complex module:   50% x 15 MD = 7.5 MD
  
  Total EMV = 28.5 MD
  Contingency reserve = 30 MD (làm tròn lên)
  
  Budget = Base estimate + Dev buffer (15%) + Contingency reserve (30 MD)
```

**Quy tắc quyết định:**
- Mitigation cost < EMV -> Làm mitigation (tiết kiệm)
- Mitigation cost > EMV -> Accept risk (không đáng đầu tư)

### 3.3. Risk Framework Design

**Risk Review Meeting (30 phút/tuần):**

```
1. Risk Trend (5 phút)
   - Bao nhiêu risk: active, closed, realized?
   - Xu hướng tốt lên hay xấu đi?

2. Top 3 Risks Review (15 phút)
   - Cập nhật trạng thái
   - Tiến độ mitigation
   - Cần escalate không?

3. New Risks (5 phút)
   - Risk mới phát hiện tháng này
   - Đánh giá ban đầu

4. Realized Risks (5 phút)
   - Risk nào đã xảy ra?
   - Xử lý thế nào?
   - Bài học kinh nghiệm
```

**Risk Indicators (Early Warning Signs):**

| Risk | Indicator | Ngưỡng | Action |
|------|-----------|--------|--------|
| Team morale thấp | Survey score | < 7/10 | 1-on-1 meeting, giải quyết lo ngại |
| Scope creep | Số CR mới | > 2 CR/sprint | Re-baseline, negotiate scope freeze |
| Quality issues | Defect density | > 10/KLOC | Thêm QA, tăng code review |
| Schedule slip | Velocity drop | < 80% average | Root cause analysis, corrective action |
| Vendor delay | Missed milestone | 1 tuần trễ | Escalate, backup plan |

### 3.4. Escalation Package cho Management

**Format escalation:**
```
Subject: Risk Escalation - R-001: Spec Ambiguity in Optimization Module

Risk: 3 điểm trong 基本設計書 team dev hiểu khác nhau
Severity: Critical (Prob: H, Impact: H, Score: 9)

Situation: BrSE báo team hiểu khác nhau, meeting minutes không ghi đủ
Impact: 
  - Delay 2 tuần nếu phải làm lại
  - Cost tăng 10 MD
  - Quality risk: wrong implementation

Mitigation Attempted: 
  - Setup meeting confirm với khách trong 24h
  - BrSE review lại tất cả meeting minutes

Request: 
  - Phê duyệt thêm 2 MD cho spec clarification sprint
  - Assign BrSE tham gia toàn thời gian 1 tuần

Recommendation: Prototype 3 điểm mơ hồ, demo cho khách confirm
Timeline: Cần quyết định trong 2 ngày
```

---

## 4. Tự kiểm tra

### Bài tập: 4 tình huống khủng hoảng

**Sử dụng bối cảnh: Dự án Boiler Operation Management System, 12 sprint, sprint 6/12**

---

**Tình huống 1: Spec Ambiguity**

Module "Optimization Calculation" có 3 điểm trong 基本設計書 team dev hiểu khác nhau. Meeting minutes không ghi đủ chi tiết.

*Câu hỏi:*
1. Đây là risk hay đã là issue? (Trả lời: Đã là ISSUE — đã xảy ra)
2. Đánh giá impact (scope, timeline, quality, cost)?
3. Immediate action (trong 24h)?
4. Preventive action (để không tái phát)?

*Gợi ý:*
- Immediate: Setup meeting confirm với khách, document lại decision
- Preventive: Cải tiến meeting minutes template, review spec với BrSE TRƯỚC khi dev

---

**Tình huống 2: Resource Loss**

1 SE senior (key person) thông báo nghỉ việc sau 1 tháng. SE này phụ trách thiết kế 2 module quan trọng nhất.

*Câu hỏi:*
1. Đánh giá impact?
2. Short-term mitigation (1 tháng)?
3. Long-term mitigation?
4. Communication plan: báo ai, khi nào, nội dung gì?

*Gợi ý:*
- Short-term: Knowledge transfer plan, pair work ngay lập tức
- Long-term: Giảm bus factor, document architecture, cross-training
- Communication: Báo management + khách hàng (qua BrSE) + team

---

**Tình huống 3: Quality Alert**

Sau sprint 5: Bug density 1.0/KLoC (target 0.5), Code review 70% (target 100%), Unit test 45% (target 80%), 指摘件数 tại design review giảm 50%.

*Câu hỏi:*
1. Quality đang tốt lên hay xấu đi? (chú ý: 指摘件数 giảm có thể là bad sign)
2. Root cause analysis cho mỗi metric?
3. Action plan để đạt quality target trước release?
4. Viết escalation report format: Problem -> Impact -> Root Cause -> Action -> Ask

*Gợi ý:*
- 指摘件数 giảm + bug density tăng = review KHÔNG KỸ, bỏ sót lỗi
- Root cause: Timeline pressure -> skip review, PG mới -> thiếu unit test
- Action: Enforce 100% code review, pair programming, quality gate strict

---

**Tình huống 4: Compound Crisis (L3)**

Sprint 8/12, đồng thời xảy ra: (a) CR lớn +15 MD, deadline/budget không đổi; (b) 2 PG báo ốm 1 tuần; (c) Critical security bug ở Authentication.

*Câu hỏi:*
1. Prioritize: xử lý a, b, c theo thứ tự nào?
2. Action plan cụ thể cho mỗi vấn đề?
3. Viết email cho khách hàng Nhật?

*Gợi ý thứ tự xử lý:*
1. **(c) Security bug TRƯỚC** — Critical, ảnh hưởng security, khách yêu cầu fix ngay
2. **(b) Resource** — Immediate, cần điều chỉnh kế hoạch tuần này
3. **(a) CR** — Negotiable, có thể defer hoặc trade-off scope

---

## 5. Tài liệu tham khảo

**Source gốc:**
- PM Competency #3: `khung-danh-gia-nang-luc-main/roles/pm/nang-luc.md`
- PM Levels (Risk section): `khung-danh-gia-nang-luc-main/roles/pm/levels.md`
- Risk Management Test: `khung-danh-gia-nang-luc-main/roles/pm/tests/risk-management.md`

**CMMI Documents:**
- PRC-PJM-RSKM-01: Risk Management Process (5 bước)
- RUL-PJM-RSKM-01: Risk Management Rule (7 danh mục, ngưỡng, thời hạn báo cáo)
- GLN-PJM-RSKM-01: Risk Management Guide (kỹ thuật, case study, agile risk)

**Nguyên tắc then chốt:**
- "Phòng bệnh hơn chữa bệnh" — Phòng ngừa > xử lý
- KHÔNG giấu bad news — báo sớm với đủ context + phương án
- Risk register KHÔNG PHẢI "shelfware" — cập nhật hàng tuần, hiển thị top risks
- Mỗi risk HIGH phải có owner + action + deadline CỤ THỂ
- Không phải "sẽ theo dõi" mà phải "sẽ LÀM gì, AI làm, KHI NÀO xong"
