# Nadigs Enterprise - Customer Service Quality Auditor (ABSA)

An automated AI-driven quality assurance dashboard designed to audit customer support interactions at scale. By replacing manual supervisor audits, this system utilizes advanced Natural Language Processing (NLP) to detect agent tone risks, analyze multi-aspect customer sentiments, and prioritize critical interactions requiring human rescue.

---

## Key Pillars & Features

### 1. Customer Satisfaction (CSR) & Agent Specific Rating (ASR) Metrics
Rather than relying on generic indicators, the interface displays dedicated audit parameters directly tied to customer retention metrics:
- **Customer Satisfaction Rating (CSR)**: A metric calculated dynamically from 0% to 100% based on customer sentiment progression throughout the conversation.
- **Agent Specific Rating (ASR)**: A performance compliance index evaluating the support agent's empathy, adherence to guidelines, and tone quality.
- **Dynamic Rating Switcher**: Interactively toggle between the CSR and ASR detailed analysis views directly from the dashboard card controllers.

### 2. Aspect-Based Sentiment Analysis (ABSA)
Generic sentiment analysis fails to isolate root issues. Our ABSA engine segments conversations into key operational aspects:
- **Agent Politeness** (evaluates courtesy, warmth, and dismissiveness)
- **Technical Resolution** (tracks whether a functional solution is supplied)
- **Response Speed** (flags long hold-times or queuing complaints)
- **Process Ease** (evaluates structural friction points, like rigid return procedures or billing blockades)

Each aspect receives a precise sentiment classification (`Positive`, `Neutral`, or `Negative`) with a numeric intensity score ranging from `-1.0` to `+1.0`. The actual transcript line containing the evidence is extracted and highlighted dynamically.

### 3. Sentiment Analysis Meter (Using VADER Methodology)
At the core of the rating system is a secure server-side implementation of **VADER (Valence Aware Dictionary and sEntiment Reasoner)** metrics:
- Splits overall text sentiment into raw ratios: **Positive**, **Neutral**, and **Negative**.
- Produces a **Compound Sentiment Score** (ranging from `-1.0` to `+1.0`) representing the conversation's absolute emotional vector.

### 4. Dynamic Risk Priority Weighting
The system cross-references agent tone classification against customer loyalty metrics and compound sentiment to prevent churn:
- **Tone Classifier**: Evaluates whether the agent's tone leans toward being "high risk" (e.g., *Defensive*, *Impatient*, *Passive-Aggressive*, *Hostile*, or *Unempathetic*).
- **Loyalty Multipliers**: Adjusts priority based on customer status:
  - **VIP Customer** (Urgent premium response routing)
  - **Loyal Customer** (High weight multi-year accounts)
  - **Churn-Risk Account** (Critical retention flag)
  - **Regular / New Customers** (Standard base weight)
- **Priority Scores**: An analytical value calculated from `0` to `100` that dynamically groups interactions into `Critical`, `High`, `Medium`, or `Low` triage categories.

---

## Architecture & Tech Stack

This application is built with a **Full-Stack Client-Server architecture** conforming to enterprise-grade security standards.

### Backend (`/server.ts`)
- **Node.js + Express**: Provides the API endpoints (`/api/audits`, `/api/audit`, and `/api/audit/:id`).
- **VADER & Heuristic NLP Engine**: A lexical parsing fallback that executes aspect detection, tone evaluation, and sentiment analysis when API keys are unconfigured.

### Frontend (`/src/`)
- **React 18 + TypeScript**: Powers highly responsive UI rendering, state management, and strict type-safety boundaries (`/src/types.ts`).
- **Sophisticated Dark Theme**: A customized aesthetic utilizing deep space-slate canvases (`#0A0A0B`), high-contrast amber accents, and glowing indicators.
- **Lucide Icons & Fonts**: Elegant typography utilizing *Inter* for body readability, *Space Grotesk* for display headers, and *JetBrains Mono* for system logs.

---


The server starts up immediately on port `3000`, serving both the static React build and live Express endpoints.



---

- **JSON Schema Constraints**: Enforces types on sentiment ratios, aspect categories, tone markers, and recommended supervisor rescue playbooks.
- **Secured Fallbacks**: If the AI model faces rate-limiting or service hiccups, the heuristic analyzer intercepts the request silently to ensure uninterrupted dashboard audits.
