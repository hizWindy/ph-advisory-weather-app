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

1. **Get the weather.** The backend fetches the hourly forecast from [Open-Meteo](https://open-meteo.com/) and saves it.
2. **Work out the facts.** Plain code checks the rain for each hour and the heat level.
3. **Explain it.** An AI model, through OpenRouter, turns those facts into short advice.

The numbers always come from code. The AI only puts them into words, so it can't make up a rain chance or a temperature.

## Tech stack

| Part | Tools |
|---|---|
| Frontend | React with Vite |
| Backend | Python with FastAPI |
| Database | PostgreSQL |
| Weather data | Open-Meteo |
| AI | OpenRouter, LangChain |
| Testing | pytest, Postman |

## Status

Planning. There is no app code yet. Setup and run steps will be added here with the starter code.

## Repo layout

```
docs/
  product-brief.pdf           What the app is and who it's for
  team-guide.pdf              Roles, how we work, tools
  github-projects-kanban.md   How our task board works
CONTRIBUTING.md               Git and teamwork rules
README.md                     This file
```

## Team

| Name | Role |
|---|---|
| Khair | Project Manager and Tech Lead |
| Joan | UI/UX Designer |
| Miguel | Frontend Developer |
| MJ | Data Engineer |
| Fredelina | Backend Developer |
| JC | AI Integrator |
| Angela | QA and Docs |

## Getting started

1. Read [CONTRIBUTING.md](CONTRIBUTING.md) for how we use Git and work together.
2. Read [docs/github-projects-kanban.md](docs/github-projects-kanban.md) for how to pick up and move a card.
3. Clone the repo:

   ```bash
   git clone https://github.com/hizWindy/ph-advisory-weather-app.git
   cd ph-advisory-weather-app
   ```

## Limits

- The advice is written by AI from forecast data. It is not an official forecast.
- The heat level is an estimate from the "feels like" temperature, not PAGASA's heat index.
- The app never predicts class or work suspensions. Check official announcements.
