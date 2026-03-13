# Automation Setup Guide - AI Agent Project

**Version:** 1.0
**Last Updated:** 2026-03-13
**Purpose:** Step-by-step setup guide for Make.com/n8n automation workflows

---

## 📋 Overview

This skill provides comprehensive guidance for setting up automation workflows for AI Agent Social Automation project using Make.com or n8n.

## 🎯 When to Use This Skill

**Use this skill when:**
- ✅ Setting up automation for the first time
- ✅ Choosing between Make.com vs n8n
- ✅ Configuring integrations (Notion, Claude API, social platforms)
- ✅ Troubleshooting automation issues
- ✅ Creating new automation workflows

---

## 🔄 Tool Comparison: Make.com vs n8n

### Make.com (Recommended for Beginners)

**Pros:**
- ✅ Visual, intuitive interface
- ✅ Pre-built integrations (200+ apps)
- ✅ No coding required
- ✅ Excellent documentation
- ✅ Reliable execution
- ✅ Built-in error handling
- ✅ Cloud-hosted (no server needed)

**Cons:**
- ❌ Cost: $9-29/month (after free tier)
- ❌ Limited free tier (1,000 operations/month)
- ❌ Less flexibility for custom logic
- ❌ Vendor lock-in

**Best for:**
- Quick setup (ready in 1-2 hours)
- Non-technical users
- LinkedIn + Facebook automation
- When reliability > cost

**Pricing:**
- Free: 1,000 operations/month
- Core: $9/month (10,000 ops)
- Pro: $16/month (10,000 ops + advanced features)
- Teams: $29/month (10,000 ops + team features)

---

### n8n (Recommended for Advanced Users)

**Pros:**
- ✅ Open source & self-hosted
- ✅ Free (unlimited operations if self-hosted)
- ✅ Highly flexible (JavaScript support)
- ✅ Full control over data
- ✅ Large community
- ✅ Can integrate with any API

**Cons:**
- ❌ Requires server setup (VPS, Docker)
- ❌ Steeper learning curve
- ❌ More maintenance required
- ❌ Need technical knowledge for troubleshooting

**Best for:**
- Cost-sensitive projects (long-term)
- Technical users comfortable with Docker
- Complex custom workflows
- When full control > convenience

**Pricing:**
- Self-hosted: Free (need VPS ~$5-10/month)
- Cloud: $20/month starter

---

## 🚀 Quick Start: Make.com Setup

### Phase 1: Account Setup (15 minutes)

#### Step 1: Create Make.com Account

1. Go to https://www.make.com
2. Sign up with email
3. Verify email address
4. Choose "Core" plan (start with free tier)

#### Step 2: Familiarize with Interface

- **Scenarios**: Workflows/automations
- **Modules**: Individual steps in workflow
- **Routes**: Conditional paths
- **Data Store**: Store data between runs
- **Webhooks**: Trigger scenarios via HTTP

---

### Phase 2: Core Integrations (30-45 minutes)

#### Integration 1: Notion Setup

**Purpose:** Content queue & metrics storage

**Steps:**
1. In Make.com, add "Notion" module
2. Click "Create a connection"
3. Authorize Make.com to access Notion
4. Select workspace
5. Test connection

**Notion Database Setup:**
```
Content Queue Database:
- Title (Title)
- Platform (Select: LinkedIn, Facebook Tech, Facebook Chinese)
- Content Type (Select: Thought Leadership, Tutorial, News, etc.)
- Status (Select: Draft, Ready, Published, Scheduled)
- Publish Date (Date)
- Content (Text)
- Generated Content (Text)
- Image URL (URL)
- Performance (Number)
- Notes (Text)
```

**Test:**
- Create a test entry manually
- Use Make.com to read it
- Verify data appears correctly

---

#### Integration 2: Claude API Setup

**Purpose:** AI content generation

**Steps:**
1. Get API key from https://console.anthropic.com
2. In Make.com, add "HTTP" module
3. Configure request:
   - Method: POST
   - URL: https://api.anthropic.com/v1/messages
   - Headers:
     ```
     x-api-key: YOUR_CLAUDE_API_KEY
     anthropic-version: 2023-06-01
     content-type: application/json
     ```
   - Body:
     ```json
     {
       "model": "claude-3-5-sonnet-20241022",
       "max_tokens": 1024,
       "messages": [
         {
           "role": "user",
           "content": "Your prompt here"
         }
       ]
     }
     ```

**Test:**
- Send test request: "Write a LinkedIn post about AI automation"
- Verify response contains generated content
- Check token usage (should be < 1000 tokens)

**Cost Estimate:**
- Input: $3 per million tokens
- Output: $15 per million tokens
- Average post: ~500 tokens = $0.0075 per post
- 100 posts/month = ~$0.75

---

#### Integration 3: LinkedIn API (Optional - Manual Posting Recommended)

**Note:** LinkedIn API requires company page + approval process. For personal profiles, manual posting is recommended.

**For Company Pages:**
1. Create LinkedIn App at https://www.linkedin.com/developers
2. Get Client ID & Secret
3. Request access to "Share on LinkedIn" API
4. Generate access token (OAuth 2.0)
5. Configure Make.com LinkedIn module

**Alternative: Manual Posting**
- Claude generates content → Notion
- Review in Notion
- Copy & paste to LinkedIn (1-2 minutes)
- Track metrics manually

---

#### Integration 4: Meta Graph API (Facebook)

**Purpose:** Auto-post to Facebook Pages

**Steps:**
1. Create Facebook App at https://developers.facebook.com
2. Get Page Access Token:
   - Tools → Graph API Explorer
   - Select your page
   - Generate token with permissions:
     - `pages_show_list`
     - `pages_read_engagement`
     - `pages_manage_posts`
3. In Make.com, add "HTTP" module
4. Configure POST request:
   - URL: `https://graph.facebook.com/v18.0/{page-id}/feed`
   - Method: POST
   - Body:
     ```json
     {
       "message": "Your post content",
       "access_token": "YOUR_PAGE_ACCESS_TOKEN"
     }
     ```

**Test:**
- Post "Test from Make.com automation"
- Verify appears on Facebook Page
- Check response includes post ID

---

#### Integration 5: Telegram Notifications

**Purpose:** Get notified when workflows run/fail

**Steps:**
1. Create Telegram bot:
   - Message @BotFather on Telegram
   - Send `/newbot`
   - Follow instructions
   - Save bot token
2. Get your Chat ID:
   - Message your bot
   - Visit: `https://api.telegram.org/bot{TOKEN}/getUpdates`
   - Find your `chat_id`
3. In Make.com, add "HTTP" module
4. Configure:
   - URL: `https://api.telegram.org/bot{TOKEN}/sendMessage`
   - Method: POST
   - Body:
     ```json
     {
       "chat_id": "YOUR_CHAT_ID",
       "text": "Workflow notification message"
     }
     ```

**Test:**
- Send test message
- Verify received on Telegram
- Try with emojis & formatting (Markdown)

---

### Phase 3: First Workflow Creation (60 minutes)

#### Workflow 1: LinkedIn Content Generation

**Flow:**
```
Notion (Watch Records)
  → Filter (Status = "Ready")
  → Claude API (Generate Content)
  → Notion (Update Record with Generated Content)
  → Telegram (Notify Success)
```

**Step-by-step:**

1. **Module 1: Notion - Watch Records**
   - Select "Content Queue" database
   - Filter: Platform = LinkedIn, Status = Ready
   - Schedule: Every 1 hour
   - Limit: 1 record

2. **Module 2: Set Variables**
   - Extract: Title, Content Type, Notes
   - Prepare prompt template

3. **Module 3: HTTP Request (Claude API)**
   - Use prompt from `prompts/linkedin/` based on Content Type
   - Pass variables: {{title}}, {{notes}}
   - Parse response: `{{response.content[0].text}}`

4. **Module 4: Notion - Update Record**
   - Update record with ID from step 1
   - Set "Generated Content" = Claude response
   - Set "Status" = "Review"

5. **Module 5: Telegram - Send Message**
   - Message: "✅ Generated LinkedIn post: {{title}}"
   - Only if success

**Prompt Template Example:**
```
You are a LinkedIn content creator for IT professionals.

Topic: {{title}}
Type: {{contentType}}
Additional context: {{notes}}

Write a LinkedIn post that:
- Starts with a hook
- Provides value (insights, tips, or actionable advice)
- Uses 3-5 short paragraphs
- Includes 3-5 relevant hashtags
- Length: 150-200 words

Tone: Professional but conversational
```

**Test Workflow:**
- Create test Notion entry
- Run scenario manually
- Check Notion updated correctly
- Verify Telegram notification
- Review generated content quality

---

#### Workflow 2: Facebook Auto-Posting (Scheduled)

**Flow:**
```
Schedule (Daily 9 AM)
  → Notion (Get Record where Status = "Scheduled" & Publish Date = Today)
  → Meta Graph API (Post to Facebook)
  → Notion (Update Status = "Published")
  → Telegram (Notify)
```

**Configuration:**
- Schedule: 9:00 AM daily (Vietnam timezone)
- Limit: 1 post per run
- Platform filter: Facebook Tech OR Facebook Chinese

---

### Phase 4: Testing & Debugging (30 minutes)

#### Testing Checklist

- [ ] Test each module individually
- [ ] Test complete workflow end-to-end
- [ ] Test error scenarios (API failure, missing data)
- [ ] Test with real data (not just test entries)
- [ ] Verify Telegram notifications work
- [ ] Check Notion updates correctly
- [ ] Validate generated content quality
- [ ] Test scheduling (run at correct time)

#### Common Issues & Solutions

**Issue: Claude API returns error**
- Check API key is correct
- Verify headers match exactly
- Check request body JSON format
- Review token limits (4096 max)
- Check quota (rate limits)

**Issue: Notion doesn't update**
- Verify database ID is correct
- Check permissions (Make.com has access)
- Validate field names match exactly
- Check data types (text vs select vs date)

**Issue: Workflow doesn't trigger**
- Check schedule is active
- Verify trigger conditions
- Review Notion filter criteria
- Check "Watch Records" limit setting

**Issue: Facebook post fails**
- Verify Page Access Token is valid
- Check token hasn't expired
- Validate page permissions
- Review post content (no banned words)

---

## 🔧 Advanced Configuration

### Error Handling

**Add error handling to every workflow:**

1. **Error Handler Module** (after each critical step)
   - Catches errors
   - Logs to Notion "Error Log" database
   - Sends Telegram alert
   - Stops workflow gracefully

**Example:**
```
HTTP Request (Claude API)
  → [Success] Continue workflow
  → [Error] → Telegram Alert → Notion Log → Stop
```

### Rate Limiting

**Claude API:**
- Limit: 50 requests/minute
- Add "Sleep" module if making multiple requests

**Meta Graph API:**
- Limit: 200 calls/hour per user
- Add delay between posts

### Data Validation

**Before posting to social media:**
- Check content length (LinkedIn: 3,000 chars, Facebook: 63,206 chars)
- Validate hashtags (LinkedIn: max 30, Facebook: max 30)
- Ensure images exist (if URL provided)
- Check for banned words/phrases

---

## 📊 Monitoring & Optimization

### Key Metrics to Track

**In Notion Dashboard:**
- Total posts generated (weekly/monthly)
- Success rate (% posted successfully)
- Average generation time
- API costs (Claude, Facebook)
- Engagement per post

**In Make.com:**
- Operations used (vs limit)
- Error rate
- Execution time per scenario
- Data transfer

### Cost Optimization

**Reduce Make.com operations:**
- Use webhooks instead of polling
- Increase interval between checks
- Batch operations where possible
- Use filters to reduce unnecessary runs

**Reduce Claude API costs:**
- Use shorter prompts
- Reuse prompts (template-based)
- Optimize max_tokens setting
- Cache common responses (if applicable)

---

## 🚀 n8n Setup (Alternative)

### Quick Start (Self-Hosted)

**Prerequisites:**
- VPS/server with Docker installed
- Domain name (optional, for webhooks)

**Installation:**
```bash
# Pull n8n Docker image
docker pull n8nio/n8n

# Run n8n
docker run -it --rm \
  --name n8n \
  -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n \
  n8nio/n8n

# Access at http://localhost:5678
```

**Setup Integrations:**
- Same process as Make.com
- Use n8n credentials system
- Create workflows (called "workflows" not "scenarios")

**Advantages over Make.com:**
- Unlimited operations
- Full JavaScript support
- Can run locally (test without internet)
- Better for complex logic

**Disadvantages:**
- Need to manage server uptime
- Need to handle backups
- More complex setup

---

## 📚 Resources

### Documentation
- Make.com: https://www.make.com/en/help
- n8n: https://docs.n8n.io
- Claude API: https://docs.anthropic.com
- Notion API: https://developers.notion.com
- Meta Graph API: https://developers.facebook.com/docs/graph-api

### Community
- Make.com Community: https://community.make.com
- n8n Community: https://community.n8n.io
- Claude Discord: https://discord.gg/anthropic

### Skills Integration
- Use with: **prompt-engineering.md** for prompt templates
- Use with: **notion-database.md** for database schemas
- Use with: **content-templates.md** for content structure

---

## ✅ Setup Completion Checklist

After completing this guide:

- [ ] Make.com/n8n account created
- [ ] Notion workspace setup with databases
- [ ] Claude API key configured & tested
- [ ] Social platform APIs connected (Facebook)
- [ ] Telegram bot created for notifications
- [ ] First workflow created & tested
- [ ] Error handling configured
- [ ] Monitoring dashboard in Notion
- [ ] Documentation updated with API keys (in password manager)
- [ ] Backup workflows exported to `workflows/` folder

---

**Last Updated:** 2026-03-13
**Version:** 1.0.0
**Author:** VictorAurelius + Claude Sonnet 4.5
