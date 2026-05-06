import requests

LATITUDE = 51.607
LONGITUDE = 13.3124

forecast_url = "https://api.open-meteo.com/v1/forecast"

parameters = {
    "latitude": LATITUDE,
    "longitude": LONGITUDE,
    "daily": "temperature_2m_max,temperature_2m_min",
    "timezone": "Europe/Berlin",
    "forecast_days": 7,
}


response = requests.get(forecast_url, params=parameters)

print(response)
if response.status_code == 200:
    data = response.json()

    print(data)
    daily = data.get("daily", {})
    dates = daily.get("time", [])
    max_temps = daily.get("temperature_2m_max", [])
    min_temps = daily.get("temperature_2m_min", [])

    for i in range(len(dates)):
        print(f"Datum: {dates[i]}")
        print(f"  Max Temperatur: {max_temps[i]}°C")
        print(f"  Min Temperatur: {min_temps[i]}°C")
        print()
