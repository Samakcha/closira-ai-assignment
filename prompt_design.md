# Prompt Design – Closira AI Support Workflow

## Overview

This document explains the prompt engineering and design decisions behind the AI-powered customer support workflow built for the Closira AI Engineering Internship assignment.

The goal of the assistant is to provide reliable customer support for **Bloom Aesthetics Clinic** while staying grounded in SOP data, qualifying leads, escalating safely when needed, and generating useful summaries.

---

# 1. System Prompt

## System Prompt Used

You are an AI customer support assistant for Bloom Aesthetics Clinic.

Rules:

1. Answer ONLY using the provided SOP information.
2. Never make up facts not present in the SOP.
3. If the answer is unavailable in SOP:
   - clearly state that the information is unavailable
   - recommend escalation to a human support agent
4. Maintain a warm, professional, concise tone.
5. Escalate immediately if:
   - customer is angry
   - customer asks a medical question
   - customer requests a human
   - customer asks something outside SOP
   - customer negotiates pricing

Always prioritize accuracy and safety over completeness.

---

# 2. Prompt Design Decisions

The prompt was designed with a strong emphasis on:

- reliability
- hallucination prevention
- safe escalation
- clear customer communication

The assistant is instructed to behave like a customer-facing support representative for a small business.

Primary design principle:

> Respond accurately from SOP data first.  
> If uncertain, escalate instead of guessing.

This was intentionally chosen to prioritise trust and safety over over-answering.

---

# 3. Hallucination Prevention Strategy

Preventing hallucination was a core requirement of the assignment.

The following methods were used:

### SOP-grounded responses
Each FAQ response receives the SOP JSON as context.

The model is explicitly instructed to answer only from this SOP.

---

### Explicit refusal behaviour
If information is missing from SOP, the assistant is instructed to respond:

> "I do not have information about that in the SOP. I recommend escalating this to a human support agent."

This avoids fabricated answers.

---

### No external assumptions
The assistant does not use outside knowledge or make assumptions beyond the provided SOP.

---

# 4. Confidence-Based Escalation

Escalation is handled through rule-based detection plus SOP fallback handling.

Escalation triggers include:

- complaint
- angry sentiment
- medical question
- explicit human support request
- pricing negotiation
- more than 2 unanswered questions

Examples:

### Complaint
"Your service is terrible"

### Medical
"Is Botox safe during pregnancy?"

### Human Request
"I want to speak to a manager"

### Repeated Unknown Questions
Multiple customer questions not covered by SOP

---

## Escalation Logging

When escalation occurs, the system stores:

- escalation status
- escalation reason

This information is also included in the final conversation summary.

---

# 5. Tone and Persona

The assistant tone was designed to feel:

- warm
- helpful
- professional
- concise

The tone reflects how an SMB customer support assistant would communicate with customers over WhatsApp or web chat.

Examples:

- polite and direct
- short answers
- no unnecessary verbosity
- empathetic when escalation is required

Example:

> “I do not have information about that in the SOP. I recommend escalating this to a human support agent.”

Tone priorities:

- clarity
- professionalism
- customer trust

---

# 6. Design Trade-offs

### Why rule-based escalation?
A rule-based escalation layer was chosen because it is:

- explainable
- deterministic
- easy to debug
- reliable for assignment testing

---

### Why JSON SOP instead of database?
JSON was chosen for simplicity and clarity.

It keeps the workflow lightweight and easy to understand.

---

### Why CLI instead of frontend?
The assignment explicitly states that a CLI/script is sufficient.

This allowed focus on:

- prompt design
- workflow logic
- safety
- escalation handling

instead of UI development.

---

# Summary

This workflow was designed around four priorities:

- grounded FAQ answering
- hallucination prevention
- safe escalation
- useful customer conversation summarisation

The final system aims to behave like a reliable AI customer support assistant for SMB customer communication.