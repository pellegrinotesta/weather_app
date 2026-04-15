import requests

def get_coordinates(city_name):
    """Trasforma il nome città in Latitudine e Longitudine."""
    GEO_URL = "https://geocoding-api.open-meteo.com/v1/search"
    params = {"name": city_name, "count": 1, "language": "it"}
    response = requests.get(GEO_URL, params=params, timeout=5)
    response.raise_for_status()
    data = response.json()
    return data["results"][0] if "results" in data else None

def fetch_weather(lat, lon):
    """Recupera i dati meteo correnti includendo vento, umidità e precipitazioni."""
    WEATHER_URL = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "current": ["temperature_2m", "relative_humidity_2m", "wind_speed_10m", "precipitation", "weather_code"],
        "timezone": "auto"
    }
    response = requests.get(WEATHER_URL, params=params, timeout=5)
    response.raise_for_status()
    return response.json()["current"]

def fetch_5_day_forecast(lat, lon):
    """Recupera le previsioni giornaliere per i prossimi 5 giorni."""
    WEATHER_URL = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "daily": ["temperature_2m_max", "temperature_2m_min", "weather_code"],
        "timezone": "auto",
        "forecast_days": 5
    }
    response = requests.get(WEATHER_URL, params=params, timeout=5)
    response.raise_for_status()
    return response.json()["daily"]

