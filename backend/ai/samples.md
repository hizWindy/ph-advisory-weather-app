# PH Weather Advisor – Sample Forecasts and Payo

*Draft · Ticket #28 · Location in repo: `backend/ai/samples.md`*

These 10 cases use **illustrative test data, not real forecasts**. They retain the input and output structure from the existing advice contract and use the latest writing examples supplied by the reviewer as the tone reference. No contract fields have been added, renamed, or removed.

## How to read the cases

- **One language per call.** Each case shows the full input for `language: "taglish"`. The English output represents a second call with the same facts, changing only `language` to `"english"`; the second input is not repeated.
- **Keep the payo focused on advice.** The dashboard already shows the detailed forecast, so payos generally describe rain chances as low, high, rising, or lower instead of repeating percentages. Times may be included when they help the user plan.
- **`message_source` is assigned by the backend response path.** It is shown in these illustrative outputs, but the AI should not decide or report the source itself.
- **Missing data:** a missing departure or return time and its probability use `null`; unavailable hourly rain data uses an empty array.
- **Scenario context:** Cases 09 and 10 assume the user’s activity or question is provided separately to the AI. It is not added as a new field to the contract input.

---

## Case 01 – Mag-ingat heat with low rain chances

**Scenario:** The heat level is Mag-ingat, while rain chances remain low. No departure or return time is set.

### Facts in

```json
{
  "city": "Manila",
  "date": "2026-11-16",
  "language": "taglish",
  "rain_chance_by_hour": [
    {
      "time": "2026-11-16T08:00:00+08:00",
      "chance_percent": 5
    },
    {
      "time": "2026-11-16T10:00:00+08:00",
      "chance_percent": 5
    },
    {
      "time": "2026-11-16T12:00:00+08:00",
      "chance_percent": 10
    },
    {
      "time": "2026-11-16T14:00:00+08:00",
      "chance_percent": 10
    },
    {
      "time": "2026-11-16T16:00:00+08:00",
      "chance_percent": 5
    }
  ],
  "leave_time": null,
  "rain_chance_at_leave_percent": null,
  "return_time": null,
  "rain_chance_at_return_percent": null,
  "heat_level": "Mag-ingat"
}
```

### Taglish payo out

```json
{
  "payo": "Based sa heat level, need mo mag-ingat, kaya mag-baon ka ng tubig at lumilim kapag nasa labas. Mababa na lang ang chance ng ulan ng 12 PM, kaya yung init ang need mong bantayan ngayon.",
  "message_source": "ai"
}
```

### English payo out

*Second call: same facts, with `language: "english"`.*

```json
{
  "payo": "Based on the heat level, you need to be careful, so bring water and stay in the shade when you’re outside. The chance of rain around 12 PM is low, so the heat is what you need to watch out for today.",
  "message_source": "ai"
}
```

---

## Case 02 – Rain chance is high at departure, then lower later

**Scenario:** Rain chance is high at the user’s 5 PM departure and lower by 7 PM.

### Facts in

```json
{
  "city": "Davao",
  "date": "2026-11-17",
  "language": "taglish",
  "rain_chance_by_hour": [
    {
      "time": "2026-11-17T13:00:00+08:00",
      "chance_percent": 20
    },
    {
      "time": "2026-11-17T15:00:00+08:00",
      "chance_percent": 30
    },
    {
      "time": "2026-11-17T16:00:00+08:00",
      "chance_percent": 50
    },
    {
      "time": "2026-11-17T17:00:00+08:00",
      "chance_percent": 70
    },
    {
      "time": "2026-11-17T18:00:00+08:00",
      "chance_percent": 60
    },
    {
      "time": "2026-11-17T19:00:00+08:00",
      "chance_percent": 40
    }
  ],
  "leave_time": "17:00",
  "rain_chance_at_leave_percent": 70,
  "return_time": null,
  "rain_chance_at_return_percent": null,
  "heat_level": "OK"
}
```

### Taglish payo out

```json
{
  "payo": "Mataas ang chance ng ulan sa pag-alis mo ng 5 PM, kaya magdala ka ng payong, ha. Pwede ka rin namang maghintay muna bago bumiyahe kasi mas mababa na lang ang chance ng ulan ng 7 PM.",
  "message_source": "ai"
}
```

### English payo out

*Second call: same facts, with `language: "english"`.*

```json
{
  "payo": "There’s a high chance of rain when you leave at 5 PM, so bring an umbrella. You could also wait a little before heading out, since the chance of rain is lower by 7 PM.",
  "message_source": "ai"
}
```

---

## Case 03 – High rain chances throughout the day

**Scenario:** Rain chances remain high across the listed hours, with the highest chance around midday. No travel times are set.

### Facts in

```json
{
  "city": "Cebu",
  "date": "2026-11-18",
  "language": "taglish",
  "rain_chance_by_hour": [
    {
      "time": "2026-11-18T06:00:00+08:00",
      "chance_percent": 75
    },
    {
      "time": "2026-11-18T08:00:00+08:00",
      "chance_percent": 80
    },
    {
      "time": "2026-11-18T10:00:00+08:00",
      "chance_percent": 80
    },
    {
      "time": "2026-11-18T12:00:00+08:00",
      "chance_percent": 85
    },
    {
      "time": "2026-11-18T14:00:00+08:00",
      "chance_percent": 80
    },
    {
      "time": "2026-11-18T16:00:00+08:00",
      "chance_percent": 75
    },
    {
      "time": "2026-11-18T18:00:00+08:00",
      "chance_percent": 70
    }
  ],
  "leave_time": null,
  "rain_chance_at_leave_percent": null,
  "return_time": null,
  "rain_chance_at_return_percent": null,
  "heat_level": "OK"
}
```

### Taglish payo out

```json
{
  "payo": "Mataas ang chance na umulan halos buong araw, lalo na bandang 12 PM. Kaya magdala ka ng payong or kapote kung lalabas ka.",
  "message_source": "ai"
}
```

### English payo out

*Second call: same facts, with `language: "english"`.*

```json
{
  "payo": "There’s a high chance of rain for most of the day, especially around 12 PM. Bring an umbrella or raincoat if you’re going out.",
  "message_source": "ai"
}
```

---

## Case 04 – Delikado heat with no hourly rain data

**Scenario:** The heat level is Delikado. Hourly rain information is unavailable, so the payo does not mention rain.

### Facts in

```json
{
  "city": "Davao",
  "date": "2026-11-19",
  "language": "taglish",
  "rain_chance_by_hour": [],
  "leave_time": null,
  "rain_chance_at_leave_percent": null,
  "return_time": null,
  "rain_chance_at_return_percent": null,
  "heat_level": "Delikado"
}
```

### Taglish payo out

```json
{
  "payo": "Based sa heat level, delikado ang init ngayon. Kung ’di naman kailangan, ’wag ka na muna lumabas; kung kailangan talaga, mag-baon ka ng tubig at magdala ng payong kung maglalakad ka sa labas.",
  "message_source": "ai"
}
```

### English payo out

*Second call: same facts, with `language: "english"`.*

```json
{
  "payo": "Based on the heat level, the heat is dangerous today. Stay indoors if you don’t need to go out; if you do, bring water and use an umbrella while walking outside.",
  "message_source": "ai"
}
```

### Illustrative backup outputs

**Taglish:**

```json
{
  "payo": "Delikado ang init ngayon, kaya ’wag ka munang lumabas kung hindi kailangan. Kung kailangan mong lumabas, mag-baon ka ng tubig.",
  "message_source": "backup"
}
```

**English:**

```json
{
  "payo": "The heat is dangerous today, so stay indoors if you can. Bring water if you need to go out.",
  "message_source": "backup"
}
```

---

## Case 05 – Low rain chance at departure, higher at return

**Scenario:** The 7 AM departure has a low rain chance, while the user’s 5 PM trip home has a higher one.

### Facts in

```json
{
  "city": "Cebu",
  "date": "2026-11-20",
  "language": "taglish",
  "rain_chance_by_hour": [
    {
      "time": "2026-11-20T07:00:00+08:00",
      "chance_percent": 15
    },
    {
      "time": "2026-11-20T10:00:00+08:00",
      "chance_percent": 25
    },
    {
      "time": "2026-11-20T13:00:00+08:00",
      "chance_percent": 40
    },
    {
      "time": "2026-11-20T15:00:00+08:00",
      "chance_percent": 55
    },
    {
      "time": "2026-11-20T17:00:00+08:00",
      "chance_percent": 75
    },
    {
      "time": "2026-11-20T19:00:00+08:00",
      "chance_percent": 60
    }
  ],
  "leave_time": "07:00",
  "rain_chance_at_leave_percent": 15,
  "return_time": "17:00",
  "rain_chance_at_return_percent": 75,
  "heat_level": "OK"
}
```

### Taglish payo out

```json
{
  "payo": "Okay naman ang alis mo ng 7 AM, kasi mababa lang ang chance ng ulan. Kaso mas mataas ang chance ng ulan sa uwian mo mamayang 5 PM, kaya magdala ka ng payong.",
  "message_source": "ai"
}
```

### English payo out

*Second call: same facts, with `language: "english"`.*

```json
{
  "payo": "Your 7 AM departure looks fine because the chance of rain is low. But rain is more likely on your way home at 5 PM, so bring an umbrella.",
  "message_source": "ai"
}
```

---

## Case 06 – High rain chance in the morning, lower at return

**Scenario:** The 7 AM departure has a high rain chance, while the chance is lower by the user’s 5 PM trip home.

### Facts in

```json
{
  "city": "Manila",
  "date": "2026-11-21",
  "language": "taglish",
  "rain_chance_by_hour": [
    {
      "time": "2026-11-21T06:00:00+08:00",
      "chance_percent": 70
    },
    {
      "time": "2026-11-21T07:00:00+08:00",
      "chance_percent": 80
    },
    {
      "time": "2026-11-21T09:00:00+08:00",
      "chance_percent": 65
    },
    {
      "time": "2026-11-21T12:00:00+08:00",
      "chance_percent": 40
    },
    {
      "time": "2026-11-21T15:00:00+08:00",
      "chance_percent": 30
    },
    {
      "time": "2026-11-21T17:00:00+08:00",
      "chance_percent": 20
    },
    {
      "time": "2026-11-21T19:00:00+08:00",
      "chance_percent": 15
    }
  ],
  "leave_time": "07:00",
  "rain_chance_at_leave_percent": 80,
  "return_time": "17:00",
  "rain_chance_at_return_percent": 20,
  "heat_level": "OK"
}
```

### Taglish payo out

```json
{
  "payo": "Mukhang kailangan mo ng payong sa pag-alis mo ng 7 AM kasi mataas ang chance ng ulan. Pero mas mababa na lang ang chance pag-uwi mo ng 5 PM, kaya mas okay ang biyahe mo pauwi.",
  "message_source": "ai"
}
```

### English payo out

*Second call: same facts, with `language: "english"`.*

```json
{
  "payo": "You’ll probably need an umbrella when you leave at 7 AM because the chance of rain is high. The chance is lower by your 5 PM trip home, so the ride back should be easier.",
  "message_source": "ai"
}
```

---

## Case 07 – Mag-ingat heat with scheduled travel times

**Scenario:** The heat level is Mag-ingat. The user has a 10 AM departure and a 3 PM return, both with low rain chances.

### Facts in

```json
{
  "city": "Davao",
  "date": "2026-11-22",
  "language": "taglish",
  "rain_chance_by_hour": [
    {
      "time": "2026-11-22T08:00:00+08:00",
      "chance_percent": 5
    },
    {
      "time": "2026-11-22T10:00:00+08:00",
      "chance_percent": 10
    },
    {
      "time": "2026-11-22T12:00:00+08:00",
      "chance_percent": 10
    },
    {
      "time": "2026-11-22T15:00:00+08:00",
      "chance_percent": 15
    },
    {
      "time": "2026-11-22T17:00:00+08:00",
      "chance_percent": 10
    }
  ],
  "leave_time": "10:00",
  "rain_chance_at_leave_percent": 10,
  "return_time": "15:00",
  "rain_chance_at_return_percent": 15,
  "heat_level": "Mag-ingat"
}
```

### Taglish payo out

```json
{
  "payo": "Based sa heat level, need mo mag-ingat, kaya mag-baon ka ng tubig bago ka umalis ng 10 AM. Mababa lang rin naman ang chance ng ulan sa pag-alis mo at sa pag-uwi mo mamayang 3 PM.",
  "message_source": "ai"
}
```

### English payo out

*Second call: same facts, with `language: "english"`.*

```json
{
  "payo": "Based on the heat level, take extra care and bring water before you leave at 10 AM. The chance of rain is low both when you leave and when you head home at 3 PM.",
  "message_source": "ai"
}
```

---

## Case 08 – Very high rain chance during the return trip

**Scenario:** The chance of rain is very high during the user’s 6 PM trip home.

### Facts in

```json
{
  "city": "Cebu",
  "date": "2026-11-23",
  "language": "taglish",
  "rain_chance_by_hour": [
    {
      "time": "2026-11-23T08:00:00+08:00",
      "chance_percent": 25
    },
    {
      "time": "2026-11-23T12:00:00+08:00",
      "chance_percent": 50
    },
    {
      "time": "2026-11-23T15:00:00+08:00",
      "chance_percent": 75
    },
    {
      "time": "2026-11-23T17:00:00+08:00",
      "chance_percent": 90
    },
    {
      "time": "2026-11-23T18:00:00+08:00",
      "chance_percent": 95
    },
    {
      "time": "2026-11-23T20:00:00+08:00",
      "chance_percent": 85
    }
  ],
  "leave_time": "08:00",
  "rain_chance_at_leave_percent": 25,
  "return_time": "18:00",
  "rain_chance_at_return_percent": 95,
  "heat_level": "OK"
}
```

### Taglish payo out

```json
{
  "payo": "Sobrang taas ng chance umulan sa uwi mo ng 6 PM. Magdala ka ng payong or kapote, at ingat ka sa biyahe pauwi.",
  "message_source": "ai"
}
```

### English payo out

*Second call: same facts, with `language: "english"`.*

```json
{
  "payo": "There’s a very high chance of rain on your way home at 6 PM. Bring an umbrella or raincoat, and take care on your way back.",
  "message_source": "ai"
}
```

---

## Case 09 – Laundry planning

**Scenario:** The user wants to hang laundry. The chance of rain is low late in the morning and higher by mid-afternoon. The activity itself is assumed to be available to the AI outside the contract facts.

### Facts in

```json
{
  "city": "Manila",
  "date": "2026-11-24",
  "language": "taglish",
  "rain_chance_by_hour": [
    {
      "time": "2026-11-24T07:00:00+08:00",
      "chance_percent": 10
    },
    {
      "time": "2026-11-24T09:00:00+08:00",
      "chance_percent": 10
    },
    {
      "time": "2026-11-24T11:00:00+08:00",
      "chance_percent": 15
    },
    {
      "time": "2026-11-24T13:00:00+08:00",
      "chance_percent": 25
    },
    {
      "time": "2026-11-24T15:00:00+08:00",
      "chance_percent": 60
    },
    {
      "time": "2026-11-24T17:00:00+08:00",
      "chance_percent": 75
    }
  ],
  "leave_time": null,
  "rain_chance_at_leave_percent": null,
  "return_time": null,
  "rain_chance_at_return_percent": null,
  "heat_level": "OK"
}
```

### Taglish payo out

```json
{
  "payo": "Pwede kang magsampay ngayong umaga kasi mababa lang ang chance ng ulan ng 11 AM. Kaso tataas ang chance ng ulan bandang 3 PM, kaya kunin mo na yung mga sinampay bago mag-3 PM.",
  "message_source": "ai"
}
```

### English payo out

*Second call: same facts, with `language: "english"`.*

```json
{
  "payo": "You can hang the laundry this morning because the chance of rain around 11 AM is low. But rain becomes more likely around 3 PM, so bring the laundry in before then.",
  "message_source": "ai"
}
```

---

## Case 10 – Farm or outdoor work with later rain

**Scenario:** The user plans to work outdoors or in the field. The chance of rain is low in the morning and higher by 2 PM. The activity itself is assumed to be available to the AI outside the contract facts.

### Facts in

```json
{
  "city": "Cebu",
  "date": "2026-11-25",
  "language": "taglish",
  "rain_chance_by_hour": [
    {
      "time": "2026-11-25T06:00:00+08:00",
      "chance_percent": 10
    },
    {
      "time": "2026-11-25T08:00:00+08:00",
      "chance_percent": 10
    },
    {
      "time": "2026-11-25T10:00:00+08:00",
      "chance_percent": 15
    },
    {
      "time": "2026-11-25T12:00:00+08:00",
      "chance_percent": 20
    },
    {
      "time": "2026-11-25T14:00:00+08:00",
      "chance_percent": 45
    },
    {
      "time": "2026-11-25T16:00:00+08:00",
      "chance_percent": 65
    }
  ],
  "leave_time": null,
  "rain_chance_at_leave_percent": null,
  "return_time": null,
  "rain_chance_at_return_percent": null,
  "heat_level": "OK"
}
```

### Taglish payo out

```json
{
  "payo": "Sulitin mo ang umaga para sa gawain sa bukid o sa labas kasi mababa lang ang chance ng ulan ng 10 AM. Pagdating ng 2 PM, mas tataas ang chance ng ulan, kaya tapusin mo na yung mga gagawin mo bago ang oras na iyon.",
  "message_source": "ai"
}
```

### English payo out

*Second call: same facts, with `language: "english"`.*

```json
{
  "payo": "Make the most of the morning for farm or outdoor work because the chance of rain around 10 AM is low. The chance gets higher by 2 PM, so try to finish your tasks before then.",
  "message_source": "ai"
}
```

---

## Language and tone notes

### Taglish style

- **Conversational, not bulletin-style.** Write as if giving someone a useful reminder. Natural phrasing may include expressions such as *“Based sa heat level,” “need mo,” “okay naman,” “kaso,” “kaya,” “naman,”* and *“yung,”* when they fit the sentence.
- **Work the heat guidance into the sentence.** Avoid treating `Mag-ingat` or `Delikado` as an official label to read aloud. For example, say *“Based sa heat level, need mo mag-ingat”* or *“Based sa heat level, delikado ang init ngayon.”*
- **Use descriptions instead of dashboard statistics.** Prefer *“mababa lang ang chance,” “mataas ang chance,” “mas mababa na lang,”* or *“sobrang taas ng chance”* over listing percentages. Mention a time when it helps the user plan.
- **Give a practical next step.** Examples include bringing an umbrella or raincoat, bringing water, waiting before travelling, taking laundry in, or finishing outdoor tasks earlier.
- **English should sound natural too.** Do not translate the Taglish line word-for-word. Keep the same weather facts and recommendation, but use everyday English.
- **Backup wording follows the same tone.** It may be shorter and simpler, but should still sound helpful and natural in the requested language.
- **Do not make probability sound certain.** A lower chance does not mean there will be no rain. Do not say rain has stopped or will definitely happen based only on probability data.

### Phrase-bank expressions that need additional facts

The current contract does not supply every observation needed for these expressions, so do not use them as factual claims unless the required data is available:

| Expression | Additional information needed |
|---|---|
| “May kinakasal na tikbalang” | A confirmed sunshower |
| “Makulimlim” | An observed cloudy or overcast sky |
| “Umaambon na” / “Umuulan na” | Current observed rainfall, not just rain probability |
| “Tumila na ang ulan” | Confirmation that rain has stopped |
| “Baha na” | Reliable flood information |
| “Maalinsangan” / “Sobrang lagkit” | Humidity or other supporting weather information |
| “Bagyo na naman” | Confirmed typhoon information |

## Validation checklist

- [x] Exactly 10 cases are included and cover the requested scenarios.
- [x] Each input retains the nine existing contract fields and their expected value types.
- [x] Each case includes Taglish and English outputs; the English output is for a second call changing only the language.
- [x] AI payos contain two sentences and use the same facts and recommendations across languages.
- [x] Detailed percentages are kept out of the payo unless a specific implementation requirement calls for them; times are retained where useful.
- [x] Every time mentioned in a payo is supported by that case’s input facts.
- [x] Departure and return probabilities match the hourly entry at the same time.
- [x] Hourly timestamps use ISO 8601 with the `+08:00` offset.
- [x] Missing travel data uses `null`; unavailable hourly data uses `[]`.
- [x] Heat levels use only `OK`, `Mag-ingat`, or `Delikado` and are phrased conversationally.
- [x] No unsupported temperature, humidity, sky-condition, flood, typhoon, road-condition, or official-warning claims are introduced.
- [x] Pending: reviewer sign-off and native-speaker read-through.
