# Open-Meteo Weather Data Documentation

## 1. API Overview

This project uses the **Open-Meteo Forecast API** to retrieve weather forecast information for three cities in the Philippines: Manila, Cebu, and Davao.

The API provides hourly and daily weather information in JSON format. The TypeScript implementation uses the `openmeteo` package and its `fetchWeatherApi()` function to retrieve and process the forecast data.

| Item | Details |
|---|---|
| API Provider | Open-Meteo |
| API Name | Forecast API |
| API Endpoint | `https://api.open-meteo.com/v1/forecast` |
| HTTP Method | GET |
| Response Format | JSON |
| Timezone | Asia/Manila (UTC+8) |
| Forecast Duration | 7 days |
| TypeScript Package | `openmeteo` |

## 2. API Request Parameters

The API request uses the following parameters:

| Parameter | Description |
|---|---|
| `latitude` | Latitude coordinate of the selected city |
| `longitude` | Longitude coordinate of the selected city |
| `hourly` | List of weather variables requested for hourly forecasts |
| `daily` | List of weather variables requested for daily forecasts |
| `timezone` | Sets the forecast time to the Asia/Manila timezone |
| `forecast_days` | Sets the forecast duration to 7 days |

### API Endpoint and URL Format

The base API endpoint is:

```text
https://api.open-meteo.com/v1/forecast
```

The request URL follows this format:

```text
https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly={hourly_variables}&daily={daily_variables}&timezone=Asia%2FManila&forecast_days=7
```

The latitude and longitude values change depending on the selected city. The hourly and daily variables are passed through the TypeScript `params` object.

### Forecast Locations

The following coordinates are used for the city requests:

| City | Latitude | Longitude |
|---|---:|---:|
| Manila | 14.6042 | 120.9822 |
| Cebu | 10.3167 | 123.8907 |
| Davao | 7.1907 | 125.4553 |

**Note:** The Davao coordinates above are from the earlier Davao API request. The current `davao.ts` script needs to be updated because it currently contains Cebu's coordinates.

## 3. Hourly Weather Variables

The hourly forecast provides weather information for each hour of the forecast period.

| Field | Description | Unit |
|---|---|---|
| `time` | Date and time of the hourly forecast | ISO 8601 |
| `temperature_2m` | Air temperature measured at 2 meters above ground | °C |
| `apparent_temperature` | Feels-like temperature experienced by people | °C |
| `precipitation_probability` | Probability of precipitation during the preceding hour | % |
| `weather_code` | Numeric code representing the weather condition | WMO code |
| `relative_humidity_2m` | Relative humidity measured at 2 meters above ground | % |
| `dew_point_2m` | Dew point temperature measured at 2 meters | °C |
| `showers` | Amount of convective showers during the preceding hour | mm |
| `pressure_msl` | Atmospheric pressure adjusted to mean sea level | hPa |
| `soil_temperature_54cm` | Soil temperature at 54 cm depth | °C |
| `soil_temperature_18cm` | Soil temperature at 18 cm depth | °C |
| `soil_temperature_6cm` | Soil temperature at 6 cm depth | °C |
| `soil_temperature_0cm` | Temperature at the soil or surface level | °C |
| `soil_moisture_0_to_1cm` | Soil water content at 0–1 cm depth | m³/m³ |
| `soil_moisture_1_to_3cm` | Soil water content at 1–3 cm depth | m³/m³ |
| `soil_moisture_3_to_9cm` | Soil water content at 3–9 cm depth | m³/m³ |
| `soil_moisture_9_to_27cm` | Soil water content at 9–27 cm depth | m³/m³ |
| `soil_moisture_27_to_81cm` | Soil water content at 27–81 cm depth | m³/m³ |
| `wind_gusts_10m` | Maximum wind gust speed at 10 meters | km/h |
| `wind_speed_10m` | Wind speed measured at 10 meters | km/h |
| `precipitation` | Total precipitation, including rain, showers, and snow | mm |
| `rain` | Amount of rainfall during the preceding hour | mm |
| `visibility` | Estimated horizontal viewing distance | m |
| `cloud_cover_low` | Percentage of the sky covered by low-level clouds | % |
| `wind_direction_10m` | Wind direction measured at 10 meters | ° |
| `cloud_cover` | Percentage of the sky covered by clouds | % |
| `evapotranspiration` | Estimated water loss through evaporation and plant transpiration | mm |
| `et0_fao_evapotranspiration` | Reference evapotranspiration based on the FAO method | mm |
| `vapour_pressure_deficit` | Difference between the amount of moisture the air can hold and the amount it contains | kPa |
| `surface_pressure` | Atmospheric pressure measured at the surface | hPa |

## 4. Daily Weather Variables

The daily forecast provides summarized weather information for each forecast date.

| Field | Description | Unit |
|---|---|---|
| `time` | Date of the daily forecast | ISO 8601 |
| `temperature_2m_max` | Maximum air temperature for the day at 2 meters | °C |
| `temperature_2m_min` | Minimum air temperature for the day at 2 meters | °C |
| `uv_index_max` | Maximum ultraviolet index for the day | UV Index |
| `uv_index_clear_sky_max` | Maximum ultraviolet index assuming clear-sky conditions | UV Index |

## 5. Timezone and Forecast Duration

All city forecasts should use the Philippine timezone:

```text
Asia/Manila
```

The forecast period is set to 7 days.

The following parameters should be included in each TypeScript `params` object:

```typescript
timezone: "Asia/Manila",
forecast_days: 7,
```

Using the Philippine timezone ensures that the hourly forecast timestamps correspond to local Philippine time.

## 6. Saved Sample Forecast Files

The retrieved forecast responses are stored in the following directory:

```text
backend/
└── data/
    └── samples/
        ├── manila.json
        ├── cebu.json
        └── davao.json
```

Each sample file contains:

- Location metadata, including latitude, longitude, and elevation.
- Hourly weather forecast data.
- Daily weather forecast data.
- Units for the requested hourly and daily variables.
- Forecast timestamps.

Each 7-day sample is expected to contain 168 hourly entries and 7 daily entries.

## 7. Understanding Weather Codes

The `weather_code` field follows the World Meteorological Organization (WMO) weather interpretation codes.

These numeric codes represent different weather conditions, including:

- Clear sky
- Mainly clear
- Partly cloudy
- Overcast
- Fog
- Drizzle
- Rain
- Snowfall
- Rain showers
- Snow showers
- Thunderstorms

The application can use these codes to identify weather conditions and display the corresponding descriptions and weather icons.

## 8. Important Notes

- Temperature values are measured in degrees Celsius.
## Notes

- Precipitation probability is represented as a percentage.
- Wind speed and wind gust values are measured in kilometers per hour.
- Precipitation, rain, and showers are measured in millimeters.
- Visibility is measured in meters.
- Soil moisture is represented as a volumetric ratio in m³/m³.
- Weather codes follow WMO interpretation codes.
- Weather forecasts may change whenever the API is requested again.
- The saved JSON files serve as sample forecast responses for local development and testing.
- The API response latitude and longitude may differ slightly from the requested coordinates because the response identifies the weather grid location used.

## PostgreSQL Database Plan

### Overview

The Philippine Advisory Weather Application uses PostgreSQL to store city information and weather forecasts.

The database contains two main tables:

1. cities
2. forecasts

### Database Relationship

One city can have multiple forecast records.

cities (1) ---- (many) forecasts

The forecasts.city_id column references cities.id.

### Table 1: cities

Stores information about Philippine cities.

| Column | Data Type | Constraints |
|---|---|---|
| id | VARCHAR(50) | PRIMARY KEY, NOT NULL |
| name | VARCHAR(100) | NOT NULL |
| province | VARCHAR(100) | NOT NULL |
| region | VARCHAR(100) | NOT NULL |
| postal_code | VARCHAR(10) | NOT NULL |
| latitude | NUMERIC(9,6) | NOT NULL |
| longitude | NUMERIC(9,6) | NOT NULL |
| timezone | VARCHAR(50) | NOT NULL |

### Table 2: forecasts

Stores weather forecast records for each city.

| Column | Data Type | Constraints |
|---|---|---|
| id | BIGINT | PRIMARY KEY, GENERATED BY DEFAULT AS IDENTITY |
| city_id | VARCHAR(50) | FOREIGN KEY, NOT NULL |
| forecast_time | TIMESTAMPTZ | NOT NULL |
| temperature | NUMERIC(5,2) | NOT NULL |
| feels_like | NUMERIC(5,2) | NOT NULL |
| rain_chance | SMALLINT | NOT NULL, CHECK (0-100) |
| weather_code | SMALLINT | NOT NULL |
| fetched_at | TIMESTAMPTZ | NOT NULL, DEFAULT CURRENT_TIMESTAMP |

### Relationships and Constraints

- cities.id is the primary key of the cities table.
- forecasts.id is the primary key of the forecasts table.
- forecasts.city_id references cities.id.
- One city can have multiple forecast records.
- rain_chance must be between 0 and 100.
- fetched_at automatically records when the forecast is inserted.

### Notes

- City IDs are stored as VARCHAR(50).
- Temperature values use NUMERIC(5,2).
- Forecast timestamps use TIMESTAMPTZ.
- Database credentials and passwords must not be committed to the repository.

## 9. References

Open-Meteo Forecast API Documentation:

https://open-meteo.com/en/docs

WMO Weather Interpretation Codes:

https://open-meteo.com/en/docs#weathervariables
