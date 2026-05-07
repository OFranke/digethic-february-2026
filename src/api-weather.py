import requests
import json

LATITUDE = 52.5244
LONGITUDE = 13.4105
LOCATION_NAME = "Berlin"

forecast_url = "https://api.open-meteo.com/v1/forecast"

forecast_params = {
    "latitude": LATITUDE,
    "longitude": LONGITUDE,
    "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum",
    "timezone": "Europe/Berlin",
    "forecast_days": 5,
}

print(f"Aufgabe 1.2: Wettervorhersage für {LOCATION_NAME}:")

browser_url = f"{forecast_url}?latitude={LATITUDE}&longitude={LONGITUDE}&daily={forecast_params['daily']}&timezone={forecast_params['timezone']}&forecast_days={forecast_params['forecast_days']}"
print(f"\nBrowser-URL:\n{browser_url}\n")

response = requests.get(forecast_url, params=forecast_params)

if response.status_code == 200:
    data = response.json()

    daily = data.get("daily", {})
    dates = daily.get("time", [])
    max_temps = daily.get("temperature_2m_max", [])
    min_temps = daily.get("temperature_2m_min", [])
    precipitation = daily.get("precipitation_sum", [])

    for i in range(len(dates)):
        print(f"Datum: {dates[i]}")
        print(f"  Max Temperatur: {max_temps[i]}°C")
        print(f"  Min Temperatur: {min_temps[i]}°C")
        print(f"  Niederschlag: {precipitation[i]} mm")
        print()
else:
    print(f"Fehler bei der API-Anfrage: {response.status_code}")
    print(response.text)

print("Aufgabe 1.3: Wetterdaten für den 08. März 2019")

historical_url = "https://archive-api.open-meteo.com/v1/archive"

historical_params = {
    "latitude": LATITUDE,
    "longitude": LONGITUDE,
    "start_date": "2019-03-08",
    "end_date": "2019-03-08",
    "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum",
    "timezone": "Europe/Berlin",
}

# Browser-URL zum manuellen Testen:
historical_browser_url = f"{historical_url}?latitude={LATITUDE}&longitude={LONGITUDE}&start_date={historical_params['start_date']}&end_date={historical_params['end_date']}&daily={historical_params['daily']}&timezone={historical_params['timezone']}"
print(f"\nBrowser-URL:\n{historical_browser_url}\n")

# API-Anfrage durchführen
response = requests.get(historical_url, params=historical_params)

if response.status_code == 200:
    data = response.json()

    print(f"Wetterdaten für {LOCATION_NAME} am 08. März 2019:")

    daily = data.get("daily", {})
    dates = daily.get("time", [])
    max_temps = daily.get("temperature_2m_max", [])
    min_temps = daily.get("temperature_2m_min", [])
    precipitation = daily.get("precipitation_sum", [])

    if dates:
        print(f"Datum: {dates[0]}")
        print(f"  Max Temperatur: {max_temps[0]}°C")
        print(f"  Min Temperatur: {min_temps[0]}°C")
        print(f"  Niederschlag: {precipitation[0]} mm")

    print("\nVollständige API-Response (JSON):")
    print(json.dumps(data, indent=2))
else:
    print(f"Fehler bei der API-Anfrage: {response.status_code}")
    print(response.text)
