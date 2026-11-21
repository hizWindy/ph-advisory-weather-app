# Week 1 Demo Notes: Setup & Foundations

- **Date:** Friday, November 14, 2026 (Submitted before 3:00 PM)
- **Author:** Angela (QA and Docs)
- **Reviewer:** Khair (Project Manager & Tech Lead)
- **Team:** Joan (UI/UX), Miguel (Frontend), MJ (Data), Fredelina (Backend), JC (AI), Angela (QA/Docs)

---

## Week 1 Milestone Goal

> **Week 1: Set up** — Everyone makes a first pull request. Both apps start. We agree how the parts talk to each other. First sketches.

All team members have opened their first pull requests, both applications (React frontend and FastAPI backend) run cleanly on local laptops from a fresh clone, and foundational data, AI, design, and testing contracts are established.

---

## 1. What Works

### 1.1 Both Applications Run Locally
- **Frontend App (React + Vite):**
  - Initialized with React 19, TypeScript, and Vite hot-module reloading.
  - Successfully installs via `npm install` and starts via `npm run dev` at `http://localhost:5173/`.
  - Production build verified with `npm run build` (`tsc && vite build`) with zero errors.
  - Setup and execution instructions documented in [`frontend/README.md`](../../frontend/README.md).
- **Backend Service (FastAPI):**
  - Initialized with FastAPI, Pydantic schemas, and Uvicorn server.
  - Successfully creates a virtual environment, installs dependencies from `requirements.txt`, and runs via `uvicorn app.main:app --reload` at `http://127.0.0.1:8000`.
  - Core endpoints active and working:
    - `GET /` — Root index and endpoint map.
    - `GET /health` — Health status (`healthy`), ISO 8601 UTC timestamp, and uptime in seconds.
    - `GET /cities` — Returns catalog of Philippine cities loaded from `backend/data/cities.json`.
    - `GET /cities/{city_id}` — Returns specific city coordinates and metadata (e.g., `manila`, `cebu-city`, `davao-city`).
    - Interactive OpenAPI Swagger docs live at `http://127.0.0.1:8000/docs`.
  - Automated test suite verified with `pytest -v` (`backend/tests/test_main.py`): 100% passing tests.
  - Setup and execution instructions documented in [`backend/README.md`](../../backend/README.md).
- **Single Source of Truth Setup Guide:**
  - Added "Run it on your laptop" section to root [`README.md`](../../README.md) linking both apps and verified from a fresh clone following only the README.

### 1.2 Data Engineering & External APIs
- **Open-Meteo Integration Samples:**
  - Curated 7-day hourly and daily weather sample datasets for three major Philippine metropolitan hubs: Manila, Cebu, and Davao (`backend/data/samples/`).
  - Standardized timestamps and timezones to `Asia/Manila`.
- **Philippine Cities Catalog:**
  - Standardized JSON list of Philippine cities with coordinates, elevation, province, region, and postal codes (`backend/data/cities.json`).
  - Created validation and forecast fetching test script (`backend/scripts/check-city-forecasts.cjs`).
- **Database Architecture Plan:**
  - Documented PostgreSQL relational schema plan (`docs/data.md` and database plan PR) for cities, forecast cache, and user advisory logs.

### 1.3 System Contracts & Business Rules
- **API Contract ([`docs/api.md`](../api.md)):**
  - Full schema agreement between frontend (Miguel) and backend (Fredelina).
  - Defined request and response payloads for `/health`, `/cities`, `/forecast`, and `/payo`.
- **Rain & Heat Check Rules ([`docs/rules.md`](../rules.md)):**
  - Rain rule: hourly precipitation probability $\ge 60\%$ flags a "Rainy Hour".
  - Heat check rule: 3-tier user-facing levels based on feels-like temperature ($^\circ\text{C}$):
    - **OK**: $< 33^\circ\text{C}$ ("Weather is comfortable. Stay hydrated as usual.")
    - **Mag-ingat**: $33^\circ\text{C} - 41^\circ\text{C}$ ("Drink more water, wear light clothing, take breaks in shade.")
    - **Delikado**: $\ge 42^\circ\text{C}$ ("Stay out of noon sun 10am-4pm, hydrate frequently.")

### 1.4 AI Advice & Taglish Phrasing
- **Taglish Weather Phrase Bank ([`backend/ai/taglish-phrases.md`](../../backend/ai/taglish-phrases.md)):**
  - Natural, conversational Filipino/Taglish guidance avoiding robotic translations.
- **Advice Function Contract & Test Cases ([`backend/ai/samples.md`](../../backend/ai/samples.md)):**
  - Documented 10 realistic test cases with forecast inputs and expected Taglish and English payo advice outputs.
  - Established rule: numbers strictly come from forecast code; AI only verbalizes facts.

### 1.5 UX Design & User Research
- **Design Wireframes:**
  - Joan created initial sketches and UI wireframes linked in [`links.md`](../../links.md).
- **User Research Synthesis ([`docs/user-research.md`](../user-research.md)):**
  - Synthesized interviews from 31 respondents across 3 key findings:
    1. Rain probability and hourly timing are top daily priorities (87% of respondents).
    2. Need timely alerts for sudden weather shifts (84% experienced sudden rain disruption).
    3. Plain language and localized updates are essential.

### 1.6 QA & Team Process
- GitHub pull request and bug report templates created and active (`.github/`).
- Comprehensive QA Test Plan v1 authored in [`docs/test-plan.md`](../test-plan.md) covering all four core features (7-Day Forecast, Payo for Today, Alis-Uwi Rain Planner, Heat Check).

---

## 2. What's Next (Week 2: Connect)

Our goal for Week 2 is **Connect: Real weather saved in the database. Rain check, heat level and advice work. The screens use real data.**

1. **Connect Database (MJ & Fredelina):**
   - Spin up PostgreSQL instance (local docker / cloud service).
   - Create migrations for cities table and hourly forecast caching table.
2. **Implement Weather & Rule Services (Fredelina & MJ):**
   - Implement `GET /forecast?city={city_id}` calling Open-Meteo live API and caching results.
   - Implement rain detection logic ($\ge 60\%$) and 3-tier heat check logic in Python.
3. **Connect AI Advice Service (JC & Fredelina):**
   - Implement `GET /payo` endpoint integrating LangChain / OpenRouter with prompt templates and the Taglish phrase bank.
4. **Connect Frontend Screens (Miguel & Joan):**
   - Integrate `CityPicker`, `ForecastList`, `PayoCard`, and `HeatCard` with live backend endpoints (`/cities`, `/forecast`, `/payo`).
   - Style components according to Joan's Figma wireframes.
5. **QA & Validation (Angela):**
   - Execute Test Plan v1 against live connected endpoints.
   - Set up Postman collection for automated regression testing.

---

## 3. What's Blocked / Needs Team Alignment

1. **OpenRouter API Key Provisioning:**
   - Need an active `OPENROUTER_API_KEY` for team development and AI advice testing in Week 2.
   - *Action:* Khair / JC to configure and share key securely via private team channels (never committed to git).
2. **PostgreSQL Environment Standard:**
   - Need agreement on local database setup (Docker Compose vs local Postgres installation) to ensure consistency across developer laptops.
   - *Action:* MJ to provide `docker-compose.yml` or local setup instructions for Week 2 Day 1.
3. **Week 1 Pull Request Merges:**
   - Multiple Week 1 branches are ready and awaiting final review/merge by Khair:
     - PR #20 (`17-app-frame` — frontend components)
     - PR #21 (`20-city-list` — cities catalog)
     - PR #22 (`23-advice-contract` — advice doc)
     - PR #26 (`24-api-contract` — API contract)
     - PR #27 (`32-user-interviews` — user research)
     - PR #30 (`26-rain-heat-rules` — rules)
     - PR #31 (`28-advice-samples` — advice samples)
     - PR #32 (`33-test-plan` — test plan)
   - *Action:* Khair to review and merge so everyone starts Week 2 on a unified `main`.
4. **Endpoint Parameter Confirmation for `/payo`:**
   - Confirm whether "Payo for Today" and "Alis-Uwi Planner" share `GET /payo` with optional `leave`/`return` query parameters, or if they will be distinct endpoints.
   - *Action:* Fredelina, JC, and Miguel to confirm on Monday morning standup.

---

*Submitted for the Friday Week 1 Demo. All setup steps verified and reproducible.*
