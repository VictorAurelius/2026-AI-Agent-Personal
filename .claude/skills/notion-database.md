# Notion Database Setup - AI Agent Project

**Version:** 1.0
**Last Updated:** 2026-03-13
**Purpose:** Notion database schemas and setup for AI Agent automation

---

## 📋 Overview

This skill provides complete Notion database schemas for managing content queue, tracking metrics, and organizing AI Agent workflows.

## 🗄️ Database 1: Content Queue

**Purpose:** Central hub for all social media content (draft → review → published)

### Schema

| Property | Type | Options/Format | Purpose |
|----------|------|----------------|---------|
| **Title** | Title | - | Post title/topic |
| **Platform** | Select | LinkedIn, Facebook Tech, Facebook Chinese | Target platform |
| **Content Type** | Select | See options below | Template type |
| **Status** | Select | Draft, Ready, Generating, Review, Scheduled, Published | Workflow stage |
| **Publish Date** | Date | DateTime | When to post |
| **Priority** | Select | High, Medium, Low | Queue priority |
| **Generated Content** | Text | Long text | AI-generated post |
| **Final Content** | Text | Long text | Edited/approved post |
| **Image URL** | URL | - | Featured image |
| **Notes** | Text | - | Additional context for AI |
| **Hashtags** | Multi-select | Auto-populated | Hashtags used |
| **Engagement** | Number | - | Total engagement |
| **Reach** | Number | - | Post reach |
| **Clicks** | Number | - | Link clicks |
| **Performance Score** | Formula | Engagement/Reach*100 | % engagement rate |
| **Created** | Created time | - | When created |
| **Last Edited** | Last edited time | - | Last update |
| **Author** | Person | - | Who created |

### Content Type Options

**LinkedIn:**
- Thought Leadership
- Tutorial/How-To
- Product Showcase
- Career Advice

**Facebook Tech:**
- Tech News
- Tutorial
- Tool Review
- Code Snippet
- Comparison
- Meme/Humor
- Resource List

**Facebook Chinese:**
- Daily Vocabulary
- Grammar Point
- Listening Practice
- Cultural Insight
- Pronunciation Tips
- HSK Exam Tips
- Flashcard Set
- Conversation Practice

### Status Workflow

```
Draft → Ready → Generating → Review → Scheduled → Published
  ↑                                                      ↓
  └──────────────────← (Archive/Reuse) ←────────────────┘
```

### Views

**1. Content Pipeline (Kanban)**
- Group by: Status
- Sort: Priority (High → Low), then Publish Date
- Filter: None (show all)

**2. This Week (Calendar)**
- Layout: Calendar by Publish Date
- Filter: Status = Scheduled OR Published
- Properties: Title, Platform, Status

**3. Ready to Generate (Table)**
- Filter: Status = Ready
- Sort: Priority (High → Low)
- Properties: Title, Platform, Content Type, Notes

**4. Needs Review (Table)**
- Filter: Status = Review
- Sort: Created (newest first)
- Properties: Title, Generated Content, Platform

**5. Performance Dashboard (Table)**
- Filter: Status = Published
- Sort: Performance Score (high → low)
- Properties: Title, Platform, Engagement, Reach, Performance Score

---

## 📊 Database 2: Metrics Dashboard

**Purpose:** Track overall performance and analytics

### Schema

| Property | Type | Format | Purpose |
|----------|------|--------|---------|
| **Week** | Title | "W1 2026", "W2 2026" | Week identifier |
| **Date Range** | Date | Start-End | Week period |
| **Platform** | Select | LinkedIn, Facebook Tech, Facebook Chinese | Platform |
| **Posts Published** | Number | - | Total posts |
| **Total Engagement** | Number | - | Likes + Comments + Shares |
| **Total Reach** | Number | - | Total people reached |
| **Avg Engagement Rate** | Number | % | Avg engagement/reach |
| **Followers Gained** | Number | - | New followers |
| **Best Performing Post** | Relation | → Content Queue | Link to top post |
| **Top Hashtag** | Text | - | Most engaging hashtag |
| **Content Mix** | Text | - | Breakdown by content type |
| **Notes** | Text | - | Observations/insights |

### Views

**1. Weekly Overview (Table)**
- Group by: Platform
- Sort: Week (newest first)
- Show: Last 12 weeks

**2. Growth Trend (Board)**
- Group by: Platform
- Sort: Date Range
- Visualize follower growth

**3. Content Performance (Table)**
- Sort: Avg Engagement Rate (high → low)
- Filter: Last 4 weeks
- Compare platforms

---

## 📁 Database 3: Workflow Logs

**Purpose:** Track automation runs and errors

### Schema

| Property | Type | Format | Purpose |
|----------|------|--------|---------|
| **Timestamp** | Title | DateTime | When workflow ran |
| **Workflow** | Select | LinkedIn Gen, FB Post, etc. | Which workflow |
| **Status** | Select | Success, Failed, Partial | Run status |
| **Records Processed** | Number | - | Items handled |
| **Errors** | Text | - | Error messages |
| **Duration** | Number | Seconds | How long it took |
| **Cost** | Number | $ | API costs |
| **Notes** | Text | - | Additional context |

### Views

**1. Recent Runs (Table)**
- Sort: Timestamp (newest first)
- Filter: Last 7 days
- Show: Workflow, Status, Errors

**2. Error Log (Table)**
- Filter: Status = Failed
- Sort: Timestamp (newest first)
- Show: Workflow, Errors, Notes

**3. Cost Tracking (Table)**
- Group by: Workflow
- Sum: Cost
- Period: Last 30 days

---

## 📁 Database 4: Prompt Library

**Purpose:** Store and version AI prompts

### Schema

| Property | Type | Format | Purpose |
|----------|------|--------|---------|
| **Prompt Name** | Title | - | Identifier |
| **Platform** | Select | LinkedIn, FB Tech, FB Chinese | Target |
| **Content Type** | Select | See Content Queue types | Template |
| **Prompt Text** | Text | Long text | Full prompt |
| **Version** | Number | 1.0, 1.1, etc. | Version number |
| **Status** | Select | Active, Testing, Deprecated | Current state |
| **Performance** | Number | 1-5 | Quality rating |
| **Last Used** | Date | - | Last usage |
| **Created** | Created time | - | When created |

### Views

**1. Active Prompts (Table)**
- Filter: Status = Active
- Group by: Platform
- Sort: Performance (high → low)

**2. Testing Lab (Table)**
- Filter: Status = Testing
- Show: Prompt Name, Performance, Last Used

---

## 🔧 Setup Instructions

### Step 1: Create Databases

1. In Notion, create new database (Table)
2. Name it "Content Queue"
3. Add all properties from schema above
4. Set property types correctly
5. Configure Select options

### Step 2: Create Relations

**Link Content Queue → Metrics Dashboard:**
- In Metrics Dashboard, add Relation property
- Link to "Content Queue" database
- Name: "Best Performing Post"
- Allow linking to one page

### Step 3: Create Views

**For Content Queue:**
1. Click "+ Add a view"
2. Choose view type (Table/Board/Calendar)
3. Name the view
4. Configure filters
5. Set sort order
6. Choose visible properties

### Step 4: Set Permissions

**Make.com Integration:**
1. Share database with Make.com
2. Grant "Edit" permissions
3. Copy database ID from URL
4. Configure in Make.com

### Step 5: Add Test Data

Create 5-10 sample entries to test:
- Different platforms
- Different content types
- Different statuses
- Test automation triggers

---

## 🔗 API Integration Patterns

### Read from Notion (Make.com)

```
Notion → Search Objects
  Database: Content Queue
  Filter: Status = "Ready"
  Limit: 1
  Sort: Priority desc, Created asc
```

### Update Notion

```
Notion → Update a Database Item
  Database: Content Queue
  Page ID: {{from previous step}}
  Properties:
    - Status: "Review"
    - Generated Content: {{claude_response}}
```

### Create New Entry

```
Notion → Create a Database Item
  Database: Workflow Logs
  Properties:
    - Timestamp: {{now}}
    - Workflow: "LinkedIn Generation"
    - Status: "Success"
    - Records Processed: {{count}}
```

---

## 📊 Database Maintenance

### Weekly Tasks
- [ ] Archive published posts older than 3 months
- [ ] Review "Review" status items (shouldn't stay > 3 days)
- [ ] Update Metrics Dashboard for past week
- [ ] Check for failed workflow logs

### Monthly Tasks
- [ ] Analyze performance trends
- [ ] Update top-performing hashtags list
- [ ] Review and deprecate low-performing prompts
- [ ] Backup all databases (export as CSV)

---

## 💡 Pro Tips

**Formula Examples:**

**Performance Score:**
```
prop("Engagement") / prop("Reach") * 100
```

**Days Since Published:**
```
dateBetween(now(), prop("Publish Date"), "days")
```

**Is Overdue:**
```
and(
  prop("Status") == "Scheduled",
  prop("Publish Date") < now()
)
```

**Automation Ideas:**
- Auto-move to "Ready" when all required fields filled
- Auto-archive posts published > 90 days ago
- Auto-calculate performance score daily
- Auto-notify if engagement rate < 1%

---

**Last Updated:** 2026-03-13
**Version:** 1.0.0
**Author:** VictorAurelius + Claude Sonnet 4.5
