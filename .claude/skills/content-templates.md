# Content Templates Library - AI Agent Project

**Version:** 1.0
**Last Updated:** 2026-03-13
**Purpose:** Reusable content templates for LinkedIn, Facebook Tech, and Facebook Chinese pages

---

## 📋 Overview

This skill provides comprehensive content templates for all social media platforms in the AI Agent project. Use these templates with Claude API to generate consistent, high-quality content.

## 🎯 When to Use This Skill

**Use this skill when:**
- ✅ Creating new social media posts
- ✅ Setting up AI prompts for content generation
- ✅ Planning content calendar
- ✅ Training AI for specific content types
- ✅ Maintaining brand voice consistency

---

## 🔷 LinkedIn Templates (4 Pillars)

### Pillar 1: Thought Leadership

**Purpose:** Establish expertise, share insights, build authority

**Structure:**
```
[Hook/Question]

[Personal story or observation - 2-3 sentences]

[Key insight #1]
[Key insight #2]
[Key insight #3]

[Call to action / Question for engagement]

[3-5 hashtags]
```

**Example:**
```
The biggest mistake I see developers make? Optimizing code before validating the idea.

Last month, I spent 3 weeks perfecting a feature that users never wanted. The code was beautiful, test coverage was 95%, performance was amazing... and nobody used it.

Here's what I learned:

→ Ship fast, iterate faster
→ User feedback > perfect code
→ Solve real problems, not imaginary ones

What's your approach to feature development?

#SoftwareDevelopment #ProductThinking #DeveloperLife
```

**Variables for AI:**
- `{{topic}}`: Main subject
- `{{personalExperience}}`: Brief story
- `{{keyInsights}}`: 3-5 bullet points
- `{{questionForEngagement}}`: Open-ended question

**Best Posting Times:** Tuesday-Thursday, 7-9 AM or 12-1 PM

---

### Pillar 2: Tutorial/How-To

**Purpose:** Provide value, teach skills, establish credibility

**Structure:**
```
[Problem statement]

Here's how to [solve it]:

1. [Step 1] - [Brief explanation]
2. [Step 2] - [Brief explanation]
3. [Step 3] - [Brief explanation]

[Optional: Code snippet or screenshot]

[Benefit/Result]

Saved? Share with someone who needs this.

[3-5 hashtags]
```

**Example:**
```
Struggling with Docker multi-stage builds?

Here's how to reduce your image size by 80%:

1. Use alpine base images - 5MB vs 200MB
2. Multi-stage builds - separate build & runtime
3. .dockerignore - exclude unnecessary files

Before: 850MB
After: 170MB

Your deployments will thank you.

#Docker #DevOps #CloudNative
```

**Variables for AI:**
- `{{problem}}`: Pain point
- `{{steps}}`: 3-5 numbered steps
- `{{result}}`: Measurable outcome
- `{{benefit}}`: Why it matters

**Best Posting Times:** Monday-Wednesday, 8-10 AM

---

### Pillar 3: Product Showcase

**Purpose:** Promote your software products, demonstrate value

**Structure:**
```
[Pain point users have]

I built [product name] to solve this.

What it does:
→ [Feature 1]
→ [Feature 2]
→ [Feature 3]

[Social proof / early results]

[Call to action with link]

[3-5 hashtags]
```

**Example:**
```
Managing team tasks across 5 different tools is chaos.

I built TaskMaster to centralize everything.

What it does:
→ Sync tasks from Jira, Asana, Trello
→ AI-powered priority sorting
→ One dashboard for the entire team

Early users saved 10+ hours/week on coordination.

Try it free: [link]

#ProductivityTools #ProjectManagement #SaaS
```

**Variables for AI:**
- `{{painPoint}}`: User problem
- `{{productName}}`: Product name
- `{{features}}`: 3-5 key features
- `{{socialProof}}`: Testimonial or metrics
- `{{cta}}`: Call to action

**Best Posting Times:** Tuesday-Thursday, 12-2 PM

---

### Pillar 4: Career/Professional Development

**Purpose:** Connect with professionals, share career insights

**Structure:**
```
[Career observation or lesson]

My journey:
[2-3 sentences about your experience]

Key lessons:
• [Lesson 1]
• [Lesson 2]
• [Lesson 3]

[Question or advice for readers]

[3-5 hashtags]
```

**Example:**
```
Your GitHub profile is more important than your resume.

5 years ago, I had a perfect resume but no GitHub activity. Got 2 interviews.

Last year, I had 50+ repos (even small ones). Got 15+ interview requests.

Key lessons:
• Build in public
• Consistency > perfection
• Open source contributions matter

What's helped your career most?

#CareerAdvice #SoftwareEngineering #GitHubTips
```

**Variables for AI:**
- `{{careerLesson}}`: Main insight
- `{{personalJourney}}`: Brief story
- `{{keyLessons}}`: 3-5 takeaways
- `{{engagement}}`: Question or advice

**Best Posting Times:** Friday-Sunday, 6-8 PM

---

## 📘 Facebook Tech Page Templates (7 Types)

### Type 1: Tech News Summary

**Purpose:** Share breaking tech news, drive engagement

**Structure:**
```
🚨 [Headline]

[2-3 sentence summary]

Tại sao quan trọng:
• [Impact 1]
• [Impact 2]

[Your take / opinion]

Nguồn: [link]

[2-4 hashtags]
```

**Example:**
```
🚨 OpenAI ra mắt GPT-5 với khả năng reasoning mạnh gấp 10 lần

GPT-5 có thể giải quyết các bài toán phức tạp, lập kế hoạch dài hạn, và tự phản biện kết quả. Giá vẫn giữ nguyên như GPT-4.

Tại sao quan trọng:
• Thay đổi cách chúng ta code (AI pair programming)
• Automation nhiều task phức tạp hơn
• Cạnh tranh giữa các AI model tăng cao

My take: Đây là bước nhảy vọt. Devs cần học cách làm việc với AI.

Nguồn: [link]

#GPT5 #AI #TechNews
```

**Variables for AI:**
- `{{headline}}`: News headline
- `{{summary}}`: 2-3 sentences
- `{{impacts}}`: Why it matters
- `{{opinion}}`: Personal take

**Best Posting Times:** Daily, 7-9 AM or 7-9 PM

---

### Type 2: Tutorial/Guide

**Purpose:** Teach technical skills, provide value

**Structure:**
```
📚 [Title]

[Brief intro về vấn đề]

Các bước:
1️⃣ [Step 1]
2️⃣ [Step 2]
3️⃣ [Step 3]
4️⃣ [Step 4]

💡 Pro tip: [Bonus advice]

Save lại để dùng sau nhé!

[2-4 hashtags]
```

**Example:**
```
📚 Cách setup Docker cho dự án Node.js trong 5 phút

Không cần phức tạp, đây là cách đơn giản nhất:

Các bước:
1️⃣ Tạo Dockerfile với base image node:18-alpine
2️⃣ Copy package.json và run npm install
3️⃣ Copy source code
4️⃣ Expose port và CMD ["node", "app.js"]

💡 Pro tip: Dùng .dockerignore để giảm image size

Save lại để dùng sau nhé!

#Docker #NodeJS #DevOps #Tutorial
```

**Variables for AI:**
- `{{title}}`: Tutorial title
- `{{problem}}`: What it solves
- `{{steps}}`: 4-6 steps
- `{{proTip}}`: Bonus advice

**Best Posting Times:** Weekend mornings, 8-10 AM

---

### Type 3: Tool Review

**Purpose:** Introduce useful tools, provide recommendations

**Structure:**
```
🛠️ [Tool Name] - [One-line description]

Features:
✅ [Feature 1]
✅ [Feature 2]
✅ [Feature 3]

Pricing: [Free/Paid/$X]

Đánh giá:
👍 [Pros]
👎 [Cons]

Dùng khi nào: [Use cases]

Link: [URL]

[2-4 hashtags]
```

**Example:**
```
🛠️ Cursor - AI Code Editor cho developers

Features:
✅ AI pair programming (giống GitHub Copilot++)
✅ Chat với codebase (hỏi về bất kỳ file nào)
✅ Multi-file editing với AI
✅ Hỗ trợ nhiều ngôn ngữ

Pricing: $20/tháng (free trial 14 ngày)

Đánh giá:
👍 Productivity tăng 30-40%
👍 AI context hiểu code rất tốt
👎 Hơi đắt so với Copilot ($10/tháng)

Dùng khi nào: Khi bạn code nhiều, cần AI mạnh hơn Copilot

Link: cursor.sh

#CodingTools #AI #Productivity
```

**Variables for AI:**
- `{{toolName}}`: Tool name
- `{{features}}`: 3-4 key features
- `{{pricing}}`: Cost
- `{{pros}}`: Advantages
- `{{cons}}`: Disadvantages
- `{{useCases}}`: When to use

**Best Posting Times:** Wednesday-Friday, 6-8 PM

---

### Type 4: Code Snippet

**Purpose:** Share useful code, tips & tricks

**Structure:**
```
💻 [Problem you're solving]

[Brief explanation]

Code:
```
[Code block]
```

Giải thích:
• [Line 1 explanation]
• [Line 2 explanation]

Bonus: [Additional tip]

[2-4 hashtags]
```

**Example:**
```
💻 Cách handle async errors trong Express.js gọn gàng

Thay vì try-catch ở mọi route, dùng wrapper này:

Code:
```javascript
const asyncHandler = (fn) => (req, res, next) => {
  Promise.resolve(fn(req, res, next)).catch(next);
};

// Usage
app.get('/users', asyncHandler(async (req, res) => {
  const users = await User.find();
  res.json(users);
}));
```

Giải thích:
• Wrap async function và auto catch errors
• Pass error to next() để error middleware xử lý
• Clean code, không cần try-catch mỗi nơi

Bonus: Kết hợp với error middleware để handle tất cả errors

#JavaScript #NodeJS #ExpressJS #WebDev
```

**Variables for AI:**
- `{{problem}}`: What problem it solves
- `{{explanation}}`: Brief context
- `{{code}}`: Code snippet
- `{{lineExplanations}}`: How it works

**Best Posting Times:** Weekday evenings, 7-9 PM

---

### Type 5: Comparison Post

**Purpose:** Help choose between tools/frameworks

**Structure:**
```
⚖️ [Tool A] vs [Tool B]

Use [Tool A] when:
• [Scenario 1]
• [Scenario 2]

Use [Tool B] when:
• [Scenario 1]
• [Scenario 2]

TL;DR:
[Tool A]: [Summary]
[Tool B]: [Summary]

Bạn đang dùng cái nào?

[2-4 hashtags]
```

**Example:**
```
⚖️ Next.js vs Remix

Use Next.js when:
• Bạn cần ISR (Incremental Static Regeneration)
• App lớn với nhiều pages
• Cần Vercel hosting (deploy dễ nhất)

Use Remix when:
• Bạn cần performance tốt hơn (nested routes)
• SEO quan trọng (streaming SSR)
• Muốn deploy ở bất kỳ đâu (Cloudflare, AWS, etc.)

TL;DR:
Next.js: Dễ dùng, ecosystem lớn, Vercel tối ưu
Remix: Performance cao, flexibility, modern approach

Bạn đang dùng cái nào?

#NextJS #Remix #React #WebDev
```

**Variables for AI:**
- `{{toolA}}`, `{{toolB}}`: Tools being compared
- `{{scenariosA}}`, `{{scenariosB}}`: Use cases
- `{{summaryA}}`, `{{summaryB}}`: TL;DR

**Best Posting Times:** Tuesday-Thursday, 12-2 PM

---

### Type 6: Meme/Humor

**Purpose:** Engagement, relatability, virality

**Structure:**
```
[Relatable tech situation]

[Funny observation or meme description]

Tag những người bạn làm dev 😂

[2-4 hashtags]
```

**Example:**
```
Khi sếp hỏi: "Mất bao lâu để fix cái bug này?"

Dev: "5 phút"

[2 giờ sau]

Dev vẫn đang Google "why is my code not working"

Tag những người bạn làm dev 😂

#DeveloperLife #Memes #Programming
```

**Note:** Pair with image/meme for better engagement

**Best Posting Times:** Weekend, 8-11 PM

---

### Type 7: Resource List

**Purpose:** Provide curated resources, save value

**Structure:**
```
📚 [Number] [Resources] để [Goal]

1. [Resource 1] - [Brief description]
2. [Resource 2] - [Brief description]
3. [Resource 3] - [Brief description]
4. [Resource 4] - [Brief description]
5. [Resource 5] - [Brief description]

Save lại và học dần nhé!

Bạn đã biết cái nào rồi?

[2-4 hashtags]
```

**Example:**
```
📚 5 khoá học FREE để học AI/ML cho developers

1. Fast.ai - Practical Deep Learning (best for beginners)
2. Andrew Ng's ML Course - Math foundation
3. Hugging Face Course - NLP & Transformers
4. Google's ML Crash Course - Quick start
5. DeepLearning.AI - Advanced topics

Save lại và học dần nhé!

Bạn đã biết cái nào rồi?

#MachineLearning #AI #FreeCourses
```

**Variables for AI:**
- `{{number}}`: Number of resources
- `{{goal}}`: What they help achieve
- `{{resources}}`: List with descriptions

**Best Posting Times:** Sunday evening, 6-9 PM

---

## 🇨🇳 Facebook Chinese Page Templates (8 Types)

### Type 1: Daily Vocabulary

**Purpose:** Teach HSK vocabulary, build learning habit

**Structure:**
```
📖 Từ vựng hôm nay

[Chinese characters] - [Pinyin] - [Vietnamese meaning]

Ví dụ:
• [Example sentence 1]
• [Example sentence 2]

💡 Ghi nhớ: [Memory tip]

HSK Level: [1-6]

[2-3 hashtags]
```

**Example:**
```
📖 Từ vựng hôm nay

努力 - nǔlì - Nỗ lực, cố gắng

Ví dụ:
• 我要努力学习中文 (Wǒ yào nǔlì xuéxí zhōngwén) - Tôi sẽ cố gắng học tiếng Trung
• 他很努力工作 (Tā hěn nǔlì gōngzuò) - Anh ấy làm việc rất chăm chỉ

💡 Ghi nhớ: 力 (lì) = sức mạnh. Nỗ lực = dùng hết sức mạnh

HSK Level: 3

#HọcTiếngTrung #HSK3 #TừVựng
```

**Variables for AI:**
- `{{chineseWord}}`: Chinese characters
- `{{pinyin}}`: Pronunciation
- `{{meaning}}`: Vietnamese translation
- `{{examples}}`: 2-3 example sentences
- `{{memoryTip}}`: How to remember
- `{{hskLevel}}`: HSK level

**Best Posting Times:** Daily, 7-8 AM

---

### Type 2: Grammar Point

**Purpose:** Explain Chinese grammar rules

**Structure:**
```
📝 Ngữ pháp: [Grammar pattern]

Công thức:
[Pattern structure]

Ý nghĩa: [Meaning]

Ví dụ:
✅ [Correct example 1]
✅ [Correct example 2]
❌ [Common mistake]

HSK Level: [1-6]

[2-3 hashtags]
```

**Example:**
```
📝 Ngữ pháp: 一边...一边... (vừa...vừa...)

Công thức:
一边 + Động từ 1 + 一边 + Động từ 2

Ý nghĩa: Làm 2 việc cùng lúc

Ví dụ:
✅ 我一边吃饭一边看电视 - Tôi vừa ăn cơm vừa xem TV
✅ 他一边走路一边听音乐 - Anh ấy vừa đi bộ vừa nghe nhạc
❌ 我一边很饿一边吃饭 (SAI - không dùng với tính từ)

HSK Level: 3

#NgữPhápTiếngTrung #HSK3 #HọcTiếngTrung
```

**Variables for AI:**
- `{{grammarPattern}}`: Pattern name
- `{{formula}}`: Structure
- `{{meaning}}`: What it means
- `{{correctExamples}}`: 2-3 correct uses
- `{{commonMistake}}`: Common error

**Best Posting Times:** Tuesday, Thursday, 6-7 PM

---

### Type 3: Listening Practice

**Purpose:** Improve listening skills with audio

**Structure:**
```
🎧 Luyện nghe - [Topic]

Nghe câu sau và điền từ còn thiếu:

[Sentence với ___ cho missing words]

Đáp án: (comment bên dưới trước khi xem)
.
.
.
[Full sentence with answer]

Dịch: [Vietnamese translation]

HSK Level: [1-6]

[2-3 hashtags]
```

**Example:**
```
🎧 Luyện nghe - Đặt hàng đồ ăn

Nghe câu sau và điền từ còn thiếu:

我想 ___ 一 ___ 咖啡和一 ___ 三明治

Đáp án: (comment bên dưới trước khi xem)
.
.
.
我想要(yào)一杯(bēi)咖啡和一个(gè)三明治

Dịch: Tôi muốn một cốc cà phê và một cái sandwich

HSK Level: 2

#LuyệnNghe #HSK2 #HọcTiếngTrung
```

**Note:** Pair with audio file or voice note

**Best Posting Times:** Wednesday, Saturday, 7-8 PM

---

### Type 4: Cultural Insight

**Purpose:** Teach Chinese culture alongside language

**Structure:**
```
🏮 Văn hóa Trung Quốc

[Topic name]

[2-3 paragraphs about the cultural aspect]

Từ vựng liên quan:
• [Word 1] - [Meaning]
• [Word 2] - [Meaning]
• [Word 3] - [Meaning]

Bạn đã biết điều này chưa?

[2-3 hashtags]
```

**Example:**
```
🏮 Văn hóa Trung Quốc

Tại sao người Trung Quốc hay hỏi "你吃了吗?" (Bạn ăn cơm chưa?)

Đây không phải câu hỏi thật sự muốn biết bạn ăn chưa. Đây là cách chào hỏi phổ biến, giống như "How are you?" trong tiếng Anh.

Nguồn gốc: Ngày xưa, ăn no là điều quan trọng nhất. Hỏi "ăn chưa" = quan tâm đến cuộc sống của người khác.

Từ vựng liên quan:
• 吃饭 (chīfàn) - Ăn cơm
• 问候 (wènhòu) - Chào hỏi
• 传统 (chuántǒng) - Truyền thống

Bạn đã biết điều này chưa?

#VănHóaTrungQuốc #HọcTiếngTrung #TiếngTrungThúVị
```

**Variables for AI:**
- `{{culturalTopic}}`: Cultural aspect
- `{{explanation}}`: Description
- `{{relatedWords}}`: Vocabulary

**Best Posting Times:** Weekend, 9-11 AM

---

### Type 5: Pronunciation Tips

**Purpose:** Help with tricky Chinese sounds

**Structure:**
```
🗣️ Phát âm: [Sound/Tone]

Sự khác biệt:
[Sound 1] vs [Sound 2]

Tips:
• [Tip 1]
• [Tip 2]

Luyện tập:
[Practice words/sentences]

HSK Level: [All levels]

[2-3 hashtags]
```

**Example:**
```
🗣️ Phát âm: zh, ch, sh vs z, c, s

Sự khác biệt:
zh, ch, sh - Lưỡi cuộn lên (retroflex)
z, c, s - Lưỡi thẳng (dental)

Tips:
• zh, ch, sh: Lưỡi chạm vào vòm miệng (giống "j" trong "jeans")
• z, c, s: Lưỡi chạm răng (giống "ts" trong "cats")

Luyện tập:
• 知道 (zhīdào) vs 自豪 (zìháo)
• 吃饭 (chīfàn) vs 词汇 (cíhuì)

HSK Level: Tất cả

#PhátÂm #HọcTiếngTrung #TipsHọcTiếngTrung
```

**Variables for AI:**
- `{{sound}}`: Sound/tone being taught
- `{{differences}}`: What makes it different
- `{{tips}}`: How to pronounce
- `{{practice}}`: Practice words

**Best Posting Times:** Monday, Friday, 6-7 PM

---

### Type 6: HSK Exam Tips

**Purpose:** Help students prepare for HSK exams

**Structure:**
```
✍️ Tips thi HSK [Level]

[Specific section]: [Reading/Listening/Writing]

Chiến thuật:
1. [Strategy 1]
2. [Strategy 2]
3. [Strategy 3]

Lưu ý:
⚠️ [Common mistake to avoid]

Thời gian ôn: [Recommended study time]

[2-3 hashtags]
```

**Example:**
```
✍️ Tips thi HSK 3

Phần Đọc hiểu (Reading)

Chiến thuật:
1. Đọc câu hỏi trước, rồi mới đọc đoạn văn
2. Gạch chân keywords trong câu hỏi
3. Tìm keywords trong đoạn văn (thường ở gần đáp án)

Lưu ý:
⚠️ Không dịch từng từ! Hiểu ý chính là đủ
⚠️ Đừng dành quá 2 phút cho 1 câu

Thời gian ôn: 2-3 tháng với 1 giờ/ngày

#HSK3 #ThiHSK #HọcTiếngTrung
```

**Variables for AI:**
- `{{hskLevel}}`: HSK level
- `{{section}}`: Exam section
- `{{strategies}}`: Test-taking strategies
- `{{mistakes}}`: What to avoid
- `{{studyTime}}`: Recommended prep time

**Best Posting Times:** 2 months before HSK exam dates

---

### Type 7: Flashcard Set

**Purpose:** Grouped vocabulary by theme

**Structure:**
```
🃏 Flashcards: [Theme]

[Word 1] - [Pinyin] - [Meaning]
[Word 2] - [Pinyin] - [Meaning]
[Word 3] - [Pinyin] - [Meaning]
[Word 4] - [Pinyin] - [Meaning]
[Word 5] - [Pinyin] - [Meaning]

Câu ví dụ:
[Example sentence using multiple words]

Save lại để học nhé!

HSK Level: [1-6]

[2-3 hashtags]
```

**Example:**
```
🃏 Flashcards: Thức ăn & Đồ uống

咖啡 - kāfēi - Cà phê
茶 - chá - Trà
米饭 - mǐfàn - Cơm
面条 - miàntiáo - Mì
水果 - shuǐguǒ - Hoa quả

Câu ví dụ:
我想吃米饭和水果，喝一杯咖啡
(Tôi muốn ăn cơm và hoa quả, uống một cốc cà phê)

Save lại để học nhé!

HSK Level: 1-2

#TừVựng #HSK #HọcTiếngTrung
```

**Variables for AI:**
- `{{theme}}`: Topic/category
- `{{words}}`: 5-7 related words
- `{{exampleSentence}}`: Using multiple words
- `{{hskLevel}}`: Level

**Best Posting Times:** Weekend, 7-9 AM

---

### Type 8: Conversation Practice

**Purpose:** Practical dialogue for real situations

**Structure:**
```
💬 Hội thoại: [Situation]

A: [Line 1 in Chinese]
   [Pinyin]
   [Vietnamese translation]

B: [Line 2 in Chinese]
   [Pinyin]
   [Vietnamese translation]

[Continue for 4-6 exchanges]

Từ vựng mới:
• [New word 1]
• [New word 2]

HSK Level: [1-6]

[2-3 hashtags]
```

**Example:**
```
💬 Hội thoại: Mua đồ ở cửa hàng

A: 你好，我想买这个
   Nǐ hǎo, wǒ xiǎng mǎi zhège
   Xin chào, tôi muốn mua cái này

B: 好的，一共50块钱
   Hǎo de, yīgòng 50 kuài qián
   Được, tổng cộng 50 tệ

A: 可以用信用卡吗？
   Kěyǐ yòng xìnyòngkǎ ma?
   Có thể dùng thẻ tín dụng không?

B: 可以，这边请
   Kěyǐ, zhèbiān qǐng
   Được, mời bên này

Từ vựng mới:
• 一共 (yīgòng) - Tổng cộng
• 信用卡 (xìnyòngkǎ) - Thẻ tín dụng

HSK Level: 2

#HộiThoại #HSK2 #HọcTiếngTrung
```

**Variables for AI:**
- `{{situation}}`: Context
- `{{dialogue}}`: 4-6 exchanges
- `{{newWords}}`: New vocabulary

**Best Posting Times:** Thursday, Sunday, 6-8 PM

---

## 🎨 Template Usage Guide

### With AI (Claude API)

**In Make.com/n8n workflow:**

1. Fetch content idea from Notion
2. Select template based on `Content Type` field
3. Pass template + variables to Claude API
4. Claude generates content following template
5. Save to Notion for review

**Example prompt:**
```
Use this template to create a LinkedIn Thought Leadership post:

Template: [paste template structure]

Variables:
- topic: "AI automation in content creation"
- personalExperience: "I automated my LinkedIn posting and saved 10 hours/week"
- keyInsights: ["AI handles 80% of work", "Human review is essential", "Consistency beats perfection"]
- questionForEngagement: "How are you using AI in your workflow?"

Generate the post following the template exactly.
```

---

### Manual Use

1. Choose appropriate template for platform & content type
2. Fill in variables
3. Adjust tone/length as needed
4. Add personal touch
5. Proofread before posting

---

## 📊 Template Performance Tracking

**Track in Notion:**
- Template type used
- Engagement rate
- Best performing templates
- Template variants testing

**Optimize based on:**
- Time of day posted
- Template structure
- Content length
- Call-to-action effectiveness

---

## 🔗 Integration with Other Skills

**Use with:**
- **automation-setup.md**: Integrate templates into workflows
- **prompt-engineering.md**: Create AI prompts using templates
- **notion-database.md**: Store template performance data
- **analytics-tracking.md**: Measure template effectiveness

---

**Last Updated:** 2026-03-13
**Version:** 1.0.0
**Author:** VictorAurelius + Claude Sonnet 4.5
