# InsightForge - Technology Stack

## 1. Frontend

- **HTML5:** Semantic structure dividing the application into modular architectures (`index`, `dashboard`, `about`).
- **Vanilla CSS3:** Highly customized, dependency-free CSS driving complex layout grids, glassmorphism, responsive hamburger menus, and dynamic micro-animations without relying on heavy frameworks like Tailwind.
- **Vanilla JavaScript (ES6 Modules):** Manages DOM state, asynchronous JSON fetching, Intersection Observers for scroll animations, and dynamic UI mocking—all decoupled from frameworks like React to ensure raw performance and simplicity.
- **Hosting:** Firebase Hosting (Google Cloud)

## 2. Backend Engine

- **Language:** Python 3.10+
- **Framework:** FastAPI (for high-performance, asynchronous REST API generation).
- **Core Libraries:**
  - `pandas` & `numpy` for localized data preparation, gap calculation, and statistical aggregation.
  - `uvicorn` as the ASGI web server execution layer.
- **Hosting Target:** Railway (Live Production Environment)
- **Deployment URL:** `https://insightforge-production-57a5.up.railway.app`

## 3. DevOps & Version Control

- **Git & GitHub:** Version control with granular tracking mapping structural changes to specific version branches (e.g., V1.0 - V1.3).
- **Format:** Markdown (`.md`) specifically optimized for enterprise documentation styling standards.
