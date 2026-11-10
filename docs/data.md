# Open-Meteo Weather Data Documentation

## 1. API Overview

This project uses the **Open-Meteo Forecast API** to retrieve weather forecast data for three major cities in the Philippines: Manila, Cebu, and Davao.

The API provides hourly and daily weather information in JSON format.

- **API Provider:** Open-Meteo
- **API Endpoint:** `https://api.open-meteo.com/v1/forecast`
- **HTTP Method:** GET
- **Response Format:** JSON
- **Timezone:** Asia/Manila
- **Forecast Duration:** 7 days

## 2. API Parameters

| Parameter | Description |
|---|---|
| `latitude` | Latitude of the selected city |
| `longitude` | Longitude of the selected city |
| `hourly` | Requests hourly weather information |
| `daily` | Requests daily weather information |
| `timezone` | Sets the forecast timezone to Asia/Manila |
| `forecast_days` | Sets the forecast duration to 7 days |

### Requested Hourly Variables

- `temperature_2m` – Air temperature measured at 2 meters above ground.
- `apparent_temperature` – Feels-like temperature.
- `precipitation_probability` – Probability of precipitation.
- `weather_code` – Weather condition represented by a WMO weather code.

### Requested Daily Variables

- `temperature_2m_max` – Maximum temperature for the day.
- `temperature_2m_min` – Minimum temperature for the day.

## 3. Sample Locations

The following coordinates were used in the saved sample responses:

| City | Latitude | Longitude |
|---|---:|---:|
| Manila | 14.586995 | 121.002785 |
| Cebu | 10.298770 | 123.848860 |
| Davao | 7.205624 | 125.482230 |

## 4. Data Fields and Units

### Hourly Data

| Field | Description | Unit |
|---|---|---|
| `time` | Date and time of the forecast | ISO 8601 |
| `temperature_2m` | Air temperature at 2 meters | °C |
| `apparent_temperature` | Feels-like temperature | °C |
| `precipitation_probability` | Chance of precipitation | % |
| `weather_code` | Weather condition code | WMO code |

### Daily Data

| Field | Description | Unit |
|---|---|---|
| `time` | Forecast date | ISO 8601 |
| `temperature_2m_max` | Maximum daily temperature | °C |
| `temperature_2m_min` | Minimum daily temperature | °C |

## 5. Sample JSON Files

The API responses are saved locally in the following directory:

```text
backend/
└── data/
    └── samples/
        ├── manila.json
        ├── cebu.json
        └── davao.json
```

Each sample contains:

- 7 days of daily forecast data.
- 168 hourly forecast entries (24 hours × 7 days).
- Hourly temperature, feels-like temperature, precipitation probability, and weather codes.
- Daily maximum and minimum temperatures.

## 6. Weather Code Reference

The `weather_code` field follows the **World Meteorological Organization (WMO) weather interpretation codes**.

These codes represent different weather conditions, such as clear skies, cloudy conditions, fog, drizzle, rain, snow, and thunderstorms.

The application can use these codes to identify and display the corresponding weather condition and icon.

## 7. Notes

- All saved samples use the `Asia/Manila` timezone.
- Temperature values are measured in degrees Celsius.
- Precipitation probability is represented as a percentage.
- The sample JSON files are stored locally for development and testing.
- Weather forecasts may change when the API is requested again.
- The saved JSON files represent sample responses retrieved during development.