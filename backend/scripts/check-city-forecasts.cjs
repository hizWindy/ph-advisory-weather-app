
const fs = require("node:fs");
const path = require("node:path");

const citiesPath = path.join(
  __dirname,
  "../data/cities.json"
);

const API_URL = "https://api.open-meteo.com/v1/forecast";

async function checkCity(city) {
  try {
    if (
      !city.id ||
      !city.name ||
      !Number.isFinite(city.latitude) ||
      !Number.isFinite(city.longitude)
    ) {
      throw new Error("Invalid city information");
    }

    const params = new URLSearchParams({
      latitude: String(city.latitude),
      longitude: String(city.longitude),
      timezone: city.timezone || "Asia/Manila",
      current: "temperature_2m,weather_code",
      daily: "weather_code,temperature_2m_max,temperature_2m_min",
      forecast_days: "7"
    });

    const response = await fetch(
      `${API_URL}?${params.toString()}`,
      { signal: AbortSignal.timeout(15000) }
    );

    const data = await response.json();

    if (!response.ok || data.error) {
      throw new Error(
        data.reason || `HTTP ${response.status}`
      );
    }

    if (
      !data.current ||
      !Number.isFinite(data.current.temperature_2m) ||
      !Number.isFinite(data.current.weather_code)
    ) {
      throw new Error("Current weather data missing");
    }

    if (
      !data.daily ||
      !Array.isArray(data.daily.time) ||
      data.daily.time.length === 0 ||
      !Number.isFinite(data.daily.temperature_2m_max?.[0]) ||
      !Number.isFinite(data.daily.temperature_2m_min?.[0])
    ) {
      throw new Error("Daily forecast data missing");
    }

    return {
      success: true,
      city: city.name,
      temperature: data.current.temperature_2m,
      forecastDays: data.daily.time.length
    };

  } catch (error) {
    return {
      success: false,
      city: city.name || city.id || "Unknown",
      error: error.message
    };
  }
}

async function main() {
  try {
    const cities = JSON.parse(
      fs.readFileSync(citiesPath, "utf8")
    );

    if (!Array.isArray(cities) || cities.length === 0) {
      throw new Error("Invalid or empty cities.json");
    }

    console.log("\n===== CITY FORECAST VALIDATION =====");
    console.log(`Total cities: ${cities.length}\n`);

    const results = [];

    for (const city of cities) {
      const result = await checkCity(city);
      results.push(result);

      if (result.success) {
        console.log(
          `[PASS] ${result.city} | ` +
          `${result.temperature}°C | ` +
          `${result.forecastDays} forecast days`
        );
      } else {
        console.log(
          `[FAIL] ${result.city} | ${result.error}`
        );
      }
    }

    const passed = results.filter(r => r.success).length;
    const failed = results.length - passed;

    console.log("\n===== VALIDATION SUMMARY =====");
    console.log(`Total:  ${results.length}`);
    console.log(`Passed: ${passed}`);
    console.log(`Failed: ${failed}`);

    if (failed > 0) {
      console.log("\nFailed cities:");

      results
        .filter(r => !r.success)
        .forEach(r => console.log(
          `- ${r.city}: ${r.error}`
        ));
    }

    if (failed === 0) {
      console.log("\nSUCCESS: All cities returned forecasts!");
    } else {
      console.log("\nSome cities need further checking.");
      process.exitCode = 1;
    }

  } catch (error) {
    console.error("\nVALIDATION ERROR:", error.message);
    process.exitCode = 1;
  }
}

main();
