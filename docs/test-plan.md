Weather App – Test Plan v1

1. Setup Instructions
   
1. Start the Weather App and make sure the API is reachable.
2. Call GET /health and confirm that status is healthy. Check that timestamp and uptime are returned.
3. Call GET /cities and confirm that the response contains a cities list. 
4. Use a valid city's id (for example, manila, cebu, or davao) as the city value in the forecast request.
5. Call GET /forecast?city=manila and check that the response contains the forecast data described below.
Use the agreed API contract in api.md as the source of truth for field names. Forecast numbers must come from the API/application code; AI may explain the numbers but must not invent or change them.

2. Feature Testing
   
Feature 1: 7-Day Forecast

1. Select a city from cities using its id, and confirm the displayed city matches the corresponding name and country.
2. Check that daily.time contains seven dates for the 7-day forecast. Confirm that the displayed dates are in the same order as daily.time.
3. For each date, check that the displayed high and low temperatures match the corresponding values in daily.temperature_2m_max and daily.temperature_2m_min.
4. Check that the displayed UV information matches the corresponding values in daily.uv_index_max.
5. For hourly conditions, check that values are aligned by index with hourly.time and use the correct fields: hourly.temperature_2m, hourly.precipitation_probability, hourly.weather_code, and hourly.wind_speed_10m. Use hourly_units to display the correct units.

Feature 2: Payo for Today
   
1. Check that Payo receives the selected city and requested lang value and that the response's city and language match the request.
2. Check that Payo displays the response's summary in the requested language (for example, fil for Filipino/Taglish as supported by the app, or the agreed English language code).
3. Check that Payo displays advice from recommendations and does not create recommendations unrelated to the returned weather information.
4. Check that Payo's displayed weather highlights match weather_highlights.max_temperature_avg, weather_highlights.min_temperature_avg, weather_highlights.dominant_weather_code, and weather_highlights.rain_probability_peak.
5. Check the rain warning against the forecast's hourly.precipitation_probability values. Payo must only describe rain as likely/high when the value meets the high-rain threshold agreed by the team; do not invent a threshold. Payo must not invent or alter forecast numbers.

Feature 3: Alis-Uwi Rain Planner

1. Check that the planner sends the selected city, leave, return, and lang values to GET /payo as shown in the API contract.
2. Check that the response's travel_window.leave and travel_window.return match the dates selected by the user.
3. Check that the response's language matches the requested lang value.
4. Check that the planner uses recommendations and weather_highlights.rain_probability_peak to explain rain conditions during the selected travel window.
5. Compare its rain advice with the corresponding forecast data in hourly.time and hourly.precipitation_probability; the planner must not claim a high chance of rain when the forecast does not meet the team's agreed threshold.
   
Feature 4: Heat Check

1. Check that the selected date's high and low temperatures match daily.temperature_2m_max and daily.temperature_2m_min.
2. Check that the displayed UV value matches daily.uv_index_max for the same date.
3. Check that temperature and UV values use the units declared in daily_units (including temperature_2m_max, temperature_2m_min, and uv_index_max).
4. Check that heat advice or warnings are shown only when the agreed app rules/thresholds are met by the source weather data.
5. Check that missing temperature or UV data does not cause the app to display invented values or an unsupported heat warning.

3. Contract Fields Referenced by These Checks

1. GET /health: status, timestamp, uptime
2. GET /cities: cities, and each city object's id, name, country, latitude, longitude, timezone, elevation
3. GET /forecast: daily.time, daily.temperature_2m_max, daily.temperature_2m_min, daily.uv_index_max, hourly.time, hourly.temperature_2m, hourly.relative_humidity_2m, hourly.precipitation_probability, hourly.weather_code, hourly.wind_speed_10m, daily_units, hourly_units
4. GET /payo request parameters shown in the example: city, leave, return, lang
5. GET /payo response: city, travel_window.leave, travel_window.return, language, summary, recommendations, weather_highlights.max_temperature_avg, weather_highlights.min_temperature_avg, weather_highlights.dominant_weather_code, weather_highlights.rain_probability_peak

4. Notes / Items to Confirm with the Team

- The GET /forecast example in the supplied api.md screenshot shows only two entries in daily.time, while v1 requires a 7-day forecast. Confirm that the real endpoint returns seven daily entries, or update the API implementation/contract before accepting the 7-day forecast check.
- The supplied contract example shows GET /payo with city, leave, return, and lang. Confirm whether Payo for Today uses the same endpoint without the travel dates, or whether a separate request shape is defined elsewhere.
- The supplied contract does not show a dedicated heat-index field or the numeric thresholds for high heat or high rain probability. Khair, Fredelina, and the feature owners should confirm the app's rules/thresholds. Do not make up these thresholds in testing.
- The sample weather_highlights.rain_probability_peak is formatted as a percentage string (for example, 35%), while hourly.precipitation_probability is shown as numeric percentages. Confirm the agreed comparison/formatting behavior in the implementation.
- The supplied /payo example uses lang=fil and returns Filipino text. Confirm the agreed language code for English and whether fil is the intended code for the app's Taglish option.
  
5. Review Checklist
   
- All four v1 features and the setup steps are covered.
- Each feature owner has read their section.
- Checks use the exact field names from the API contract.
- The team has confirmed the rain and heat thresholds.
- Khair and Fredelina have reviewed the test plan.
