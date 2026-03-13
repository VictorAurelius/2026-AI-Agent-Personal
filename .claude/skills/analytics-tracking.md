# Analytics & Tracking - AI Agent Project

**Version:** 1.0
**Last Updated:** 2026-03-13
**Purpose:** Metrics framework and optimization strategies for social media performance

---

## 📋 Overview

This skill provides a comprehensive analytics framework for tracking, measuring, and optimizing AI-generated social media content across all platforms.

## 📊 Key Metrics by Platform

### LinkedIn Metrics

**Engagement Metrics:**
- **Impressions**: Total views of your post
- **Reactions**: Likes, celebrates, loves, etc.
- **Comments**: Discussion quality indicator
- **Shares**: Amplification metric
- **Click-through rate (CTR)**: Link clicks / impressions
- **Engagement rate**: (Reactions + Comments + Shares) / Impressions * 100

**Growth Metrics:**
- **Follower growth**: New followers per week/month
- **Profile views**: Visibility indicator
- **Post reach**: Unique accounts reached
- **Connection requests**: Network expansion

**Benchmarks (LinkedIn):**
- Engagement rate: **2-5%** = Good, **>5%** = Excellent
- CTR: **>1%** = Good
- Comment rate: **>0.5%** = Strong engagement

---

### Facebook Page Metrics

**Engagement Metrics:**
- **Reach**: People who saw your post
- **Reactions**: Likes, loves, etc.
- **Comments**: Discussion depth
- **Shares**: Virality indicator
- **Saves**: Value indicator
- **Engagement rate**: (Reactions + Comments + Shares + Saves) / Reach * 100

**Growth Metrics:**
- **Page likes**: Total followers
- **Page views**: Profile visits
- **Post reach**: Organic vs paid
- **Video views**: For video content

**Benchmarks (Facebook):**
- Engagement rate: **1-3%** = Good, **>3%** = Excellent
- Share rate: **>0.5%** = Viral potential
- Save rate: **>1%** = High value content

---

## 📈 Weekly Review Process

### Monday Morning Review (30 minutes)

**Step 1: Data Collection**
```
1. Export last week's data from:
   - LinkedIn Analytics (CSV)
   - Facebook Insights (CSV)
   - Notion Content Queue (filter: Published last week)

2. Input into Metrics Dashboard:
   - Total posts published
   - Platform breakdown
   - Engagement totals
   - Reach totals
```

**Step 2: Calculate KPIs**
```
For each platform:
- Average engagement rate
- Top performing post (by engagement rate)
- Worst performing post
- Best content type
- Best posting time
- Top hashtags
```

**Step 3: Identify Trends**
```
Compare to previous week:
- Engagement rate: Up/Down/Flat?
- Follower growth: Accelerating/Decelerating?
- Best content type shifted?
- New patterns in posting times?
```

**Step 4: Action Items**
```
Based on data:
- Double down on: [Best performing content type]
- Reduce: [Underperforming content type]
- Test: [New hypothesis based on trends]
- Optimize: [Posting time/hashtags/format]
```

### Weekly Review Template

```markdown
# Week [X] - Social Media Review

## Summary
- Total posts: [X]
- Avg engagement rate: [X]%
- Follower growth: +[X]
- Best platform: [Platform]

## Platform Breakdown

### LinkedIn
- Posts: [X]
- Engagement rate: [X]%
- Best post: [Title] ([X]% engagement)
- Insight: [Key observation]

### Facebook Tech
- Posts: [X]
- Engagement rate: [X]%
- Best post: [Title] ([X]% engagement)
- Insight: [Key observation]

### Facebook Chinese
- Posts: [X]
- Engagement rate: [X]%
- Best post: [Title] ([X]% engagement)
- Insight: [Key observation]

## Actions for Next Week
1. [Action 1]
2. [Action 2]
3. [Action 3]
```

---

## 📅 Monthly Analysis Framework

### End of Month Deep Dive (2 hours)

**1. Performance Analysis**
```
For each platform:
- Total posts published
- Average engagement rate (trend over 4 weeks)
- Total reach (trend)
- Follower growth (net new)
- Best performing content types (%)
- Posting time optimization
```

**2. Content Mix Analysis**
```
LinkedIn:
- Thought leadership: [X]% of posts, [X]% of engagement
- Tutorials: [X]% of posts, [X]% of engagement
- Product showcase: [X]% of posts, [X]% of engagement
- Career advice: [X]% of posts, [X]% of engagement

Optimal mix: [Recommendation based on performance]
```

**3. ROI Calculation**
```
Costs:
- Make.com: $[X]
- Claude API: $[X]
- Canva Pro: $[X]
- Total: $[X]

Time saved:
- Manual content creation: [X] hours
- Scheduling: [X] hours
- Total: [X] hours
- Value (@$[Y]/hour): $[Z]

ROI: $[Time saved value] / $[Costs] = [X]%
```

**4. Goal Progress**
```
LinkedIn:
- Goal: 1,000 followers in 3 months
- Current: [X] followers
- Progress: [X]%
- On track? Yes/No
- Projected: [X] followers at current rate

Facebook Tech:
- Goal: 5,000 followers in 6 months
- Current: [X] followers
- Progress: [X]%
- On track? Yes/No

Facebook Chinese:
- Goal: 5,000 followers in 6 months
- Current: [X] followers
- Progress: [X]%
- On track? Yes/No
```

---

## 🧪 A/B Testing Guidelines

### What to Test

**Content Variables:**
- Hook styles (question vs statement vs stat)
- Post length (short <150 words vs long >200 words)
- Formatting (paragraphs vs bullets)
- Hashtag count (3 vs 5 vs 7)
- Call-to-action type (question vs request vs none)
- Emoji usage (none vs moderate vs heavy)

**Timing Variables:**
- Day of week (weekday vs weekend)
- Time of day (morning vs afternoon vs evening)
- Posting frequency (3x vs 5x vs 7x per week)

### A/B Test Framework

**Week 1-2: Test A**
```
Variable: Post length
Option A: 150-200 words (10 posts)
Track: Engagement rate, reach, CTR
```

**Week 3-4: Test B**
```
Variable: Post length
Option B: 200-250 words (10 posts)
Track: Same metrics
```

**Analysis:**
```
Compare:
- Which had higher engagement rate?
- Which had better reach?
- Which took less editing time?

Winner: [Option A/B]
Action: Use winner going forward
```

### Testing Log Template

| Test # | Variable | Option A | Option B | Winner | Insight |
|--------|----------|----------|----------|--------|---------|
| 1 | Post length | 150-200w | 200-250w | A | Shorter performs better |
| 2 | Hook type | Question | Statement | B | Statements get more clicks |
| 3 | Posting time | 8AM | 12PM | B | Lunchtime engagement higher |

---

## 📊 Dashboard Setup

### Notion Dashboard

**KPI Cards:**
```
┌─────────────────┬─────────────────┬─────────────────┐
│ Total Followers │ This Week Posts │ Avg Engagement  │
│     12,450      │       15        │      3.2%       │
│  +234 (↑2.1%)   │   ↑ vs 12 LW    │  ↑ vs 2.8% LW   │
└─────────────────┴─────────────────┴─────────────────┘

┌─────────────────┬─────────────────┬─────────────────┐
│ LinkedIn        │ Facebook Tech   │ Facebook Chinese│
│   4,200 (↑3%)   │  5,600 (↑2.5%)  │  2,650 (↑1.8%)  │
└─────────────────┴─────────────────┴─────────────────┘
```

**Content Performance Chart:**
```
Engagement Rate by Content Type (Last 30 days)

Thought Leadership  ████████ 3.8%
Tutorial            ███████ 3.2%
Tool Review         ██████ 2.9%
Tech News           █████ 2.4%
Product Showcase    ████ 1.9%
```

**Growth Trend (Line Chart):**
```
Followers over time (Last 12 weeks)
[Insert visualization in Notion]
```

---

## 🎯 Optimization Strategies

### Strategy 1: Content Type Optimization

```
IF Thought Leadership engagement > Tutorial engagement
THEN Increase Thought Leadership posts from 30% to 40%
     Decrease Tutorial posts from 30% to 20%
     Monitor for 2 weeks
```

### Strategy 2: Posting Time Optimization

```
Test Matrix:
Monday: 8AM, 12PM, 6PM (rotate)
Wednesday: 8AM, 12PM, 6PM (rotate)
Friday: 8AM, 12PM, 6PM (rotate)

After 3 weeks:
Identify best time slot per day
Apply to schedule
```

### Strategy 3: Hashtag Optimization

```
Track hashtag performance:
- #AI: 3,200 avg reach, 2.8% engagement
- #TechTrends: 2,100 avg reach, 3.5% engagement
- #CodingLife: 1,800 avg reach, 4.2% engagement

Action: Prioritize #CodingLife (highest engagement)
```

### Strategy 4: Format Testing

```
Test same topic, different formats:

Format A: Text-only
Format B: Text + image
Format C: Text + carousel
Format D: Video

Winner: Track over 4 weeks
```

---

## 📱 Tools & Integrations

### Analytics Tools

**Native Platform Analytics:**
- LinkedIn Analytics (free)
- Facebook Insights (free)
- Export weekly to Notion

**Third-party Tools (Optional):**
- Buffer (scheduling + analytics): $6/month
- Metricool (multi-platform): $18/month
- Hootsuite (enterprise): $99/month

**Recommendation:** Start with native analytics, upgrade only if needed.

### Tracking Links

**Use Bitly or UTM parameters:**
```
https://yoursite.com/product?utm_source=linkedin&utm_medium=social&utm_campaign=week12
```

Track in Google Analytics:
- Which platform drives most traffic
- Which content type converts best
- ROI per platform

---

## 🚨 Red Flags & Alerts

### Set up alerts for:

**Engagement Drop:**
```
IF engagement rate < 1.5% for 3 consecutive posts
THEN Review content quality
     Check if audience preferences changed
     Test different content types
```

**Follower Decline:**
```
IF followers decrease 2 weeks in a row
THEN Review recent posts (controversial content?)
     Check if automation is posting correctly
     Survey followers for feedback
```

**Low Reach:**
```
IF reach drops >30% week-over-week
THEN Check platform algorithm changes
     Review posting times
     Increase hashtag variety
```

---

## 📋 Monthly Checklist

- [ ] Export analytics from all platforms
- [ ] Update Notion Metrics Dashboard
- [ ] Calculate engagement rates
- [ ] Identify top 3 performing posts
- [ ] Identify worst 3 performing posts
- [ ] Update content mix percentages
- [ ] Review and adjust posting schedule
- [ ] Test 1 new content format
- [ ] Update hashtag strategy
- [ ] Calculate ROI
- [ ] Set goals for next month
- [ ] Archive old posts in Notion

---

## 🔗 Integration with Other Skills

**Use with:**
- **content-templates.md**: Test template variations
- **automation-setup.md**: Track automation effectiveness
- **notion-database.md**: Store and visualize metrics
- **prompt-engineering.md**: Optimize prompts based on performance

---

**Last Updated:** 2026-03-13
**Version:** 1.0.0
**Author:** VictorAurelius + Claude Sonnet 4.5
