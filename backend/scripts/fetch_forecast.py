
import argparse
import json
import math
from pathlib import Path
from typing import Any

import httpx


# Project paths
BACKEND_DIR = Path(__file__).resolve().parents[1]
CITY_LIST_PATH = BACKEND_DIR / "data" / "cities.json"

# Open-Meteo API
API_URL = "https://api.open-meteo.com/v1/forecast"

HOURLY_FIELDS = [
    "temperature_2m",
    "precipitation_probability",
]


def get_city_by_id(city_id: str) -> dict[str, Any] | None:
    """Find a city in cities.json using its ID."""

    with CITY_LIST_PATH.open("r", encoding="utf-8") as file:
        cities = json.load(file)

    if not isinstance(cities, list):
        raise ValueError("cities.json must contain a JSON array.")

    for city in cities:
        if isinstance(city, dict) and city.get("id") == city_id:
            return city

    return None


def fetch_forecast(city: dict[str, Any]) -> dict[str, Any]:
    """Fetch seven days of hourly forecast data from Open-Meteo."""

    params = {
        "latitude": city["latitude"],
        "longitude": city["longitude"],
        "hourly": ",".join(HOURLY_FIELDS),
        "forecast_days": 7,
        "timezone": city["timezone"],
    }

    response = httpx.get(
        API_URL,
        params=params,
        timeout=20.0,
    )

    response.raise_for_status()

    data = response.json()

    if not isinstance(data, dict):
        raise ValueError("Unexpected API response format.")

    hourly = data.get("hourly")

    if not isinstance(hourly, dict):
        raise ValueError("API response does not contain hourly forecast data.")

    return hourly


def validate_forecast(hourly: dict[str, Any]) -> list[str]:
    """Check for missing and out-of-range forecast values."""

    warnings = []

    times = hourly.get("time")
    temperatures = hourly.get("temperature_2m")
    rain_probabilities = hourly.get("precipitation_probability")

    arrays = {
        "time": times,
        "temperature_2m": temperatures,
        "precipitation_probability": rain_probabilities,
    }

    for field, values in arrays.items():
        if not isinstance(values, list):
            warnings.append(f"Missing or invalid {field} array.")

    # Use empty lists for safe validation and printing.
    if not isinstance(times, list):
        times = []

    if not isinstance(temperatures, list):
        temperatures = []

    if not isinstance(rain_probabilities, list):
        rain_probabilities = []

    if not times:
        warnings.append("Forecast time array is empty.")

    # Check that all hourly arrays have matching lengths.
    for field, values in [
        ("temperature_2m", temperatures),
        ("precipitation_probability", rain_probabilities),
    ]:
        if len(values) != len(times):
            warnings.append(
                f"{field} has {len(values)} values, "
                f"but time has {len(times)} values."
            )

    for index, hour in enumerate(times):

        if not isinstance(hour, str) or not hour.strip():
            warnings.append(f"Missing or empty forecast hour at index {index}.")

        # Validate temperature.
        if index >= len(temperatures) or temperatures[index] is None:
            warnings.append(f"Missing temperature at index {index}.")

        elif (
            isinstance(temperatures[index], bool)
            or not isinstance(temperatures[index], (int, float))
            or not math.isfinite(temperatures[index])
        ):
            warnings.append(f"Invalid temperature at index {index}.")

        # Validate rain probability.
        if index >= len(rain_probabilities):
            warnings.append(f"Missing rain probability at index {index}.")

        else:
            rain = rain_probabilities[index]

            if rain is None:
                warnings.append(f"Missing rain probability at index {index}.")

            elif (
                isinstance(rain, bool)
                or not isinstance(rain, (int, float))
                or not math.isfinite(rain)
            ):
                warnings.append(f"Invalid rain probability at index {index}.")

            elif not 0 <= rain <= 100:
                warnings.append(
                    f"Rain probability out of range at index {index}: {rain}%."
                )

    return warnings


def format_value(value: Any, unit: str) -> str:
    """Format a forecast value safely for display."""

    if (
        value is None
        or isinstance(value, bool)
        or not isinstance(value, (int, float))
        or not math.isfinite(value)
    ):
        return "N/A"

    return f"{value:g}{unit}"


def print_forecast(city: dict[str, Any], hourly: dict[str, Any]) -> None:
    """Print hourly forecast data grouped by date."""

    times = hourly.get("time", [])
    temperatures = hourly.get("temperature_2m", [])
    rain_probabilities = hourly.get("precipitation_probability", [])

    print("\n" + "=" * 55)
    print("SEVEN-DAY WEATHER FORECAST")
    print("=" * 55)

    print(f"City: {city['name']}")
    print(f"City ID: {city['id']}")
    print(f"Timezone: {city['timezone']}")
    print(f"Forecast entries: {len(times)}")

    if not times:
        print("\nNo hourly forecast entries available.")
        return

    current_date = None

    for index, timestamp in enumerate(times):

        if isinstance(timestamp, str) and timestamp.strip():
            forecast_date = timestamp[:10]
            forecast_hour = timestamp[11:16] if len(timestamp) >= 16 else timestamp
        else:
            forecast_date = "Unknown date"
            forecast_hour = "Missing hour"

        if forecast_date != current_date:
            print(f"\nDate: {forecast_date}")
            print("-" * 55)
            current_date = forecast_date

        temperature = (
            temperatures[index] if index < len(temperatures) else None
        )

        rain = (
            rain_probabilities[index]
            if index < len(rain_probabilities)
            else None
        )

        print(
            f"{forecast_hour} | "
            f"Temperature: {format_value(temperature, '°C')} | "
            f"Rain chance: {format_value(rain, '%')}"
        )

    print("\n" + "=" * 55)


def main() -> int:
    """Run the forecast script."""

    parser = argparse.ArgumentParser(
        description="Fetch and validate a city's seven-day weather forecast."
    )

    parser.add_argument(
        "city_id",
        help="City ID from backend/data/cities.json",
    )

    args = parser.parse_args()

    try:
        city = get_city_by_id(args.city_id)

        if city is None:
            print(f"ERROR: City with ID '{args.city_id}' was not found.")
            return 1

        # Validate required city information.
        for field in ("latitude", "longitude", "timezone"):
            if field not in city or city[field] is None:
                raise ValueError(
                    f"City '{args.city_id}' is missing required field: {field}"
                )

        print(f"Fetching forecast for {city['name']}...")

        hourly = fetch_forecast(city)

        warnings = validate_forecast(hourly)

        print_forecast(city, hourly)

        if warnings:
            print("\nFORECAST WARNINGS:")

            for warning in warnings:
                print(f"WARNING: {warning}")

        else:
            print("\nValidation successful. No warnings found.")

        return 0

    except httpx.HTTPStatusError as error:
        print(
            f"API ERROR: HTTP {error.response.status_code} "
            f"- {error}"
        )
        return 1

    except httpx.RequestError as error:
        print(f"NETWORK ERROR: {error}")
        return 1

    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(f"ERROR: {error}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
