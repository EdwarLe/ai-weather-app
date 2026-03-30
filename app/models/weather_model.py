class WeatherData:
    """Modelo para almacenar datos del clima de una ciudad"""
    def __init__(self, city, temperature_celsius, temperature_fahrenheit, latitude, longitude, timestamp):
        self.city = city
        self.temperature_celsius = temperature_celsius
        self.temperature_fahrenheit = temperature_fahrenheit
        self.latitude = latitude
        self.longitude = longitude
        self.timestamp = timestamp
    
    def to_json(self):
        """Convierte el modelo a formato JSON"""
        return {
            "success": True,
            "city": self.city,
            "temperature": {
                "celsius": self.temperature_celsius,
                "fahrenheit": round(self.temperature_fahrenheit, 1)
            },
            "coordinates": {
                "latitude": self.latitude,
                "longitude": self.longitude
            },
            "timestamp": self.timestamp
        }
