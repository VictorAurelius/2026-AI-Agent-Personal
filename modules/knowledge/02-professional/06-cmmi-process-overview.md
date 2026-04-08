# CMMI Process Areas Overview

> **Mục tiêu:** Hiểu cấu trúc và cách vận hành Process Asset Library (PAL) CMMI Level 3 cho dự án outsource Nhật Bản
> **Level:** L1 -> L2 -> L3
> **Thời gian đọc:** ~30 phút
> **Liên quan:** PM Competency #4 (品質管理) / CMMI PA: OPF, OPD, PPQA, MA

---

## 1. Khái niệm cơ bản (L1)

### 1.1 CMMI là gì?

**CMMI** (Capability Maturity Model Integration) là mô hình đánh giá độ trưởng thành của quy trình phát triển phần mềm. Mục tiêu: đảm bảo chất lượng (説明できる品質) và cải tiến liên tục (改善 Kaizen).

**5 Maturity Levels:**

```
Level 5: Optimizing     — Cải tiến liên tục bằng dữ liệu
Level 4: Quantitatively — Quản lý bằng số liệu thống kê
          Managed
Level 3: Defined        — Quy trình chuẩn hóa toàn tổ chức  <-- MỤC TIÊU
Level 2: Managed        — Quy trình cơ bản theo dự án
Level 1: Initial        — Ad-hoc, không có quy trình
```

### 1.2 Process Asset Library (PAL) — 6 loại tài liệu

PAL là kho tài sản quy trình của tổ chức, chứa 247 tài liệu chia làm 6 loại:

```
+-------------------------------------------------------------+
|                      POLICY (POL) - 19 docs                  |
|              "Đặt mục tiêu và cam kết cấp cao"              |
|               Ví dụ: "Chất lượng là số 1"                   |
+---------------------------+---------------------------------+
                            | defines goals
                            v
+-------------------------------------------------------------+
|                     PROCESS (PRC) - 36 docs                  |
|              "Định nghĩa workflow phải làm"                  |
|            Ví dụ: Code Review có 5 bước                      |
+----------+----------------+-----------------+----------------+
           |                |                 |
           v                v                 v
+----------+--+  +----------+--+  +-----------+-+
| RULE (RUL)  |  |TEMPLATE(TPL)|  |CHECKLIST(CHK)|
| 43 docs     |  | 65 docs     |  | 38 docs      |
| "Ngưỡng và  |  | "Biểu mẫu  |  | "Kiểm tra đã |
|  tiêu chí"  |  |  chuẩn"     |  |  làm đúng?"  |
| <=200LOC/hr |  | MR template |  | [x] Reviewed  |
+----------+--+  +----------+--+  +-----------+-+
           |                |                 |
           +----------------+-----------------+
                            |
                            v
              +-------------+--------+
              |  GUIDELINE (GLN)     |
              |  46 docs             |
              |  "Hướng dẫn chi tiết |
              |   cách làm tốt"     |
              |  Examples, tips      |
              +----------------------+
```

### 1.3 Naming Convention

**Format chuẩn:** `[TYPE]-[AREA]-[PA]-[##]-[Description].md`

| Component | Mô tả | Ví dụ |
|-----------|-------|-------|
| TYPE | Loại tài liệu | POL, PRC, TPL, RUL, CHK, GLN |
| AREA | CMMI Area | ENG, PJM, PMG, SUP |
| PA | Process Area | TS, REQM, PP, PMC, PPQA, CM |
| ## | Số thứ tự | 01, 02, 03 |
| Description | Mô tả ngắn | Technical-Solution-Policy |

**Ví dụ đọc tên tài liệu:**

```
RUL-ENG-TS-04-Review-Rule.md
 |    |   |  |     |
 |    |   |  |     +-- Mô tả: Quy định review
 |    |   |  +-------- Số thứ tự: 04
 |    |   +----------- Process Area: Technical Solution
 |    +--------------- CMMI Area: Engineering
 +-------------------- Loại: Rule (quy định bắt buộc)
```

### 1.4 Vai trò và sử dụng tài liệu

| Vai trò | Tài liệu thường dùng |
|---------|---------------------|
| PM | POL (đọc chính sách) -> PRC (hiểu quy trình) -> TPL (copy biểu mẫu) |
| Developer | RUL (nắm ngưỡng) -> TPL (dùng template) -> CHK (tự kiểm tra) |
| QA | PRC (audit theo quy trình) -> CHK (dùng checklist) -> RUL (kiểm ngưỡng) |
| Tất cả | GLN (tham khảo hướng dẫn khi cần chi tiết) |

---

## 2. Thực hành nâng cao (L2)

### 2.1 25 Process Areas — 4 nhóm

**Engineering (ENG) — 6 PAs:**

| PA | Tên đầy đủ | Mục đích |
|----|-----------|---------|
| REQM | Requirements Management | Quản lý yêu cầu, traceability |
| RD | Requirements Development | Phát triển và phân tích yêu cầu |
| TS | Technical Solution | Thiết kế, coding, kiến trúc |
| PI | Product Integration | Tích hợp các component |
| VER | Verification | Kiểm thử (Unit, Integration, System) |
| VAL | Validation | Thẩm định với khách hàng (UAT) |

**Project Management (PJM) — 5 PAs:**

| PA | Tên đầy đủ | Mục đích |
|----|-----------|---------|
| PP | Project Planning | Lập kế hoạch, WBS, estimation |
| PMC | Project Monitoring & Control | Giám sát tiến độ, chi phí, chất lượng |
| IPM | Integrated Project Management | Quản lý dự án tích hợp |
| RSKM | Risk Management | Nhận diện và xử lý rủi ro |
| SAM | Supplier Agreement Mgmt | Quản lý nhà cung cấp |

**Process Management (PMG) — 5 PAs:**

| PA | Tên đầy đủ | Mục đích |
|----|-----------|---------|
| OPF | Organizational Process Focus | Cải tiến quy trình tổ chức (bao gồm CAR) |
| OPD | Organizational Process Definition | Định nghĩa quy trình chuẩn |
| OT | Organizational Training | Đào tạo nhân sự |
| MA | Measurement & Analysis | Đo lường và phân tích |
| PPQA | Process & Product QA | Đảm bảo chất lượng quy trình |

**Support (SUP) — 4 PAs:**

| PA | Tên đầy đủ | Mục đích |
|----|-----------|---------|
| CM | Configuration Management | Quản lý cấu hình, version control |
| DAR | Decision Analysis & Resolution | Phân tích quyết định |
| SAM | Supplier Agreement Mgmt | Quản lý thỏa thuận nhà cung cấp |
| SEC | Information Security | Bảo mật thông tin |

### 2.2 Tailoring theo quy mô dự án

| Size | Tiêu chí | Ứng dụng |
|------|---------|---------|
| **S (Small)** | < 100 MD, <= 3 người, < 2 tháng | Bug fixes, minor enhancements |
| **M (Medium)** | 100-500 MD, 4-10 người, 2-6 tháng | Feature development, module mới |
| **L (Large)** | > 500 MD, > 10 người, > 6 tháng | Sản phẩm mới, platform migration |

**Ma trận Tailoring (ví dụ nhóm PJM):**

| Process | Size S | Size M | Size L |
|---------|--------|--------|--------|
| Project Initiation | Lite (3 steps) | Standard (6 steps) | Full (6 steps) |
| Estimation | Expert judgment | PERT/Analogy | Full (historical data) |
| Monitoring | Weekly email | Weekly report | Report + Dashboard |
| Risk Management | Checklist only | Monthly review | Weekly review |
| PPQA Audit | Giữa + Cuối dự án | Monthly | Bi-weekly |

**Tương tự cho nhóm ENG:** Size S dùng User Stories + PR review, Size M dùng SRS Lite + HLD Lite + Coverage, Size L dùng Full SRS + Full HLD/LLD + Full test suite.

### 2.3 Process Flow — Từ POL đến GLN

```
POL "Chất lượng là #1"
 |-> PRC "Code Review: 5 bước"
      |-> RUL "<=200 LOC/hr"     (ngưỡng bắt buộc)
      |-> TPL "MR Template"      (biểu mẫu chuẩn)
      |-> CHK "[x] Logic? [x] Naming? [x] Test?" (kiểm tra)
           |-> GLN "Cách review hiệu quả: đọc context trước, focus logic..."
```

### 2.4 Process Areas BẮT BUỘC cho mọi dự án

Theo PAL, tất cả dự án outsource Nhật Bản PHẢI áp dụng:

```
BẮT BUỘC (tất cả dự án):
  +-----+------+------+------+------+------+------+
  | REQM|  TS  | VER  |  PP  | PMC  | PPQA |  CM  |
  +-----+------+------+------+------+------+------+
  | Yêu | Thiết| Kiểm | Kế   | Giám | Đảm  | Quản |
  | cầu | kế   | thử  | hoạch| sát  | bảo  | lý   |
  |     | Code |      |      |      | CL   | config|
  +-----+------+------+------+------+------+------+

THÊM cho dự án lớn (> 6 tháng):
  +-----+------+------+------+
  | IPM | RSKM |  MA  | CAR  |
  +-----+------+------+------+

THÊM khi có nhà cung cấp:
  +-----+
  | SAM |
  +-----+
```

### 2.5 Cross-Area Integration

Các Process Area liên kết với nhau tạo thành hệ thống hoàn chỉnh:

```
PP (Kế hoạch)
  |-- scope/schedule --> TS (Thiết kế/Coding)
  |-- test plan -------> VER (Kiểm thử)
  |-- UAT plan --------> VAL (Thẩm định)
                              |
                              | metrics
                              v
                         MA (Đo lường & Phân tích)
                         |-- Moving Average 4 kỳ
                         |-- RAG: Xanh <10%, Vàng 10-20%, Đỏ >20%
                         |-- Vàng 3 kỳ liên -> tự động Đỏ
                              |
                              | metrics đã phân tích
                              v
                         PMC (Giám sát & Điều khiển)
                         |-- Escalation timeline
                         |-- Hành động khắc phục
```

### 2.6 Metrics & RAG Status

| Vùng | Ngưỡng | Hành động |
|------|--------|----------|
| **Xanh (Green)** | Sai lệch < 10% | Tiếp tục giám sát bình thường |
| **Vàng (Amber)** | Sai lệch 10-20% | Cần chú ý, lập kế hoạch phòng ngừa |
| **Đỏ (Red)** | Sai lệch > 20% HOẶC Vàng 3 kỳ liên | Can thiệp ngay, escalate |

**Moving Average:** `MA(t) = (X(t) + X(t-1) + X(t-2) + X(t-3)) / 4` — Dùng MA 4 kỳ để loại bỏ biến động ngắn hạn, tập trung xu hướng thực sự. Vàng 3 kỳ liên tiếp tự động chuyển Đỏ.

---

## 3. Chiến lược & Dẫn dắt (L3)

### 3.1 Process Improvement Governance

**Vòng đời cải tiến quy trình (5 bước):**

```
B1: THU THẬP FEEDBACK
    |-- PPQA Audit findings
    |-- CAR (Root Cause Analysis)
    |-- Project Retrospectives
    |-- Team suggestions
    |-- Metrics vùng Red/Yellow
         |
B2: ĐÁNH GIÁ & ƯU TIÊN
    |-- Ma trận Tác động/Effort
    |   +------------------+------------------+
    |   | THẮNG NHANH      | CHIẾN LƯỢC       |
    |   | (High Impact,    | (High Impact,    |
    |   |  Low Effort)     |  High Effort)    |
    |   +------------------+------------------+
    |   | TIỆN THỂ         | TỪ CHỐI          |
    |   | (Low Impact,     | (Low Impact,     |
    |   |  Low Effort)     |  High Effort)    |
    |   +------------------+------------------+
    |-- Scoring: ROI + Phạm vi + Rủi ro >= 10 điểm mới triển khai
         |
B3: TRIỂN KHAI CẢI TIẾN
    |-- Soạn thảo thay đổi
    |-- AI Quality Check (BẮT BUỘC cho new/updated process)
    |-- Peer review với EPG
    |-- Pilot test 1-2 dự án (tối thiểu 1 tháng)
         |
B4: DEPLOY & COMMUNICATE
    |-- Cập nhật PAL
    |-- Email thông báo + ngày hiệu lực
    |-- Training cho team bị ảnh hưởng
    |-- Kênh hỗ trợ Q&A
         |
B5: ĐÁNH GIÁ HIỆU QUẢ
    |-- Adoption rate >= 80% sau 3 tháng
    |-- Compliance >= 90% sau 6 tháng
    |-- Feedback tích cực >= 60%
    |-- Quyết định: Giữ / Tinh chỉnh / Rollback
```

### 3.2 PAL Versioning — Patch vs Major

| Loại | Khi nào | Ví dụ |
|------|---------|-------|
| **Patch** (1.0 -> 1.1) | Typo fixes, clarifications | Sửa lỗi chính tả trong template |
| **Major** (1.x -> 2.0) | Thêm/xóa sections, đổi ngưỡng | Thêm bước mới vào quy trình, đổi review threshold |

**Quy tắc version PAL:**
- PAL được review và cập nhật major (v2.0, v3.0) định kỳ **6 tháng 1 lần**
- Chỉ cập nhật dựa trên cải tiến đã Pilot thành công
- Mọi thay đổi Policy cấp 100 PHẢI có chữ ký CEO

### 3.3 Pilot Validation

**Tiêu chí pilot:**
- Chọn 1-2 dự án thử (đa dạng: 1 nhỏ + 1 trung bình)
- Thời gian: tối thiểu 1 tháng (hoặc 2 Sprint)
- Thu thập metrics so sánh (Trước vs Sau)
- Feedback tích cực >= 60%
- Không có vấn đề blocking
- Effort thực hiện trong phạm vi dự kiến (+/- 20%)

### 3.4 Feedback Loop: PPQA -> CAR -> OPF -> OPD

```
+-------+     findings     +-------+    root causes    +-------+
| PPQA  |----------------->|  CAR  |------------------>|  OPF  |
| Audit |                  | Root  |                   | Cải   |
|       |                  | Cause |                   | tiến  |
+-------+                  +-------+                   +---+---+
                                                           |
    +---------+    updated processes    +-------+           |
    | Projects|<-----------------------|  OPD  |<----------+
    | áp dụng |                        | Định  |  process
    | quy trình|                       | nghĩa |  updates
    +---------+                        +-------+

Luồng chi tiết:
  1. PPQA audit phát hiện non-conformance tại dự án X
  2. CAR phân tích nguyên nhân gốc (5-Whys, Fishbone)
  3. OPF đề xuất cải tiến quy trình (Improvement Backlog)
  4. EPG thiết kế thay đổi, pilot test
  5. OPD cập nhật PAL (Process, Template, Rule...)
  6. Deploy và training cho tất cả dự án
  7. PPQA audit lại để xác minh hiệu quả
  => Vòng lặp liên tục (Kaizen cycle)
```

### 3.5 Governance — Xem xét định kỳ

| Cấp độ | Tần suất | Nội dung | Người chủ trì |
|--------|---------|---------|--------------|
| Project-level | Sprint Retro / Monthly | Cải tiến cụ thể cho dự án | PM |
| Organization-level | Quarterly | Review PAL, metrics, audit results | EPG |
| Strategic | Annual | Định hướng chiến lược, OKRs | CEO/Steering Committee |

**Quy định:** Steering Committee chủ trì xem xét mỗi QUÝ. Thay đổi Policy cấp 100 cần CEO ký duyệt.
**Nguồn feedback:** PPQA Audit, CAR Records, Retrospectives, Metrics Dashboard, Team Suggestions.

## 4. Tự kiểm tra

### Bài tập 1: Phân loại tài liệu (L1)

Cho các tài liệu sau, xác định loại (POL/PRC/TPL/RUL/CHK/GLN):

| Tài liệu | Mô tả | Loại? |
|----------|-------|-------|
| A | "Chất lượng sản phẩm phải đạt tiêu chuẩn Nhật Bản" | ??? |
| B | "Bước 1: Tạo branch -> Bước 2: Code -> Bước 3: Tạo MR -> Bước 4: Review -> Bước 5: Merge" | ??? |
| C | "[x] Logic correct? [x] Naming standard? [x] Test passed?" | ??? |
| D | "Code review tối đa 200 LOC/giờ" | ??? |
| E | "[Project Name] [Date] [Author] [Reviewer]" (form trống) | ??? |
| F | "Cách review code hiệu quả: đọc context trước, focus logic..." | ??? |

**Đáp án:** A=POL, B=PRC, C=CHK, D=RUL, E=TPL, F=GLN

### Bài tập 2: Map dự án vào CMMI Process Areas (L2)

**Tình huống:** Dự án Size M (300 MD), 8 người, 5 tháng. Phát triển module báo cáo cho khách hàng Nhật. Mô hình Hybrid.

**Yêu cầu:**
1. Liệt kê tất cả Process Areas BẮT BUỘC áp dụng
2. Xác định tailoring level cho mỗi process
3. Chọn 5 metrics chính để theo dõi (áp dụng GQM)
4. Thiết kế lịch PPQA audit

### Bài tập 3: Thiết kế Process Improvement (L3)

**Tình huống:** PPQA audit phát hiện 3 dự án liên tiếp bị trễ tiến độ > 15% ở phase Integration Test. CAR xác định nguyên nhân: test case viết trễ, không có tiêu chuẩn test case.

**Yêu cầu:**
1. Đề xuất cải tiến (quy trình mới? cập nhật quy trình cũ? template mới?)
2. Lập kế hoạch pilot (dự án nào? thời gian? metrics?)
3. Thiết kế kế hoạch deploy và training
4. Xác định tiêu chí đánh giá hiệu quả

---

## 5. Tài liệu tham khảo

### Từ kho CMMI PAL (247 tài liệu)
- **README.md** — Tổng quan PAL, cấu trúc, naming convention
- **PRC-PMG-OPF-01** — Process Improvement Process (5 bước)
- **PRC-PMG-OPF-03** — Governance Process (Strategic planning, monitoring)
- **GLN-PMG-OPD-01** — Tailoring Guidelines (Ma trận S/M/L)
- **GLN-PMG-OPF-01** — Process Improvement Guide (Impact/Effort matrix)
- **GLN-PMG-MA-01** — Metrics Selection Guide (GQM, SMART, RAG)
- **RUL-PMG-OPF-01** — Process Improvement Rule (Scoring >= 10, Pilot BẮT BUỘC)
- **RUL-PMG-OPF-03** — Governance Rule (Quarterly review, CEO approval)

### Từ khung năng lực PM
- **Competency #4** — 品質管理 (Quản lý chất lượng) — 12% trọng số
- **Competency #6** — Agile/Scrum/Kanban — Sprint Review, DOD, Velocity
- **SYP03 Phần 6** — Giám sát & Điều chỉnh

### Tham khảo ngoài
- CMMI-DEV v2.0 Model (ISACA/CMMI Institute), Process Improvement Essentials (Persse 2006)
