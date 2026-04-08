# Business Acumen for Engineers

> **Mục tiêu:** Phát triển tư duy kinh doanh cho kỹ sư IT để đóng góp giá trị cao hơn trong dự án outsource
> **Level:** L1 → L2 → L3
> **Thời gian đọc:** ~15 phút
> **Liên quan:** PM Competency #1 (計画・見積力), #2 (要件管理), #7 (ステークホルダー管理)

---

## 1. Khái niệm cơ bản (L1)

### 1.1 Tại sao Engineer cần hiểu Business?

Trong môi trường outsource Nhật Bản, khách hàng không chỉ cần code chạy đúng. Họ cần:
- **QCD balance:** Quality - Cost - Delivery phải cân bằng
- **Business value:** Feature nào mang lại giá trị kinh doanh nhất?
- **Explainable decisions:** Tại sao chọn solution A thay vì B? (説明できる品質)

Engineer hiểu business sẽ:
- Ưu tiên đúng feature quan trọng cho khách hàng
- Giao tiếp hiệu quả hơn với PM và khách hàng
- Đề xuất giải pháp tối ưu về chi phí và thời gian
- Được khách hàng tin tưởng và đánh giá cao hơn

### 1.2 QCD — Tam giác Chất lượng, Chi phí, Thời hạn

| Thành phần | Tiếng Nhật | Ý nghĩa | Ví dụ |
|------------|-----------|---------|-------|
| **Quality** | 品質 (Hinshitsu) | Chất lượng sản phẩm | Bug density, test coverage, code quality |
| **Cost** | コスト (Kosuto) | Chi phí dự án | Man-month, license, infrastructure |
| **Delivery** | 納期 (Nouki) | Thời hạn giao hàng | Sprint deadline, release date, milestone |

**Nguyên tắc:** Không thể có cả 3 ở mức cao nhất. Khi 1 thay đổi, ít nhất 1 cái khác phải điều chỉnh.

| Tình huống | Điều chỉnh |
|-----------|-----------|
| Khách thêm feature (Scope +) | Tăng cost HOẶC lùi deadline HOẶC giảm quality cho feature khác |
| Khách rút deadline (Time -) | Giảm scope HOẶC tăng cost (thêm resource) HOẶC chấp nhận quality thấp hơn |
| Khách cắt budget (Cost -) | Giảm scope HOẶC lùi deadline |

### 1.3 Customer Perspective — Góc nhìn khách hàng

**Hiểu người dùng cuối (End User):**
- Khách hàng của bạn (công ty Nhật) có khách hàng của họ
- Feature bạn làm phục vụ ai? Giải quyết vấn đề gì?
- Ưu tiên: feature ảnh hưởng nhiều người dùng > feature cho 1 người

**Business Process Flow:**
- Trước khi code, hiểu quy trình nghiệp vụ
- Ví dụ: Nếu làm system quản lý kho hàng (WMS)
  - Nhập kho → Lưu kho → Xuất kho → Kiểm kê → Báo cáo
  - Mỗi bước có quy tắc riêng, constraint riêng
  - Hiểu flow này giúp code đúng và đề xuất cải tiến

**Hỏi đúng câu hỏi:**
- "Feature này giúp user giải quyết vấn đề gì?"
- "Ai là người sử dụng chính của chức năng này?"
- "Nếu không có feature này, user làm thế nào?"
- "Tần suất sử dụng feature này như thế nào?"

### 1.4 Success Criteria — Định nghĩa thành công

Mỗi dự án/feature cần có tiêu chí thành công đo lường được:

| Loại | Ví dụ | Cách đo |
|------|-------|---------|
| **Functional** | Tất cả requirement đã implement | Requirement coverage 100% |
| **Quality** | Bug density < target | Bug density = bugs / KLOC |
| **Performance** | Response time < 3s | Load test result |
| **User** | User hài lòng | User acceptance test pass rate |
| **Schedule** | Giao đúng hạn | Actual vs planned delivery date |
| **Cost** | Trong budget | Actual effort vs estimated effort |

---

## 2. Thực hành nâng cao (L2)

### 2.1 ROI & Cost-Benefit Analysis

**ROI (Return on Investment) = (Lợi ích - Chi phí) / Chi phí x 100%**

**Ví dụ: Có nên đầu tư vào Automation Testing?**

| Hạng mục | Giá trị |
|----------|---------|
| **Chi phí đầu tư** | |
| Setup framework + training | 15 man-day |
| Viết automation test cases | 20 man-day |
| Bảo trì hàng tháng | 2 man-day/tháng |
| **Tổng chi phí (1 năm)** | **59 man-day** |
| | |
| **Lợi ích** | |
| Giảm manual regression test | -8 man-day/sprint x 12 sprints = 96 man-day |
| Giảm bug lọt qua test | -5 production bugs x 3 man-day/bug = 15 man-day |
| Faster feedback loop | Khó đo lường, ước tính +10 man-day |
| **Tổng lợi ích (1 năm)** | **121 man-day** |
| | |
| **ROI** | **(121 - 59) / 59 = 105%** |

**Kết luận:** ROI 105% — đáng đầu tư. Hoàn vốn sau khoảng 6 tháng.

**Khi nào KHÔNG nên đầu tư automation:**
- Dự án ngắn (< 3 tháng) — không đủ thời gian hoàn vốn
- UI thay đổi liên tục — chi phí bảo trì cao
- Team không có kỹ năng automation — chi phí training lớn
- Test cases ít và đơn giản — manual nhanh hơn

### 2.2 MVP Identification — Xác định sản phẩm tối thiểu

**MVP (Minimum Viable Product):** Tập hợp feature ít nhất để mang lại giá trị cho người dùng.

**Phương pháp ưu tiên:**

**MoSCoW:**

| Ưu tiên | Ý nghĩa | Ví dụ (System quản lý đơn hàng) |
|---------|---------|-------------------------------|
| **Must have** | Bắt buộc, không có thì không dùng được | Tạo đơn hàng, thanh toán, xác nhận |
| **Should have** | Quan trọng, có thể tạm thời không có | Tìm kiếm nâng cao, báo cáo thống kê |
| **Could have** | Có thì tốt, không có cũng được | Export PDF, email notification |
| **Won't have** | Không làm trong phase này | Mobile app, AI recommendation |

**Nguyên tắc 80/20:** 20% features mang lại 80% giá trị. Xác định và ưu tiên 20% đó.

**Value vs Cost Matrix:**

```
        Giá trị cao
            |
    Quick   |   Big
    Wins    |   Projects
  (Làm ngay)|   (Lên kế hoạch)
            |
 -----------+-----------> Chi phí cao
            |
    Fill    |   Luxury
    Ins     |   (Hoãn lại)
  (Làm khi  |
   rảnh)    |
            |
        Giá trị thấp
```

### 2.3 Scope Management — Quản lý phạm vi

**Khi khách hàng yêu cầu thêm feature (Change Request):**

Quy trình 5 bước (theo CMMI):
1. **Ghi nhận:** `ご要望は承知いたしました` — Xác nhận đã nhận yêu cầu
2. **Đánh giá impact:** Scope, timeline, cost, quality, resource
3. **Phê duyệt:** Trình bày impact, cho khách quyết định
4. **Thực hiện:** Nếu đồng ý, cập nhật plan và thực hiện
5. **Bàn giao:** Xác nhận hoàn thành, cập nhật baseline

**Cách nói "Không" mà vẫn lịch sự (trong context Nhật):**
- KHÔNG nói: "Không làm được" / `無理です`
- NÊN nói: "Đề xuất phương án thay thế"

```
ご要望は承知いたしました。
現在のスケジュール内での実現は難しい状況ですが、
以下の代替案をご検討いただけますでしょうか。

案1: Phase 2 で対応 (品質を維持しつつ、確実に実装)
案2: 一部機能のみ今回対応 (CSV export のみ、PDF は次フェーズ)
案3: 他の機能と入れ替え (優先度の低い○○を次回に回す)
```

### 2.4 Industry Knowledge — Hiểu ngành của khách hàng

| Ngành | Keyword | Điểm cần biết |
|-------|---------|-------------|
| **Manufacturing (製造業)** | 生産管理, 在庫, ロット, 品質管理 | Quy trình sản xuất, Kanban, 5S |
| **Logistics (物流)** | 配送, 倉庫管理, トラッキング | Chuỗi cung ứng, WMS, route optimization |
| **Finance (金融)** | 取引, 決済, セキュリティ, 監査 | Regulation, audit trail, bảo mật nghiêm ngặt |
| **Retail (小売)** | POS, 在庫, 顧客管理, EC | Customer journey, inventory management |
| **Healthcare (医療)** | 電子カルテ, 患者管理, 個人情報 | Data privacy, HIPAA-like regulations |

**Cách tìm hiểu ngành mới:**
1. Đọc tài liệu yêu cầu kỹ (要件定義書) — không chỉ đọc spec, đọc cả context
2. Hỏi BrSE về nghiệp vụ khách hàng
3. Tìm hiểu competitor của khách hàng
4. Đọc báo cáo ngành (industry report)

---

## 3. Chiến lược & Dẫn dắt (L3)

### 3.1 Strategic Thinking — Tư duy chiến lược

**Nhìn xa hơn 1 sprint:**
- Feature này ảnh hưởng gì đến roadmap dài hạn?
- Architecture này có scale được khi user tăng 10x?
- Technical debt này có chấp nhận được không?
- Có nên đầu tư vào platform/framework cho dự án sau?

**Đề xuất proactive cho khách hàng:**
- Phân tích dữ liệu sử dụng để đề xuất cải tiến
- Đề xuất automation cho quy trình manual lặp đi lặp lại
- Đề xuất performance optimization trước khi user phàn nàn
- Đề xuất security hardening trước khi có incident

### 3.2 Financial Awareness — Hiểu biết tài chính dự án

**Các chỉ số tài chính cần biết:**

| Chỉ số | Công thức | Ý nghĩa |
|--------|----------|---------|
| **Budget Variance** | (Actual - Planned) / Planned x 100% | Chênh lệch ngân sách |
| **Cost Performance Index (CPI)** | Earned Value / Actual Cost | < 1.0 = vượt budget |
| **Schedule Performance Index (SPI)** | Earned Value / Planned Value | < 1.0 = trễ tiến độ |
| **Burn Rate** | Chi phí / tháng | Tốc độ "đốt" ngân sách |

**Ví dụ thực tế:**
- Dự án 12 tháng, budget 100 man-month
- Sprint 6 (tháng 6): đã dùng 60 man-month
- Burn rate: 10 man-month/tháng (đúng kế hoạch)
- Còn lại: 40 man-month cho 6 tháng → Đúng budget

Nhưng nếu Sprint 6 đã dùng 70 man-month:
- Burn rate thực tế: 11.7 man-month/tháng
- Dự kiến: 70 + (11.7 x 6) = 140 man-month → VƯỢT 40%
- Cần: giảm scope, tăng efficiency, hoặc xin thêm budget

### 3.3 Refactoring Decisions — Khi nào refactor?

| Tiêu chí | Nên refactor | KHÔNG nên refactor |
|----------|-------------|-------------------|
| **Timeline** | Còn đủ thời gian (> 2 sprints) | Sát deadline |
| **Impact** | Code được dùng lại nhiều lần | Code chỉ dùng 1 lần |
| **Technical debt** | Đang gây bug hoặc slow | Chỉ là "không đẹp" |
| **Team** | Team hiểu code đó | Người viết đã rời team |
| **Business value** | Giảm bug/tăng performance rõ ràng | Không ai phàn nàn |

**Cách trình bày cho khách hàng (tinh thần 説明できる品質):**

```
【提案】コードリファクタリングの実施

背景: Order module の bug density が 2.5件/KLOC
(全体平均 0.8件/KLOC の3倍)

提案: 2 sprint を使ってリファクタリング実施
見込み効果:
- Bug density: 2.5 → 0.8 (-68%)
- 今後の feature 追加工数: -30%
- メンテナンス工数: -50%

リファクタリングしない場合のリスク:
- 毎スプリント追加 bug fix: +3 man-day
- 12ヶ月累計: 36 man-day (リファクタリング工数の2倍)
```

---

## 4. Tự kiểm tra

### Bài tập L1
1. Giải thích tam giác QCD. Khi khách thêm feature nhưng không dời deadline, bạn đề xuất gì?
2. Cho 1 feature list, phân loại theo MoSCoW
3. Định nghĩa 3 tiêu chí thành công cho 1 dự án web application

### Bài tập L2: Tính ROI cho Automation Testing
Dự kiến:
- Chi phí setup: 10 man-day
- Chi phí viết test: 30 man-day/1000 test cases
- Chi phí bảo trì: 3 man-day/tháng
- Lợi ích: giảm 10 man-day manual test/sprint, 12 sprints/năm
- Lợi ích: giảm 8 production bugs/năm x 2 man-day/bug

Tính:
1. Tổng chi phí 1 năm
2. Tổng lợi ích 1 năm
3. ROI
4. Thời gian hoàn vốn (break-even)

### Bài tập L3
1. Dự án 12 tháng đã chạy được 8 tháng. Budget đã dùng 75%. Phân tích tình hình và đề xuất giải pháp
2. Khách hàng muốn thêm module mới, nhưng không dời deadline và budget. Viết email đề xuất 3 phương án với impact analysis

---

## 5. Tài liệu tham khảo

### Tài liệu nội bộ
- PM nang-luc.md: #1 (計画・見積力), #2 (要件管理)
- GLN-PJM-PP-02: Estimation Best Practices Guide
- GLN-PJM-RSKM-01: Risk Management Guide

### Frameworks
- QCD Triangle (Quality-Cost-Delivery)
- MoSCoW Prioritization
- Earned Value Management (EVM)
- Value vs Cost Matrix

### Sách khuyên đọc
- "The Lean Startup" — Eric Ries (MVP concept)
- "Measure What Matters" — John Doerr (OKRs)
- "Software Estimation: Demystifying the Black Art" — Steve McConnell
