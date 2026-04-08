# Measurement & Analysis (Đo lường và Phân tích)

> **Mục tiêu:** Nắm vững quy trình đo lường, thiết lập ngưỡng chỉ số, phân tích xu hướng và đưa ra quyết định dựa trên dữ liệu (data-driven decisions) trong dự án outsource Nhật Bản
> **Level:** L1 -> L2 -> L3
> **Thời gian đọc:** ~25 phút
> **Liên quan:** PM Competency #4 (品質管理), CMMI PA: PMG-MA (Measurement & Analysis)

---

## 1. Khái niệm cơ bản (L1)

### 1.1 Tại sao cần đo lường?

Trong dự án outsource Nhật Bản, khách hàng yêu cầu **説明できる品質** (chất lượng có thể giải thích được). PM không thể bảo "chất lượng tốt" mà không có số liệu cụ thể. Đo lường giúp:

- **Biết dự án đang ở đâu:** Tiến độ thật sự so với kế hoạch
- **Phát hiện vấn đề sớm:** Trước khi trở thành khủng hoảng
- **Ra quyết định dựa trên dữ liệu:** Không dựa vào cảm tính
- **Báo cáo chuyên nghiệp:** Khách hàng Nhật đánh giá cao báo cáo có số liệu

### 1.2 Ba loại metric cơ bản cần thu thập

**A. Tiến độ (Schedule):**

| Metric | Công thức | Ví dụ |
|--------|-----------|-------|
| Schedule Variance (SV) | (Thực tế - Kế hoạch) / Kế hoạch x 100% | Xong 40/50 tasks = -20% (trễ) |
| Velocity | Story Points hoàn thành / Sprint | Sprint 3 = 28 SP, Sprint 4 = 25 SP |
| Milestone completion | Số milestone đúng hạn / Tổng milestone | 3/4 = 75% |

**B. Chất lượng (Quality):**

| Metric | Công thức | Ví dụ |
|--------|-----------|-------|
| Bug count | Số bug phát hiện theo phase | UT: 15, IT: 8, ST: 3 |
| Defect Density | Bug / KLOC | 25 bugs / 8 KLOC = 3.1 bug/KLOC |
| Test pass rate | Test cases pass / Total test cases | 180/200 = 90% |

**C. Năng suất (Productivity):**

| Metric | Công thức | Ví dụ |
|--------|-----------|-------|
| Team velocity | SP completed / Sprint | Trung bình 26 SP/Sprint |
| Effort variance | (Actual effort - Planned effort) / Planned x 100% | (110 MD - 100 MD) / 100 = +10% |

### 1.3 Quy trình đo lường 4 bước (PRC-PMG-MA-01)

```
BƯỚC 1: ĐỊNH NGHĨA METRICS (Cần đo gì? Tại sao?)
  |
BƯỚC 2: THIẾT LẬP THU THẬP (Tự động hay thủ công?)
  |
BƯỚC 3: THU THẬP & PHÂN TÍCH (Xu hướng, sai lệch)
  |
BƯỚC 4: BÁO CÁO & HÀNH ĐỘNG (Green/Yellow/Red)
  |
  (Vòng lặp: Đánh giá lại chỉ số hàng quý)
```

### 1.4 Phương pháp GQM (Goal-Question-Metric)

Trước khi chọn metric, dùng GQM để đảm bảo metric có mục đích:

| Goal (Mục tiêu) | Question (Câu hỏi) | Metric (Chỉ số) |
|------------------|--------------------|-----------------|
| Kiểm soát tiến độ | Dự án có đúng tiến độ không? | Schedule Variance (%) |
| Đảm bảo chất lượng | Chất lượng mã nguồn chấp nhận được không? | Defect Density (bug/KLOC) |
| Tối ưu nguồn lực | Ước lượng có chính xác không? | Estimation Accuracy (%) |
| Hài lòng khách hàng | Khách hàng có hài lòng không? | Customer Satisfaction Score (/5) |

---

## 2. Thực hành nâng cao (L2)

### 2.1 Ngưỡng chỉ số bắt buộc (RUL-PMG-MA-01)

#### A. Ngưỡng sai lệch - Vùng RAG (Red/Amber/Green)

| Vùng | Sai lệch | Hành động |
|------|----------|-----------|
| **Green (Xanh)** | < 10% | Không cần hành động, tiếp tục giám sát |
| **Yellow (Vàng)** | 10% - 20% | PM BẮT BUỘC báo cáo vào Watch-list, chuẩn bị phương án dự phòng |
| **Red (Đỏ)** | > 20% | BẮT BUỘC phân tích CAR, lập kế hoạch khắc phục trong 48h |

**Quy tắc tự động chuyển Đỏ:** Nếu chỉ số ở vùng Vàng liên tục 3 kỳ --> TỰ ĐỘNG chuyển sang trạng thái Đỏ.

Ví dụ: SV = 12%, 14%, 15% (3 kỳ liên tiếp Yellow) --> Chuyển sang Red dù chưa vượt 20%.

#### B. Ngưỡng chất lượng Review/Test (theo công đoạn)

**Design Review (Basic/Detail Design) -- Đơn vị: shiteki/Page:**

| Chỉ số | Ngưỡng dưới | Ngưỡng trên |
|--------|-------------|-------------|
| Self-check density | 0.5 | 1 |
| Internal review density | 0.25 | 0.5 |
| Customer review density | 0.05 | 0.1 |

**Code Review -- Đơn vị: shiteki/KLOC:**

| Chỉ số | Ngưỡng dưới | Ngưỡng trên |
|--------|-------------|-------------|
| Self-check density | 7 | 10 |
| Internal review density | 3 | 7 |
| Customer review density | 0.5 | 1 |

**Test Case Density -- Đơn vị: case/KLOC, Bug/KLOC:**

| Chỉ số | Đơn vị | Ngưỡng dưới | Ngưỡng trên |
|--------|--------|-------------|-------------|
| Test case density | case/KLOC | 70 | 100 |
| Bug density | Bug/KLOC | 2 | 5 |

**Cách đọc ngưỡng:**
- Giá trị < Ngưỡng dưới: Review/test chưa đủ kỹ --> kiểm tra lại quy trình
- Giá trị trong ngưỡng: Đạt yêu cầu chất lượng
- Giá trị > Ngưỡng trên: Chất lượng đầu vào kém hoặc tiêu chuẩn quá nghiêm ngặt

### 2.2 Trung bình trượt (Moving Average) và Phân tích xu hướng

**KHÔNG BAO GIỜ** chỉ dựa trên 1 data point. PHẢI tính Moving Average của 4 kỳ gần nhất:

```
MA(t) = (X(t) + X(t-1) + X(t-2) + X(t-3)) / 4
```

**Ví dụ thực tế dự án 6 tháng:**

| Kỳ | SV thực tế | MA (4 kỳ) | Vùng | Nhận xét |
|----|-----------|-----------|------|----------|
| T1 | 5% | - | - | Chưa đủ dữ liệu |
| T2 | 8% | - | - | |
| T3 | 12% | - | - | |
| T4 | 10% | 8.75% | Green | MA vùng Xanh |
| T5 | 15% | 11.25% | Yellow | MA chuyển Vàng --> Watch-list |
| T6 | 18% | 13.75% | Yellow | MA vùng Vàng (kỳ 2) |
| T7 | 14% | 14.25% | **RED** | MA vẫn Vàng kỳ 3 --> Tự động chuyển Đỏ |

--> Tại T7, dù SV giảm còn 14%, nhưng đã 3 kỳ liên tiếp Yellow --> Tự động escalate lên Red.

### 2.3 Response Timeline khi vùng Đỏ

Khi bất kỳ metric nào rơi vào vùng Đỏ:

| Thời gian | Hành động bắt buộc |
|-----------|-------------------|
| **4 giờ** | PM PHẢI thông báo PMO |
| **48 giờ** | PHẢI nộp Corrective Action Plan đã được duyệt |
| **1 tuần** | PHẢI có buổi họp Review đặc biệt đánh giá hiệu quả hành động |
| **Đồng thời** | Thông báo khách hàng trong 2h khi trạng thái Đỏ (theo RUL-PJM-PMC-01) |

### 2.4 Phân tích sai lệch (Variance Analysis)

Khi phát hiện sai lệch, thực hiện 5 bước:

1. **Xác nhận sai lệch:** Kiểm tra dữ liệu có chính xác không (loại trừ lỗi nhập liệu)
2. **Phân loại mức độ:** Green / Yellow / Red
3. **Xác định nguyên nhân gốc:** Sử dụng 5-Whys hoặc Fishbone
4. **Đề xuất hành động:** Dựa trên nguyên nhân, KHÔNG chỉ triệu chứng
5. **Theo dõi hiệu quả:** Đánh giá sau 1-2 kỳ

**Ví dụ 5-Whys cho SV = 25% (Đỏ):**

```
Vấn đề: SV = 25% (Đỏ)
Why 1: Tại sao trễ tiến độ? --> Module X chưa hoàn thành
Why 2: Tại sao Module X trễ? --> Thiếu 1 developer
Why 3: Tại sao thiếu? --> Developer chuyển sang dự án khác
Why 4: Tại sao chuyển? --> Dự án khác escalate khẩn cấp
Why 5: Tại sao không có người thay? --> KHÔNG có kế hoạch backup

--> Nguyên nhân gốc: Thiếu resource planning / backup plan
--> Hành động: Bổ sung resource, cập nhật resource plan có backup
```

### 2.5 Phân tích tương quan

Tìm mối quan hệ giữa các chỉ số để hiểu bức tranh toàn cảnh:

| Chỉ số A | Chỉ số B | Mối quan hệ kỳ vọng |
|----------|----------|---------------------|
| Test Coverage tăng | Defect Density giảm | Test nhiều hơn --> ít lỗi hơn |
| Velocity tăng | Defect Escape Rate tăng | Nhanh hơn --> có thể nhiều lỗi lọt |
| Estimation Accuracy giảm | SV/EV tăng | Ước lượng kém --> sai lệch lớn |

**Lưu ý:** Tương quan KHÔNG phải nhân quả. Cần phân tích thêm trước khi kết luận.

---

## 3. Chiến lược & Dẫn dắt (L3)

### 3.1 EAC/ETC Forecasting (Dự báo nghị trạng)

Khi dự án đã chạy được 40-60%, PM có đủ dữ liệu để dự báo:

**EAC (Estimate at Completion):** Tổng chi phí/effort dự kiến khi kết thúc dự án

```
EAC = Actual Cost + (Budget - Earned Value) / CPI
     Hoặc đơn giản:
EAC = Budget / CPI  (nếu xu hướng hiện tại tiếp tục)
```

**ETC (Estimate to Complete):** Effort còn lại cần để hoàn thành

```
ETC = EAC - Actual Cost
```

**Ví dụ:** Dự án budget 100 MD, đã dùng 60 MD, nhưng chỉ hoàn thành 50% (EV = 50 MD)
- CPI = EV / AC = 50/60 = 0.83 (đang vượt budget)
- EAC = 100 / 0.83 = **120 MD** (dự kiến vượt 20%)
- ETC = 120 - 60 = **60 MD** còn lại

--> PM báo cáo: "Dự án sẽ vượt 20% effort. Cần tăng 2 developer hoặc giảm scope."

### 3.2 Thiết kế Metrics Framework cho tổ chức

Khi lên L3, PM không chỉ đo lường cho dự án mà góp phần thiết kế framework cho toàn tổ chức:

**Bộ chỉ số theo quy mô dự án:**

| Quy mô | Chỉ số bắt buộc | Chỉ số tùy chọn |
|--------|----------------|-----------------|
| **Size S** (<100 MD) | SV, EV, Defect count | Velocity (nếu Agile) |
| **Size M** (100-500 MD) | SV, EV, DD, Test Coverage | CPI, SPI, Customer Satisfaction |
| **Size L** (>500 MD) | Toàn bộ bắt buộc + EVM (CPI, SPI, EAC) | Tất cả tùy chọn |

### 3.3 Organizational Measurement Repository (OMR)

OMR là kho dữ liệu đo lường cấp tổ chức, lưu trữ metrics lịch sử từ tất cả dự án:

| Loại dữ liệu | Ví dụ | Cập nhật khi |
|--------------|-------|-------------|
| Effort data | Effort thực tế theo phase (BD, DD, Coding, Test) | Đóng dự án/milestone |
| Quality data | Defect density, distribution by phase, severity | Đóng dự án/milestone |
| Productivity | FP/MD, LOC/MD theo technology stack | Đóng dự án |
| Estimation accuracy | Planned vs actual effort, schedule | Đóng dự án |

**Cách sử dụng OMR cho dự án mới:**
1. Tìm dự án tương tự trong OMR (cùng technology, domain, team size)
2. Lấy productivity baseline: "Java web app trung bình = 8 FP/MD"
3. Điều chỉnh theo đặc thù dự án (team mới x1.2, technology mới x1.5)
4. Ghi nhận nguồn: "Estimation dựa trên OMR Q4/2025, dự án XYZ"

### 3.4 Báo cáo theo đối tượng

| Đối tượng | Nội dung | Tần suất | Mức chi tiết |
|----------|---------|----------|-------------|
| **Team** | Dashboard thời gian thực | Hàng ngày | Chi tiết |
| **PM** | Bảng tổng hợp + sai lệch | Hàng tuần | Trung bình |
| **PMO / Stakeholder** | Tóm tắt trạng thái + hành động | Hàng tuần/tháng | Tổng quan |
| **Ban Giám đốc** | KPI tổ chức + xu hướng | Hàng quý | Tóm lược |

### 3.5 Anti-patterns cần tránh

| Anti-pattern | Vấn đề | Cách khắc phục |
|-------------|--------|----------------|
| Thu thập nhưng không phân tích | Tốn effort không có giá trị | Mỗi chỉ số PHẢI có người đọc và hành động |
| Quá nhiều chỉ số | Mất tập trung | Giới hạn 5-10 KPIs cho mỗi dự án |
| Dùng chỉ số để đổ lỗi | Team sợ, làm sai lệch dữ liệu | Tập trung cải tiến quy trình, không cá nhân |
| Mục tiêu phi thực tế | Team mất động lực | Dựa trên baseline + cải thiện dần |
| Chỉ đo cuối dự án | Quá muộn để hành động | Đo thường xuyên (hàng tuần) |

---

## 4. Tự kiểm tra

### Bài tập 1: Xây dựng Metrics Dashboard (L1-L2)

**Tình huống:** Bạn quản lý dự án Size M, Agile/Scrum, 6 tháng, team 8 người, khách hàng Nhật.

**Yêu cầu:**
1. Dùng GQM xác định 5 metrics cần thiết cho dự án
2. Thiết lập ngưỡng RAG cho từng metric (dựa trên RUL-PMG-MA-01)
3. Tính Moving Average cho dữ liệu sau và xác định trạng thái:

| Sprint | Velocity (SP) | Bug Density (bug/KLOC) | SV (%) |
|--------|--------------|----------------------|--------|
| S1 | 20 | 3.0 | 5% |
| S2 | 22 | 4.2 | 8% |
| S3 | 18 | 3.5 | 12% |
| S4 | 16 | 5.8 | 15% |
| S5 | 19 | 4.0 | 18% |
| S6 | 15 | 6.2 | 22% |

4. Xác định metric nào cần escalate và hành động cụ thể

### Bài tập 2: EAC Forecasting (L3)

**Tình huống:** Dự án đã chạy 4/8 tháng:
- Budget: 200 man-day
- Actual Cost (AC): 120 man-day
- Planned Value (PV): 100 man-day (50% kế hoạch)
- Earned Value (EV): 80 man-day (40% khối lượng thực tế)

**Yêu cầu:**
1. Tính CPI, SPI
2. Tính EAC, ETC
3. Viết email báo cáo cho khách hàng Nhật về tình trạng dự án (Hou-Ren-Sou format)
4. Đề xuất ít nhất 2 phương án xử lý

### Đáp án tham khảo Bài tập 1:

**MA cho SV tại S4-S6:**
- MA(S4) = (5+8+12+15)/4 = 10% --> Yellow
- MA(S5) = (8+12+15+18)/4 = 13.25% --> Yellow (kỳ 2)
- MA(S6) = (12+15+18+22)/4 = 16.75% --> Yellow (kỳ 3) --> **TỰ ĐỘNG RED**

**Hành động:** Thông báo PMO trong 4h, nộp Corrective Action Plan trong 48h.

---

## 5. Tài liệu tham khảo

| Tài liệu | Vai trò |
|----------|---------|
| PRC-PMG-MA-01 | Quy trình Đo lường và Phân tích (4 bước) |
| RUL-PMG-MA-01 | Ngưỡng chỉ số, vùng RAG, Moving Average, Response Timeline |
| GLN-PMG-MA-01 | Hướng dẫn chọn chỉ số (GQM, SMART), phân tích xu hướng, báo cáo |
| TPL-PMG-MA-01 | Mẫu kế hoạch đo lường |
| TPL-PMG-MA-02 | Mẫu báo cáo chỉ số |
| TPL-PMG-MA-03~11 | Báo cáo chất lượng theo công đoạn (BD, DD, Coding, TC, Bug) |
| CHK-PMG-MA-01 | Checklist chất lượng chỉ số |
| GLN-PMG-OPF-02 | Governance Guide - Dashboard quản trị, RAG system |
