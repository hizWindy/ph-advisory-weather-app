
# PH Weather Advisor – Advice Function Contract

## Input (`facts`)

| Field | Type | Example |
|---|---|---|
| `city` | string | `"Manila"` |
| `date` | string (`YYYY-MM-DD`) | `"2026-11-12"` |
| `language` | enum: `"taglish"` or `"english"` | `"taglish"` |
| `rain_chance_by_hour` | array of `HourlyRainChance` | `[{"time": "2026-11-12T07:00:00+08:00", "chance_percent": 10}]` |
| `leave_time` | string (`HH:mm`) or `null` | `"07:00"` |
| `rain_chance_at_leave_percent` | number (0–100) or `null` | `10` |
| `return_time` | string (`HH:mm`) or `null` | `"18:00"` |
| `rain_chance_at_return_percent` | number (0–100) or `null` | `80` |
| `heat_level` | enum: `"OK"`, `"Mag-ingat"`, or `"Delikado"` | `"OK"` |

### `HourlyRainChance`

| Field | Type | Example |
|---|---|---|
| `time` | string (ISO 8601 datetime) | `"2026-11-12T07:00:00+08:00"` |
| `chance_percent` | number (0–100) | `10` |

## Heat Level Values

- `OK`
- `Mag-ingat`
- `Delikado`

## Output

| Field | Type | Example |
|---|---|---|
| `payo` | string (2–3 sentences) | `"May 80% chance ng ulan sa uwian mo. Magdala ka ng payong."` |
| `message_source` | enum: `"ai"` or `"backup"` | `"ai"` |

## Full Examples: Facts In, Payo Out

### Example 1 — Taglish, AI response

**Facts in:**

```json
{
  "city": "Manila",
  "date": "2026-11-12",
  "language": "taglish",
  "rain_chance_by_hour": [
    {
      "time": "2026-11-12T07:00:00+08:00",
      "chance_percent": 10
    },
    {
      "time": "2026-11-12T12:00:00+08:00",
      "chance_percent": 30
    },
    {
      "time": "2026-11-12T18:00:00+08:00",
      "chance_percent": 80
    }
  ],
  "leave_time": "07:00",
  "rain_chance_at_leave_percent": 10,
  "return_time": "18:00",
  "rain_chance_at_return_percent": 80,
  "heat_level": "OK"
}

### Payo out

{
  "payo": "Okay ang alis mo ng 7:00 AM; 10% ang chance ng ulan sa oras na iyon. May 80% chance ng ulan sa uwian mong 6:00 PM, kaya magdala ka ng payong.",
  "message_source": "ai"
}

###Example 2 — English, backup response
**Facts in:**

```json
{
  "city": "Cebu",
  "date": "2026-11-12",
  "language": "english",
  "rain_chance_by_hour": [
    {
      "time": "2026-11-12T08:00:00+08:00",
      "chance_percent": 10
    },
    {
      "time": "2026-11-12T12:00:00+08:00",
      "chance_percent": 30
    },
    {
      "time": "2026-11-12T17:00:00+08:00",
      "chance_percent": 70
    }
  ],
  "leave_time": "08:00",
  "rain_chance_at_leave_percent": 10,
  "return_time": "17:00",
  "rain_chance_at_return_percent": 70,
  "heat_level": "Mag-ingat"
}

### Payo out
{
  "payo": "Your heat level is Mag-ingat today. Drink water and take breaks in the shade. There is a 70% chance of rain at your 5:00 PM return, so bring an umbrella.",
  "message_source": "backup"
}

