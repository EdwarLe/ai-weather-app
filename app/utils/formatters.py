def celsius_to_fahrenheit(celsius):
    """Convierte Celsius a Fahrenheit: F = (C × 9/5) + 32"""
    return (celsius * 9/5) + 32


def format_weather(weather_data):
    """Formatea los datos del clima para mostrar en consola"""
    return (f"\n🌍 Ciudad: {weather_data.city}"
            f"\n🌡️  Temperatura: {weather_data.temperature_celsius}°C / {weather_data.temperature_fahrenheit:.1f}°F"
            f"\n📍 Coordenadas: ({weather_data.latitude}, {weather_data.longitude})"
            f"\n🕐 Hora: {weather_data.timestamp}")
