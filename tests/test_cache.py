import unittest
import time
from app.utils.cache import WeatherCache
from app.models.weather_model import WeatherData

class TestWeatherCache(unittest.TestCase):
    """Tests para el sistema de caché"""
    
    def setUp(self):
        """Configuración antes de cada test"""
        self.cache = WeatherCache(expiration_hours=3)
        self.sample_data = WeatherData("Madrid", 22.5, 72.5, 40.4165, -3.70256, "2024-03-25T10:00")
    
    def test_cache_set_and_get(self):
        """Test: Almacenar y recuperar datos del caché"""
        self.cache.set("Madrid", self.sample_data)
        result = self.cache.get("Madrid")
        
        self.assertIsNotNone(result)
        self.assertEqual(result.city, "Madrid")
        self.assertEqual(result.temperature_celsius, 22.5)
    
    def test_cache_key_normalization(self):
        """Test: Las claves se normalizan (mayúsculas/minúsculas y espacios)"""
        self.cache.set("Madrid", self.sample_data)
        
        # Debe encontrar con diferentes formatos
        self.assertIsNotNone(self.cache.get("madrid"))
        self.assertIsNotNone(self.cache.get("MADRID"))
        self.assertIsNotNone(self.cache.get("  Madrid  "))
    
    def test_cache_miss(self):
        """Test: Retorna None cuando no existe la ciudad en caché"""
        result = self.cache.get("Barcelona")
        self.assertIsNone(result)
    
    def test_cache_expiration(self):
        """Test: Los datos expiran después del tiempo configurado"""
        # Crear caché con expiración de 1 segundo para testing
        cache = WeatherCache(expiration_hours=1/3600)  # 1 segundo
        cache.set("Madrid", self.sample_data)
        
        # Debe existir inmediatamente
        self.assertIsNotNone(cache.get("Madrid"))
        
        # Esperar 2 segundos
        time.sleep(2)
        
        # Debe haber expirado
        self.assertIsNone(cache.get("Madrid"))
    
    def test_clear_expired(self):
        """Test: Limpiar entradas expiradas"""
        cache = WeatherCache(expiration_hours=1/3600)  # 1 segundo
        
        cache.set("Madrid", self.sample_data)
        cache.set("Barcelona", self.sample_data)
        
        time.sleep(2)
        
        # Agregar una entrada nueva que no debe expirar
        cache.set("Paris", self.sample_data)
        
        # Limpiar expiradas
        expired_count = cache.clear_expired()
        
        self.assertEqual(expired_count, 2)
        self.assertIsNone(cache.get("Madrid"))
        self.assertIsNone(cache.get("Barcelona"))
        self.assertIsNotNone(cache.get("Paris"))
    
    def test_clear_all(self):
        """Test: Limpiar todo el caché"""
        self.cache.set("Madrid", self.sample_data)
        self.cache.set("Barcelona", self.sample_data)
        
        count = self.cache.clear_all()
        
        self.assertEqual(count, 2)
        self.assertIsNone(self.cache.get("Madrid"))
        self.assertIsNone(self.cache.get("Barcelona"))
    
    def test_get_stats(self):
        """Test: Obtener estadísticas del caché"""
        self.cache.set("Madrid", self.sample_data)
        self.cache.set("Barcelona", self.sample_data)
        
        stats = self.cache.get_stats()
        
        self.assertEqual(stats['total_entries'], 2)
        self.assertIn('madrid', stats['cities'])
        self.assertIn('barcelona', stats['cities'])

if __name__ == '__main__':
    unittest.main()
