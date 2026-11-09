# PH Weather Advisory

A weather app for the Philippines that turns the forecast into simple advice for your day, in Taglish or English.

> Not an official forecast. For storm warnings and alerts, check [PAGASA](https://www.pagasa.dost.gov.ph/).

## What it does

Version 1 has four features:

| Feature | What you get |
|---|---|
| 7-day forecast | Pick a city and see the week ahead |
| Payo for today | 2 to 3 sentences of advice for the day |
| Alis-Uwi | Set the time you leave and the time you go home, and see if it will rain then |
| Heat check | How hot it will really feel: OK, Mag-ingat or Delikado |

Example payo:

> Mainit sa umaga, pero uulan after 3pm. Magdala ka ng payong at umalis ka na before 4:30.

## How it works

1. **Get the weather.** The backend gets the hourly forecast from [Open-Meteo](https://open-meteo.com/) and saves it.
2. **Work out the facts.** Plain code checks the rain for each hour and the heat level.
3. **Explain it.** An AI model, through OpenRouter, turns those facts into short advice.

The numbers always come from code. The AI only puts them into words, so it can't make up a rain chance or a temperature.

## Tools we use

| Part | Tools |
|---|---|
| Frontend (what people see) | React with Vite |
| Backend (the server) | Python with FastAPI |
| Database | PostgreSQL |
| Weather data | Open-Meteo |
| AI | OpenRouter, LangChain |
| Design | Figma, Google Stitch |
| Testing | pytest, Postman, Swagger |
| Task board | GitHub Projects |

## Status

Planning. There is no app code yet. We build it in 3 weeks:

| Week | Goal |
|---|---|
| Week 1: Set up | Everyone makes a first pull request. Both apps start. We agree how the parts talk to each other. First sketches. |
| Week 2: Connect | Real weather saved in the database. Rain check, heat level and advice work. The screens use real data. |
| Week 3: Finish | Alis-Uwi and the heat card are done. Everything is tested. Final demo. |

## Project structure

```
frontend/   The app people see and tap (React)
backend/    The server, the weather data and the AI (FastAPI)
design/     Sketches and screens
docs/       Guides, plans and notes
```

These folders get added as we build. [docs/project-structure.md](docs/project-structure.md) shows every folder, who owns it, and sample files.

## Team

| Name | Role | Works in |
|---|---|---|
| Khair | Project Manager and Tech Lead | Reviews and merges every pull request |
| Joan | UI/UX Designer | `design/`, `DESIGN.md` |
| Miguel | Frontend Developer | `frontend/` |
| MJ | Data Engineer | `backend/data/`, `backend/scripts/` |
| Fredelina | Backend Developer | `backend/app/` |
| JC | AI Integrator | `backend/ai/` |
| Angela | QA and Docs | `README.md`, testing, `docs/` |

## Getting started

1. **Accept the GitHub invite.** Check your email or [github.com/notifications](https://github.com/notifications).
2. **Read [CONTRIBUTING.md](CONTRIBUTING.md).** Our rules, and how to make a pull request.
3. **Read [docs/github-projects-kanban.md](docs/github-projects-kanban.md).** How our task board works.
4. **Read [docs/project-structure.md](docs/project-structure.md).** Where your files go.
5. **Find your cards.** Open the **Projects** tab, open our board, and type `assignee:@me` in the filter.
6. **Writing code?** Install what your role needs, then clone the repo:

   | Role | Install |
   |---|---|
   | Everyone | [VS Code](https://code.visualstudio.com/), [Git](https://git-scm.com/) |
   | Miguel (frontend) | [Node.js](https://nodejs.org/), the LTS version |
   | MJ, Fredelina, JC (backend, data, AI) | [Python](https://www.python.org/downloads/) 3.12 |
   | Joan (design) | A [Figma](https://www.figma.com/) account |
   | Angela (QA) | [Postman](https://www.postman.com/downloads/) |

   ```bash
   git clone https://github.com/hizWindy/ph-advisory-weather-app.git
   cd ph-advisory-weather-app
   ```

## How to run it

Coming soon. The steps will be in `frontend/README.md` and `backend/README.md` once the starter code is added.

## Rules in short

- Never push straight to `main`. Use a pull request.
- Never put API keys or passwords in the code, the repo or the group chat.
- Numbers come from code, never from the AI.
- Work in your own folder. Ask before you change someone else's.
- Stuck for 30 minutes? Ask a teammate, then Khair.

The full rules are in [CONTRIBUTING.md](CONTRIBUTING.md).

## Our docs

| File | What it's for |
|---|---|
| [CONTRIBUTING.md](CONTRIBUTING.md) | Rules for Git, pull requests and teamwork |
| [docs/project-structure.md](docs/project-structure.md) | Where files go and who owns them |
| [docs/github-projects-kanban.md](docs/github-projects-kanban.md) | How our task board works |
| [docs/product-brief.pdf](docs/product-brief.pdf) | What the app is and who it's for |
| [docs/team-guide.pdf](docs/team-guide.pdf) | Roles, how we work, tools |

## Limits

- The advice is written by AI from forecast data. It is not an official forecast.
- The heat level is an estimate from the "feels like" temperature, not PAGASA's heat index.
- The app never predicts class or work suspensions. Check official announcements.
