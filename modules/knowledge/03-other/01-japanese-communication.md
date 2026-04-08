# Japanese Business Communication — Horenso (報連相)

> **Mục tiêu:** Thành thạo giao tiếp business với khách hàng Nhật Bản trong dự án outsource
> **Level:** L1 → L2 → L3
> **Thời gian đọc:** ~25 phút
> **Liên quan:** SE Competency #4 (コミュニケーション), PM Competency #5, #7

---

## 1. Khái niệm cơ bản (L1)

### 1.1 Horenso là gì?

**報連相 (Horenso)** là nguyên tắc giao tiếp cơ bản bắt buộc trong môi trường làm việc Nhật Bản:

| Thành phần | Kanji | Romaji | Ý nghĩa | Khi nào dùng |
|------------|-------|--------|---------|-------------|
| **報告** | 報告 | Houkoku | Báo cáo kết quả | Hoàn thành task, phát hiện vấn đề, thay đổi schedule |
| **連絡** | 連絡 | Renraku | Liên lạc thông tin | Thay đổi lịch meeting, nghỉ phép, thông tin ảnh hưởng nhiều người |
| **相談** | 相談 | Soudan | Trao đổi ý kiến | Không rõ cách làm, gặp issue kỹ thuật, cần quyết định từ cấp trên |

**Nguyên tắc vàng:** Khi báo cáo vấn đề, LUÔN kèm theo đề xuất giải pháp. Không bao giờ chỉ nêu vấn đề mà không có phương án.

### 1.2 Keigo cơ bản trong email

Ba loại 敬語 (Keigo) cần biết:

**尊敬語 (Sonkeigo) — Tôn trọng người khác (khách hàng, sếp):**

| Thường | Sonkeigo | Ý nghĩa |
|--------|----------|---------|
| 言う (iu) | おっしゃる (ossharu) | nói |
| 見る (miru) | ご覧になる (goran ni naru) | xem |
| する (suru) | なさる (nasaru) | làm |
| 知る (shiru) | ご存じ (gozonji) | biết |
| 来る (kuru) | いらっしゃる (irassharu) | đến |

**謙譲語 (Kenjougo) — Hạ thấp bản thân:**

| Thường | Kenjougo | Ý nghĩa |
|--------|----------|---------|
| 言う (iu) | 申し上げる (moushiageru) | nói |
| 見る (miru) | 拝見する (haiken suru) | xem |
| する (suru) | いたす (itasu) | làm |
| 聞く (kiku) | 伺う (ukagau) | nghe/hỏi |
| もらう (morau) | いただく (itadaku) | nhận |

**丁寧語 (Teineigo) — Lịch sự cơ bản:** Thêm です/ます vào cuối câu.

### 1.3 Câu chào mẫu trong email

**Mở đầu (Opening):**
- `お疲れ様です。` — Dùng với đồng nghiệp, nội bộ
- `いつもお世話になっております。` — Dùng với khách hàng (bắt buộc)
- `初めてメールを差し上げます。` — Email lần đầu tiên
- `ご無沙汰しております。` — Lâu không liên lạc

**Kết thúc (Closing):**
- `よろしくお願いいたします。` — Kính mong được hợp tác (standard)
- `何卒よろしくお願い申し上げます。` — Rất mong được hợp tác (very formal)
- `お忙しいところ恐縮ですが。` — Xin lỗi vì làm phiền khi bận

### 1.4 Format báo cáo hàng ngày (Daily Report)

```
【報告】タスク完了のご報告

山田様

お疲れ様です。Nguyen Van Aです。

本日のタスクが完了しましたので、ご報告いたします。

【完了したタスク】
- ログイン機能の実装
- 単体テストの作成

【所要時間】
- 予定: 6時間
- 実績: 5.5時間

【成果物】
- UserService.java
- UserServiceTest.java

【次のステップ】
明日は結合テストを実施いたします。

以上、よろしくお願いいたします。

Nguyen Van A
```

### 1.5 Cụm từ xác nhận thường dùng

| Tiếng Nhật | Romaji | Tiếng Việt | Mức độ |
|------------|--------|-----------|--------|
| 承知いたしました | Shouchi itashimashita | Tôi đã hiểu / đã nhận | Formal (dùng với khách) |
| かしこまりました | Kashikomarimashita | Vâng, tôi hiểu | Very formal |
| 了解しました | Ryoukai shimashita | Đã hiểu | Nội bộ only |
| 確認いたしました | Kakunin itashimashita | Tôi đã xác nhận | Standard |

---

## 2. Thực hành nâng cao (L2)

### 2.1 Cấu trúc email chuyên nghiệp

Format chuẩn cho mọi email business Nhật Bản:

```
[件名 / Subject]: [プロジェクト名] - [内容の要約]

[宛先 / To]:
[会社名] [部署名] [役職] [氏名]様

[挨拶 / Greeting]:
お疲れ様です。
[会社名]の[名前]です。
いつもお世話になっております。

[本文 / Body]:
→ Context: Mô tả bối cảnh ngắn gọn
→ Request: Nội dung chính, yêu cầu cụ thể
→ Options: Đưa ra phương án (nếu có)

[結び / Closing]:
お忙しいところ恐縮ですが、
ご確認のほどよろしくお願いいたします。

[署名 / Signature]:
---
[名前] ([tên tiếng Nhật])
[会社名] [部署名]
Email: ... | Tel: ...
---
```

### 2.2 Email mẫu: Xác nhận spec

```
件名：【確認依頼】燃料情報削除時の使用燃料テーブルとの関連について

SYP ○○様

お疲れ様です。△△です。

燃料情報管理モジュールの詳細設計を進める中で、
確認させていただきたい点がございます。

【確認事項】
燃料情報を削除する際、該当の燃料が「使用燃料テーブル（fuel_usage）」で
使用されている場合の処理について、要件定義書に明記されていないため、
ご確認をお願いいたします。

【案1】削除不可とする
使用燃料テーブルで参照されている場合は、エラーメッセージを表示し、
削除を拒否する。
メリット：データの整合性を保てる
デメリット：運用上、不要な燃料を削除できないケースが発生する

【案2】警告表示後に削除可能とする
警告メッセージを表示し、ユーザーが確認した上で論理削除を実行する。
使用燃料テーブルのデータはそのまま保持する。
メリット：運用の柔軟性が高い
デメリット：使用燃料テーブルに削除済み燃料への参照が残る

弊社としては、データの整合性を重視し、【案1】を推奨いたしますが、
ご意見をいただけますでしょうか。

お忙しいところ恐れ入りますが、ご確認のほどよろしくお願いいたします。

△△
```

**Điểm nổi bật của email này:**
- Có [確認依頼] trong subject line để khách biết mục đích
- Mô tả vấn đề rõ ràng với bối cảnh cụ thể
- Đưa ra 2+ phương án với merit/demerit
- Có recommendation của mình
- Kết bằng câu lịch sự chuẩn

### 2.3 Biên bản họp (議事録) — Gửi trong vòng 24h

```
【議事録】[Project Name] 定例会議 (2026/02/10)

■ 日時: 2026年2月10日(月) 14:00-15:00
■ 場所: Teams Meeting
■ 出席者:
  - [客先] 山田部長、佐藤課長
  - [自社] Nguyen PM、Tran BrSE、Le TL
■ 議題: Sprint 6 Review + Sprint 7 Planning

━━━━━━━━━━━━━━━━━━━━
1. 前回のアクション確認
━━━━━━━━━━━━━━━━━━━━
| # | Action | 担当 | 期限 | 状況 |
|---|--------|------|------|------|
| 1 | API仕様書の修正 | Tran | 2/7 | 完了 |
| 2 | テストデータ準備 | Le | 2/7 | 完了 |

━━━━━━━━━━━━━━━━━━━━
2. 議論内容
━━━━━━━━━━━━━━━━━━━━

【議題1】Sprint 6 Review
- 完了: 8/10 story points (80%)
- 未完了:
  - Alert notification email: blocked (mail server config)
  - Batch monitoring: +3 man-day needed
- 佐藤課長: mail server config は来週対応予定

【議題2】Sprint 7 Planning
- 対象stories: 12 story points
- リスク: Optimization module の工数超過可能性

━━━━━━━━━━━━━━━━━━━━
3. 決定事項
━━━━━━━━━━━━━━━━━━━━
- Alert email を Sprint 7 carry over
- Optimization module の re-estimation 実施

━━━━━━━━━━━━━━━━━━━━
4. 次回アクション
━━━━━━━━━━━━━━━━━━━━
| # | Action | 担当 | 期限 |
|---|--------|------|------|
| 1 | Optimization module re-estimation | Nguyen | 2/14 |
| 2 | Mail server config confirmation | 佐藤 | 2/14 |
| 3 | Sprint 7 backlog refinement | Tran | 2/12 |

次回会議: 2026年2月17日(月) 14:00-15:00

以上
作成者: Nguyen Van A
```

### 2.4 Escalation Rules

| Mức độ | Màu | Thời gian báo cáo | Đối tượng báo cáo | Ví dụ |
|--------|-----|-------------------|-------------------|-------|
| **Critical (Red)** | 🔴 | Trong vòng 1-4h | PM + Delivery Manager + Khách hàng | Production bug, data loss, security breach |
| **High (Orange)** | 🟠 | Trong vòng 1 ngày | PM + BrSE | Delay > 3 ngày, resource issue, technical blocker |
| **Medium (Yellow)** | 🟡 | Weekly report | PM | Minor delay, spec clarification needed |
| **Low (Green)** | 🟢 | Sprint review | Team | Minor improvement suggestions |

**Nguyên tắc báo cáo tin xấu (Bad News Reporting):**

1. **早め (Hayame)** — Càng sớm càng tốt. KHÔNG đợi có giải pháp mới báo
2. **正確 (Seikaku)** — Chính xác, cụ thể, có số liệu
3. **対策付き (Taisaku tsuki)** — Kèm giải pháp đề xuất
4. **誠実 (Seijitsu)** — Chân thành, nhận trách nhiệm, không đổ lỗi

**Cấu trúc Bad News Report:**

```
1. 謝罪 (Shazai) — Xin lỗi
   ↓
2. 事実報告 (Jijitsu Houkoku) — Báo cáo sự thật
   ↓
3. 原因分析 (Gen'in Bunseki) — Phân tích nguyên nhân
   ↓
4. 対応策 (Taiousaku) — Giải pháp khắc phục
   ↓
5. 今後の対策 (Kongo no Taisaku) — Phòng ngừa tương lai
   ↓
6. 再度謝罪 (Saido Shazai) — Xin lỗi lần nữa
```

### 2.5 Email mẫu: Báo cáo delay

```
件名: [ABC Project] 納期遅延のお詫びと対応策のご報告

山田部長様

お疲れ様です。DEF株式会社の Nguyen Van A です。
いつも大変お世話になっております。

誠に申し訳ございません。
今回、ユーザー管理機能の納品が予定より遅延する見込みとなりました。

【遅延の詳細】
・当初納期: 2026年2月15日(金)
・新納期: 2026年2月22日(金)
・遅延日数: 5営業日

【遅延の原因】
1. データベース設計の変更要求への対応に想定以上の時間を要した
2. 外部API連携のテストで予期しない不具合が発生
3. 初期見積もりの甘さ

【対応策】
1. 即時対応
   - 開発メンバーを2名から3名に増員
   - 毎日の進捗ミーティング実施
2. 短期対策
   - テストの並行実施
   - レビュープロセスの効率化

【進捗報告】
本件については、毎日17:00(JST)に進捗状況をご報告いたします。

【今後の再発防止策】
1. 見積もりにバッファを20%追加
2. 週次リスク評価の実施
3. 進捗率が80%を下回った場合即報告

この度は、ご迷惑をおかけし、誠に申し訳ございません。
チーム一丸となって対応してまいりますので、
何卒ご理解とご支援を賜りますようお願い申し上げます。

---
Nguyen Van A (グエン・ヴァン・A)
DEF株式会社 プロジェクトマネージャー
Email: nguyen.a@def.com
Tel: +84-123-456-789
---
```

### 2.6 Weekly Report Format

```
件名: [ABC Project] 週次進捗報告 (2026/02/03-02/07)

山田部長様

お疲れ様です。DEF株式会社の Nguyen Van A です。
いつもお世話になっております。

今週の進捗状況をご報告させていただきます。

━━━━━━━━━━━━━━━━━━━━
1. 今週の実績 (Thực tế tuần này)
━━━━━━━━━━━━━━━━━━━━
- Sprint 6 完了: 8/10 story points (80%)
- Bug fix: 5 bugs resolved, 2 bugs mới phát hiện (1 Medium, 1 Low)
- 未完了:
  - Alert notification email — blocked (mail server config)
  - Batch job monitoring — underestimated (+3 man-day)

━━━━━━━━━━━━━━━━━━━━
2. 課題・リスク (Issue & Risk)
━━━━━━━━━━━━━━━━━━━━
- [Risk] Optimization Calculation module có thể delay 1 sprint
  (phức tạp hơn dự kiến)
- [Issue] 1 PG nghỉ phép 2 ngày (đã plan thay thế)

━━━━━━━━━━━━━━━━━━━━
3. 来週の予定 (Kế hoạch tuần sau)
━━━━━━━━━━━━━━━━━━━━
- Sprint 7 kick-off
- Optimization module re-estimation
- Alert email carry-over implementation

━━━━━━━━━━━━━━━━━━━━
4. 確認事項 (Items cần confirm)
━━━━━━━━━━━━━━━━━━━━
- Mail server config schedule?
- Optimization module scope có thể thu gọn?

ご不明な点がございましたら、お気軽にお問い合わせください。
引き続きよろしくお願いいたします。

Nguyen Van A
```

---

## 3. Chiến lược & Dẫn dắt (L3)

### 3.1 Proposal Writing cho khách hàng Nhật

Khi cần đề xuất giải pháp hoặc thay đổi lớn, cấu trúc proposal:

1. **Background (背景):** Bối cảnh và lý do đề xuất
2. **Current Issue (現状の課題):** Vấn đề hiện tại, có số liệu cụ thể
3. **Proposal (提案内容):** Giải pháp chi tiết với 2-3 phương án
4. **Impact Analysis (影響分析):** Scope, timeline, cost, quality, resource
5. **Recommendation (推奨):** Phương án mình khuyến nghị và lý do
6. **Schedule (スケジュール):** Timeline triển khai chi tiết
7. **Risk (リスク):** Rủi ro và biện pháp phòng ngừa

**Lưu ý:** Người Nhật rất coi trọng số liệu. Mọi luận điểm phải có metrics, không dùng cảm tính. Đây là tinh thần 説明できる品質 (Setsumei dekiru hinshitsu — Chất lượng giải thích được).

### 3.2 Meeting Facilitation với khách Nhật

**Trước meeting:**
- Gửi agenda trước ít nhất 1 ngày
- Chuẩn bị tài liệu đầy đủ, print-ready
- Thực hiện 根回し (Nemawashi) — align với stakeholder chính TRƯỚC meeting
- Test thiết bị (mic, camera, screen share)
- Join sớm 5 phút

**Trong meeting:**
- Mở đầu: cảm ơn tham dự, giới thiệu agenda, confirm thời gian
- Điều phối: đảm bảo mọi người được nói, timebox mỗi mục
- Ghi chép: action items, decisions, open questions
- Kết thúc: tóm tắt quyết định, xác nhận action items + deadline
- KHÔNG tranh cãi trực tiếp — nếu có bất đồng, ghi nhận và xử lý offline

**Sau meeting:**
- Gửi 議事録 (biên bản họp) trong vòng 24h
- Follow-up action items
- Báo cáo tiến độ thực hiện

### 3.3 Customize Report Format theo Stakeholder

| Stakeholder | Nội dung ưu tiên | Tần suất | Format |
|-------------|-----------------|----------|--------|
| **部長 (Buchou)** — Director | QCD summary, risk overview, key decisions | Bi-weekly | Executive summary 1 page |
| **課長 (Kachou)** — Manager | Sprint progress, bug metrics, CR status | Weekly | Detailed report + charts |
| **Tech Lead (日本側)** | Design decisions, technical issues, review status | Per sprint | Technical report + diagrams |
| **End User** | Feature demo, user guide updates | Per release | Demo video + release notes |

### 3.4 Multi-language Documentation Strategy

Trong dự án Nhật, tài liệu thường cần quản lý bằng nhiều ngôn ngữ:

| Loại tài liệu | Ngôn ngữ chính | Dịch sang | Trách nhiệm |
|---------------|---------------|-----------|-------------|
| 仕様書 (Spec) | Tiếng Nhật | Tiếng Việt (summary) | BrSE |
| Design doc | Tiếng Việt/Anh | Tiếng Nhật (key sections) | BrSE + SE |
| Source code | Tiếng Anh | — | Dev |
| Test case | Tiếng Việt/Anh | Tiếng Nhật (test report) | QA + BrSE |
| Meeting minutes | Tiếng Nhật | Tiếng Việt | BrSE |
| Weekly report | Tiếng Nhật | — | PM via BrSE |

**Best practice:** Tất cả technical terms giữ nguyên tiếng Nhật trong mọi tài liệu để tránh hiểu nhầm. Ví dụ: dùng `排他制御` thay vì "xử lý độc quyền" trong context làm việc với Nhật.

### 3.5 Xử lý Change Request từ khách hàng

Khi khách gửi CR, KHÔNG chấp nhận hoặc từ chối ngay. Quy trình:

1. **Acknowledge:** `ご要望は承知いたしました。` (Tôi đã nhận yêu cầu)
2. **Impact Analysis:** Đánh giá 5 chiều — Scope, Timeline, Cost, Quality, Resource
3. **Đưa ra 3+ options:** Accept all / Partial accept / Defer to next phase
4. **Recommend:** Chọn 1 phương án, giải thích lý do
5. **Confirm:** Cho khách quyết định, ghi nhận vào CR log

**Email mẫu: Response CR**

```
件名: [ABC Project] 変更要求への影響分析と対応案

山田部長様

お疲れ様です。Nguyen Van Aです。

ご要望を承知いたしました。影響分析の結果をご報告いたします。

【変更内容】
CSV・PDFエクスポート機能の追加 + テンプレート5種→10種

【影響分析】
- 工数: +20人日
- スケジュール: 1スプリント分の遅延リスク
- 品質: 追加テスト工数が必要
- リソース: 現チームで対応可能

【対応案】
案1: 全て受入 → 納期1スプリント延長
案2: CSV優先実装、PDF/テンプレートはPhase 2 → 納期変更なし (推奨)
案3: 全て次フェーズへ → 現スコープ維持

弊社としては【案2】を推奨いたします。
理由: 最優先のCSV機能を先に提供しつつ、納期を守れるため。

ご検討のほど、よろしくお願いいたします。
```

---

## 4. Tự kiểm tra

### Bài tập L1
1. Viết email tiếng Nhật xác nhận 1 điểm chưa rõ trong spec (có 件名, 挨拶, 本文, 締め)
2. Viết daily report format chuẩn cho 1 ngày làm việc của bạn
3. Kể tên 3 thành phần của Horenso và cho ví dụ mỗi thành phần

### Bài tập L2
1. Viết email báo cáo delay 3 ngày cho khách hàng, kèm giải pháp và commitment mới
2. Viết biên bản họp (議事録) cho 1 buổi Sprint Review
3. Phân biệt cách dùng `承知いたしました` vs `了解しました` vs `かしこまりました`

### Bài tập L3
1. Viết impact analysis cho 1 CR từ khách hàng với 3+ phương án negotiate
2. Mô tả cách bạn chuẩn bị và điều phối 1 buổi review meeting với khách Nhật
3. Viết Quality Improvement Plan trình bày cho khách hàng sau khi phát hiện vấn đề chất lượng nghiêm trọng

### Case Study: Trust Recovery
Khách hàng phát hiện 15 bugs báo "fixed" nhưng chưa fix, 3 features khác với 詳細設計書, performance test chưa chạy. Khách gửi email yêu cầu họp về 品質改善計画.

Bạn cần:
- Viết kế hoạch cải tiến chất lượng (Acknowledgement, Root cause, Corrective + Preventive actions, Metrics cam kết)
- Chuẩn bị agenda cho meeting

---

## 5. Tài liệu tham khảo

### Sách & tài liệu
- "Japanese Business Culture and Practices" — Parissa Haghirian
- "The Japanese Mind: Understanding Contemporary Japanese Culture" — Roger Davies

### Tài liệu nội bộ
- GLN-PJM-PMC-02: Japanese Communication Guide (CMMI)
- TPL-PJM-PMC-03: Meeting Minutes Template
- TPL-PJM-PMC-04: Terminology Glossary Template

### Online Resources
- JLPT Official: https://www.jlpt.jp/
- NHK Keigo Guide: https://www.nhk.or.jp/bunken/summary/kotoba/term/

### Checklist trước khi gửi email
- [ ] Subject line rõ ràng, có [Project Name]
- [ ] Có `お疲れ様です` / `いつもお世話になっております`
- [ ] Sử dụng 敬語 (Keigo) đúng
- [ ] Nội dung rõ ràng, có cấu trúc (heading, bullet points)
- [ ] Có kết luận / action items rõ ràng
- [ ] Có `よろしくお願いいたします` ở cuối
- [ ] Có signature đầy đủ
- [ ] CC đúng người
- [ ] Attach file nếu có đề cập
