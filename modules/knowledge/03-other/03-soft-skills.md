# Soft Skills for IT Professionals

> **Mục tiêu:** Phát triển kỹ năng mềm thiết yếu cho kỹ sư và PM trong môi trường outsource Nhật Bản
> **Level:** L1 → L2 → L3
> **Thời gian đọc:** ~20 phút
> **Liên quan:** PM Competency #5 (コミュニケーション), #8 (リーダーシップ)

---

## 1. Khái niệm cơ bản (L1)

### 1.1 Problem Solving — Giải quyết vấn đề

**Root Cause Analysis (Phân tích nguyên nhân gốc):**

Không fix triệu chứng, phải tìm nguyên nhân gốc. Sử dụng kỹ thuật 5 Whys:

| Bước | Câu hỏi | Ví dụ |
|------|---------|-------|
| Why 1 | Tại sao bug lọt lên production? | Vì unit test không cover case này |
| Why 2 | Tại sao unit test không cover? | Vì test case review không kỹ |
| Why 3 | Tại sao review không kỹ? | Vì không có checklist review test case |
| Why 4 | Tại sao không có checklist? | Vì chưa ai định nghĩa tiêu chuẩn |
| Root Cause | → | Cần tạo test case review checklist và enforce |

**Quy trình giải quyết vấn đề có hệ thống:**
1. **Xác định vấn đề:** Mô tả chính xác vấn đề là gì (không phải triệu chứng)
2. **Thu thập dữ liệu:** Log, metrics, reproduce steps
3. **Phân tích nguyên nhân:** 5 Whys, Fishbone diagram, timeline analysis
4. **Đề xuất giải pháp:** >= 2 phương án với pros/cons
5. **Chọn và thực hiện:** Quyết định dựa trên dữ liệu, không cảm tính
6. **Kiểm tra kết quả:** Xác nhận vấn đề đã được giải quyết
7. **Phòng ngừa tái phát:** Cập nhật quy trình, checklist, monitoring

### 1.2 Time Management — Quản lý thời gian

**Ma trận ưu tiên (Eisenhower Matrix):**

| | Khẩn cấp (Urgent) | Không khẩn cấp (Not Urgent) |
|---|---|---|
| **Quan trọng (Important)** | **DO FIRST:** Production bug, deadline hôm nay, khách hàng escalation | **SCHEDULE:** Design review, refactoring, học kỹ năng mới, process improvement |
| **Không quan trọng (Not Important)** | **DELEGATE:** Email thông thường, meeting không cần thiết | **ELIMINATE:** Social media, việc không liên quan |

**Nguyên tắc cam kết deadline:**
- Ước lượng thêm buffer 20% cho mỗi task
- Nếu có nguy cơ trễ, báo NGAY không đợi (報告 — Houkoku)
- Không cam kết những gì không chắc chắn — nói rõ "cần xác nhận thêm"
- Track tiến độ hàng ngày, so sánh planned vs actual

**Kỹ thuật quản lý workload:**
- Giới hạn Work In Progress (WIP) — không làm nhiều thứ cùng lúc
- Time-boxing: đặt giới hạn thời gian cho mỗi task
- Pomodoro: 25 phút tập trung + 5 phút nghỉ
- End-of-day review: kiểm tra những gì đã làm, plan cho ngày mai

### 1.3 Professional Ethics — Đạo đức nghề nghiệp

**Trung thực trong báo cáo:**
- Báo cáo tiến độ thật: nếu xong 60% thì nói 60%, KHÔNG nói 90%
- Không giấu bug hoặc vấn đề — báo sớm là tốt nhất
- Nhận lỗi khi sai, đề xuất giải pháp khắc phục

**Trách nhiệm cá nhân (Accountability):**
- Khi có vấn đề, không đổ lỗi cho người khác
- Nói: "Tôi sẽ tìm hiểu và giải quyết" thay vì "Do người khác làm sai"
- Theo tinh thần Nhật: `責任感` (Sekininkan — Tinh thần trách nhiệm)

**Bảo mật thông tin:**
- KHÔNG chia sẻ code/tài liệu khách hàng ra ngoài
- KHÔNG lưu tài liệu nhạy trên máy cá nhân không có bảo mật
- Tuân thủ NDA nghiêm ngặt

---

## 2. Thực hành nâng cao (L2)

### 2.1 Emotional Intelligence — Trí tuệ cảm xúc

**Tự nhận thức (Self-awareness):**
- Nhận biết cảm xúc của mình trong tình huống căng thẳng
- Hiểu điều gì trigger stress của bạn (deadline, conflict, ambiguity)
- Journal hàng tuần: ghi lại tình huống khó và cách bạn xử lý

**Đồng cảm (Empathy):**
- Hiểu góc nhìn của người khác trước khi phản ứng
- Trong xung đột, hỏi: "Người này đang lo lắng điều gì?"
- Với khách Nhật: hiểu rằng họ có áp lực từ cấp trên của họ

**Quản lý stress dưới áp lực deadline:**

| Cấp độ stress | Dấu hiệu | Cách xử lý |
|--------------|----------|-----------|
| **Nhẹ** | Lo lắng nhẹ, khó tập trung | Time-boxing, chia nhỏ task, Pomodoro |
| **Trung bình** | Mất ngủ, irritable, quality giảm | Nói chuyện với PM/lead, xin hỗ trợ, điều chỉnh scope |
| **Nặng** | Kiệt sức, muốn bỏ việc, sức khỏe ảnh hưởng | Escalate lên manager, nghỉ phép ngắn, tìm hỗ trợ chuyên nghiệp |

**Thực tế trong dự án Nhật:** Overtime liên tục là dấu hiệu quản lý kém, KHÔNG phải chăm chỉ. PM tốt cần nhận ra và xử lý sớm.

### 2.2 Analytical Thinking — Tư duy phân tích

**Data Interpretation — Đọc hiểu dữ liệu:**
- Không nhìn một số liệu đơn lẻ, nhìn trend
- So sánh với benchmark: bug density 1.5 có tốt không? → So với industry average 1-3
- Hỏi "Số này có nghĩa gì?" trước khi báo cáo

**Trade-off Analysis — Phân tích đánh đổi:**

Khi cần quyết định, làm bảng so sánh:

| Tiêu chí | Option A: Dùng framework X | Option B: Tự build | Trọng số |
|----------|--------------------------|-------------------|----------|
| Thời gian dev | 2 tuần | 4 tuần | 30% |
| Maintenance | Dễ — có community | Khó — phải tự maintain | 25% |
| Performance | Trung bình | Cao (tối ưu riêng) | 20% |
| Learning curve | Team chưa biết | Team đã có kinh nghiệm | 15% |
| Rủi ro | Thấp (mature framework) | Cao (chưa tested) | 10% |
| **Điểm** | **7.5/10** | **6.0/10** | |

**Decision Documentation:**
- Ghi lại MỌI THỨ quyết định quan trọng: lý do, phương án được xem xét, ai quyết định
- Dùng cho: design decisions, technology choices, process changes
- Giúp: onboard người mới, giải thích cho khách, lesson learned

### 2.3 Presentation Skills — Kỹ năng trình bày

**Giải thích Design Spec cho khách hàng:**

1. **Mở đầu:** Bối cảnh và mục tiêu (30 giây)
2. **Overview:** Sơ đồ tổng quan, flow chính (2 phút)
3. **Chi tiết:** Đi vào từng phần, có hình minh họa (5-10 phút)
4. **Q&A:** Sẵn sàng trả lời câu hỏi, có backup slides

**Logic flow clarity:**
- Mỗi slide chỉ 1 message chính
- Dùng diagram thay vì text khi có thể
- So sánh: trước/sau, option A/B
- Kết thúc bằng kết luận rõ ràng và next steps

**Visual aids hiệu quả:**
- Bảng so sánh: tốt hơn bullet points khi so sánh options
- Flowchart: tốt hơn text khi mô tả process
- Timeline: tốt hơn list khi mô tả schedule
- Metrics chart: tốt hơn text khi báo cáo tiến độ

### 2.4 Conflict Resolution — Giải quyết xung đột

**Framework ARISE:**

| Bước | Hành động | Ví dụ |
|------|-----------|-------|
| **A** — Acknowledge | Thừa nhận vấn đề tồn tại | "Tôi hiểu rằng có sự bất đồng giữa QA và Dev về timeline" |
| **R** — Research | Tìm hiểu góc nhìn mỗi bên | Nói chuyện riêng với QA Lead và Dev Lead |
| **I** — Invite | Mời các bên thảo luận cùng | Tổ chức meeting với agenda rõ ràng |
| **S** — Solve | Tìm giải pháp cùng nhau | Đưa ra 2-3 options, để nhóm chọn |
| **E** — Evaluate | Đánh giá kết quả sau 1 tuần | Kiểm tra: xung đột đã giảm? Mọi người hài lòng? |

**Case study:** QA Lead đòi thêm 1 sprint để regression test. Dev Lead muốn focus fix bug. Khách hàng yêu cầu deliver đúng hạn.

Giải pháp win-win có thể:
- Chia regression test thành 2 phase: critical tests chạy song song với fix bug
- Dev fix bug ưu tiên theo mức độ ảnh hưởng đến regression test
- Báo cáo khách: "Để đảm bảo chất lượng, chúng tôi triển khai test song song"
- Result: chất lượng được đảm bảo, deadline được giữ, team không quá tải

---

## 3. Chiến lược & Dẫn dắt (L3)

### 3.1 Leadership trong dự án Offshore

**Team Building với team phân tán:**
- Regular 1-1 meetings (bi-weekly) — không chỉ nói công việc, hỏi về môi trường làm việc
- Team health check hàng tháng: dùng survey ngắn 5 câu hỏi
- Celebrate thành công — nhấn mạnh đóng góp của cả team, không chỉ cá nhân
- Tạo môi trường an toàn để nói lên vấn đề (Psychological Safety)

**Coaching & Delegation:**

| Level thành viên | Cách dẫn dắt | Ví dụ |
|-----------------|-------------|-------|
| Junior (< 1 năm) | Directive — chỉ rõ cách làm, review kỹ | Giao task cụ thể, review code 100% |
| Mid (1-3 năm) | Coaching — giải thích lý do, cho tự làm | Giao feature, review design + code |
| Senior (3+ năm) | Delegating — giao mục tiêu, để tự chọn cách | Giao module, review ở mức architecture |

**Xử lý khi team mất động lực:**

Root causes thường gặp:
1. Overtime liên tục > 2 tuần → Giảm workload, redistribute
2. Không được công nhận → Public recognition, feedback tích cực
3. Công việc nhàm chán → Rotate task, giao thử thách mới
4. Môi trường toxic → 1-1 với từng người, xử lý conflict
5. Không thấy cơ hội phát triển → Career path discussion, training

### 3.2 Decision Making dưới Áp lực

**Khi không đủ thông tin mà phải quyết định:**

1. Xác định: quyết định này có đảo ngược được không? (Reversible vs Irreversible)
2. Nếu reversible (có thể sửa): quyết định nhanh, điều chỉnh sau
3. Nếu irreversible (không thể sửa): thu thập thêm thông tin, tham vấn senior
4. Ghi lại lý do quyết định → Accountability và lesson learned

**Framework ra quyết định:**
```
Quyết định: [Mô tả quyết định]
Bối cảnh: [Tại sao cần quyết định ngay]
Options đã xem xét:
  - Option A: [Mô tả] — Pros: ... / Cons: ...
  - Option B: [Mô tả] — Pros: ... / Cons: ...
Quyết định chọn: [Option X]
Lý do: [Tại sao chọn option này]
Risk: [Rủi ro của quyết định này]
Mitigation: [Cách giảm rủi ro]
Review date: [Khi nào review lại quyết định]
```

### 3.3 Crisis Management — Quản lý khủng hoảng

**Khi đối mặt khủng hoảng (production down, team nghỉ đông, mất lòng tin khách):**

| Giai đoạn | Hành động | Thời gian |
|-----------|-----------|-----------|
| **Immediate** | Stabilize — ngăn vấn đề lớn thêm | 0-4h |
| **Short-term** | Root cause + Quick fix | 1-3 ngày |
| **Medium-term** | Corrective actions + Process improvement | 1-4 tuần |
| **Long-term** | Preventive actions + Culture change | 1-3 tháng |

**Nguyên tắc:** Không tìm người đổ lỗi. Tìm nguyên nhân hệ thống. Fix process, không chỉ fix người.

### 3.4 Self-assessment và Continuous Learning

**Monthly self-reflection:**
1. Tháng này tôi đã học được gì mới?
2. Tình huống nào tôi xử lý tốt? Tại sao?
3. Tình huống nào tôi có thể làm tốt hơn? Làm gì khác?
4. Feedback nào tôi đã nhận được? Đồng ý hay không?
5. Mục tiêu tháng sau là gì?

---

## 4. Tự kiểm tra

### Case Study 1: Deadline Pressure
Sprint cuối cùng trước release. Team còn 20% công việc nhưng chỉ còn 1 tuần. QA bảo cần thêm thời gian test. Khách hàng không cho phép delay.

Hỏi:
1. Bạn sẽ làm gì đầu tiên? (Immediate action)
2. Giải pháp nào cân bằng chất lượng và deadline?
3. Bạn báo cáo khách hàng như thế nào?

### Case Study 2: Conflict Resolution
Developer A và Developer B tranh cãi về cách implement feature. A muốn dùng microservices, B muốn monolith. Tranh cãi kéo dài 3 ngày, ảnh hưởng tiến độ.

Hỏi:
1. Bạn sẽ làm gì để giải quyết xung đột này?
2. Dựa trên tiêu chí nào để quyết định?
3. Làm sao để cả hai bên đều chấp nhận kết quả?

### Case Study 3: Ethical Dilemma
Bạn phát hiện 1 thành viên team đã báo cáo tiến độ 90% nhưng thực tế chỉ 60%. Deadline còn 3 ngày.

Hỏi:
1. Bạn xử lý như thế nào với thành viên đó? (1-1, không trước mặt team)
2. Bạn báo cáo PM/khách hàng như thế nào?
3. Biện pháp phòng ngừa cho tương lai?

---

## 5. Tài liệu tham khảo

### Frameworks
- Eisenhower Matrix — Time Management
- 5 Whys — Root Cause Analysis
- ARISE — Conflict Resolution
- Kirkpatrick Model — Training Evaluation (GLN-PMG-OT-01)

### Tài liệu nội bộ
- PM nang-luc.md: #5 Communication, #8 Leadership
- PM tests/communication.md: Case studies on team morale, trust recovery
- GLN-PMG-OT-01: Training Best Practices Guide

### Sách khuyên đọc
- "Emotional Intelligence 2.0" — Travis Bradberry
- "The 7 Habits of Highly Effective People" — Stephen Covey
- "Crucial Conversations" — Patterson, Grenny, McMillan, Switzler
