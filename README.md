# Closira AI Support Workflow Assignment

## Overview

This project is a Python-based AI customer support workflow built for the Closira AI Engineering Internship assignment.

It simulates an AI-powered customer support assistant for **Bloom Aesthetics Clinic** that can:

- answer customer FAQs using SOP data only
- avoid hallucinating information outside SOP
- qualify leads through structured questions
- detect escalation scenarios
- generate structured conversation summaries
- save conversation transcripts automatically

---

## Features

### 1. FAQ Answering
Answers customer questions strictly using provided SOP data.

Examples:
- Botox pricing
- Fillers pricing
- Booking process
- Cancellation policy

---

### 2. Hallucination Prevention
If a customer asks something outside the SOP:

Example:
> Do you offer laser treatment?

The AI does not guess.

Instead it responds:

> I do not have information about that in the SOP. I recommend escalating this to a human support agent.

---

### 3. Lead Qualification
After successful FAQ handling, the AI asks:

- What type of business do you run?
- How large is your team?
- What tools are you currently using?

Responses are collected and stored for summary generation.

---

### 4. Escalation Detection
The AI escalates when detecting:

- complaints
- angry sentiment
- medical questions
- pricing negotiation
- explicit request for human support
- more than 2 unanswered questions

---

### 5. Conversation Summary
At the end of the session, the AI generates a structured summary including:

- Customer Intent
- Key Details Collected
- Escalation Status
- SOP Gaps Identified
- Recommended Next Action

---

### 6. Transcript Saving
Every conversation session is automatically saved inside:

```bash
test_transcripts/
session_transcript_1.md
session_transcript_2.md
```

## Project Structure
```bash
closira-ai-assignment/
│
├── app/
├── data/
├── test_transcripts/
├── README.md
├── prompt_design.md
└── requirements.txt
```

## Setup Instructions

### 1.  Clone Repository
```bash
git clone <repo-url>
cd closira-ai-assignment
```

### 2. Create Virtual Environment
```bash
python3 -m venv venv
for windows:
source venv/Scripts/activate

for macos/linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Add OpenAI API key
Create a `.env` file in the root directory with your OpenAI key:

```env
OPENAI_API_KEY=your-api-key-here
```

### 5. Run the Application
```bash
python app/main.py
```

## Example Conversation

```text
AI Support Agent Started
-------------------------

Customer: Hi, I would like to know about your botox prices.

AI: Botox starts from £200.

Customer: What is your cancellation policy?

AI: 24hr cancellation required.

Customer: That's too expensive.

AI: I do not have information about that in the SOP. I recommend escalating this to a human support agent.
```

## Testing

To test the escalation conditions:

- Say "exit" to generate a conversation summary
- Add questions outside the SOP to trigger hallucination prevention
- Use angry words (hate, terrible, etc.) to test sentiment analysis

## File Descriptions

- `data/sop.json` – Business SOP data
- `app/main.py` – Main application entry point
- `app/faq_agent.py` – FAQ answering with SOP-only constraint
- `app/escalation_agent.py` – Escalation detection logic
- `app/qualification_agent.py` – Lead data collection
- `app/summary_agent.py` – Conversation summarization
- `app/utils.py` – Transcript saving and helper functions
