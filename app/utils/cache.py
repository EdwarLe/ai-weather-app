import time
import json

class WeatherCache:
    """Sistema de caché para almacenar datos del clima con expiración de 3 horas"""
    
    def __init__(self, expiration_hours=3):
        self.cache = {}
        self.expiration_seconds = expiration_hours * 3600
    
    def _get_cache_key(self, city_name):
        """Genera una clave única para la ciudad (normalizada)"""
        return city_name.lower().strip()
    
    def get(self, city_name):
        """
        Obtiene datos del caché si existen y no han expirado.
        Returns: WeatherData o None si no existe o expiró
        """
        key = self._get_cache_key(city_name)
        
        if key not in self.cache:
            return None
        
        cached_data = self.cache[key]
        current_time = time.time()
        
        # Verificar si el caché expiró
        if current_time - cached_data['timestamp'] > self.expiration_seconds:
            del self.cache[key]
            return None
        
        return cached_data['data']
    
    def set(self, city_name, weather_data):
        """Almacena datos del clima en el caché con timestamp actual"""
        key = self._get_cache_key(city_name)
        self.cache[key] = {
            'data': weather_data,
            'timestamp': time.time()
        }
    
    def clear_expired(self):
        """Limpia todas las entradas expiradas del caché"""
        current_time = time.time()
        expired_keys = [
            key for key, value in self.cache.items()
            if current_time - value['timestamp'] > self.expiration_seconds
        ]
        
        for key in expired_keys:
            del self.cache[key]
        
        return len(expired_keys)
    
    def clear_all(self):
        """Limpia todo el caché"""
        count = len(self.cache)
        self.cache.clear()
        return count
    
    def get_stats(self):
        """Obtiene estadísticas del caché"""
        return {
            'total_entries': len(self.cache),
            'cities': list(self.cache.keys())
        }
