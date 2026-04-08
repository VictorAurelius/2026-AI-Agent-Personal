# Stakeholder Management & Leadership (Quản lý Stakeholder và Dẫn dắt)

> **Mục tiêu:** Quản lý kỳ vọng stakeholder, giao tiếp đa văn hóa với khách hàng Nhật, dẫn dắt team offshore, giải quyết xung đột và xây dựng văn hóa chất lượng
> **Level:** L1 -> L2 -> L3 -> L4
> **Thời gian đọc:** ~30 phút
> **Liên quan:** PM Competency #5 (コミュニケーション), #7 (ステークホルダー管理), #8 (リーダーシップ), CMMI PA: PJM-IPM

---

## 1. Khái niệm cơ bản (L1)

### 1.1 Hiểu kỳ vọng của stakeholder

Trong dự án outsource Nhật Bản, PM phải hiểu rõ kỳ vọng của từng stakeholder:

| Stakeholder | Kỳ vọng chính | Điều họ SỢ NHẤT |
|-------------|--------------|-----------------|
| Khách hàng Nhật (PO) | Đúng hạn, đúng chất lượng, báo cáo đều | Bất ngờ (surprise) -- bad news không báo sớm |
| BrSE | PM cung cấp thông tin đầy đủ, đúng format | Thông tin không nhất quán giữa các kênh |
| Dev team | Yêu cầu rõ ràng, hỗ trợ kịp thời | Thay đổi yêu cầu liên tục mà không báo trước |
| QA team | Đủ thời gian test, spec rõ ràng | Bị ép tiến độ, cắt thời gian test |
| Ban Giám đốc | Dự án on-time/on-budget, không escalation | Mất khách hàng, lợi nhuận âm |

### 1.2 Nguyên tắc 報連相 (Hou-Ren-Sou)

Đây là nguyên tắc KHÔNG THỂ THIẾU khi làm việc với khách hàng Nhật:

| Nguyên tắc | Nghĩa | Khi nào | Ví dụ |
|------------|-------|---------|-------|
| **報告 (Houkoku)** | Báo cáo | Sau khi hoàn thành task, hàng tuần | "Sprint 6 hoàn thành 80%, 2 stories chưa xong" |
| **連絡 (Renraku)** | Liên lạc | Khi có thông tin cần chia sẻ | "FYI: 1 PG nghỉ phép 2 ngày tuần sau" |
| **相談 (Soudan)** | Trao đổi | Trước khi quyết định, khi cần ý kiến | "Tôi nghĩ nên dùng approach A, ý kiến anh/chị?" |

**Nguyên tắc quan trọng:**
- Bad news báo SỚM, KHÔNG bao GIỜ giấu
- Khi hỏi (Soudan), PHẢI có phương án đề xuất, không chỉ nêu vấn đề
- Báo cáo (Houkoku) đúng tần suất, đúng format -- khách hàng Nhật đánh giá cao sự nhất quán

### 1.3 Chuẩn bị và tham gia meeting

**Trước meeting:**
- Đọc lại agenda và tài liệu liên quan
- Chuẩn bị số liệu/metrics cần báo cáo
- Liệt kê câu hỏi cần confirm

**Trong meeting:**
- Bắt đầu và kết thúc ĐÚNG GIỜ (người Nhật rất coi trọng)
- Ghi nhận action items: Ai, Việc gì, Deadline
- Không tranh cãi trực tiếp -- dùng offline để thảo luận sau

**Sau meeting:**
- Gửi biên bản trong 24h
- Update action items trong tool
- Follow up action items overdue

---

## 2. Thực hành nâng cao (L2)

### 2.1 Stakeholder Mapping (Ma trận Power/Interest)

```
          Quan tâm CAO              Quan tâm THẤP
Quyền    +-------------------+-------------------+
lực      | QUẢN LÝ CHẶT      | GIỮ HÀI LÒNG      |
CAO      | (Manage Closely)  | (Keep Satisfied)  |
         | VD: Khách hàng PO,| VD: Ban GĐ        |
         | Sponsor           | cấp cao            |
         +-------------------+-------------------+
Quyền    | THÔNG BÁO         | THEO DÕI           |
lực      | (Keep Informed)   | (Monitor)          |
THẤP     | VD: End users,    | VD: HR, Tài        |
         | Team members      | chính              |
         +-------------------+-------------------+
```

**Cách sử dụng:**
1. Liệt kê TẤT CẢ stakeholder
2. Đánh giá Power (1-5) và Interest (1-5) cho từng người
3. Đặt vào ma trận
4. Xác định chiến lược giao tiếp phù hợp cho từng nhóm

**Ví dụ dự án E-commerce, khách Nhật, 8 tháng:**

| Stakeholder | Power | Interest | Chiến lược |
|-------------|-------|----------|-----------|
| Customer PO (Tanaka-san) | Cao | Cao | Họp tuần, báo cáo tuần, Soudan trước quyết định |
| Ban GĐ nội bộ | Cao | Thấp | Báo cáo tháng, escalate khi cần |
| Team dev (4 người) | Thấp | Cao | Daily standup, Sprint review |
| IT Infra | Thấp | Thấp | Thông báo khi cần server/deployment |

### 2.2 Quản lý kỳ vọng (Expectation Management)

PM phải quản lý kỳ vọng trên 4 chiều: Scope, Quality, Timeline, Cost (tam giác QCD).

**Kỹ thuật quản lý kỳ vọng:**

| Chiều | Cách quản lý | Ví dụ cụ thể |
|-------|-------------|-------------|
| Scope | Baseline requirements rõ ràng, change control qua CR log | "CR này +20 MD, cần điều chỉnh timeline hoặc scope" |
| Quality | Thiết lập quality criteria từ đầu, dùng metrics chứng minh | "DD < 5 bug/KLOC, test coverage >= 95%" |
| Timeline | Buffer 10-20%, báo risk sớm, không hứa những gì không chắc | "Sprint này có risk delay module X, đã có mitigation plan" |
| Cost | Track budget thực tế vs kế hoạch, báo sai lệch sớm | "EAC = 120% budget, cần discuss phương án" |

### 2.3 Xung đột và Giải quyết 1-1

**Nguyên nhân xung đột thường gặp:**

| Xung đột | Giữa ai | Giải pháp |
|----------|---------|-----------|
| Scope creep | PM <-> KH | Impact analysis + CR process |
| Chất lượng vs tiến độ | QA <-> Dev | Quality gate không thỏa hiệp, điều chỉnh scope |
| Resource sharing | PM <-> PM khác | Escalate Resource Manager với data cụ thể |
| Tech decision | TL <-> Dev | Decision matrix, team vote, TL final call |

**Quy trình giải quyết 1-1:**
1. Gặp riêng từng bên, lắng nghe THẬT SỰ
2. Xác định mục tiêu chung (thay vì vị trí đối lập)
3. Tìm phương án WIN-WIN (hoặc tối ưu nhất có thể)
4. Ghi nhận thỏa thuận và follow up

### 2.4 Team Onboarding và Delegation

**Onboarding 3 giai đoạn:**

| Giai đoạn | Thời gian | Hoạt động |
|-----------|-----------|-----------|
| Orientation | Ngày 1-2 | Project overview, architecture, workflow, tool setup |
| Shadowing | Tuần 1 | Pair programming, đọc code, tham gia meeting (observer) |
| Independence | Tuần 2 | Assign tasks that (size S-M), code review bởi buddy, 1-on-1 |

**Delegation dựa trên capacity:**

| Capacity member | Delegate gì | Hỗ trợ như thế nào |
|-----------------|------------|---------------------|
| Junior (< 1 năm) | Tasks cụ thể, có hướng dẫn rõ | Code review kỹ, pair programming |
| Mid (1-3 năm) | Tasks phức tạp hơn, ít hướng dẫn | Review deliverable, 1-1 khi cần |
| Senior (> 3 năm) | Module lớn, tự quyết định approach | Review kết quả, delegate sub-tasks |

### 2.5 Ma trận RACI

| Deliverable | PM | TL | BA | QA | Customer |
|------------|-----|-----|-----|-----|----------|
| Project Plan | **A** | C | C | I | **R** (phê duyệt) |
| Requirements | C | C | **R** | I | **A** |
| Architecture | I | **R** | C | I | I |
| Test Plan | I | C | I | **R** | **A** |
| Status Report | **R** | C | I | I | **A** |

**Nguyên tắc:** Mỗi dòng chỉ có ĐÚNG 1 chữ A (trách nhiệm rõ ràng).

---

## 3. Chiến lược & Dẫn dắt (L3)

### 3.1 Đàm phán trực tiếp (Direct Negotiation)

Khi khách hàng gửi Change Request, PM L3 đàm phán trực tiếp:

**Ví dụ CR Negotiation:**

Khách hàng muốn thêm export CSV/PDF + tăng template từ 5 lên 10.
PM estimate: +20 man-day (= 1 sprint full team). Deadline và budget không đổi.

**Bước 1 - Impact Analysis 5 chiều:**

| Chiều | Impact |
|-------|--------|
| Scope | +2 features mới (CSV export, PDF export, 5 templates mới) |
| Timeline | +1 sprint (2 tuần) nếu giữ nguyên team |
| Cost | +20 MD = khoảng $X |
| Quality | Giảm thời gian test 1 sprint, risk tăng bug |
| Resource | Cần thêm 1 frontend developer |

**Bước 2 - Đề xuất 3 phương án:**

| Phương án | Mô tả | Pros | Cons |
|-----------|-------|------|------|
| A: Accept all | Làm hết, lùi deadline 2 tuần | KH hài lòng về scope | Trễ deadline, risk chất lượng |
| B: Partial accept | CSV export + 3 templates mới | Giữ deadline, 70% nhu cầu KH | KH phải đợi PDF + 2 templates |
| C: Defer | Đưa vào Phase tiếp theo | Giữ deadline + chất lượng | KH phải chờ thêm |

**Bước 3 - Recommend với lý do:** "Chúng tôi recommend Phương án B vì giữ được deadline (KH đã cam kết với end-user), giao 70% giá trị, và đảm bảo chất lượng. Phần còn lại đưa vào Sprint đầu Phase 2."

### 3.2 Xây dựng High-performing Team

**Mục tiêu PM L3:** Team tự động hóa, PM chỉ cần giám sát và hỗ trợ.

**4 trụ cột:**

| Trụ cột | Hành động cụ thể |
|---------|-----------------|
| Psychological Safety | Cho phép sai lầm, không blame. Khuyến khích báo bad news sớm |
| Clear Expectations | DOD 3 cấp (Story, Sprint, Release), RACI rõ ràng |
| Growth Mindset | 1-1 hàng tháng, mentor junior, chia sẻ bài học |
| Recognition | Ghi nhận đóng góp trong retro, khen trước team |

### 3.3 Mentor Junior PM

PM L3 có trách nhiệm mentor 1-2 junior PM:

| Tháng | Focus | Hoạt động |
|-------|-------|-----------|
| 1-2 | Kỹ năng cơ bản | Shadowing PM L3 trong meeting, review report |
| 3-4 | Thực hành có hướng dẫn | Junior PM điều hành daily standup, viết report |
| 5-6 | Độc lập có giám sát | Junior PM quản lý sub-module, PM L3 review |

### 3.4 Cross-cultural Communication với khách Nhật

**Những điều KHÔNG BAO GIỜ làm:**

| KHÔNG làm | Tại sao | Làm thay thế |
|-----------|---------|-------------|
| Nói "No" trực tiếp | Mất thể diện | "Chúng tôi sẽ xem xét (検討します)" rồi giải thích khó khăn |
| Gửi bad news qua email trước | Thiếu context, gây hoảng | Gọi điện/họp trước, gửi email xác nhận sau |
| Trả lời "Khoảng..." | Không chính xác | Dùng số liệu cụ thể: "85% hoàn thành" |
| Skip nemawashi | Quyết định bất ngờ | Trao đổi trước với từng bên trước meeting chính thức |

**Nguyên tắc 根回し (Nemawashi) - Rồng rề trước:**
- Trước meeting quyết định quan trọng: gặp riêng từng stakeholder
- Trình bày vấn đề và phương án đề xuất
- Thu thập ý kiến và điều chỉnh
- Khi meeting chính thức: tất cả đã align --> quyết định nhanh

### 3.5 Meeting Facilitation

**Agenda template cho weekly meeting với KH Nhật:**

```
1. 先週のアクションアイテム確認 (Review action items tuần trước) -- 5 phút
2. 今週の実績 (Kết quả tuần này) -- 10 phút
   - Velocity, % hoàn thành, demo (nếu có)
3. 課題・リスク (Issues & Risks) -- 10 phút
   - RAG status, mitigation plan
4. 来週の予定 (Kế hoạch tuần sau) -- 5 phút
5. 確認事項 (Items cần confirm) -- 10 phút
6. アクションアイテム確認 (Xác nhận action items mới) -- 5 phút
```

**Nguyên tắc:** Bad news first, good news later. Dùng data/metrics, không chỉ cảm nhận.

---

## 4. Quản lý cấp tổ chức (L4)

### 4.1 Strategic Partner Positioning

PM L4 không chỉ là "người quản lý dự án" mà là **đối tác chiến lược** của khách hàng:

| Từ "Vendor" | Sang "Partner" |
|------------|---------------|
| Nhận spec, làm đúng | Đề xuất giải pháp, tư vấn cải tiến |
| Báo cáo khi được hỏi | Proactive sharing insight |
| Chỉ lo dự án hiện tại | Quan tâm business roadmap khách hàng |
| Đợi khách hàng quyết định | Cùng khách hàng ra quyết định |

**Cách đạt được:** Hiểu domain của khách hàng, đề xuất cải tiến, tạo giá trị vượt ngoài scope.

### 4.2 Xây dựng PM Capability toàn tổ chức

PM L4 góp phần xây dựng năng lực PM cho toàn công ty:

**Hoạt động:**
- Xây dựng PM competency framework (như tài liệu nang-luc.md)
- Thiết kế bài test đánh giá (L1/L2/L3)
- Mentor PM L2-L3
- Review và cải tiến quy trình PM hàng quý
- Chia sẻ case study và lessons learned

**Khuôn khổ đánh giá 360 độ:**

| Nguồn đánh giá | Đánh giá năng lực nào | Tỷ trọng |
|----------------|----------------------|----------|
| Self-assessment | Tất cả 8 nhóm | 15% |
| Direct manager (DM) | Kế hoạch, Yêu cầu, Rủi ro, Chất lượng, Agile, Leadership | 30% |
| Khách hàng Nhật | Chất lượng, Giao tiếp, Stakeholder | 25% |
| Team member | Giao tiếp, Agile, Leadership | 15% |
| BrSE | Yêu cầu, Giao tiếp, Stakeholder | 15% |

### 4.3 Portfolio-level Stakeholder Management

Quản lý stakeholder không chỉ 1 dự án mà nhiều dự án:

| Cấp | Nội dung quản lý | Tần suất |
|-----|-----------------|----------|
| Dự án | Tiến độ, chất lượng, rủi ro dự án | Hàng tuần |
| Portfolio | Phân bổ resource, ưu tiên giữa dự án, risk xuyên dự án | Hàng tháng |
| Tổ chức | Chiến lược kinh doanh, quan hệ khách hàng, expansion | Hàng quý |

### 4.4 Xây dựng văn hóa tổ chức

**3 trụ cột văn hóa mà PM L4 xây dựng:**

**A. Quality-first (説明できる品質):**
- Mọi quyết định đều có data support
- Quality gate không thỏa hiệp
- Team tự hào về chất lượng, không chỉ "xong là được"

**B. Kaizen (cải tiến liên tục):**
- Retrospective là bắt buộc, không phải hình thức
- Mọi người có quyền đề xuất cải tiến
- Improvement backlog được review hàng quý

**C. Psychological Safety (an toàn tâm lý):**
- Cho phép báo bad news sớm mà không bị phạt
- Không blame cá nhân, focus vào system/process
- Khuyến khích thử nghiệm và học từ thất bại

---

## 5. Tự kiểm tra

### Case Study 1: Báo cáo tin xấu (L1-L2)

**Tình huống:** Sprint 6/12. Bạn phát hiện effort thực tế Phase 2 sẽ vượt budget 15% (18 man-month thêm). Nguyên nhân: 2 PG mới ramp-up chậm (3 sprint thay vì 1), module Optimization Calculation phức tạp hơn 基本設計.

**Yêu cầu:**
1. Viết email báo cáo cho direct manager (Delivery Manager)
   - Mô tả vấn đề rõ ràng
   - Đề xuất >= 2 phương án giải quyết
   - Recommendation và lý do
2. Sau khi manager đồng ý, viết email cho khách hàng Nhật (qua BrSE)
   - Tone: không panic, professional
   - Có số liệu support
   - Có commitment mới

**Tiêu chí chấm:**
- Báo manager TRƯỚC, rồi mới báo khách (có plan rồi mới báo)
- Email có số liệu cụ thể, không mơ hồ
- Đề xuất phương án khả thi, không chỉ báo "có vấn đề"

### Case Study 2: Giải quyết xung đột đa bên (L2-L3)

**Tình huống:**
- QA Lead: "Cần thêm 1 sprint cho regression test. Quality chưa đủ."
- Dev Lead: "Sprint cuối focus fix bug, không thêm feature."
- Khách hàng: "Tất cả features trong scope phải deliver đúng hạn."
- BrSE: "Khách hàng rất coi trọng deadline. Trễ sẽ ảnh hưởng hợp đồng."

**Yêu cầu:**
1. Phân tích lợi ích và quan ngại của mỗi bên
2. Đề xuất giải pháp win-win (hoặc tối ưu nhất)
3. Mô tả cách facilitate meeting giải quyết (agenda, ai tham gia, expected outcome)

**Gợi ý giải pháp:**
- Phân loại features theo priority: Must (80% effort) vs Should (20%)
- Sprint cuối: fix tất cả bugs + deliver Must features
- Should features: chuyển sang mini-release 1 tuần sau
- Thêm 2 ngày regression test trước release chính thức
- Báo khách hàng với cam kết: "100% Must features on-time, Should features +1 tuần"

### Case Study 3: Phục hồi niềm tin (L3-L4)

**Tình huống:** Sau deploy staging, khách hàng phát hiện 15 bugs "fixed" nhưng chưa fix, 3 features khác 詳細設計書, performance test chưa chạy. Khách hàng gửi email yêu cầu họp về kế hoạch cải tiến chất lượng.

**Yêu cầu:**
1. Viết Quality Improvement Plan (QIP):
   - Acknowledgement (nhận trách nhiệm, KHÔNG blame)
   - Root cause analysis
   - Corrective actions (ngay lập tức)
   - Preventive actions (dài hạn)
   - Metrics cam kết
   - Timeline
2. Chuẩn bị agenda cho meeting với khách hàng

**Tiêu chí chấm:**
- Nhận trách nhiệm ngay, không biện minh
- Root cause chỉ vào system/process gap
- Corrective action cụ thể, có deadline
- Preventive action thay đổi được quy trình
- Metrics cam kết có thể đo được

---

## 6. Tài liệu tham khảo

| Tài liệu | Vai trò |
|----------|---------|
| PM nang-luc.md | Khung năng lực PM 8 nhóm (đặc biệt #5, #7, #8) |
| communication.md | Bài test Communication, Stakeholder, Leadership |
| GLN-PJM-IPM-01 | Hướng dẫn Stakeholder Engagement (Power/Interest, RACI, KT, meeting) |
| GLN-PJM-PMC-02 | Hướng dẫn giao tiếp với khách Nhật (email format, Keigo, Horenso) |
| GLN-PMG-OPF-02 | Governance Guide (OKR, dashboard, ra quyết định, escalation) |
| PRC-PJM-IPM-02 | Quy trình Giao tiếp Stakeholder |
| TPL-PJM-IPM-02 | Mẫu Onboarding Checklist |
| TPL-PJM-IPM-03 | Mẫu Kế hoạch Truyền thông |
| RUL-PJM-IPM-01 | Quy tắc Phê duyệt và Soudan |
