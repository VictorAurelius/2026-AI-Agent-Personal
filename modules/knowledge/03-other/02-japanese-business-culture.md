# Japanese Business Culture & Work Ethics

> **Mục tiêu:** Hiểu và áp dụng văn hoá làm việc Nhật Bản để xây dựng mối quan hệ tin tưởng trong dự án outsource
> **Level:** L1 → L2 → L3
> **Thời gian đọc:** ~20 phút
> **Liên quan:** PM Competency #5 (コミュニケーション), #7 (ステークホルダー管理)

---

## 1. Khái niệm cơ bản (L1)

### 1.1 Các giá trị cốt lõi trong văn hoá business Nhật

| Khái niệm | Kanji | Romaji | Ý nghĩa | Áp dụng trong IT outsource |
|-----------|-------|--------|---------|---------------------------|
| **Hoà hợp** | 和 | Wa | Sự hài hoà trong nhóm | Tránh đối đầu trực tiếp, tìm giải pháp win-win |
| **Lễ nghi** | 礼儀 | Reigi | Phép lịch sự | Dùng Keigo, gửi email đúng format, đúng giờ |
| **Hình thức** | 形式 | Keishiki | Cấu trúc chính thức | Template chuẩn, đánh số, quản lý version |
| **Đọc không khí** | 空気を読む | Kuuki wo Yomu | Hiểu điều không nói | Nhận biết "検討します" = có thể là "No" |
| **Chất lượng giải thích được** | 説明できる品質 | Setsumei dekiru Hinshitsu | Mọi thứ phải có số liệu | Report bằng metrics, không bằng cảm tính |

### 1.2 和 (Wa) — Hoà hợp và tránh đối đầu

Người Nhật cực kỳ coi trọng sự hài hoà trong nhóm. Điều này ảnh hưởng đến mọi khía cạnh giao tiếp:

**Không nói "No" trực tiếp.** Thay vào đó:
- `検討します` (Kentou shimasu — Sẽ xem xét) → Thường có nghĩa là "Không"
- `難しいです` (Muzukashii desu — Khó) → Cũng là "Không" một cách nhẹ nhàng
- `前向きに検討します` (Maemuki ni kentou shimasu — Sẽ xem xét tích cực) → Có thể là "Có" nhưng chưa chắc

**Không làm mất thể diện người khác:**
- Không chỉ ra lỗi trước mặt nhiều người
- Nếu cần feedback tiêu cực, nói riêng (1-1)
- Dùng "chúng ta" thay vì "anh/chị"

**Im lặng (沈黙 - Chinmoku) không có nghĩa là đồng ý:**
- Có thể đang suy nghĩ
- Có thể không đồng ý nhưng không muốn nói trước mặt nhiều người
- Có thể không hiểu nhưng không muốn hỏi

### 1.3 形式 (Keishiki) — Tính hình thức

Mọi thứ trong môi trường Nhật đều cần có cấu trúc chính thức:

- **Tài liệu:** Phải có header, version, date, author, approval
- **Email:** Phải có subject line rõ ràng, greeting, body có cấu trúc, closing
- **Meeting:** Phải có agenda, biên bản họp (議事録), action items
- **Báo cáo:** Phải có số liệu, bảng biểu, kết luận rõ ràng
- **File naming:** Theo quy ước thống nhất, có version number

### 1.4 Punctuality — Đúng giờ là bắt buộc

- Meeting bắt đầu đúng giờ. Đến sớm 5 phút.
- Deadline là tuyệt đối. Nếu có nguy cơ trễ, báo ngay không đợi.
- Email reply trong vòng 24h. Nếu chưa có câu trả lời, gửi email xác nhận đã nhận.
- Deliverable nộp đúng ngày, đúng giờ đã cam kết.

Câu xác nhận đã nhận email:
```
メールを拝見いたしました。
内容を確認の上、○日までにご返信いたします。
```

---

## 2. Thực hành nâng cao (L2)

### 2.1 根回し (Nemawashi) — Xây dựng đồng thuận trước cuộc họp

**Định nghĩa:** Quá trình trao đổi, thuyết phục các bên liên quan TRƯỚC khi có cuộc họp chính thức, để đảm bảo mọi người đã align và cuộc họp chỉ là hình thức xác nhận.

**Tại sao quan trọng:**
- Người Nhật không thích "bất ngờ" trong meeting
- Quyết định chính thức thường đã được đồng thuận trước đó
- Meeting là nơi xác nhận, không phải nơi tranh luận

**Cách thực hiện trong dự án outsource:**

| Bước | Hành động | Ví dụ |
|------|-----------|-------|
| 1 | Xác định stakeholder chính | PM Nhật, Tech Lead Nhật, BrSE |
| 2 | Trao đổi 1-1 trước meeting | Gửi email hoặc call riêng để trình bày ý tưởng |
| 3 | Thu thập ý kiến và điều chỉnh | Điều chỉnh đề xuất dựa trên feedback |
| 4 | Xác nhận đồng thuận | Đảm bảo mọi người đã nhất trí |
| 5 | Trình bày trong meeting chính thức | Meeting chỉ là xác nhận quyết định |

**Ví dụ thực tế:**
Trước khi đề xuất thay đổi architecture trong Sprint Review, bạn cần:
1. Trao đổi với BrSE trước để hiểu phản ứng phía Nhật
2. Gửi email cho Tech Lead Nhật giải thích lý do kỹ thuật
3. Nhận feedback và điều chỉnh phương án
4. Tại meeting chính thức, chỉ trình bày phương án đã được align

### 2.2 空気を読む (Kuuki wo Yomu) — Đọc không khí

**Những dấu hiệu cần nhận biết:**

| Dấu hiệu | Ý nghĩa thật | Cách xử lý |
|----------|-------------|-----------|
| Im lặng kéo dài sau khi bạn trình bày | Không đồng ý hoặc không hiểu | Hỏi `何かご懸念はございますでしょうか` |
| `検討します` không kèm deadline | Từ chối lịch sự | Hỏi cụ thể `いつ頃ご回答いただけますでしょうか` |
| Hỏi nhiều câu hỏi chi tiết | Quan tâm nhưng cần thêm thông tin | Chuẩn bị tài liệu bổ sung |
| Gật đầu nhưng không nói gì | Đang lắng nghe, chưa đồng ý | Tiếp tục giải thích, hỏi ý kiến |
| `ちょっと...` (Chotto...) | Từ chối hoặc cần suy nghĩ | Không ép, cho thời gian |
| Thay đổi chủ đề đột ngột | Không muốn tiếp tục mục hiện tại | Chuyển theo, quay lại sau |

### 2.3 説明できる品質 (Setsumei dekiru Hinshitsu)

**Nguyên tắc:** Chất lượng phải giải thích được bằng số liệu cụ thể, không dùng cảm tính.

**SAI:** "Chất lượng tốt" / "Team đã làm việc chăm chỉ"

**ĐÚNG:**
- Bug density: 0.5 bugs/KLOC (target: < 1.0)
- Test coverage: 85% (target: > 80%)
- Review finding rate: 3.2 issues/page (benchmark: 2-5)
- On-time delivery: 95% (target: > 90%)

**Áp dụng trong báo cáo:**
```
【品質報告】Sprint 6
- 不具合密度: 0.5件/KLOC (目標: 1.0以下) → ○ 達成
- テストカバレッジ: 85% (目標: 80%以上) → ○ 達成
- レビュー指摘件数: 平均3.2件/ページ (基準: 2-5) → ○ 正常範囲
- 納期遵守率: 95% (目標: 90%以上) → ○ 達成
```

### 2.4 Quality Mindset: Phòng ngừa > Khắc phục

Người Nhật tin rằng:

**Chi phí phòng ngừa << Chi phí khắc phục**

| Giai đoạn phát hiện bug | Chi phí tương đối | Ví dụ |
|-------------------------|-------------------|-------|
| 要件定義 (Requirement) | 1x | Thiếu requirement → phát hiện sớm |
| 基本設計 (Basic Design) | 5x | Design review phát hiện inconsistency |
| 詳細設計 (Detail Design) | 10x | Logic error phát hiện khi review |
| 実装 (Implementation) | 20x | Bug phát hiện khi unit test |
| 結合テスト (Integration) | 50x | Integration issue |
| 総合テスト (System Test) | 100x | System-level defect |
| 本番 (Production) | 500-1000x | Production incident |

**Thực hành:**
- Review tài liệu thiết kế kỹ lưỡng TRƯỚC khi code
- Code review 100% — không merge code chưa review
- Unit test trước khi integration test
- Mỗi phase có Quality Gate rõ ràng

### 2.5 Hierarchy & Seniority

**Trong email:**
- Gửi cho người chức vụ cao nhất trước: 部長 → 課長 → 主任
- Dùng 様 (sama) sau tên khách hàng: `山田部長様`
- Dùng `弊社` (heisha — công ty chúng tôi) và `貴社/御社` (kisha/onsha — quý công ty)

**Trong meeting:**
- Người chức vụ cao nhất nói trước (hoặc được mời nói trước)
- Không ngắt lời người có chức vụ cao hơn
- Khi giới thiệu, giới thiệu người chức vụ cao trước

**Trong quyết định:**
- Quyết định cuối cùng thường là người chức vụ cao nhất
- Không "vượt cấp" báo cáo — luôn qua line manager

---

## 3. Chiến lược & Dẫn dắt (L3)

### 3.1 Xây dựng Lòng tin Dài hạn (信頼関係)

Quan hệ với khách Nhật được xây dựng qua thời gian dài, không chỉ qua 1 dự án:

| Hành động | Ảnh hưởng lòng tin | Ví dụ cụ thể |
|-----------|--------------------|-------------|
| Giữ lời hứa, deliver đúng cam kết | +++ | Nộp đúng deadline, đúng chất lượng |
| Báo cáo bad news sớm, chân thành | ++ | Báo delay ngay khi phát hiện, kèm giải pháp |
| Chủ động đề xuất cải tiến | ++ | Đề xuất tự động hoá testing, giảm bug density |
| Hiểu biết về ngành của khách hàng | + | Tìm hiểu về manufacturing/logistics trước meeting |
| Trễ deadline, giấu vấn đề | --- | MẤT lòng tin, rất khó lấy lại |
| Báo cáo thiếu trung thực | --- | Báo "xong 90%" nhưng thật ra chưa test |

### 3.2 Do's and Don'ts Tổng hợp

**DO — Nên làm:**

Communication:
- Phản hồi email trong vòng 24h
- Sử dụng 敬語 trong mọi giao tiếp formal
- Xác nhận đã nhận email: `メールを拝見いたしました`
- CC những người liên quan
- Báo cáo tiến độ định kỳ (hàng tuần)
- Thông báo sớm nếu có delay hoặc vấn đề

Meeting:
- Đến đúng giờ (sớm 5 phút)
- Chuẩn bị tài liệu trước meeting
- Gửi biên bản họp trong 24h
- Follow-up action items

Work Style:
- Thực hiện 報連相 đầy đủ
- Tuân thủ deadline nghiêm ngặt
- Chú trọng chất lượng hơn tốc độ
- Document đầy đủ

**DON'T — Không nên làm:**

Communication:
- Sử dụng ngôn ngữ thường (普通形) với khách hàng
- Nói "No" trực tiếp → Dùng `難しいです` hoặc `検討させていただきます`
- Tranh cãi công khai trong meeting
- Gửi email không có subject line rõ ràng
- Sử dụng emoji trong email formal

Meeting:
- Đến trễ
- Ngắt lời người khác
- Nhìn điện thoại trong meeting
- Không chuẩn bị

Work Style:
- Tự ý quyết định không báo cáo
- Giấu vấn đề cho đến khi nghiêm trọng
- Đổ lỗi cho người khác
- Nói "không biết" mà không tìm hiểu

### 3.3 Xử lý xung đột văn hoá

| Tình huống | Cách sai | Cách đúng |
|-----------|---------|-----------|
| Khách yêu cầu bất hợp lý | Từ chối thẳng: "Không làm được" | `ご要望は承知いたしました。ただ、現在の状況では実現が難しい点がございます。代替案として...` |
| Không hiểu yêu cầu | `わかりません` (Tôi không hiểu) | `恐れ入りますが、確認させていただきたい点がございます。○○の部分について、もう少し詳しくご説明いただけますでしょうか。` |
| Phải từ chối đề xuất | "No, we can't do that" | `貴重なご提案をありがとうございます。社内で検討させていただきましたが、以下の理由により、今回は見送らせていただければと存じます。` |
| Bug trên production | "Không phải lỗi của chúng tôi" | Nhận trách nhiệm trước, phân tích nguyên nhân sau: `誠に申し訳ございません。現在、緊急対応チームで原因調査と対策を進めております。` |

### 3.4 Văn hoá Kaizen (改善) — Cải tiến liên tục

Người Nhật coi trọng việc cải tiến liên tục, không chỉ sửa lỗi mà còn nâng cấp quy trình:

**Áp dụng trong dự án:**
- Retrospective mỗi Sprint: What went well? What to improve?
- Root cause analysis cho mỗi bug quan trọng (không chỉ fix bug)
- Cập nhật risk checklist từ bài học dự án trước
- Cải tiến quy trình dựa trên metrics (bug density trend, velocity trend)
- Sprint 0 giữa các release để refactor, audit, team building

---

## 4. Tự kiểm tra

### Bài tập L1
1. Kể tên 5 giá trị văn hoá Nhật Bản ảnh hưởng đến công việc IT outsource
2. Tại sao người Nhật không nói "No" trực tiếp? Cho 3 cách nói "No" gián tiếp
3. Liệt kê 5 điều KHÔNG nên làm khi làm việc với khách Nhật

### Bài tập L2
1. Mô tả quy trình 根回し (Nemawashi) trước khi đề xuất thay đổi architecture
2. Giải thích 説明できる品質 và cho ví dụ báo cáo chất lượng bằng số liệu
3. Bạn nhận được email khách nói `検討します` — bạn làm gì tiếp theo?

### Bài tập L3
1. Khách hàng mất lòng tin sau khi phát hiện vấn đề chất lượng. Mô tả kế hoạch phục hồi lòng tin (Trust Recovery Plan)
2. Team bạn có xung đột với yêu cầu của khách hàng về deadline. Mô tả cách bạn điều phối, đảm bảo cả hai bên hài lòng
3. Viết kế hoạch Kaizen cho team sau 1 dự án có nhiều vấn đề

---

## 5. Tài liệu tham khảo

### Sách
- "Japanese Business Culture and Practices" — Parissa Haghirian
- "The Japanese Mind" — Roger Davies
- "Doing Business with Japanese Men" — Christalyn Brannen

### Tài liệu nội bộ
- GLN-PJM-PMC-02: Japanese Communication Guide
- PM nang-luc.md: Khung năng lực PM dự án Nhật
- PM tests/communication.md: Bài test Communication & Stakeholder

### Online
- NHK Keigo Guide: https://www.nhk.or.jp/bunken/summary/kotoba/term/
- JLPT Official: https://www.jlpt.jp/
