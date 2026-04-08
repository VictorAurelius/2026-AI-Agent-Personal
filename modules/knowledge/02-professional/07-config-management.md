# Configuration Management & Git Workflow

> **Mục tiêu:** Nắm vững Configuration Management (CM) từ cơ bản đến nâng cao, áp dụng Git workflow theo chuẩn CMMI cho dự án outsource Nhật Bản
> **Level:** L1 -> L2 -> L3
> **Thời gian đọc:** ~25 phút
> **Liên quan:** PM Competency #4 (品質管理 — 納品物管理) / CMMI PA: CM (SUP), PP, PMC

---

## 1. Khái niệm cơ bản (L1)

### 1.1 Configuration Management (CM) là gì?

CM là quy trình quản lý và kiểm soát configuration items (CI) — code, tài liệu, artifacts — trong suốt vòng đời dự án, đảm bảo:
- **Integrity:** Mọi thay đổi đều được kiểm soát
- **Traceability:** Biết ai thay đổi gì, khi nào, tại sao
- **Recoverability:** Có thể khôi phục bất kỳ phiên bản nào

### 1.2 Git cơ bản — 5 lệnh cần biết

```
# 1. Clone repository
git clone <URL>

# 2. Tạo branch mới
git checkout -b feature/ISSUE-123-add-login

# 3. Stage thay đổi
git add src/login.js src/login.test.js

# 4. Commit với message rõ ràng
git commit -m "feat(auth): add login function"

# 5. Push lên remote
git push origin feature/ISSUE-123-add-login
```

### 1.3 Branch Naming Conventions

| Prefix | Mục đích | Ví dụ |
|--------|---------|-------|
| `feature/` | Tính năng mới | `feature/ISSUE-123-add-login` |
| `bugfix/` | Sửa lỗi phát hiện trong dev/test | `bugfix/ISSUE-124-fix-null-pointer` |
| `hotfix/` | Sửa lỗi khẩn cấp trên production | `hotfix/ISSUE-125-critical-auth-fix` |
| `release/` | Chuẩn bị release | `release/v1.2.0` |

**Quy tắc đặt tên:**
- Luôn bắt đầu bằng prefix + `/`
- Bao gồm Issue ID (ISSUE-123)
- Mô tả ngắn gọn bằng dash `-`
- Chữ thường, không dấu, không space

### 1.4 Commit Message cơ bản

```
<type>(<scope>): <description>

Ví dụ:
  feat(auth): add OAuth2 login function
  fix(api): resolve null pointer in user endpoint
  docs(readme): update setup instructions
  test(auth): add login integration test
```

| Type | Mục đích |
|------|---------|
| `feat` | Tính năng mới |
| `fix` | Sửa lỗi |
| `docs` | Cập nhật tài liệu |
| `refactor` | Tái cấu trúc code |
| `test` | Thêm/sửa test |
| `chore` | Build, dependencies |

---

## 2. Thực hành nâng cao (L2)

### 2.1 Gitflow Strategy

**Cho dự án Size M/L (>= 100 MD):**

```
main (production) ----*-----------*---------*-------> releases
                       \         / \       /
develop (integration) --*---*---*---*---*-*---------> integration
                         \   /       \   /
feature/add-login --------*-*         \ /
                                       *
feature/add-search ---------------------*
                        \
hotfix/fix-critical -----*-- (merge vào BOTH main và develop)
```

**Rules:**
- `main`: Protected, chỉ merge từ develop hoặc hotfix
- `develop`: Protected, integration branch
- `feature/*`: Branch từ develop, merge về develop qua MR/PR
- `hotfix/*`: Branch từ main, merge về main VÀ develop
- `release/*`: Branch từ develop, merge về main khi sẵn sàng

**Cho dự án Size S (< 100 MD) — GitHub Flow:**

```
main (production) ----*-----*-----*-------> releases
                       \   / \   /
feature/add-login ------*-*   \ /
                               *
fix/auth-bug ------------------*
```

### 2.2 CI/CD Pipeline Setup

```
Push code -> Build -> Unit Tests -> Linting -> Security Scan -> Quality Gate
                                                                  |
                                                          PASS: Merge OK
                                                          FAIL: Block merge
```

**Quality Gates (bắt buộc cho Size M/L):**

| Gate | Ngưỡng | Gate | Ngưỡng |
|------|--------|------|--------|
| Test Coverage | >= 80% | Linting | 0 errors |
| Build | Success | Security | 0 critical/high |

### 2.3 Baseline Management

**Baseline** = "snapshot" chính thức của dự án tại 1 thời điểm, đã được phê duyệt.

**3 loại Baseline:**

```
+---------------------+     +---------------------+     +---------------------+
| REQUIREMENTS        |     | DESIGN              |     | PRODUCT             |
| BASELINE            |     | BASELINE            |     | BASELINE            |
|                     |     |                     |     |                     |
| Thời điểm:          |     | Thời điểm:          |     | Thời điểm:          |
| Sau khi SRS         |     | Sau khi HLD/LLD     |     | Mỗi release         |
| approved            |     | approved            |     | deployment          |
|                     |     |                     |     |                     |
| Nội dung:           |     | Nội dung:           |     | Nội dung:           |
| - SRS               |     | - Architecture docs |     | - Source code       |
| - Use Cases         |     | - Design documents  |     | - Binaries          |
| - Traceability      |     | - Diagrams          |     | - Configs           |
|   matrix            |     |                     |     | - Release notes     |
+---------------------+     +---------------------+     +---------------------+
```

**Tạo baseline bằng Git tag:**

```bash
# Tạo tag với semantic versioning
git tag -a v1.0.0 -m "Release 1.0.0: Initial production release"

# Tag cho requirements baseline
git tag -a baseline-requirements-v1.0 -m "Requirements approved by customer"

# Tag cho design baseline
git tag -a baseline-design-v1.0 -m "HLD/LLD approved"

# Push tags
git push origin --tags
```

**Tailoring Baseline theo Size:**

| Size | Baseline Frequency | Change Control | Audit |
|------|-------------------|----------------|-------|
| S | Chỉ khi đóng dự án | PM approval | Không bắt buộc |
| M | Mỗi milestone (3-4 baselines) | PM approval + Change log | Bắt buộc |
| L | Mỗi milestone + giữa milestone | CCB approval (PM+QA+Customer) | Bắt buộc + Physical storage |

### 2.4 Semantic Versioning

```
v MAJOR . MINOR . PATCH
  |        |       |
  |        |       +-- Bug fix, không đổi API
  |        +---------- Tính năng mới, backward compatible
  +------------------- Breaking change, không backward compatible

Ví dụ:
  v1.0.0  -> Initial release
  v1.0.1  -> Fix bug login
  v1.1.0  -> Thêm tính năng search (backward compatible)
  v2.0.0  -> Đổi API authentication (breaking change)
```

### 2.5 PR/MR Workflow với Code Review

```
Developer tạo PR/MR
        |
        v
+---------------------------+
| PR/MR Template            |
| - Mô tả thay đổi          |
| - Link ISSUE/requirement  |
| - Screenshots (nếu có)    |
| - Checklist tự-review     |
+---------------------------+
        |
        v
+---------------------------+
| Reviewer check:           |
| [x] Logic correct?        |
| [x] Naming standard?      |
| [x] Edge cases handled?   |
| [x] Unit test added?      |
| [x] No security issues?   |
+---------------------------+
        |
   +----+----+
   |         |
APPROVE    REQUEST CHANGES
   |         |
   v         v
[CI pass]  [Developer fix]
   |         |
   v         +---> [Push update] ---> [Re-review]
[Merge]
   |
   v
[Delete feature branch]
```

**Quy định review (theo RUL-ENG-TS-04):**
- Review tối đa **200 LOC/giờ**
- Tối thiểu **1 reviewer** phê duyệt
- CI/CD pipeline PHẢI pass trước khi merge
- Không allow direct commits to main/develop

### 2.6 Configuration Items (CI) — Xác định và Quản lý

**Phân loại CI:**

| Loại | Ví dụ | Lưu trữ |
|------|-------|--------|
| Code artifacts | Source code, test code, build scripts | Git repository |
| Documents | SRS, HLD, LLD, Test plans | Git docs/ hoặc Wiki |
| Deliverables | Binaries, DB scripts, configs, release notes | Git + CI/CD artifacts |
| Bilingual docs | JP bản chính thức + VN/EN bản dịch | Git (cùng version number) |

**Lưu ý dự án Nhật:** Tài liệu song ngữ (JP và VN/EN) của cùng 1 tài liệu PHẢI cùng version number và được sync khi có thay đổi. JP là bản chính thức (authoritative).

### 2.7 Repository Maintenance

| Tần suất | Việc cần làm | Chi tiết |
|---------|-------------|---------|
| Hàng tháng | Stale Branch Cleanup | Xóa branches > 14 ngày không commit (confirm với owner trước) |
| Hàng quý | Large File Audit | Files > 50MB chuyển Git LFS, binary không cần xóa khỏi history |
| Hàng quý | Repo Size Check | `du -sh .git`, giảm size nếu cần |

---

## 3. Chiến lược & Dẫn dắt (L3)

### 3.1 CM Strategy Design cho tổ chức

**CM Strategy Document gồm 5 phần chính:**

| Phần | Nội dung | Ví dụ |
|------|---------|-------|
| Tool Selection | VCS, Platform, CI/CD, Issue Tracking | Git + GitLab + Jenkins + Redmine |
| Repo Structure | src/, tests/, docs/, scripts/, .gitignore | Chuẩn hóa cho tất cả dự án |
| Branch Strategy | Chọn theo size dự án | S: GitHub Flow, M/L: Gitflow |
| Access Control | Visibility, branch protection, roles | Private, main/develop protected |
| Backup & DR | Frequency, RTO, RPO | Daily incremental, RTO <4h, RPO <24h |

### 3.2 Configuration Audit Process (PPQA Quarterly)

| Hạng mục | Kiểm tra |
|---------|---------|
| Version Control | 100% code trong Git, branch strategy followed, commit convention, stale branches cleanup |
| Baseline | Tạo đúng milestone, tags đúng semver, audit passed (M/L), 100% files khớp approved list |
| Change Control | CR ticket cho mỗi thay đổi baseline, impact analysis, approval ghi nhận, change log updated |
| Backup | Chạy đúng lịch, restore test quarterly, RTO/RPO đạt yêu cầu |
| Access Control | Đúng role assignment, branch protection active, không unauthorized access |

### 3.3 Change Control Board (CCB) — Dự án Size L

```
Submit CR --> CCB Meeting (3 ngày) --> CCB Review --> Decision (24h)
  |              |                       |              |
  Mô tả,         PM (Chủ tọa)            Feasibility,   APPROVED/
  Impact         QA Lead                 Risk vs        REJECTED/
  Analysis       Customer Rep            Benefit        DEFERRED
```

**Sau khi APPROVED:** Implement -> Test + Regression -> Re-run baseline audit -> New baseline version -> Update Release Notes -> Close CR

**Size S/M (Simplified):** PM review và approve (không cần CCB), ghi nhận trong Change Log.

### 3.4 Release Management Framework

| Giai đoạn | Checklist chính |
|-----------|----------------|
| PRE-RELEASE | All items completed, changes merged, tests passed, baseline audit (M/L), release notes |
| RELEASE | Tạo release branch, final testing, fix critical only, merge to main, tag vX.Y.Z, deploy |
| POST-RELEASE | Merge to develop, verify production, monitor 24-48h, notify stakeholders, archive docs |

### 3.5 Rollback Procedures

| Severity | Hành động | Thời gian |
|---------|----------|----------|
| CRITICAL (down/data loss) | Rollback ngay lập tức | < 30 phút |
| MAJOR (function broken) | Hotfix hoặc Rollback | < 4 giờ |
| MINOR (cosmetic) | Schedule fix next sprint | Next sprint |

**Rollback steps:** `git log --tags` -> `git checkout v1.0.0` -> deploy previous build -> tag rollback event -> notify stakeholders -> tạo hotfix branch fix root cause.

### 3.6 Access Control & Permissions

| Role | Quyền | Ví dụ |
|------|-------|-------|
| Owner | Full access, settings | Tech Lead / CM Manager |
| Maintainer | Merge main/develop | Senior Dev, QA Lead |
| Developer | Push feature branches, create MR | Developers |
| Reporter/Guest | Read-only | Customer, Stakeholders |

**Branch Protection:** main và develop: BLOCKED direct push, MR required, >= 1 approval, CI must pass. Feature branches: push allowed, MR recommended.

---

## 4. Tự kiểm tra

### Bài tập 1: Git Workflow cơ bản (L1)

**Tình huống:** Bạn là developer mới vào dự án. Task: implement tính năng search (ISSUE-456).

**Yêu cầu:**
1. Viết lệnh Git để: tạo branch, code, commit, push
2. Viết commit message cho 3 commits (feat, fix, test)
3. Mô tả quy trình tạo PR/MR

### Bài tập 2: Thiết kế Git Branching Strategy (L2)

**Tình huống:** Dự án Size M, 8 người, 5 tháng. Mô hình Hybrid. Khách hàng Nhật yêu cầu release mỗi 6 tuần.

**Yêu cầu:**
1. Chọn branching strategy (GitHub Flow hay Gitflow?) và giải thích lý do
2. Xác định naming convention cho branches
3. Thiết kế CI/CD pipeline với quality gates
4. Lập lịch baseline (bao nhiêu baselines? thời điểm nào?)
5. Viết Semantic Versioning plan cho 3 releases

### Bài tập 3: CM Strategy cho team 10 người (L3)

**Tình huống:** Bạn được giao nhiệm vụ thiết kế CM strategy cho phòng phát triển (10 người, 3 dự án song song, dự án Nhật Bản, CMMI Level 3).

**Yêu cầu:**
1. Thiết kế CM strategy document (tool, structure, branch, access)
2. Thiết kế Configuration Audit checklist
3. Thiết kế Change Control process (khi nào cần CCB?)
4. Thiết kế Backup & Disaster Recovery plan (RTO, RPO)
5. Thiết kế Release Management framework
6. Xác định roles & responsibilities trong CM

**Gợi ý:**
- Tham khảo PRC-SUP-CM-01 (5 bước CM process)
- Tham khảo GLN-TOOL-03 (Git workflow guide)
- Xem xét tailoring cho S/M/L
- Lưu ý tài liệu song ngữ (JP/VN) của dự án Nhật

---

## 5. Tài liệu tham khảo

### Từ kho CMMI PAL
- **PRC-SUP-CM-01** — Configuration Management Process (5 bước: Setup -> Define CI -> Version Control -> Baseline -> Change Control)
- **RUL-SUP-CM-01** — Version Control Rule (Folder structure, branch naming, commit conventions)
- **RUL-SUP-CM-02** — Baseline Rule (Audit, CCB, physical storage, naming)
- **GLN-TOOL-03** — Git Workflow Guide (Gitflow, GitHub Flow, tagging, backup)
- **GLN-TOOL-02** — GitLab Integration Guide (CI/CD, MR workflows)
- **GLN-SUP-CM-01** — CM Best Practices Guide (Change control, CCB facilitation)
- **TPL-SUP-CM-01~05** — Templates (Repo Setup, CI Registry, Baseline Record, CR, Change Log)
- **CHK-SUP-CM-01~02** — Checklists (CM Compliance, Baseline Audit)

### CMMI Mapping
| Thực hành CMMI | Nội dung | Reference |
|----------------|---------|-----------|
| CM SP 1.1 | Identify configuration items | Bước 2: Define CI |
| CM SP 1.2 | Establish CM system | Bước 1: Setup CM env |
| CM SP 1.3 | Create/release baselines | Bước 4: Baseline mgmt |
| CM SP 2.1 | Track change requests | Bước 5: Change control |
| CM SP 2.2 | Control configuration items | Bước 3+5: Version + Change |
| CM SP 3.1 | Establish CM records | Bước 2+4+5: CI Registry + Baseline + Change Log |
| CM SP 3.2 | Perform configuration audits | Bước 4: Baseline audits |

### Từ khung năng lực PM
- **Competency #4** — 品質管理 / 納品物管理: Deliverable đúng format, đúng version, kiểm soát thay đổi
- **SYP03 Phần 6** — Giám sát: CM metrics feed into project tracking

### Tham khảo ngoài
- Pro Git Book (git-scm.com/book), Gitflow (Driessen), Semantic Versioning (semver.org), CMMI-DEV v2.0
