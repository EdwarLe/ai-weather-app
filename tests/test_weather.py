import unittest
from unittest.mock import patch, MagicMock
from app.services.weather_service import WeatherService
from app.models.weather_model import WeatherData
from app.utils.formatters import format_weather, celsius_to_fahrenheit

class TestWeatherService(unittest.TestCase):
    """Tests para el servicio de clima"""
    
    @patch('app.api.weather_api.WeatherAPI.get_weather', return_value=(22.5, "2024-03-25T10:00"))
    @patch('app.api.weather_api.WeatherAPI.get_coordinates', return_value=(40.4165, -3.70256, "Madrid"))
    def test_validar_temperatura_ciudad_exitoso(self, mock_coords, mock_weather):
        """Test: Ciudad válida retorna datos correctos"""
        service = WeatherService()
        result = service.validar_temperatura_ciudad("Madrid")
        
        self.assertIsNotNone(result)
        self.assertEqual(result.city, "Madrid")
        self.assertEqual(result.temperature_celsius, 22.5)
    
    @patch('app.api.weather_api.WeatherAPI.get_coordinates', return_value=(None, None, None))
    def test_validar_temperatura_ciudad_no_encontrada(self, mock_coords):
        """Test: Ciudad inexistente retorna None"""
        service = WeatherService()
        result = service.validar_temperatura_ciudad("CiudadInexistente")
        
        self.assertIsNone(result)
    
    def test_validar_entrada_vacia(self):
        """Test: Entrada vacía retorna None"""
        service = WeatherService()
        result = service.validar_temperatura_ciudad("")
        self.assertIsNone(result)
    
    def test_validar_entrada_none(self):
        """Test: Entrada None retorna None"""
        service = WeatherService()
        result = service.validar_temperatura_ciudad(None)
        self.assertIsNone(result)
    
    def test_validar_solo_numeros(self):
        """Test: Solo números retorna None"""
        service = WeatherService()
        result = service.validar_temperatura_ciudad("12345")
        self.assertIsNone(result)

class TestWeatherModel(unittest.TestCase):
    """Tests para el modelo de datos"""
    
    def test_weather_data_creation(self):
        """Test: Creación correcta del modelo"""
        weather = WeatherData("Barcelona", 25.0, 77.0, 41.3851, 2.1734, "2024-03-25T10:00")
        
        self.assertEqual(weather.city, "Barcelona")
        self.assertEqual(weather.temperature_celsius, 25.0)
        self.assertEqual(weather.temperature_fahrenheit, 77.0)
    
    def test_weather_data_to_json(self):
        """Test: Conversión a JSON correcta"""
        weather = WeatherData("Paris", 18.5, 65.3, 48.8566, 2.3522, "2024-03-25T10:00")
        json_data = weather.to_json()
        
        self.assertTrue(json_data["success"])
        self.assertEqual(json_data["city"], "Paris")
        self.assertEqual(json_data["temperature"]["celsius"], 18.5)

class TestFormatters(unittest.TestCase):
    """Tests para utilidades de formato"""
    
    def test_celsius_to_fahrenheit(self):
        """Test: Conversión de temperatura"""
        self.assertEqual(celsius_to_fahrenheit(0), 32.0)
        self.assertEqual(celsius_to_fahrenheit(100), 212.0)
        self.assertAlmostEqual(celsius_to_fahrenheit(25), 77.0, places=1)
    
    def test_format_weather(self):
        """Test: Formato de salida contiene datos correctos"""
        weather = WeatherData("Paris", 18.5, 65.3, 48.8566, 2.3522, "2024-03-25T10:00")
        formatted = format_weather(weather)
        
        self.assertIn("Paris", formatted)
        self.assertIn("18.5°C", formatted)
        self.assertIn("65.3°F", formatted)

if __name__ == '__main__':
    unittest.main()
