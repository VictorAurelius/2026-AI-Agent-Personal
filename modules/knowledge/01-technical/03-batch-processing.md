# Batch Processing Design

> **Mục tiêu:** Nắm vững thiết kế batch (xử lý hàng loạt) cho dự án outsourcing Nhật Bản (CMMI Level 3)
> **Level:** L1 -> L2 -> L3
> **Thời gian đọc:** ~30 phút
> **Liên quan:** SE Competency #2 (基本設計力) - "Danh sách Batch & Batch flow", #3 (詳細設計力), CMMI PA: ENG-TS

---

## 1. Khái niệm cơ bản (L1)

### 1.1. Batch vs API (Sync vs Async)

| Tiêu chí | API (đồng bộ) | Batch (bất đồng bộ) |
|----------|--------------|-------------------|
| Thời gian | Trả kết quả ngay (<= 3-5 giây) | Chạy ngầm, có thể mất phút đến giờ |
| Trigger | User click / hệ thống gọi | Định kỳ (cron) hoặc event |
| Dữ liệu | 1 record hoặc ít records | Hàng nghìn đến hàng triệu records |
| Response | Response body trả ngay | Thông báo khi hoàn thành (email, notification) |
| Ví dụ | Tạo/sửa/xoá 1 nhiên liệu | Export CSV 10,000 records |
| Ví dụ | Lấy danh sách có phân trang | Import CSV hàng loạt |
| Ví dụ | Tìm kiếm | Tính toán báo cáo hàng ngày |

**Khi nào dùng batch thay vì API?**
- Xử lý > 1,000 records cùng lúc
- Thời gian xử lý > 5 giây (vượt response time target)
- Cần chạy định kỳ (hàng ngày, hàng tuần)
- Không cần kết quả trả về ngay cho user

### 1.2. Trigger Types

| Loại | Tiếng Nhật | Mô tả | Ví dụ |
|------|-----------|-------|-------|
| Định kỳ (Scheduled) | 定期実行 | Chạy theo lịch (cron) | Báo cáo hàng ngày lúc 02:00 AM |
| Event (Sự kiện) | イベント実行 | Chạy khi có sự kiện | User bấm nút "Export CSV" |
| Manual | 手動実行 | Admin chạy tay | Migration dữ liệu |

```
# Cron expression ví dụ
0 2 * * *     # Hàng ngày lúc 02:00
0 0 * * 1     # Hàng tuần thứ 2 lúc 00:00
0 6 1 * *     # Ngày 1 hàng tháng lúc 06:00
```

### 1.3. Input/Output Definition

Mỗi batch PHẢI định nghĩa rõ Input và Output:

```
Batch: fuel_info_csv_export

Input:
  - tenant_code: string (từ JWT của user trigger)
  - search_params: object (điều kiện tìm kiếm hiện tại)
    - fuel_name: string (optional)
    - fuel_type: string (optional)
    - supplier: string (optional)
  - user_id: string (người yêu cầu export)
  - request_id: UUID (ID của yêu cầu, để tracking)

Output:
  - CSV file: /export/{tenant_code}/{request_id}.csv
  - Status: success / error
  - Record count: số dòng đã export
  - Error detail: chi tiết lỗi (nếu có)
```

---

## 2. Thực hành nâng cao (L2)

### 2.1. Batch Flow Design

**3 loại flow:**

```
1. Tuần tự (Sequential):
   Step A -> Step B -> Step C
   Ví dụ: Đọc DB -> Xử lý -> Ghi CSV

2. Song song (Parallel):
   Step A -> Step B1 (parallel) -> Step C
              Step B2 (parallel)
   Ví dụ: Export CSV + Gửi email đồng thời

3. Có điều kiện (Conditional):
   Step A -> [Điều kiện] -> Step B (true)
                          -> Step C (false)
   Ví dụ: Kiểm tra số record -> Nếu > 10,000 -> Báo lỗi
```

**Ví dụ batch flow cho CSV export:**

```
[START]
  |
  v
[1. Validate input]
  | - Kiểm tra tenant_code hợp lệ
  | - Kiểm tra search_params format
  |--- Lỗi -> [Log error] -> [Update status = 'error'] -> [END]
  |
  v
[2. Count records]
  | - SELECT COUNT(*) với search conditions
  |--- > 10,000 -> [Log warning] -> [Update status = 'exceed_limit'] -> [END]
  |
  v
[3. Query data] (chunking, mỗi lần 1000 records)
  | - SELECT ... WHERE conditions LIMIT 1000 OFFSET :offset
  |
  v
[4. Write CSV]
  | - Header row
  | - Data rows (append từng chunk)
  |--- Lỗi ghi file -> [Log error] -> [Cleanup temp file] -> [Update status = 'error'] -> [END]
  |
  v
[5. Update status]
  | - status = 'completed'
  | - file_path = '/export/{tenant}/{request_id}.csv'
  | - record_count = N
  |
  v
[6. Notify user]
  | - Gửi notification (email hoặc in-app)
  |
  v
[END]
```

### 2.2. Error Handling + Retry Strategy

| Loại lỗi | Xử lý | Retry |
|----------|-------|-------|
| DB connection error | Log + retry | Có, tối đa 3 lần, interval 5s |
| File write error | Log + cleanup temp | Có, tối đa 2 lần |
| Data validation error | Log record lỗi, tiếp tục | Không (ghi vào error log) |
| Timeout | Log + partial result | Có, resume từ record cuối |
| Out of memory | Log + alert | Không (cần tăng resource) |

```python
# Retry pattern
MAX_RETRIES = 3
RETRY_INTERVAL = 5  # seconds

async def execute_with_retry(func, *args):
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            return await func(*args)
        except DBConnectionError as e:
            logger.warning(f"Attempt {attempt}/{MAX_RETRIES} failed: {e}")
            if attempt == MAX_RETRIES:
                logger.error(f"All {MAX_RETRIES} attempts failed")
                raise
            await asyncio.sleep(RETRY_INTERVAL * attempt)  # Exponential backoff
```

### 2.3. Idempotent Design

Batch PHẢI idempotent: chạy lại không tạo ra kết quả sai.

```python
# SAI - Không idempotent (chạy lại sẽ tạo trùng file)
def export_csv(params):
    filename = f"export_{datetime.now().strftime('%Y%m%d%H%M%S')}.csv"
    write_csv(filename, data)

# ĐÚNG - Idempotent (chạy lại sẽ ghi đè file cũ)
def export_csv(request_id, params):
    filename = f"export_{request_id}.csv"  # Dùng request_id làm tên file
    if os.path.exists(filename):
        os.remove(filename)  # Xoá file cũ trước khi ghi lại
    write_csv(filename, data)
```

**Nguyên tắc idempotent:**
- Dùng request_id/batch_id để định danh mỗi lần chạy
- Trước khi ghi, xoá kết quả cũ của cùng request_id
- Không dùng timestamp làm identifier
- Ghi nhận trạng thái (status) để biết batch đã chạy hay chưa

### 2.4. CSV Export với Chunking

```python
CHUNK_SIZE = 1000
MAX_RECORDS = 10000

async def export_fuel_info_csv(request_id, tenant_code, search_params, user_id):
    """Batch export CSV với chunking."""
    log_batch_start(request_id, "fuel_info_csv_export")

    try:
        # Step 1: Count
        total = await count_fuel_info(tenant_code, search_params)
        if total > MAX_RECORDS:
            raise ExceedLimitError(f"Record count {total} exceeds limit {MAX_RECORDS}")

        log_info(f"Total records to export: {total}")

        # Step 2: Export từng chunk
        filepath = f"/export/{tenant_code}/{request_id}.csv"
        offset = 0
        records_written = 0

        with open(filepath, 'w', newline='', encoding='utf-8-sig') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(CSV_HEADER)  # Header row

            while offset < total:
                chunk = await query_fuel_info(
                    tenant_code, search_params,
                    limit=CHUNK_SIZE, offset=offset
                )
                for row in chunk:
                    writer.writerow(format_csv_row(row))
                    records_written += 1

                offset += CHUNK_SIZE
                log_info(f"Progress: {records_written}/{total}")

        # Step 3: Update status
        await update_export_status(request_id, 'completed', filepath, records_written)
        log_batch_end(request_id, "fuel_info_csv_export", records_written)

    except Exception as e:
        await update_export_status(request_id, 'error', error_detail=str(e))
        log_batch_error(request_id, "fuel_info_csv_export", e)
        raise
```

### 2.5. Log Design cho Batch

Batch PHẢI có log đầy đủ để monitoring và điều tra sự cố:

| Thời điểm | Log Level | Keyword | Nội dung |
|-----------|----------|---------|---------|
| Bắt đầu | INFO | BATCH_START | batch_name, request_id, trigger_type, input_params |
| Tiến độ | INFO | BATCH_PROGRESS | request_id, processed/total |
| Kết thúc thành công | INFO | BATCH_END | request_id, record_count, duration_ms |
| Lỗi có thể retry | WARNING | BATCH_RETRY | request_id, attempt, error_type |
| Lỗi nghiêm trọng | ERROR | BATCH_ERROR | request_id, error_type, error_detail, stack_trace |

```json
// Ví dụ JSON log format
{
  "timestamp": "2026-03-28T10:00:00.000+09:00",
  "level": "INFO",
  "keyword": "BATCH_START",
  "batch_name": "fuel_info_csv_export",
  "request_id": "550e8400-e29b-41d4-a716-446655440000",
  "tenant_code": "company_a",
  "trigger_type": "event",
  "input_params": {"fuel_type": "solid"}
}
```

---

## 3. Chiến lược & Dẫn dắt (L3)

### 3.1. Complex Batch với Intermediate Interface (IF)

Khi batch liên kết nhiều hệ thống, cần thiết kế IF trung gian:

```
[Hệ thống A]                    [Hệ thống B]
     |                               |
     v                               v
[Batch Export A]              [Batch Import B]
     |                               ^
     v                               |
  [CSV/JSON] --> [IF trung gian] --> [Validate] --> [Import]
                 (shared storage)

IF trung gian:
- Định dạng: CSV, JSON, XML (thoả thuận giữa 2 hệ thống)
- Lưu trữ: shared folder, S3 bucket, message queue
- Naming: {source}_{target}_{yyyyMMdd}_{sequence}.csv
- Retention: giữ 30 ngày, sau đó archive
```

**Ví dụ batch flow phức tạp (nhiều bước, có IF):**

```
[1. Trigger] (Cron 02:00 AM)
  |
  v
[2. Export từ Hệ thống Đốt] (sequential)
  | - Query combustion_log của ngày hôm trước
  | - Ghi CSV: combustion_{yyyyMMdd}.csv
  | - Đặt lên IF trung gian (S3)
  |
  v
[3. Tính toán hiệu suất] (parallel với step 4)
  | - Đọc CSV từ IF
  | - Tính efficiency, emissions
  | - Ghi kết quả vào DB
  |
  v (wait for both)
[4. Export báo cáo] (parallel với step 3)
  | - Query dữ liệu tổng hợp
  | - Ghi report CSV
  |
  v
[5. Gửi báo cáo] (sequential)
  | - Email báo cáo cho manager
  | - Notification trên hệ thống
  |
  v
[6. Cleanup] (sequential)
  | - Xoá file tạm
  | - Archive IF files > 30 ngày
  |
  v
[END]
```

### 3.2. Data Consistency: Batch + API đồng thời

**Vấn đề:** Batch đang đọc dữ liệu, đồng thời user sửa qua API. Làm sao?

```
Giải pháp 1: Snapshot isolation (khuyến nghị)
  - Batch đọc dữ liệu tại thời điểm bắt đầu (snapshot)
  - API vẫn cập nhật bình thường
  - Batch không bị ảnh hưởng bởi thay đổi sau snapshot
  
  SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;
  -- Tất cả query trong batch đều thấy cùng 1 snapshot

Giải pháp 2: Time-based filter
  - Batch chỉ xử lý dữ liệu trước thời điểm T
  - WHERE updated_at < :batch_start_time
  
Giải pháp 3: Status flag
  - Batch mark records đang xử lý: processing_status = 'in_progress'
  - API kiểm tra trước khi update
  - Batch cập nhật status khi xong
  - Rủi ro: nếu batch crash, records bị lock. Cần có timeout.
```

### 3.3. Monitoring và Alerting

```
Dashboard metrics cho batch:

| Metric | Mô tả | Alert threshold |
|--------|-------|----------------|
| Execution time | Thời gian chạy | > 2x thời gian trung bình |
| Record count | Số record xử lý | Chênh lệch > 20% so với hôm trước |
| Error rate | % record lỗi | > 5% |
| Retry count | Số lần retry | > 3 lần cho 1 record |
| Queue depth | Số batch đang chờ | > 10 |

Alert escalation:
- WARNING: Log + notification cho dev team
- ERROR: Log + email cho TL + dev team
- CRITICAL: Log + email + phone call cho PM + TL
```

### 3.4. Thiết kế Batch toàn hệ thống

```
Danh sách batch của hệ thống:

| No | Batch | Thời điểm | Trigger | Module | Mô tả |
|----|-------|-----------|---------|--------|-------|
| B-001 | daily_combustion_report | 02:00 AM | Cron | Báo cáo | Tổng hợp dữ liệu đốt hàng ngày |
| B-002 | fuel_info_csv_export | On-demand | Event | Nhiên liệu | Export CSV theo yêu cầu user |
| B-003 | monthly_cost_calculation | 01:00 AM ngày 1 | Cron | Tài chính | Tính chi phí nhiên liệu tháng |
| B-004 | data_archive | 03:00 AM Chủ Nhật | Cron | Hệ thống | Archive dữ liệu cũ > 1 năm |
| B-005 | fuel_price_import | On-demand | Event | Nhiên liệu | Import giá nhiên liệu từ CSV |

Quy tắc:
1. Batch định kỳ chạy trong khung giờ 00:00 - 06:00 (ít user)
2. Batch không được chạy đồng thời nếu truy cập cùng bảng
3. Mỗi batch có timeout (default: 1 giờ)
4. Tất cả batch phải idempotent
```

---

## 4. Tự kiểm tra

### Câu hỏi lý thuyết

1. **L1:** Khi nào dùng batch thay vì API? Cho 3 ví dụ cụ thể.
2. **L1:** Định kỳ và event trigger khác nhau thế nào?
3. **L2:** Tại sao batch phải idempotent? Cho ví dụ batch không idempotent và hậu quả.
4. **L2:** Giải thích retry strategy với exponential backoff.
5. **L3:** Batch đang đọc 100,000 records, đồng thời user UPDATE qua API. Xảy ra gì? Giải pháp?
6. **L3:** Làm thế nào thiết kế IF trung gian giữa 2 hệ thống?

### Bài tập thực hành

**Đề bài:** Thiết kế batch flow cho import 10,000 records CSV với yêu cầu:
- File CSV upload bởi user qua màn hình
- Mỗi dòng: fuel_name, fuel_type, calorific_value, unit_price, supplier_name
- Validation: tất cả trường bắt buộc, fuel_type phải là solid/liquid/gas, số phải > 0
- Nếu dòng lỗi: ghi vào error log, tiếp tục dòng tiếp theo
- Sau khi hoàn thành: tạo report (X dòng thành công, Y dòng lỗi, danh sách dòng lỗi)
- Multi-tenant: tất cả record thuộc tenant của user upload
- Idempotent: nếu chạy lại với cùng file, không tạo trùng

**Yêu cầu output:**
1. Vẽ batch flow diagram (các bước tuần tự)
2. Định nghĩa Input/Output
3. Thiết kế error handling (mỗi loại lỗi xử lý thế nào)
4. Thiết kế log (keyword, level, nội dung)
5. Viết pseudo code cho logic chính
6. Mô tả re-run strategy (idempotent)

### Tiêu chí đạt

| Level | Tiêu chí |
|-------|---------|
| L1 | Hiểu batch vs API, biết trigger types, định nghĩa được I/O |
| L2 | Batch flow rõ ràng, error handling + retry, idempotent, log design đầy đủ |
| L3 | IF trung gian, data consistency batch + API, monitoring, thiết kế batch toàn hệ thống |

---

## 5. Tài liệu tham khảo

- **SE Competency:** nang-luc.md - Nhóm #2: "Danh sách Batch & Batch flow", Nhóm #3: "Thiết kế Batch"
- **Bài test tham khảo:** thiet-ke-co-ban.md - Phần A-2 (Danh sách Batch), Phần C (CSV export analysis)
- **Bài test tham khảo:** thiet-ke-chi-tiet.md - Phần C (Batch specification)
- **CMMI Guide:** GLN-ENG-TS-01 - Section 2: Requirements Analysis (NFR: performance, throughput)
- **CMMI Rule:** RUL-ENG-TS-01 - Section 3: Detail Design (process flow, error handling)
