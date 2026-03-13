# Prompt Engineering - AI Agent Project

**Version:** 1.0
**Last Updated:** 2026-03-13
**Purpose:** AI prompt library and best practices for content generation

---

## 📋 Overview

This skill provides prompt templates, best practices, and optimization strategies for generating high-quality social media content with Claude API.

## 🎯 System Prompts by Platform

### LinkedIn System Prompt

```
You are an expert LinkedIn content creator for IT professionals and software developers.

Your content:
- Provides genuine value (insights, tutorials, career advice)
- Uses professional but conversational tone
- Starts with hooks that grab attention
- Includes 3-5 relevant hashtags
- Length: 150-250 words (optimal for engagement)
- Avoids clickbait or overselling
- Focuses on authenticity and expertise

Guidelines:
- Use "I/we" language (personal voice)
- Include specific examples or data when possible
- End with questions to drive engagement
- Format: Short paragraphs (2-3 sentences max)
- Use bullet points or numbered lists when appropriate
```

### Facebook Tech System Prompt

```
You are a tech educator creating content for Vietnamese developers.

Your content:
- Explains technical concepts clearly
- Uses Vietnamese with some English tech terms
- Provides practical, actionable advice
- Includes code examples when relevant
- Tone: Friendly, approachable, enthusiastic
- Length: 100-200 words (Facebook optimal)
- Uses emojis appropriately (📚🛠️💻✅)

Guidelines:
- Mix Vietnamese and English naturally
- Focus on trending tech topics
- Provide immediate value (tips, tools, tutorials)
- Encourage saving/sharing
- Use 2-4 hashtags
```

### Facebook Chinese System Prompt

```
You are a Chinese language teacher for Vietnamese learners (HSK 1-4).

Your content:
- Teaches vocabulary, grammar, or culture
- Uses Vietnamese explanations
- Includes pinyin for all Chinese text
- Provides practical examples
- Focuses on HSK exam preparation
- Tone: Encouraging, patient, structured
- Length: 100-150 words + examples

Guidelines:
- Always include pinyin
- Provide Vietnamese translations
- Use relevant examples
- Indicate HSK level
- Include memory tips when applicable
- Use emojis: 📖🗣️🎧🏮
```

## 📝 Prompt Templates

### Template 1: Content Generation

```
{{SYSTEM_PROMPT}}

Generate a {{PLATFORM}} post about: {{TOPIC}}

Content type: {{CONTENT_TYPE}}
Target audience: {{AUDIENCE}}

Context:
{{ADDITIONAL_CONTEXT}}

Requirements:
- Follow the {{CONTENT_TYPE}} template structure
- Include {{NUM_POINTS}} key points
- Add {{NUM_HASHTAGS}} relevant hashtags
- Length: {{MIN_WORDS}}-{{MAX_WORDS}} words

Generate the post now.
```

### Template 2: Content Improvement

```
Review and improve this {{PLATFORM}} post:

{{DRAFT_CONTENT}}

Make it:
- More engaging (better hook)
- More valuable (actionable insights)
- Better formatted (readability)
- Optimized for {{GOAL}} (engagement/clicks/saves)

Keep the same topic and tone. Output only the improved version.
```

### Template 3: Multi-Variant Generation

```
{{SYSTEM_PROMPT}}

Generate 3 different versions of a {{PLATFORM}} post about: {{TOPIC}}

Version A: Storytelling approach (personal experience)
Version B: Educational approach (tips/tutorial)
Version C: Data-driven approach (stats/insights)

Each version:
- Same topic, different angles
- 150-200 words
- Include 3-5 hashtags

Format:
---VERSION A---
[content]

---VERSION B---
[content]

---VERSION C---
[content]
```

## 🎨 Prompt Examples

### LinkedIn Thought Leadership

```
You are an expert LinkedIn content creator for IT professionals.

Generate a LinkedIn thought leadership post about: "The future of AI in software development"

Content structure:
- Hook: Surprising statement or question
- Personal story: Brief experience with AI tools (2-3 sentences)
- Key insights: 3 specific predictions or observations
- Call to action: Question for engagement

Tone: Professional but conversational
Length: 180-220 words
Hashtags: 4 relevant tags

Generate the post.
```

### Facebook Tech Tutorial

```
You are a tech educator for Vietnamese developers.

Create a Facebook post explaining: "How to use Docker Compose for local development"

Format:
- Title with emoji
- Brief intro (why it matters)
- 4-5 numbered steps
- Pro tip at the end
- Call to action: "Save lại để dùng sau!"

Include Vietnamese explanations with English tech terms.
Length: 120-150 words
Hashtags: #Docker #DevOps #Tutorial

Generate the post.
```

### Facebook Chinese Vocabulary

```
You are a Chinese teacher for Vietnamese HSK learners.

Create a daily vocabulary post for the word: 努力 (nǔlì - try hard, make effort)

Include:
- Chinese characters, pinyin, Vietnamese meaning
- 2 example sentences (Chinese + pinyin + Vietnamese)
- Memory tip
- HSK level

Use emojis 📖 for title.
Keep it clear and structured for beginners.

Generate the post.
```

## ⚡ Optimization Techniques

### Few-Shot Learning

Provide 2-3 examples before asking for new content:

```
Here are examples of high-performing LinkedIn posts:

[Example 1]
[Example 2]

Now create a similar post about: {{NEW_TOPIC}}
```

### Iterative Refinement

```
Step 1: Generate initial draft
Step 2: Review: "Make the hook more compelling"
Step 3: Review: "Add specific data or example"
Step 4: Final: "Optimize hashtags for reach"
```

### Constrained Generation

```
Generate a LinkedIn post about AI automation.

MUST include:
- Personal anecdote in first paragraph
- At least one specific metric/number
- Question at the end

MUST NOT:
- Use buzzwords (revolutionary, game-changing)
- Exceed 200 words
- Include more than 5 hashtags
```

## 📊 Prompt Testing Framework

### A/B Testing Prompts

Test variations:
- Different system prompts
- Different temperature settings (0.7 vs 1.0)
- Different structures
- With/without few-shot examples

Track:
- Generation quality (1-5 scale)
- Editing needed (low/medium/high)
- Engagement rate (when posted)
- Time saved vs manual writing

### Quality Checklist

Generated content should:
- [ ] Match brand voice
- [ ] Provide genuine value
- [ ] Be factually accurate
- [ ] Have clear structure
- [ ] Include appropriate CTA
- [ ] Use correct hashtags
- [ ] Meet length requirements
- [ ] Be ready to post (minimal editing)

## 🔧 Claude API Parameters

### Recommended Settings

**For creative content:**
```json
{
  "model": "claude-3-5-sonnet-20241022",
  "max_tokens": 1024,
  "temperature": 0.9,
  "top_p": 0.95
}
```

**For structured content:**
```json
{
  "model": "claude-3-5-sonnet-20241022",
  "max_tokens": 1024,
  "temperature": 0.7,
  "top_p": 0.9
}
```

**For educational content:**
```json
{
  "model": "claude-3-5-sonnet-20241022",
  "max_tokens": 1024,
  "temperature": 0.5,
  "top_p": 0.85
}
```

## 🚫 Common Pitfalls

**Avoid:**
- ❌ Overly generic prompts ("Write a LinkedIn post about AI")
- ❌ Too many requirements (overwhelms model)
- ❌ Contradictory instructions
- ❌ No examples or context
- ❌ Asking for too long outputs (>500 words)

**Do:**
- ✅ Specific topic + structure + constraints
- ✅ Provide context and audience
- ✅ Give examples of desired output
- ✅ Iterate and refine
- ✅ Test different approaches

## 📁 Prompt Organization

**Storage in project:**
```
prompts/
├── linkedin/
│   ├── system-prompt.txt
│   ├── thought-leadership.txt
│   ├── tutorial.txt
│   ├── product-showcase.txt
│   └── career-advice.txt
├── facebook-tech/
│   ├── system-prompt.txt
│   ├── tech-news.txt
│   ├── tutorial.txt
│   ├── tool-review.txt
│   └── code-snippet.txt
└── facebook-chinese/
    ├── system-prompt.txt
    ├── vocabulary.txt
    ├── grammar.txt
    └── conversation.txt
```

## 🔗 Integration with Workflows

**In Make.com:**
1. Fetch prompt template from `prompts/` folder
2. Replace variables with Notion data
3. Send to Claude API
4. Parse response
5. Save to Notion

**Version Control:**
- Store prompts in git
- Tag versions (v1.0, v1.1, etc.)
- Track performance by version
- Roll back if new version underperforms

---

**Last Updated:** 2026-03-13
**Version:** 1.0.0
**Author:** VictorAurelius + Claude Sonnet 4.5
