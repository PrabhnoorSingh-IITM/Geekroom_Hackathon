# InsightForge - Product Requirements Document (PRD)

## 1. Project Overview

InsightForge is an autonomous, AI-driven e-commerce intelligence platform. It ingests raw market datasets (catalogs, reviews, competitor pricing, and performance metrics) and synthesizes them into actionable, decision-ready reports.

## 2. Target Audience

- E-Commerce Managers
- Strategy & Pricing Teams
- Online Brand Owners

## 3. Core Features

- **Multi-Source Data Ingestion:** Supports automated CSV loading for catalogs, customer reviews, competitor pricing, and sales performance.
- **Dynamic Analysis Modes:**
  - **Quick Mode:** Fast, metric-focused insights for immediate tactics (e.g., matching competitor prices).
  - **Deep Mode:** Strategic, comprehensive analysis featuring executive summaries, gap analysis, and calculated risks.
- **Business Goal Alignment:** Configurable objectives such as Growth, Profitability, Retention, and Market Expansion.
- **LLM Reasoning Engine:** Employs advanced prompt engineering inside `research_agent.py` to identify correlations (e.g., associating negative reviews with high return rates).
- **Graceful Fallbacks:** The UI gracefully shifts to offline/mock models when the live API is unreachable, ensuring uninterrupted demonstration capabilities.

## 4. Non-Functional Requirements

- **Performance:** Quick mode reports should generate within 30 seconds; Deep mode reports within 2 minutes.
- **UI/UX:** Must feature a premium, dark-mode glassmorphic aesthetic to convey enterprise value.
- **Responsiveness:** Ensure seamless functionality across Desktop, Tablet, and Mobile (<450px) viewports.
