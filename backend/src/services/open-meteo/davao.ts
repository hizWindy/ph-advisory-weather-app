import { fetchWeatherApi } from "openmeteo";

const params = {
    latitude: 7.0731,
    longitude: 125.6128,
    daily: ["temperature_2m_max", "temperature_2m_min", "uv_index_max", "uv_index_clear_sky_max"],
    hourly: ["temperature_2m", "apparent_temperature", "precipitation_probability", "weather_code", "relative_humidity_2m", "dew_point_2m", "showers", "pressure_msl", "soil_temperature_54cm", "soil_temperature_18cm", "soil_temperature_6cm", "soil_temperature_0cm", "soil_moisture_0_to_1cm", "soil_moisture_1_to_3cm", "soil_moisture_3_to_9cm", "soil_moisture_9_to_27cm", "soil_moisture_27_to_81cm", "wind_gusts_10m", "wind_speed_10m", "precipitation", "rain", "visibility", "cloud_cover_low", "wind_direction_10m", "cloud_cover", "evapotranspiration", "et0_fao_evapotranspiration", "vapour_pressure_deficit", "surface_pressure"],
};
const url = "https://api.open-meteo.com/v1/forecast";
const responses = await fetchWeatherApi(url, params);

// Process first location. Add a for-loop for multiple locations or weather models
const response = responses[0];

// Attributes for timezone and location
const latitude = response.latitude();
const longitude = response.longitude();
const elevation = response.elevation();
const utcOffsetSeconds = response.utcOffsetSeconds();

console.log(
    `\nCoordinates: ${Math.abs(latitude)}°${latitude < 0 ? 'S' : 'N'} ${Math.abs(longitude)}°${longitude < 0 ? 'W' : 'E'}`,
    `\nElevation: ${elevation}m asl`,
    `\nTimezone difference to GMT+0: ${utcOffsetSeconds}s`,
);

const hourly = response.hourly()!;
const daily = response.daily()!;

// Note: The order of weather variables in the URL query and the indices below need to match!
const weatherData = {
    hourly: {
        time: Array.from(
            { length: (Number(hourly.timeEnd()) - Number(hourly.time())) / hourly.interval() },
            (_, i) => new Date((Number(hourly.time()) + i * hourly.interval() + utcOffsetSeconds) * 1000)
        ),
        temperature_2m: hourly.variables(0)!.valuesArray(),
        apparent_temperature: hourly.variables(1)!.valuesArray(),
        precipitation_probability: hourly.variables(2)!.valuesArray(),
        weather_code: hourly.variables(3)!.valuesArray(),
        relative_humidity_2m: hourly.variables(4)!.valuesArray(),
        dew_point_2m: hourly.variables(5)!.valuesArray(),
        showers: hourly.variables(6)!.valuesArray(),
        pressure_msl: hourly.variables(7)!.valuesArray(),
        soil_temperature_54cm: hourly.variables(8)!.valuesArray(),
        soil_temperature_18cm: hourly.variables(9)!.valuesArray(),
        soil_temperature_6cm: hourly.variables(10)!.valuesArray(),
        soil_temperature_0cm: hourly.variables(11)!.valuesArray(),
        soil_moisture_0_to_1cm: hourly.variables(12)!.valuesArray(),
        soil_moisture_1_to_3cm: hourly.variables(13)!.valuesArray(),
        soil_moisture_3_to_9cm: hourly.variables(14)!.valuesArray(),
        soil_moisture_9_to_27cm: hourly.variables(15)!.valuesArray(),
        soil_moisture_27_to_81cm: hourly.variables(16)!.valuesArray(),
        wind_gusts_10m: hourly.variables(17)!.valuesArray(),
        wind_speed_10m: hourly.variables(18)!.valuesArray(),
        precipitation: hourly.variables(19)!.valuesArray(),
        rain: hourly.variables(20)!.valuesArray(),
        visibility: hourly.variables(21)!.valuesArray(),
        cloud_cover_low: hourly.variables(22)!.valuesArray(),
        wind_direction_10m: hourly.variables(23)!.valuesArray(),
        cloud_cover: hourly.variables(24)!.valuesArray(),
        evapotranspiration: hourly.variables(25)!.valuesArray(),
        et0_fao_evapotranspiration: hourly.variables(26)!.valuesArray(),
        vapour_pressure_deficit: hourly.variables(27)!.valuesArray(),
        surface_pressure: hourly.variables(28)!.valuesArray(),
    },
    daily: {
        time: Array.from(
            { length: (Number(daily.timeEnd()) - Number(daily.time())) / daily.interval() },
            (_, i) => new Date((Number(daily.time()) + i * daily.interval() + utcOffsetSeconds) * 1000)
        ),
        temperature_2m_max: daily.variables(0)!.valuesArray(),
        temperature_2m_min: daily.variables(1)!.valuesArray(),
        uv_index_max: daily.variables(2)!.valuesArray(),
        uv_index_clear_sky_max: daily.variables(3)!.valuesArray(),
    },
};

// The 'weatherData' object now contains a simple structure, with arrays of datetimes and weather information
console.log("\nHourly data:\n", weatherData.hourly)
console.log("\nDaily data:\n", weatherData.daily)
