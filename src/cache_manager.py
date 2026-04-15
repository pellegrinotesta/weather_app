import sqlite3
import json
import time
import logging
import pathlib
from .api_client import get_coordinates, fetch_weather
from .utils import interpret_wmo_code

# Assicura che le cartelle esistano
pathlib.Path("data").mkdir(exist_ok=True)
pathlib.Path("logs").mkdir(exist_ok=True)

logging.basicConfig(filename='logs/weather_app.log', level=logging.INFO, format='%(asctime)s - %(message)s')

class WeatherService:
    def __init__(self, db_path="data/weather_cache.db", ttl=3600):
        self.db_path = db_path
        self.ttl = ttl
        self._setup_db()

    def _setup_db(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("CREATE TABLE IF NOT EXISTS cache (city TEXT PRIMARY KEY, data TEXT, ts INTEGER)")

    def get_weather(self, city_name):
        city = city_name.lower().strip()
        now = int(time.time())

        with sqlite3.connect(self.db_path) as conn:
            row = conn.execute("SELECT data, ts FROM cache WHERE city=?", (city,)).fetchone()
            
            if row and (now - row[1]) < self.ttl:
                logging.info(f"CACHE HIT: {city}")
                return json.loads(row[0])

        # Se non c'è cache valida, vai online
        try:
            geo = get_coordinates(city)
            if not geo: return {"error": "Città non trovata"}
            
            w = fetch_weather(geo["latitude"], geo["longitude"])
           # Nel metodo get_weather della classe WeatherService...
            # ... (dopo la chiamata a fetch_weather)
            res = {
                "citta": f"{geo['name']}, {geo.get('country', '')}",
                "temp": w["temperature_2m"],
                "umidita": w["relative_humidity_2m"],
                "vento": w["wind_speed_10m"],
                "precipitazioni": w["precipitation"], # <-- Nuovo campo
                "desc": interpret_wmo_code(w["weather_code"])
            }
            
            with sqlite3.connect(self.db_path) as conn:
                conn.execute("INSERT OR REPLACE INTO cache VALUES (?, ?, ?)", (city, json.dumps(res), now))
            
            logging.info(f"API FETCH: {city}")
            return res
        except Exception as e:
            logging.error(f"ERRORE: {e}")
            return {"error": "Impossibile recuperare i dati"}