# Project structure

Where every file goes and who owns it.

> **This is a sample.** Use it as a guide. The real file names can change as we build. Today the repo only has `README.md`, `CONTRIBUTING.md`, `.gitignore` and `docs/`. The other folders get added as the cards are done.

## The whole project

```
ph-advisory-weather-app/
├── README.md                    What the app is and how to run it
├── CONTRIBUTING.md              Our rules for Git and teamwork
├── DESIGN.md                    Colors, fonts, spacing, buttons
├── .gitignore                   Files Git should skip (like .env)
│
├── .github/
│   ├── pull_request_template.md
│   └── ISSUE_TEMPLATE/
│       └── bug_report.md
│
├── design/
│   └── sketches/
│       ├── city-picker.png
│       └── 7-day-forecast.png
│
├── docs/
│   ├── project-structure.md     This file
│   ├── github-projects-kanban.md
│   ├── product-brief.pdf
│   ├── team-guide.pdf
│   ├── api.md                   The web addresses the app calls
│   ├── advice-contract.md       What goes into the AI and what comes out
│   ├── data.md                  The weather fields we use, with units
│   ├── model-comparison.md      Which AI model we picked and why
│   ├── test-plan.md             What to check for each feature
│   ├── user-research.md         What people told us in the interviews
│   ├── demos/
│   │   └── week-1.md
│   └── team/
│       ├── joan.md
│       └── miguel.md
│
├── frontend/
│   ├── README.md                How to run the frontend
│   ├── package.json
│   ├── index.html
│   └── src/
│       ├── main.jsx
│       ├── App.jsx
│       ├── components/
│       │   ├── CityPicker.jsx
│       │   ├── ForecastList.jsx
│       │   ├── PayoCard.jsx
│       │   ├── AlisUwi.jsx
│       │   └── HeatCard.jsx
│       ├── api/
│       │   └── client.js        The only file that calls our backend
│       └── mock/
│           └── forecast.json    Fake data until the backend is ready
│
└── backend/
    ├── README.md                How to run the backend
    ├── requirements.txt         Python packages we install
    ├── .env.example             Setting names, no real values
    ├── app/
    │   ├── main.py              Starts the server
    │   ├── routes/
    │   │   ├── cities.py        GET /cities
    │   │   ├── forecast.py      GET /forecast
    │   │   └── payo.py          GET /payo
    │   └── rules/
    │       ├── rain.py          Rain check for each hour
    │       └── heat.py          OK, Mag-ingat or Delikado
    ├── ai/
    │   ├── advice.py            Turns facts into payo
    │   ├── prompts.md
    │   └── samples.md
    ├── data/
    │   ├── cities.json
    │   └── samples/
    │       └── manila.json
    ├── scripts/
    │   └── fetch_forecast.py    Gets the weather from Open-Meteo
    └── tests/
        ├── test_rain.py
        └── test_heat.py
```

## Who owns what

You own your folders. Work there freely, through a pull request as always.

| Folder or file | Owner | What goes in it |
|---|---|---|
| `design/`, `DESIGN.md` | Joan | Sketches, screen exports, the style guide |
| `frontend/` | Miguel | Everything people see and tap |
| `backend/app/` | Fredelina | The server, the rain check and the heat level |
| `backend/ai/` | JC | Prompts, sample advice, the advice function |
| `backend/data/`, `backend/scripts/` | MJ | The city list, sample forecasts, scripts that get the weather |
| `backend/tests/` | Each owner | Tests for your own part. Example: Fredelina writes `test_heat.py`. |
| `README.md`, `.github/`, `docs/test-plan.md`, `docs/user-research.md`, `docs/demos/` | Angela | The main README, templates, testing, demo notes |
| `docs/api.md` | Fredelina | |
| `docs/advice-contract.md` | Fredelina and JC | |
| `docs/data.md` | MJ | |
| `docs/model-comparison.md` | JC | |
| `docs/team/` | Everyone | One file each |
| `CONTRIBUTING.md`, `.gitignore`, `docs/github-projects-kanban.md`, `docs/project-structure.md` | Khair | Team rules and guides |

## How the parts connect

```
Open-Meteo
   ↓
backend/scripts/ and backend/data/   MJ         gets and saves the weather
   ↓
backend/app/rules/                   Fredelina  works out rain and heat
   ↓
backend/ai/advice.py                 JC         turns the facts into payo
   ↓
backend/app/routes/                  Fredelina  sends it to the app
   ↓
frontend/src/api/client.js           Miguel     asks the backend for it
   ↓
frontend/src/components/             Miguel     shows it on screen
```

## Three rules

1. **Your folder:** change it freely, through a pull request.
2. **Someone else's folder:** ask the owner first, and add them as a reviewer on your PR.
3. **Shared files:** only add your own lines. Don't change or move other people's lines. Say in your PR that you touched a shared file.

## Shared files

More than one person adds to these files, so this is where merge conflicts usually happen. If you get one, see "When `main` has moved on" in [CONTRIBUTING.md](../CONTRIBUTING.md).

| File | Owner | Who else adds to it |
|---|---|---|
| `backend/requirements.txt` | Fredelina | MJ and JC add the packages they need, one line each |
| `backend/.env.example` | Fredelina | MJ and JC add setting names. Never real keys. |
| `backend/app/main.py` | Fredelina | MJ and JC connect their parts here in Week 2. Ask first. |
| `frontend/package.json` | Miguel | Changes when someone installs a package. Ask Miguel first. |
| `README.md` | Angela | Owners write their own folder's README. Angela links to them. |
| `docs/advice-contract.md` | Fredelina and JC | Both approve every change |
| `docs/api.md` | Fredelina | Miguel asks for changes in a comment |

## Naming files

| Kind of file | How to name it | Example |
|---|---|---|
| Screens and cards (React) | Each word starts with a capital letter, no spaces | `CityPicker.jsx` |
| Other JavaScript files | Lowercase | `client.js` |
| Python files | Lowercase, words joined with `_` | `fetch_forecast.py` |
| Tests | `test_` plus the name of the file it tests | `test_heat.py` |
| Docs and images | Lowercase, words joined with `-` | `test-plan.md`, `city-picker.png` |

Not sure where a new file goes? Ask the folder's owner, or Khair.
