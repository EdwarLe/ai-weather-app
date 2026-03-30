"""
Demostración del sistema de caché
Ejecuta este archivo para ver cómo funciona el caché con temporalidad de 3 horas
"""

from app.services.weather_service import WeatherService
import time

def demo_cache():
    """Demuestra el funcionamiento del caché"""
    service = WeatherService()
    
    print("=" * 70)
    print("DEMOSTRACIÓN DEL SISTEMA DE CACHÉ")
    print("=" * 70)
    
    # Primera consulta - debe ir a la API
    print("\n" + "=" * 70)
    print("CONSULTA 1: Madrid (primera vez - debe consultar API)")
    print("=" * 70)
    result1 = service.validar_temperatura_ciudad("Madrid")
    
    if result1:
        print(f"\n✅ Temperatura obtenida: {result1.temperature_celsius}°C")
    
    # Segunda consulta inmediata - debe usar caché
    print("\n" + "=" * 70)
    print("CONSULTA 2: Madrid (inmediata - debe usar caché)")
    print("=" * 70)
    result2 = service.validar_temperatura_ciudad("Madrid")
    
    if result2:
        print(f"\n✅ Temperatura obtenida: {result2.temperature_celsius}°C")
    
    # Tercera consulta con variación de mayúsculas - debe usar caché
    print("\n" + "=" * 70)
    print("CONSULTA 3: MADRID (mayúsculas - debe usar caché)")
    print("=" * 70)
    result3 = service.validar_temperatura_ciudad("MADRID")
    
    if result3:
        print(f"\n✅ Temperatura obtenida: {result3.temperature_celsius}°C")
    
    # Consulta de otra ciudad - debe ir a la API
    print("\n" + "=" * 70)
    print("CONSULTA 4: Barcelona (primera vez - debe consultar API)")
    print("=" * 70)
    result4 = service.validar_temperatura_ciudad("Barcelona")
    
    if result4:
        print(f"\n✅ Temperatura obtenida: {result4.temperature_celsius}°C")
    
    # Mostrar estadísticas del caché
    print("\n" + "=" * 70)
    print("ESTADÍSTICAS DEL CACHÉ")
    print("=" * 70)
    stats = service.cache.get_stats()
    print(f"📊 Total de entradas en caché: {stats['total_entries']}")
    print(f"🌍 Ciudades almacenadas: {', '.join(stats['cities'])}")
    
    print("\n" + "=" * 70)
    print("INFORMACIÓN DEL CACHÉ")
    print("=" * 70)
    print("⏱️  Tiempo de expiración: 3 horas")
    print("💾 Los datos se almacenan en memoria")
    print("🔄 Después de 3 horas, se consulta nuevamente la API")
    print("🚀 Mejora el rendimiento y reduce peticiones HTTP")
    
    print("\n" + "=" * 70)
    print("DEMOSTRACIÓN COMPLETADA")
    print("=" * 70)

if __name__ == "__main__":
    demo_cache()
