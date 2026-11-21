# PH Weather Advisory - Backend API

FastAPI backend service for the Philippine Weather Advisory App. Provides endpoints for system health, city catalog data, and future weather forecast and AI advice services.

---

## Prerequisites

- **Python**: Version 3.10, 3.11, or 3.12+ (Python 3.12 recommended)
- **Git**

---

## Quick Start Guide

Follow these steps to run the backend locally on your laptop:

### 1. Open a terminal and navigate to `backend/`

```bash
cd backend
```

---

### 2. Create a virtual environment

Create an isolated Python virtual environment named `.venv`:

- **Windows (Command Prompt / PowerShell):**
  ```powershell
  python -m venv .venv
  ```
  *(If `python` is not recognized, use `py -m venv .venv`)*

- **macOS / Linux:**
  ```bash
  python3 -m venv .venv
  ```

---

### 3. Activate the virtual environment

- **Windows PowerShell:**
  ```powershell
  .venv\Scripts\Activate.ps1
  ```
  *(If execution policies block scripts, run: `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`)*

- **Windows Command Prompt (cmd.exe):**
  ```cmd
  .venv\Scripts\activate.bat
  ```

- **macOS / Linux:**
  ```bash
  source .venv/bin/activate
  ```

When activated, you will see `(.venv)` in your terminal prompt.

---

### 4. Install dependencies

Upgrade `pip` and install all required packages:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

---

### 5. Configure environment variables

Copy `.env.example` to create your local `.env` file:

- **Windows (PowerShell):**
  ```powershell
  Copy-Item .env.example .env
  ```

- **Windows (Command Prompt):**
  ```cmd
  copy .env.example .env
  ```

- **macOS / Linux:**
  ```bash
  cp .env.example .env
  ```

*Note:* `.env.example` lists `OPENROUTER_API_KEY` with no value by default. You can leave it empty for Day 3/4 testing or supply an OpenRouter API key when testing AI advice generation later.

---

### 6. Start the development server

Start the FastAPI backend with hot-reload enabled:

```bash
uvicorn app.main:app --reload
```

The server will start at:
- **Base URL:** [http://127.0.0.1:8000](http://127.0.0.1:8000)
- **Interactive Swagger Docs:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc Documentation:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## Available API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Root greeting and endpoint index |
| `GET` | `/health` | Service health status, UTC timestamp, and uptime |
| `GET` | `/cities` | List of Philippine cities loaded from `backend/data/cities.json` |
| `GET` | `/cities/{city_id}` | Details for a specific city by ID (e.g. `manila`, `cebu-city`, `davao-city`) |
| `GET` | `/docs` | Interactive OpenAPI Swagger UI |

### Sample Responses

#### `GET /health`

```json
{
  "status": "healthy",
  "timestamp": "2026-11-14T00:30:00Z",
  "uptime": 120
}
```

#### `GET /cities`

```json
{
  "cities": [
    {
      "id": "manila",
      "name": "Manila",
      "province": "NCR",
      "region": "National Capital Region",
      "postal_code": "1000",
      "latitude": 14.5995,
      "longitude": 120.9842,
      "timezone": "Asia/Manila"
    },
    {
      "id": "cebu-city",
      "name": "Cebu City",
      "province": "Cebu",
      "region": "Central Visayas",
      "postal_code": "6000",
      "latitude": 10.3157,
      "longitude": 123.8854,
      "timezone": "Asia/Manila"
    },
    {
      "id": "davao-city",
      "name": "Davao City",
      "province": "Davao del Sur",
      "region": "Davao Region",
      "postal_code": "8000",
      "latitude": 7.1907,
      "longitude": 125.4553,
      "timezone": "Asia/Manila"
    }
  ]
}
```

---

## Running Automated Tests

Run the test suite using `pytest`:

```bash
pytest -v
```

All tests verify that `/`, `/health`, `/cities`, and `/cities/{city_id}` return HTTP 200 with valid schema structures.

---

## Directory Structure

```text
backend/
├── README.md               # Setup and execution guide (this file)
├── requirements.txt        # Python package dependencies
├── .env.example            # Template environment variables
├── .env                    # Local environment variables (ignored by git)
├── app/
│   ├── __init__.py
│   └── main.py             # FastAPI entrypoint and routes
├── data/
│   ├── cities.json         # MJ's curated list of Philippine cities
│   └── samples/            # Open-Meteo 7-day weather sample datasets
│       ├── cebu.json
│       ├── davao.json
│       └── manila.json
└── tests/
    ├── __init__.py
    └── test_main.py        # Automated test suite
```

