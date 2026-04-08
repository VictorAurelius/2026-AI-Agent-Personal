# Japanese IT Project Glossary — Từ điển Nhật-Việt-Anh

> **Mục tiêu:** Tra cứu nhanh thuật ngữ Nhật Bản thường gặp trong dự án IT outsource
> **Tổng số thuật ngữ:** 100+
> **Cách sử dụng:** Tìm theo category hoặc Ctrl+F theo kanji/romaji/tiếng Việt
> **Liên quan:** Tất cả competencies SE/PM

---

## 1. Quy trình phát triển (Process Phases)

| Tiếng Nhật | Romaji | Tiếng Việt | English | Ví dụ sử dụng |
|-----------|--------|-----------|---------|--------------|
| 要件定義 | Youken Teigi | Định nghĩa yêu cầu | Requirement Definition | 要件定義フェーズで仕様を確定する (Xác định spec trong phase định nghĩa yêu cầu) |
| 基本設計 | Kihon Sekkei | Thiết kế cơ bản | Basic Design / High-Level Design | 基本設計書のレビューを実施する (Thực hiện review tài liệu thiết kế cơ bản) |
| 詳細設計 | Shousai Sekkei | Thiết kế chi tiết | Detailed Design / Low-Level Design | 詳細設計の工数が不足している (Công sức thiết kế chi tiết đang thiếu) |
| 実装 | Jissou | Lập trình / Triển khai | Implementation / Coding | 実装フェーズに入りました (Đã vào phase implementation) |
| 単体テスト | Tantai Tesuto | Test đơn vị | Unit Test | 単体テストのカバレッジは85%です (Unit test coverage là 85%) |
| 結合テスト | Ketsugou Tesuto | Test tích hợp | Integration Test | 結合テストで不具合が発生しました (Bug xuất hiện trong integration test) |
| 総合テスト | Sougou Tesuto | Test tổng hợp | System Test | 総合テストの開始日を確認したい (Muốn xác nhận ngày bắt đầu system test) |
| 受入テスト | Ukeire Tesuto | Test nghiệm thu | Acceptance Test (UAT) | 受入テストの合格基準を教えてください (Xin cho biết tiêu chí pass UAT) |
| 納品 | Nouhin | Nộp hàng / Bàn giao | Delivery | 納品日は2月15日です (Ngày bàn giao là 15/2) |

---

## 2. Tài liệu thiết kế (Design Documents)

| Tiếng Nhật | Tiếng Việt | English | Ví dụ sử dụng |
|-----------|-----------|---------|--------------|
| 要件定義書 | Tài liệu định nghĩa yêu cầu | Requirement Specification | 要件定義書に記載がありません (Không có ghi trong requirement spec) |
| 機能一覧 | Danh sách chức năng | Function List | 機能一覧を更新してください (Xin cập nhật function list) |
| 画面一覧 | Danh sách màn hình | Screen List | 画面一覧に新しい画面を追加する (Thêm màn hình mới vào screen list) |
| 画面遷移図 | Sơ đồ di chuyển màn hình | Screen Transition Diagram | 画面遷移図を確認させてください (Cho tôi xác nhận screen transition) |
| 画面仕様書 | Tài liệu đặc tả màn hình | Screen Specification | 画面仕様書のレビュー結果 (Kết quả review screen spec) |
| 画面共通設計書 | Thiết kế common màn hình | Common Screen Design | 画面共通設計に従って実装する (Implement theo common screen design) |
| API一覧 | Danh sách API | API List | API一覧に新しいAPIを追記する (Thêm API mới vào list) |
| API仕様書 | Tài liệu đặc tả API | API Specification | API仕様書の最新版を送ってください (Gửi version mới nhất của API spec) |
| API共通設計 | Thiết kế common API | Common API Design | API共通設計のルールに従う (Theo rule của common API design) |
| バッチ一覧 | Danh sách Batch | Batch List | バッチ一覧を確認する (Kiểm tra batch list) |
| バッチ仕様書 | Tài liệu đặc tả Batch | Batch Specification | バッチ仕様書を作成中です (Đang viết batch spec) |
| バッチフロー定義書 | Tài liệu định nghĩa luồng Batch | Batch Flow Definition | バッチフローの承認をお願いします (Xin phê duyệt batch flow) |
| テーブル定義書 | Tài liệu định nghĩa bảng | Table Definition | テーブル定義書を修正しました (Đã sửa table definition) |
| ログ一覧 | Danh sách Log | Log List | ログ一覧にエラーログを追加する (Thêm error log vào log list) |
| 共通処理一覧 | Danh sách xử lý chung | Common Process List | 共通処理のライブラリを整備する (Chỉnh đốn library xử lý chung) |
| メッセージ一覧 | Danh sách message | Message List | メッセージ一覧のIDを採番する (Đánh số ID cho message list) |
| コード一覧 | Danh sách mã | Code List | コード一覧にステータスコードを追加 (Thêm status code vào code list) |

---

## 3. Thuật ngữ thiết kế (Design Terms)

| Tiếng Nhật | Romaji | Tiếng Việt | English | Ví dụ sử dụng |
|-----------|--------|-----------|---------|--------------|
| 共通化 | Kyoutsuu-ka | Common hóa | Commonization / Standardization | ヘッダーを共通化する (Common hóa header) |
| 標準化 | Hyoujun-ka | Tiêu chuẩn hóa | Standardization | コーディング標準化ルール (Rule tiêu chuẩn hóa coding) |
| 排他制御 | Haita Seigyo | Xử lý exclusive | Exclusive Control / Optimistic Lock | 排他制御の方式を検討する (Xem xét phương thức exclusive control) |
| 論理削除 | Ronri Sakujo | Xóa logic | Soft Delete / Logical Delete | 論理削除フラグを追加する (Thêm flag logical delete) |
| 物理削除 | Butsuri Sakujo | Xóa vật lý | Hard Delete / Physical Delete | 物理削除は行わない方針 (Phương châm không dùng physical delete) |
| 入出力項目 | Nyuushutsuryoku Koumoku | Mục nhập/xuất | Input/Output Items | 入出力項目の一覧を作成する (Tạo list input/output items) |
| イベント処理 | Ibento Shori | Xử lý event | Event Processing | ボタンクリックのイベント処理 (Event processing khi click button) |
| 初期表示 | Shoki Hyouji | Hiển thị ban đầu | Initial Display | 画面の初期表示データを設定する (Set data hiển thị ban đầu của màn hình) |
| 入力チェック | Nyuuryoku Chekku | Kiểm tra đầu vào | Input Validation | 入力チェックのロジックを実装する (Implement logic input validation) |
| 単項目チェック | Tan Koumoku Chekku | Check đơn mục | Single Item Check | 単項目チェック：必須入力、文字数、型 (Single check: required, length, type) |
| 相関チェック | Soukan Chekku | Check tương quan | Correlation Check | 開始日と終了日の相関チェック (Correlation check giữa start date và end date) |
| 業務チェック | Gyoumu Chekku | Check nghiệp vụ | Business Logic Check | 在庫数の業務チェックを行う (Thực hiện business check số lượng tồn kho) |
| 非機能要件 | Hi Kinou Youken | Yêu cầu phi chức năng | Non-Functional Requirement (NFR) | 非機能要件にレスポンス時間を追加 (Thêm response time vào NFR) |
| マルチテナント | Maruchi Tenanto | Multi-tenant | Multi-tenant | マルチテナント対応の設計 (Thiết kế hỗ trợ multi-tenant) |
| マスタ | Masuta | Master (dữ liệu gốc) | Master Data | マスタテーブルを更新する (Cập nhật master table) |
| トランザクション | Toranzakushon | Transaction | Transaction | トランザクションデータの処理 (Xử lý transaction data) |

---

## 4. Quản lý dự án (Management Terms)

| Tiếng Nhật | Romaji | Tiếng Việt | English | Ví dụ sử dụng |
|-----------|--------|-----------|---------|--------------|
| 品質 | Hinshitsu | Chất lượng | Quality | 品質目標を設定する (Thiết lập mục tiêu chất lượng) |
| コスト | Kosuto | Chi phí | Cost | コスト超過のリスクがある (Có rủi ro vượt chi phí) |
| 納期 | Nouki | Thời hạn nộp | Delivery / Deadline | 納期に間に合わない可能性がある (Có khả năng không kịp deadline) |
| QCD | QCD | Chất lượng - Chi phí - Thời hạn | Quality - Cost - Delivery | QCDのバランスを検討する (Xem xét cân bằng QCD) |
| 見積 | Mitsumori | Ước lượng | Estimation | 見積もりを再計算する (Tính lại estimation) |
| 工数 | Kousuu | Công sức (man-day/man-hour) | Effort / Man-hours | 工数が不足している (Thiếu công sức) |
| 進捗 | Shinchoku | Tiến độ | Progress | 進捗報告をお願いします (Xin báo cáo tiến độ) |
| 課題管理 | Kadai Kanri | Quản lý vấn đề | Issue Management | 課題管理表を更新する (Cập nhật bảng quản lý issue) |
| 変更管理 | Henkou Kanri | Quản lý thay đổi | Change Management | 変更管理プロセスに従う (Theo quy trình change management) |
| リスク | Risuku | Rủi ro | Risk | リスクを早期に特定する (Nhận diện risk sớm) |
| レビュー | Rebyuu | Review | Review | 設計レビューを実施する (Thực hiện design review) |
| 指摘 | Shiteki | Chỉ ra lỗi / Nhận xét | Finding / Comment | レビューの指摘件数は15件 (Số finding review là 15) |
| 確認依頼 | Kakunin Irai | Yêu cầu xác nhận | Confirmation Request | 確認依頼のメールを送る (Gửi email yêu cầu xác nhận) |
| 仕様変更 | Shiyou Henkou | Thay đổi đặc tả | Specification Change | 仕様変更の影響を分析する (Phân tích ảnh hưởng thay đổi spec) |

---

## 5. Giao tiếp (Communication Terms)

| Tiếng Nhật | Romaji | Tiếng Việt | English | Ví dụ sử dụng |
|-----------|--------|-----------|---------|--------------|
| 報連相 | Horenso | Báo cáo - Liên lạc - Trao đổi | Report - Relay - Consult | 報連相を徹底する (Thực hiện triệt để Horenso) |
| 報告 | Houkoku | Báo cáo | Report | 完了報告をお願いします (Xin báo cáo hoàn thành) |
| 連絡 | Renraku | Liên lạc | Relay / Notification | 会議時間変更の連絡 (Liên lạc thay đổi giờ meeting) |
| 相談 | Soudan | Trao đổi / Tham vấn | Consult / Discussion | 技術的な課題について相談したい (Muốn trao đổi về vấn đề kỹ thuật) |
| 敬語 | Keigo | Kính ngữ | Honorific Language | 敬語を正しく使う (Dùng keigo đúng cách) |
| 議事録 | Gijiroku | Biên bản họp | Meeting Minutes | 議事録を24時間以内に送付 (Gửi meeting minutes trong 24h) |
| 仕様書 | Shiyousho | Tài liệu đặc tả | Specification Document | 仕様書を確認してください (Xin kiểm tra spec) |
| 設計書 | Sekkeisho | Tài liệu thiết kế | Design Document | 設計書のバージョンを更新する (Cập nhật version design doc) |
| 打ち合わせ | Uchiawase | Cuộc họp / Meeting | Meeting / Discussion | 明日の打ち合わせの件 (Về cuộc họp ngày mai) |
| 定例会議 | Teirei Kaigi | Họp định kỳ | Regular Meeting | 週次定例会議のアジェンダ (Agenda họp định kỳ hàng tuần) |
| 確認事項 | Kakunin Jikou | Hạng mục cần xác nhận | Items to Confirm | 確認事項が3点あります (Có 3 điểm cần xác nhận) |

---

## 6. Chất lượng (Quality Terms)

| Tiếng Nhật | Romaji | Tiếng Việt | English | Ví dụ sử dụng |
|-----------|--------|-----------|---------|--------------|
| 品質保証 | Hinshitsu Hoshou | Đảm bảo chất lượng | Quality Assurance (QA) | 品質保証プロセスを強化する (Tăng cường quy trình QA) |
| 品質管理 | Hinshitsu Kanri | Quản lý chất lượng | Quality Control (QC) | 品質管理の基準を見直す (Xem lại tiêu chuẩn QC) |
| 説明できる品質 | Setsumei dekiru Hinshitsu | Chất lượng giải thích được | Explainable Quality | 説明できる品質を目指す (Hướng tới chất lượng giải thích được) |
| テスト | Tesuto | Test / Kiểm thử | Test | テスト計画を作成する (Tạo test plan) |
| テストケース | Tesuto Keesu | Test case | Test Case | テストケースを100件作成した (Đã tạo 100 test cases) |
| 不具合 | Fuguai | Lỗi / Bug | Bug / Defect | 不具合が3件発生した (Xuất hiện 3 bugs) |
| 障害 | Shougai | Sự cố / Lỗi nghiêm trọng | Incident / Failure | 本番環境で障害が発生 (Sự cố xảy ra trên production) |
| バグ密度 | Bagu Mitsudo | Mật độ bug | Bug Density | バグ密度は0.5件/KLOC (Bug density là 0.5 bugs/KLOC) |
| カバレッジ | Kabareji | Độ phủ | Coverage | テストカバレッジ85% (Test coverage 85%) |
| 回帰テスト | Kaiki Tesuto | Test hồi quy | Regression Test | 回帰テストを実施する (Thực hiện regression test) |
| ウォークスルー | Wookusuruu | Walk-through | Walkthrough | 設計のウォークスルーを行う (Thực hiện design walkthrough) |
| 根本原因分析 | Konpon Gen'in Bunseki | Phân tích nguyên nhân gốc | Root Cause Analysis (RCA) | 根本原因分析の結果を報告 (Báo cáo kết quả RCA) |

---

## 7. Vai trò (Roles)

| Tiếng Nhật | Romaji | Tiếng Việt | English | Vai trò chính |
|-----------|--------|-----------|---------|-------------|
| SE | Esu Ii | Kỹ sư phần mềm | Software Engineer | Thiết kế + code + test |
| PG | Pii Jii | Lập trình viên | Programmer | Code + unit test |
| PM | Pii Emu | Quản lý dự án | Project Manager | Quản lý QCD, stakeholder |
| PL | Pii Eru | Trưởng nhóm dự án | Project Leader | Dẫn dắt team dev/QA |
| BrSE | Burijji Esu Ii | Kỹ sư cầu nối | Bridge SE | Phiên dịch + điều phối Nhật-Việt |
| テスター | Tesutaa | Tester | Tester | Thiết kế + thực thi test case |
| TL | Tii Eru | Trưởng nhóm kỹ thuật | Technical Lead | Quyết định kỹ thuật, review code |
| QA | Kyuu Ei | Đảm bảo chất lượng | Quality Assurance | Audit process, đảm bảo chất lượng |
| BA | Bii Ei | Phân tích nghiệp vụ | Business Analyst | Phân tích yêu cầu, viết spec |

---

## 8. Cụm từ business thường dùng

### 8.1 Mở đầu email

| Tiếng Nhật | Romaji | Tiếng Việt | Khi nào dùng |
|-----------|--------|-----------|-------------|
| お疲れ様です | Otsukaresama desu | Cảm ơn vì làm việc vất vả | Nội bộ, đồng nghiệp |
| いつもお世話になっております | Itsumo osewa ni natte orimasu | Cảm ơn vì luôn hỗ trợ | Khách hàng (bắt buộc) |
| 初めてメールを差し上げます | Hajimete meeru wo sashiagemasu | Đây là lần đầu gửi email | Email lần đầu tiên |
| ご無沙汰しております | Gobusata shite orimasu | Lâu rồi không liên lạc | Sau thời gian dài không contact |

### 8.2 Yêu cầu & Request

| Tiếng Nhật | Romaji | Tiếng Việt |
|-----------|--------|-----------|
| ご確認いただけますでしょうか | Gokakunin itadakemasu deshouka | Có thể xác nhận được không? |
| ご検討くださいますようお願いいたします | Gokentou kudasaimasu you onegai itashimasu | Kính mong xem xét |
| ご教示いただけますと幸いです | Gokyouji itadakemasu to saiwai desu | Rất cảm kích nếu được chỉ dạy |
| お手数をおかけしますが | Otesuu wo okake shimasu ga | Xin lỗi vì làm phiền |
| 恐れ入りますが | Osore irimasu ga | Xin lỗi vì làm phiền (formal) |
| お忙しいところ恐縮ですが | Oisogashii tokoro kyoushuku desu ga | Xin lỗi vì làm phiền khi bận |

### 8.3 Xin lỗi

| Tiếng Nhật | Romaji | Tiếng Việt | Level |
|-----------|--------|-----------|-------|
| すみません | Sumimasen | Xin lỗi | Casual |
| 申し訳ございません | Moushiwake gozaimasen | Rất xin lỗi | Formal |
| 大変申し訳ございません | Taihen moushiwake gozaimasen | Vô cùng xin lỗi | Very formal |
| 深くお詫び申し上げます | Fukaku owabi moushiagemasu | Chân thành xin lỗi | Extremely formal |
| ご迷惑をおかけして申し訳ございません | Gomeiwaku wo okake shite moushiwake gozaimasen | Xin lỗi vì đã làm phiền | Standard business |

### 8.4 Cảm ơn

| Tiếng Nhật | Romaji | Tiếng Việt |
|-----------|--------|-----------|
| ありがとうございます | Arigatou gozaimasu | Cảm ơn |
| 誠にありがとうございます | Makoto ni arigatou gozaimasu | Chân thành cảm ơn |
| 感謝申し上げます | Kansha moushiagemasu | Xin bày tỏ lòng biết ơn |
| お忙しい中ありがとうございました | Oisogashii naka arigatou gozaimashita | Cảm ơn vì đã dành thời gian dù bận |

### 8.5 Kết thúc email

| Tiếng Nhật | Romaji | Tiếng Việt |
|-----------|--------|-----------|
| よろしくお願いいたします | Yoroshiku onegai itashimasu | Kính mong được hợp tác |
| 何卒よろしくお願い申し上げます | Nanitozo yoroshiku onegai moushiagemasu | Kính mong được hợp tác (very formal) |
| 引き続きよろしくお願いいたします | Hikitsuzuki yoroshiku onegai itashimasu | Tiếp tục mong được hợp tác |
| 今後ともよろしくお願いいたします | Kongo tomo yoroshiku onegai itashimasu | Mong được hợp tác lâu dài |

### 8.6 Xác nhận

| Tiếng Nhật | Romaji | Tiếng Việt | Lưu ý |
|-----------|--------|-----------|-------|
| 承知いたしました | Shouchi itashimashita | Đã hiểu / Đã nhận | Formal — dùng với khách |
| かしこまりました | Kashikomarimashita | Vâng, tôi hiểu | Very formal |
| 了解しました | Ryoukai shimashita | Đã hiểu | Nội bộ ONLY — không dùng với khách |
| 確認いたしました | Kakunin itashimashita | Đã xác nhận | Standard |

---

## 9. Từ vựng chuyên ngành IT bổ sung

| Tiếng Nhật | English | Tiếng Việt |
|-----------|---------|-----------|
| 本番環境 | Production Environment | Môi trường production |
| ステージング環境 | Staging Environment | Môi trường staging |
| 開発環境 | Development Environment | Môi trường dev |
| デプロイ | Deploy | Triển khai |
| ロールバック | Rollback | Quay lại phiên bản trước |
| ホットフィックス | Hotfix | Sửa lỗi khẩn cấp |
| マイグレーション | Migration | Di chuyển dữ liệu/hệ thống |
| リリース | Release | Phát hành |
| スプリント | Sprint | Sprint (Agile) |
| バックログ | Backlog | Danh sách công việc |
| ベロシティ | Velocity | Vận tốc team (Agile) |
| ストーリーポイント | Story Point | Điểm story (Agile estimation) |
| リファクタリング | Refactoring | Tái cấu trúc code |
| コードレビュー | Code Review | Review code |
| プルリクエスト | Pull Request | Pull request |
| CI/CD | CI/CD | Tích hợp/triển khai liên tục |

---

## 10. Lưu ý văn hóa khi sử dụng thuật ngữ

### Những cụm từ "bẫy"
| Cụm từ | Ý nghĩa literal | Ý nghĩa thật trong context Nhật |
|--------|----------------|-------------------------------|
| 検討します | Sẽ xem xét | Thường là "Không" một cách lịch sự |
| 難しいです | Khó | "Không thể" — không phải "khó nhưng có thể" |
| 大丈夫です | OK / Fine | Có thể là "OK" hoặc "Không, cảm ơn" — tùy context |
| ちょっと... | Một chút... | Đang từ chối hoặc do dự |
| 前向きに検討します | Sẽ xem xét tích cực | Có thể là "Có" nhưng chưa chắc chắn |

### Nguyên tắc dùng thuật ngữ trong tài liệu
- Giữ nguyên tiếng Nhật trong mọi tài liệu khi làm việc với Nhật
- Ví dụ: dùng `排他制御` thay vì "xử lý độc quyền"
- Điều này tránh hiểu nhầm và thể hiện sự chuyên nghiệp
- Khi cần dịch, ghi cả 2: `排他制御 (Exclusive Control / Xử lý exclusive)`
