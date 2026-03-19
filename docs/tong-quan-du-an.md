# Tổng quan Dự án - AI Agent Social Automation

**Phiên bản:** 2.0
**Cập nhật:** 2026-03-19

---

## Dự án là gì?

AI Agent Social Automation là hệ thống **tự động hóa nội dung social media** chạy hoàn toàn trên máy local (WSL2 + Docker). Hệ thống sử dụng AI (Llama 3.1 8B qua Ollama) để tạo nội dung, và n8n để orchestrate workflows.

### Đặc điểm nổi bật
- **100% local** - Không phụ thuộc cloud, chạy offline
- **$0/tháng** - Hoàn toàn miễn phí
- **3 platforms** - LinkedIn, Facebook Tech, Facebook Chinese
- **Telegram Bot** - Điều khiển mọi thứ qua điện thoại
- **Auto-comment** - Tự động comment đáp án quiz

## Kiến trúc hệ thống

```
┌─────────────────────────────────────────────────────────────────┐
│  WSL2 Docker Compose                                            │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐       │
│  │   n8n    │  │ Postgres │  │  Ollama  │  │  Redis   │       │
│  │  :5678   │  │  :5432   │  │  :11434  │  │  :6379   │       │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘       │
│       │              │             │                            │
│  9 Workflows:                                                   │
│  ├── WF1:  Content Generate      (manual)                      │
│  ├── WF2:  Batch Generate        (Mon/Wed/Fri 8AM, 3 platforms)│
│  ├── WF3:  Daily Digest          (Daily 9AM)                   │
│  ├── WF5:  Healthcheck           (Every 5min)                  │
│  ├── WF6:  Telegram Bot          (Always on, 15 commands)      │
│  ├── WF7:  Facebook Auto-Post    (manual/cron)                 │
│  ├── WF8:  LinkedIn Post Helper  (manual)                      │
│  ├── WF11: Quiz Generator        (manual/telegram)             │
│  └── WF12: Auto-Comment          (Every 30min)                 │
└─────────────────────────────────────────────────────────────────┘
                              │
              ┌───────────────┼────────────────┐
              ▼               ▼                ▼
        ┌──────────┐   ┌──────────┐    ┌──────────┐
        │ LinkedIn │   │ Facebook │    │ Telegram │
        │ (manual) │   │ (API)    │    │ (bot)    │
        └──────────┘   └──────────┘    └──────────┘
```

## Content Types

| Loại | Mô tả | Workflows |
|------|--------|-----------|
| **Post** | Bài viết text thông thường | WF1, WF2 |
| **Quiz** | Câu hỏi trắc nghiệm + auto-comment đáp án | WF11, WF12 |
| **Carousel** | PDF slides swipeable (design ready) | WF9 (planned) |
| **Infographic** | Hình ảnh thông tin (design ready) | WF10 (planned) |

## Platforms & Content Pillars

### LinkedIn
| Pillar | % | Tần suất |
|--------|---|----------|
| Tech Insights | 40% | Mon 9AM |
| Career/Productivity | 30% | Wed 12PM |
| Product/Project | 20% | Fri 5PM |
| Personal Stories | 10% | Fri 5PM (alternate) |

### Facebook Tech
| Pillar | % | Tần suất |
|--------|---|----------|
| Tech News | 35% | 2-3/tuần |
| Tutorials | 30% | 2/tuần |
| Tools & Tips | 20% | 1-2/tuần |
| Community | 15% | 1/tuần |

### Facebook Chinese
| Pillar | % | Tần suất |
|--------|---|----------|
| Vocabulary | 35% | Hàng ngày |
| Grammar | 25% | 2-3/tuần |
| Culture | 20% | 1-2/tuần |
| Practice | 20% | 1-2/tuần |

## Database

### Tables

| Table | Mục đích | Records |
|-------|----------|---------|
| `content_queue` | Quản lý content lifecycle | Dynamic |
| `prompts` | Template prompts cho AI | 18 |
| `topic_ideas` | Ý tưởng chủ đề | 40 |
| `metrics` | Engagement tracking | Dynamic |
| `workflow_logs` | Log workflow executions | Dynamic |

### Content Status Flow

```
draft → generating → pending_review → approved → scheduled → published
                                    → rejected (kèm lý do)
```

### Content Formats
- `post` - Bài viết thông thường
- `quiz` - Câu hỏi trắc nghiệm (có quiz_answer JSONB)
- `carousel` - PDF slides (planned)
- `infographic` - Hình ảnh thông tin (planned)

## Telegram Bot Commands

### Tạo nội dung
| Lệnh | Mô tả |
|-------|--------|
| `/generate <topic>` | Tạo bài LinkedIn |
| `/suggest` | AI gợi ý 5 topics |
| `/addtopic <topic>\|<pillar>\|<priority>` | Thêm topic |
| `/quiz <topic>` | Tạo quiz (planned) |

### Quản lý nội dung
| Lệnh | Mô tả |
|-------|--------|
| `/status` | Thống kê content queue |
| `/pending` | Liệt kê bài chờ review |
| `/view <id>` | Xem nội dung đầy đủ |
| `/approve <id>` | Duyệt bài |
| `/reject <id> <lý do>` | Từ chối bài |

### Đăng bài
| Lệnh | Mô tả |
|-------|--------|
| `/post_linkedin` | Lấy bài LI để đăng |
| `/post_fb` | Lấy bài FB để đăng |
| `/published <id> <url>` | Cập nhật đã đăng |

### Hệ thống
| Lệnh | Mô tả |
|-------|--------|
| `/topics` | Xem topics chưa dùng |
| `/health` | Kiểm tra services |
| `/help` | Trợ giúp |

## Tài liệu liên quan

| Tài liệu | Đường dẫn |
|-----------|-----------|
| Hướng dẫn Workflows chi tiết | `docs/huong-dan-workflows.md` |
| Content Pillars LinkedIn | `docs/content-pillars.md` |
| Content Pillars Facebook | `docs/content-pillars-facebook.md` |
| Operations Runbook | `docs/runbook.md` |
| Thiết kế Telegram Bot | `docs/design-telegram-bot-interactive.md` |
| Thiết kế Auto-posting | `docs/design-auto-posting.md` |
| Thiết kế Quiz + Auto-comment | `docs/design-quiz-auto-comment.md` |
| Thiết kế Image Generation | `docs/design-image-generation.md` |
| Thiết kế Facebook Plans | `docs/design-facebook-platforms.md` |
| Docker Setup | `docker/README.md` |
| Telegram Config | `docker/telegram-config.md` |

## Quick Start

```bash
# 1. Clone repo
git clone https://github.com/VictorAurelius/2026-AI-Agent-Social-Automation.git

# 2. Setup Docker
cd docker && cp .env.example .env
nano .env  # Edit passwords
cd .. && bash scripts/setup.sh

# 3. Import workflows vào n8n
# Mở http://localhost:5678 → Workflows → Import

# 4. Test Telegram Bot
# Gửi /help cho bot
```

---

**Tác giả:** VictorAurelius
**Cập nhật:** 2026-03-19
