# UI/Frontend Design Specifications (画面設計)

> **Mục tiêu:** Nắm vững thiết kế màn hình chi tiết (画面詳細設計) theo chuẩn dự án Nhật Bản — từ layout cơ bản đến design system toàn hệ thống
> **Level:** L1 (điền template) -> L2 (viết spec đầy đủ) -> L3 (thiết kế design system)
> **Thời gian đọc:** ~25 phút
> **Liên quan:** SE Competency #3 (詳細設計力), #5 (品質意識), CMMI PA: ENG-TS (PRC-ENG-TS-03)

---

## 1. Khái niệm cơ bản (L1)

### 1.1. Cấu trúc màn hình (Screen Layout)

Mỗi màn hình trong dự án Nhật Bản được chia thành 4 vùng chính:

```
+----------------------------------------------------------+
|  Header Area (共通)                                       |
|  Logo | Navigation | User Info | Logout                  |
+----------------------------------------------------------+
|  Search Area (検索エリア)                                  |
|  [Field 1] [Field 2] [Field 3]  [Search] [Clear]        |
+----------------------------------------------------------+
|  Result Area (結果エリア)                                  |
|  | Col A | Col B | Col C | Col D | Action |              |
|  |-------|-------|-------|-------|--------|              |
|  | data  | data  | data  | data  | Edit/Del|             |
|  Showing 1-20 of 150  [<] [1] [2] [3] [>]               |
+----------------------------------------------------------+
|  Action Area (アクションエリア)                             |
|  [CSV Export] [New Registration]                          |
+----------------------------------------------------------+
```

**Phân biệt vùng common và vùng riêng:**
- **Common (共通):** Header, Footer, Breadcrumb, Error message area — dùng chung toàn hệ thống
- **Riêng (個別):** Search area, Result area, Action area — thay đổi theo từng màn hình

### 1.2. Các loại Input Control cơ bản

| Control | Tên Nhật | Sử dụng khi | Ví dụ |
|---------|----------|-------------|-------|
| Text Input | テキスト入力 | Nhập chuỗi tự do | Tên, địa chỉ, keyword |
| Select Box | セレクトボックス | Chọn 1 từ danh sách cố định | Loại nhiên liệu (solid/liquid/gas) |
| Radio Button | ラジオボタン | Chọn 1 từ 2-5 options | Giới tính, trạng thái |
| Checkbox | チェックボックス | Chọn nhiều từ danh sách | Quyền hạn, filter |
| Date Picker | 日付入力 | Nhập ngày tháng | Ngày bắt đầu, ngày kết thúc |
| Textarea | テキストエリア | Nhập văn bản dài | Ghi chú, mô tả |
| Number Input | 数値入力 | Nhập số | Số lượng, đơn giá |

### 1.3. Validation cơ bản (Đơn mục / 単項目チェック)

Mỗi input field cần kiểm tra tối thiểu:

| Loại check | Mô tả | Ví dụ |
|------------|-------|-------|
| **Bắt buộc** (必須) | Field không được để trống | fuel_name: required |
| **Kiểu dữ liệu** (型) | Đúng kiểu: số, chuỗi, ngày | unit_price: integer only |
| **Độ dài** (桁数) | Max length, min length | fuel_name: max 100 chars |
| **Format** (形式) | Regex pattern | email: xxx@xxx.xxx |
| **Phạm vi** (範囲) | Min/max value | page: >= 1, size: 1-100 |

**Mẫu đặc tả validation đơn giản:**

```
| # | Field        | Bắt buộc | Kiểu    | Độ dài | Format     | Ghi chú          |
|---|------------- |----------|---------|--------|------------|------------------|
| 1 | fuel_name    | Không    | String  | Max 100| -          | Partial match    |
| 2 | fuel_type    | Không    | String  | -      | solid/liquid/gas | Selectbox   |
| 3 | page         | Không    | Integer | -      | >= 1       | Default: 1       |
| 4 | size         | Không    | Integer | -      | 1-100      | Default: 20      |
```

### 1.4. Đặc tả mục nhập/xuất (入出力項目)

Với mỗi mục trên màn hình, cần mô tả:

| Thuộc tính | Mô tả | Ví dụ |
|------------|-------|-------|
| **Tên hiển thị** (表示名) | Label trên UI | "Fuel Name" / "燃料名" |
| **Loại control** (コントロール種別) | Text/Select/Radio/... | Text Input |
| **Format hiển thị** (表示形式) | Định dạng | #,##0 (số), YYYY/MM/DD (ngày) |
| **Nguồn dữ liệu** (データソース) | Lấy từ đâu | API response field: fuel_name |
| **Giá trị mặc định** (初期値) | Giá trị ban đầu | "" (trống) |

---

## 2. Thực hành nâng cao (L2)

### 2.1. Component Design (Atoms / Molecules / Organisms)

Áp dụng Atomic Design để tổ chức UI components:

```
Atoms (原子)
├── Button (primary, secondary, danger, disabled)
├── Input (text, number, date, password)
├── Label
├── Icon
├── Badge (status indicator)
└── Spinner (loading)

Molecules (分子)
├── FormField = Label + Input + ErrorMessage
├── SearchBar = Input + Button(search)
├── Pagination = Button(prev) + PageNumbers + Button(next)
├── SortHeader = Label + SortIcon
└── ConfirmDialog = Title + Message + Button(OK) + Button(Cancel)

Organisms (有機体)
├── SearchForm = FormField[] + Button(search) + Button(clear)
├── DataTable = SortHeader[] + DataRow[] + Pagination
├── NavigationBar = Logo + NavItems + UserMenu
└── ActionBar = Button[] (CSV Export, New, Delete)
```

**Ví dụ đặc tả component FormField:**

```
Component: FormField
Props:
  - label: string (required)     — Label text
  - type: string (default: "text") — Input type
  - required: boolean (default: false)
  - errorMessage: string | null  — Validation error
  - value: string               — Current value
  - onChange: (value) => void    — Change handler
Behavior:
  - Hiển thị label phía trên input
  - Nếu required=true, hiển thị "*" đỏ bên cạnh label
  - Nếu errorMessage != null, hiển thị đỏ phía dưới input
  - Border input chuyển đỏ khi có error
```

### 2.2. State Management

| Loại state | Lưu ở đâu | Ví dụ | Khi nào mất |
|------------|-----------|-------|-------------|
| **Component state** | useState (React) / data (Vue) | Form input values, dropdown open/close | Component unmount |
| **Page state** | URL query params | Search params, page number, sort | Navigate away |
| **Session state** | SessionStorage | Form draft (chưa submit) | Close tab |
| **Persistent state** | LocalStorage | User preferences, language | Clear browser |
| **Global state** | Redux / Vuex / Context | Login user info, tenant_code, role | Logout |

**Nguyên tắc quản lý state cho màn hình Search + List:**

```
// Page state (lưu trên URL để có thể bookmark/share)
searchParams = {
  fuel_name: string | null,
  fuel_type: string | null,
  supplier: string | null
}
sortState = {
  sort_by: "fuel_name" | "unit_price" | "calorific_value",
  sort_order: "asc" | "desc"
}
pageState = {
  page: number,    // default: 1
  size: number     // default: 20
}

// Component state (không lưu trên URL)
isLoading: boolean
selectedRows: string[]    // fuel_info_id[]
showDeleteConfirm: boolean
```

### 2.3. Event Handling — 4 loại

Mỗi event trên màn hình phải phân loại rõ:

**Loại 1: Client-only (no API call)**

```
Event: Toggle sort direction
Trigger: Click vào sort header
Xử lý:
  1. Đọc sort_by hiện tại
  2. Nếu cùng cột → toggle sort_order (asc ↔ desc)
  3. Nếu khác cột → set sort_by = cột mới, sort_order = "asc"
  4. Update URL params
  → Trigger API call (chuyển sang Loại 2)
```

**Loại 2: Liên kết BE (API call)**

```
Event: Initial Display (初期表示)
Trigger: Page load / componentDidMount
Xử lý:
  1. Lấy tenant_code từ global state (login info)
  2. Call API: GET /api/v1/fuel-infos?page=1&size=20&sort_by=fuel_name&sort_order=asc
  3. Xử lý response:
     - 200: Binding data[] vào DataTable, update pagination
     - 401: Redirect to login page
     - 403: Hiển thị MSG_COM_002 "権限がありません"
     - 500: Hiển thị MSG_COM_001 "システムエラーが発生しました"
  4. Nếu data.length == 0: Hiển thị MSG_FUEL_001 "検索条件に一致するデータがありません"
```

**Loại 3: State management** — Thay đổi state nội bộ (vd: click checkbox → add/remove ID từ selectedRows[] → enable/disable Delete button)

**Loại 4: Side effect** — Download file, gửi mail (vd: CSV Export → call API với search params hiện tại → 200: trigger download, 400: MSG_FUEL_005, 500: MSG_COM_001)

### 2.4. Error Display Strategy

| Strategy | Khi nào dùng | UX |
|----------|-------------|-----|
| **Inline** (インライン) | Validation error cho từng field | Text đỏ ngay dưới field, border đỏ |
| **Toast** (トースト) | Success message, warning nhẹ | Góc trên phải, tự động biến mất sau 5s |
| **Modal** (モーダル) | Confirm action (delete), error nghiêm trọng | Dialog chắn màn hình, cần nhấn OK |
| **Banner** (バナー) | System-wide error, maintenance notice | Phía trên cùng page, màu vàng/đỏ |
| **Page** (ページ) | 404, 403, 500 — không thể hiển thị data | Full page error với message + action |

**Mapping error code → display strategy:**

```
| HTTP Status | Error Code        | Display      | Message ID  |
|-------------|-------------------|------------- |-------------|
| 200 (empty) | -                 | Banner       | MSG_FUEL_001|
| 400         | invalid_parameter | Inline       | (per field) |
| 401         | unauthorized      | Page redirect| -           |
| 403         | forbidden         | Modal        | MSG_COM_002 |
| 409         | conflict          | Modal        | MSG_FUEL_004|
| 500         | internal_error    | Modal        | MSG_COM_001 |
```

### 2.5. Pagination UI

**Server-side pagination (BẮT BUỘC cho list > 100 records):**

```
API Request:  GET /api/v1/fuel-infos?page=2&size=20
API Response: { data: [...], result: { total_count: 150, total_pages: 8, current_page: 2 } }

UI Display:
  "Showing 21-40 of 150 results"
  [<< First] [< Prev] [1] [2] [3] ... [8] [Next >] [Last >>]

Quy tắc hiển thị page numbers:
  - Luôn hiển thị: first, last, current, current-1, current+1
  - Dùng "..." khi có gap > 1 page
  - Ví dụ page=5, total=20: [1] ... [4] [5] [6] ... [20]
```

---

## 3. Chiến lược & Dẫn dắt (L3)

### 3.1. Design System Creation

Khi thiết kế toàn hệ thống, cần định nghĩa:

**Design Tokens (biến thiết kế):**

```css
/* Colors */
--color-primary: #1976D2;
--color-primary-hover: #1565C0;
--color-danger: #D32F2F;
--color-success: #388E3C;
--color-warning: #F57C00;
--color-text: #212121;
--color-text-secondary: #757575;
--color-border: #E0E0E0;
--color-background: #FAFAFA;

/* Spacing (8px grid system) */
--spacing-xs: 4px;
--spacing-sm: 8px;
--spacing-md: 16px;
--spacing-lg: 24px;
--spacing-xl: 32px;

/* Typography */
--font-family: "Noto Sans JP", sans-serif;
--font-size-sm: 12px;
--font-size-md: 14px;
--font-size-lg: 16px;
--font-size-xl: 20px;
--font-size-heading: 24px;

/* Border Radius */
--radius-sm: 4px;
--radius-md: 8px;
--radius-lg: 12px;
```

**Component Library Checklist:**

| Category | Components | Priority |
|----------|-----------|----------|
| **Form** | Input, Select, DatePicker, Checkbox, Radio, Textarea | Must |
| **Action** | Button, IconButton, Link, Dropdown | Must |
| **Data Display** | Table, Card, Badge, Tag, Tooltip | Must |
| **Feedback** | Toast, Modal, Spinner, ProgressBar, Skeleton | Must |
| **Navigation** | Breadcrumb, Tabs, Sidebar, Pagination | Must |
| **Layout** | Grid, Stack, Divider, Spacer | Should |

### 3.2. i18n Strategy (Quốc tế hóa)

Trong dự án Nhật Bản, thường cần hỗ trợ ít nhất 2 ngôn ngữ: Japanese (ja) và English (en).

**Cấu trúc file ngôn ngữ:**

```
src/
  locales/
    ja.json    — "search_button": "検索"
    en.json    — "search_button": "Search"
    vi.json    — "search_button": "Tìm kiếm" (nếu cần)
```

**Quy tắc i18n:**

| Rule | Mô tả |
|------|-------|
| KHÔNG hardcode text | Tất cả string hiển thị phải lấy từ file ngôn ngữ |
| Message ID có hệ thống | Format: `{module}_{screen}_{element}` (vd: `fuel_list_search_btn`) |
| Date format theo locale | ja: YYYY/MM/DD, en: MM/DD/YYYY |
| Number format theo locale | ja: 1,234.56 (same as en) |
| Error message có ID | MSG_COM_001, MSG_FUEL_001 — không phụ thuộc ngôn ngữ |

### 3.3. Cross-Module UI Consistency

**Checklist nhất quán giữa các module:**

- [ ] Header/Footer giống nhau toàn hệ thống
- [ ] Button style: primary (xanh), secondary (trắng), danger (đỏ) — nhất quán
- [ ] Table style: header màu xám, hover row highlight, stripe pattern
- [ ] Form layout: label trên, input dưới, error message dưới input
- [ ] Spacing: dùng grid system 8px, không dùng giá trị tùy ý
- [ ] Loading state: Spinner tại cùng vị trí (center of content area)
- [ ] Empty state: Cùng format message khi không có data
- [ ] Error handling: Cùng strategy (inline/toast/modal) cho cùng loại error

### 3.4. Responsive Design

| Breakpoint | Name | Layout | Target |
|------------|------|--------|--------|
| >= 1280px | Desktop | Full layout, sidebar visible | PC |
| 768-1279px | Tablet | Collapsed sidebar, table scroll horizontal | Tablet |
| < 768px | Mobile | Stack layout, hamburger menu | Phone |

**Nguyên tắc responsive cho dự án Nhật:**
- Desktop-first (đa số dự án nội bộ là PC-only)
- Nếu có mobile: table chuyển sang card view
- Form: 2 columns (desktop) → 1 column (mobile)
- Action buttons: fixed bottom bar trên mobile

### 3.5. Accessibility (A11y) Cơ bản

| Tiêu chí | Mô tả | WCAG |
|----------|-------|------|
| **Contrast** | Text/background ratio >= 4.5:1 | AA |
| **Keyboard** | Tất cả action có thể thực hiện bằng keyboard (Tab, Enter, Esc) | A |
| **Label** | Mỗi input có label tương ứng (htmlFor/id) | A |
| **Alt text** | Mỗi image có alt text mô tả | A |
| **Focus** | Focus indicator rõ ràng (outline) khi navigate bằng keyboard | AA |
| **Error** | Error message không chỉ dùng màu (thêm icon hoặc text) | A |

---

## 4. Tự kiểm tra

### Bài tập: Viết Screen Spec cho màn hình "Search + List + Detail"

**Đề bài:** Cho màn hình "Danh sách thông tin nhiên liệu" (燃料情報一覧画面), hãy viết đặc tả đầy đủ gồm:

1. **Layout màn hình** — Vẽ phân vùng (search area, result area, action area), phân biệt common/riêng

2. **Đặc tả mục nhập/xuất** — Bảng liệt kê tất cả mục với: tên hiển thị, control type, format, nguồn dữ liệu, giá trị mặc định

3. **Đặc tả event xử lý** — Tối thiểu 6 events:
   - a) Initial display (初期表示)
   - b) Search (検索)
   - c) Sort (ソート)
   - d) Paging (ページング)
   - e) Delete (削除)
   - f) CSV Export

   Mỗi event cần: trigger → xử lý → API call → response handling → UI update

4. **Đặc tả validation** — Client-side vs Server-side, đơn mục + tương quan

5. **Danh sách message** — Message ID, nội dung, điều kiện hiển thị

**Tiêu chí đánh giá (theo Rubric dự án Nhật):**

| Tiêu chí | L1 (>= 60%) | L2 (>= 70%) | L3 (>= 80%) |
|----------|-------------|-------------|-------------|
| Layout đầy đủ vùng | Có 3 vùng chính | + Phân biệt common/riêng | + Responsive strategy |
| Event xử lý | 3-4 events cơ bản | Đầy đủ 6 events + error handling | + Edge cases (race condition, token expired) |
| Validation | Đơn mục cơ bản | + Tương quan + client/server | + Nghiệp vụ phức tạp |
| Message mapping | Có message | Đầy đủ ID + nội dung | + i18n ready |

---

## 5. Tài liệu tham khảo

| Tài liệu | Nội dung |
|----------|---------|
| SE năng-lực.md #3 (詳細設計力) | Tiêu chí đánh giá screen spec theo level |
| SE test thiết-kế-chi-tiết.md Phần B | Đề thi mẫu + đáp án screen spec |
| GLN-ENG-TS-02 | Hướng dẫn viết Detail Design, bao gồm screen spec |
| RUL-ENG-TS-01 Section 2.1 | Màn hình thiết kế bắt buộc trong Basic Design |
| RUL-ENG-TS-01 Section 3.1 | Nội dung bắt buộc trong Detail Design |
| RUL-ENG-TS-02 Section 2.2 | Tiêu chí từ chối design review cho Basic Design |
| SE năng-lực.md #5 (品質意識) | Tính nhất quán, trường hợp ngoại lệ, NFR |
