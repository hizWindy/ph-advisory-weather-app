
### Endpoint: GET /health

{
  "status": "healthy",
  "timestamp": "2026-11-13T22:26:00Z",
  "uptime": 3600
}

###Endpoint: GET /cities

{
  "cities": [
    {
      "id": "manila",
      "name": "Manila",
      "country": "Philippines",
      "latitude": 14.6042,
      "longitude": 120.9822,
      "timezone": "Asia/Manila",
      "elevation": 10.0
    },
    {
      "id": "cebu",
      "name": "Cebu",
      "country": "Philippines",
      "latitude": 10.3167,
      "longitude": 123.8907,
      "timezone": "Asia/Manila",
      "elevation": 14.0
    },
    {
      "id": "davao",
      "name": "Davao",
      "country": "Philippines",
      "latitude": 7.1907,
      "longitude": 125.4553,
      "timezone": "Asia/Manila",
      "elevation": 20.0
    }
  ]
}

###Endpoint: GET /forecast

GET /forecast?city=manila

{
  "latitude": 14.6042,
  "longitude": 120.9822,
  "generationtime_ms": 0.1234,
  "utc_offset_seconds": 28800,
  "timezone": "Asia/Manila",
  "timezone_abbreviation": "PST",
  "elevation": 10.0,
  "hourly_units": {
    "time": "iso8601",
    "temperature_2m": "°C",
    "relative_humidity_2m": "%",
    "precipitation_probability": "%",
    "weather_code": "WMO code",
    "wind_speed_10m": "km/h"
  },
  "hourly": {
    "time": [
      "2026-11-13T00:00",
      "2026-11-13T01:00",
      "2026-11-13T02:00"
    ],
    "temperature_2m": [28.5, 27.9, 27.4],
    "relative_humidity_2m": [78, 82, 85],
    "precipitation_probability": [10, 15, 20],
    "weather_code": [1, 2, 3],
    "wind_speed_10m": [12.5, 10.1, 9.4]
  },
    "daily_units": {
    "time": "iso8601",
    "temperature_2m_max": "°C",
    "temperature_2m_min": "°C",
    "uv_index_max": "UV Index"
  },
  "daily": {
    "time": [
      "2026-11-13",
      "2026-11-14"
    ],
    "temperature_2m_max": [32.1, 31.5],
    "temperature_2m_min": [25.0, 24.8],
    "uv_index_max": [8.5, 7.9]
  }
}

###Endpoint: GET /payo

GET /payo?city=manila&leave=2026-11-15&return=2026-11-18&lang=fil

{
  "city": "Manila",
  "travel_window": {
    "leave": "2026-11-15",
    "return": "2026-11-18"
  },
  "language": "fil",
  "summary": "Inaasahan ang maulap na kalangitan na may bahagyang pag-ulan sa ilang araw. Magdala ng payong.",
  "recommendations": [
    "Magdala ng payong o kapote dahil may tsansa ng pag-ulan sa hapon.",
    "Ang temperatura ay aabot sa 32°C, kaya magsuot ng magagaang kasuotan.",
    "Mabuti ang kondisyon para sa paglalakbay sa labas tuwing umaga."
  ],
  "weather_highlights": {
    "max_temperature_avg": 31.8,
    "min_temperature_avg": 25.2,
    "dominant_weather_code": 2,
    "rain_probability_peak": "35%"
  }
}





