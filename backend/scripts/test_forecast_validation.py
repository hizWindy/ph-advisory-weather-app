
from fetch_forecast import validate_forecast

# Simulated forecast data with an invalid rain probability
test_data = {
    "time": ["2026-11-14T00:00"],
    "temperature_2m": [27],
    "precipitation_probability": [120]
}

# Run validation
warnings = validate_forecast(test_data)

# Display results
if warnings:
    print("FORECAST WARNINGS:")

    for warning in warnings:
        print(f"WARNING: {warning}")
else:
    print("Validation successful. No warnings found.")
