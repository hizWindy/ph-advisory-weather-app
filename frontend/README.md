# PH Weather Advisory - Frontend App

React web application for the Philippine Weather Advisory App, built with React 19 and Vite.

---

## Prerequisites

- **Node.js**: LTS version (v18, v20, or higher recommended)
- **npm** (comes with Node.js) or **pnpm**

---

## Quick Start Guide

Follow these steps to run the frontend on your laptop:

### 1. Open a terminal and navigate to `frontend/`

```bash
cd frontend
```

---

### 2. Install dependencies

```bash
npm install
```

---

### 3. Start the development server

```bash
npm run dev
```

The app will start with Vite hot-reload enabled:
- **Local URL:** [http://localhost:5173/](http://localhost:5173/)
- **Network URL:** Run `npm run dev -- --host` to expose to your local network.

Open [http://localhost:5173/](http://localhost:5173/) in your web browser. You should see the PH Weather Advisory welcome screen.

---

## Available Scripts

In the `frontend` directory, you can run:

| Command | Description |
|---|---|
| `npm run dev` | Starts the local Vite development server with hot-module replacement |
| `npm run build` | Compiles TypeScript and builds the production bundle in `dist/` |
| `npm run preview` | Locally serves the production build from `dist/` for testing |

---

## Project Structure

```text
frontend/
├── README.md              # Setup and execution guide (this file)
├── index.html             # HTML entry point
├── package.json           # Dependencies and npm scripts
├── package-lock.json      # Locked dependency tree
├── tsconfig.json          # TypeScript compiler configuration
├── public/                # Static public assets (favicons, SVG icons)
│   ├── favicon.svg
│   └── icons.svg
└── src/                   # React application source code
    ├── main.jsx           # React DOM mounting entrypoint
    ├── App.jsx            # Main app shell and layout
    ├── style.css          # Core styles and design system tokens
    ├── counter.ts         # Utility module
    ├── assets/            # App images and illustrations
    └── components/        # Weather UI components (in progress)
```

---

## Connecting to Backend

During local development:
- The FastAPI backend runs at [http://127.0.0.1:8000](http://127.0.0.1:8000).
- The backend has CORS enabled for all local development origins (`*`).
- In Week 2, frontend components will fetch live weather data and advice directly from backend endpoints:
  - `GET http://127.0.0.1:8000/cities`
  - `GET http://127.0.0.1:8000/forecast?city={city_id}`
  - `GET http://127.0.0.1:8000/payo?city={city_id}&leave={time}&return={time}&lang={lang}`
