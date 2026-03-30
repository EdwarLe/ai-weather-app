import json
from app.services.weather_service import WeatherService
from app.utils.formatters import format_weather

class CLI:
    """Interfaz de línea de comandos para la aplicación del clima"""
    
    def __init__(self):
        self.service = WeatherService()
    
    def run(self):
        """Ejecuta la aplicación de consola"""
        print("="*50)
        print("🌤️  APLICACIÓN DE CLIMA - Open-Meteo")
        print("="*50)
        
        city = input("\nIngresa el nombre de la ciudad: ")
        
        weather = self.service.validar_temperatura_ciudad(city)
        
        if weather:
            # Mostrar formato legible
            print(format_weather(weather))
            
            # Mostrar formato JSON
            print("\n📊 Formato JSON:")
            print(json.dumps(weather.to_json(), indent=2, ensure_ascii=False))
        else:
            print("\n❌ No se pudo obtener la temperatura")
