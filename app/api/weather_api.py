import requests
import json
from config import GEOCODING_API_URL, WEATHER_API_URL

class WeatherAPI:
    """Cliente para interactuar con las APIs de Open-Meteo"""
    
    @staticmethod
    def get_coordinates(city):
        """
        Obtiene latitud y longitud de una ciudad.
        Returns: (latitude, longitude, official_name) o (None, None, None) si hay error
        """
        try:
            response = requests.get(
                GEOCODING_API_URL,
                params={"name": city, "count": 1, "language": "es"},
                timeout=10
            )
            
            if response.status_code != 200:
                print(f"❌ Error: API respondió con código {response.status_code}")
                return None, None, None
            
            data = response.json()
            
            if "results" not in data or not data["results"]:
                return None, None, None
            
            result = data["results"][0]
            return result["latitude"], result["longitude"], result.get("name", city)
            
        except requests.exceptions.Timeout:
            print("❌ Error: Petición tardó demasiado (timeout)")
            return None, None, None
        except requests.exceptions.ConnectionError:
            print("❌ Error: No se pudo conectar a la API")
            return None, None, None
        except (json.JSONDecodeError, KeyError, IndexError, TypeError) as e:
            print(f"❌ Error: Datos inválidos: {e}")
            return None, None, None
    
    @staticmethod
    def get_weather(latitude, longitude):
        """
        Obtiene temperatura actual usando coordenadas.
        Returns: (temperature, timestamp) o (None, None) si hay error
        """
        try:
            response = requests.get(
                WEATHER_API_URL,
                params={
                    "latitude": latitude,
                    "longitude": longitude,
                    "current_weather": True,
                    "temperature_unit": "celsius"
                },
                timeout=10
            )
            
            if response.status_code != 200:
                print(f"❌ Error: API del clima respondió con código {response.status_code}")
                return None, None
            
            data = response.json()
            
            if "current_weather" not in data:
                print("❌ Error: No hay datos del clima actual")
                return None, None
            
            current = data["current_weather"]
            temperature = current.get("temperature")
            timestamp = current.get("time", "N/A")
            
            if temperature is None:
                return None, None
            
            return temperature, timestamp
            
        except requests.exceptions.Timeout:
            print("❌ Error: Petición tardó demasiado (timeout)")
            return None, None
        except requests.exceptions.ConnectionError:
            print("❌ Error: No se pudo conectar a la API del clima")
            return None, None
        except (json.JSONDecodeError, KeyError, TypeError) as e:
            print(f"❌ Error: Datos inválidos: {e}")
            return None, None
