from app.api.weather_api import WeatherAPI
from app.models.weather_model import WeatherData
from app.utils.formatters import celsius_to_fahrenheit
from app.utils.cache import WeatherCache

class WeatherService:
    """Servicio para validar y obtener temperatura de ciudades"""
    
    def __init__(self):
        self.api = WeatherAPI()
        self.cache = WeatherCache(expiration_hours=3)
    
    def validar_temperatura_ciudad(self, nombre_ciudad):
        """
        Valida y obtiene la temperatura de una ciudad.
        
        Pasos: 1) Valida entrada → 2) Obtiene coordenadas → 3) Consulta temperatura
        
        Args:
            nombre_ciudad: Nombre de la ciudad
        
        Returns:
            WeatherData o None si hay error
        """
        # PASO 1: Validación de entrada
        print(f"🔍 Iniciando validación para: '{nombre_ciudad}'")
        
        if nombre_ciudad is None:
            print("❌ Error: El nombre no puede ser None")
            return None
        
        if not isinstance(nombre_ciudad, str):
            print(f"❌ Error: Debe ser texto, recibí: {type(nombre_ciudad).__name__}")
            return None
        
        nombre_ciudad = nombre_ciudad.strip()
        
        if len(nombre_ciudad) == 0:
            print("❌ Error: El nombre no puede estar vacío")
            return None
        
        if len(nombre_ciudad) < 2:
            print("❌ Error: Nombre demasiado corto (mínimo 2 caracteres)")
            return None
        
        if nombre_ciudad.isdigit():
            print("❌ Error: El nombre no puede ser solo números")
            return None
        
        print("✅ Validación exitosa")
        
        # Verificar si hay datos en caché
        cached_data = self.cache.get(nombre_ciudad)
        if cached_data:
            print("💾 Datos obtenidos del caché (actualizados hace menos de 3 horas)")
            return cached_data
        
        # PASO 2: Obtener coordenadas
        print(f"🌍 Buscando coordenadas de '{nombre_ciudad}'...")
        lat, lon, nombre_oficial = self.api.get_coordinates(nombre_ciudad)
        
        if lat is None:
            print(f"❌ No se encontró la ciudad '{nombre_ciudad}'")
            print("   Sugerencia: Verifica la ortografía")
            return None
        
        print(f"✅ Coordenadas: ({lat}, {lon})")
        
        # PASO 3: Obtener temperatura
        print("🌡️  Obteniendo temperatura...")
        temp_celsius, timestamp = self.api.get_weather(lat, lon)
        
        if temp_celsius is None:
            print("❌ No se pudo obtener la temperatura")
            return None
        
        temp_fahrenheit = celsius_to_fahrenheit(temp_celsius)
        
        print(f"✅ Temperatura: {temp_celsius}°C / {temp_fahrenheit:.1f}°F")
        
        # Crear objeto WeatherData
        weather_data = WeatherData(nombre_oficial, temp_celsius, temp_fahrenheit, lat, lon, timestamp)
        
        # Almacenar en caché
        self.cache.set(nombre_ciudad, weather_data)
        print("💾 Datos almacenados en caché (válidos por 3 horas)")
        
        return weather_data
