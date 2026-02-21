# InsightForge - Full System Explanation

## 1. High-Level Architecture

InsightForge operates under a dual-client system: a visually premium, static web application hosted on Firebase, and an active Python AI engine server currently tunneled via Localtunnel (bypassing the Railway deployment limitations).

## 2. The Python Backend (`src/research_agent.py` & `api/main.py`)

- **Data Ingestion:** The agent utilizes `pandas` to read normalized e-commerce data (pricing, catalog, performance, reviews).
- **Core Engine:** It correlates multiple independent datasets to generate a unified gap analysis. It isolates missing features, outsized negative review sentiments, and uncompetitive pricing margins.
- **API Wrapping:** `api/main.py` uses FastAPI to expose the backend over HTTP. The standard `/analyze` endpoint takes in the user's `brief` parameters from the frontend and synchronously streams back a structured intelligence report via JSON.

## 3. The Web Application (`webapp/index.html` & `app.js`)

- **Routing & State:** The web application natively switches between landing, the active dashboard (`dashboard.html`), and storytelling (`about.html`).
- **Dynamic Configuration:** `config.js` maintains the active state of the API base URL, dynamically executing Cross-Origin Resource Sharing (CORS) fetch requests.
- **Fail-safes:** The frontend integrates structured error handling. If `fetch()` drops due to server sleep (common with free-tier backend hosting), the UI seamlessly toggles into an elegant `mock-mode` to ensure demonstrations run uninterrupted.
