"""
Casos de prueba para la función validar_temperatura_ciudad
Ejecuta este archivo para probar diferentes escenarios
"""

import json
from app.services.weather_service import WeatherService

def ejecutar_pruebas():
    """Ejecuta todos los casos de prueba"""
    service = WeatherService()
    
    print("=" * 70)
    print("CASOS DE PRUEBA - VALIDACIÓN DE TEMPERATURA")
    print("=" * 70)
    
    # CASO 1: Ciudad válida
    print("\n" + "=" * 70)
    print("CASO 1: Ciudad válida (Madrid)")
    print("=" * 70)
    resultado = service.validar_temperatura_ciudad("Madrid")
    if resultado:
        print("\n📊 Resultado JSON:")
        print(json.dumps(resultado.to_json(), indent=2, ensure_ascii=False))
    print("\n✅ CASO 1: PASÓ" if resultado else "\n❌ CASO 1: FALLÓ")
    
    # CASO 2: Ciudad con espacios extra
    print("\n" + "=" * 70)
    print("CASO 2: Ciudad con espacios extra ('  Barcelona  ')")
    print("=" * 70)
    resultado = service.validar_temperatura_ciudad("  Barcelona  ")
    if resultado:
        print("\n📊 Resultado JSON:")
        print(json.dumps(resultado.to_json(), indent=2, ensure_ascii=False))
    print("\n✅ CASO 2: PASÓ" if resultado else "\n❌ CASO 2: FALLÓ")
    
    # CASO 3: Ciudad que no existe
    print("\n" + "=" * 70)
    print("CASO 3: Ciudad que no existe ('CiudadInventada123')")
    print("=" * 70)
    resultado = service.validar_temperatura_ciudad("CiudadInventada123")
    print("\n✅ CASO 3: PASÓ (correctamente retornó None)" if resultado is None else "\n❌ CASO 3: FALLÓ")
    
    # CASO 4: Entrada vacía
    print("\n" + "=" * 70)
    print("CASO 4: Entrada vacía ('')")
    print("=" * 70)
    resultado = service.validar_temperatura_ciudad("")
    print("\n✅ CASO 4: PASÓ (correctamente retornó None)" if resultado is None else "\n❌ CASO 4: FALLÓ")
    
    # CASO 5: Solo números
    print("\n" + "=" * 70)
    print("CASO 5: Solo números ('12345')")
    print("=" * 70)
    resultado = service.validar_temperatura_ciudad("12345")
    print("\n✅ CASO 5: PASÓ (correctamente retornó None)" if resultado is None else "\n❌ CASO 5: FALLÓ")
    
    # CASO 6: Entrada None
    print("\n" + "=" * 70)
    print("CASO 6: Entrada None")
    print("=" * 70)
    resultado = service.validar_temperatura_ciudad(None)
    print("\n✅ CASO 6: PASÓ (correctamente retornó None)" if resultado is None else "\n❌ CASO 6: FALLÓ")
    
    # CASO 7: Nombre muy corto
    print("\n" + "=" * 70)
    print("CASO 7: Nombre muy corto ('A')")
    print("=" * 70)
    resultado = service.validar_temperatura_ciudad("A")
    print("\n✅ CASO 7: PASÓ (correctamente retornó None)" if resultado is None else "\n❌ CASO 7: FALLÓ")
    
    # CASO 8: Ciudad internacional
    print("\n" + "=" * 70)
    print("CASO 8: Ciudad internacional (Tokyo)")
    print("=" * 70)
    resultado = service.validar_temperatura_ciudad("Tokyo")
    if resultado:
        print("\n📊 Resultado JSON:")
        print(json.dumps(resultado.to_json(), indent=2, ensure_ascii=False))
        print(f"\n📌 Verificación de conversión:")
        print(f"   Celsius: {resultado.temperature_celsius}°C")
        print(f"   Fahrenheit: {resultado.temperature_fahrenheit}°F")
    print("\n✅ CASO 8: PASÓ" if resultado else "\n❌ CASO 8: FALLÓ")
    
    # CASO 9: Ciudad con caracteres especiales
    print("\n" + "=" * 70)
    print("CASO 9: Ciudad con caracteres especiales (São Paulo)")
    print("=" * 70)
    resultado = service.validar_temperatura_ciudad("São Paulo")
    if resultado:
        print("\n📊 Resultado JSON:")
        print(json.dumps(resultado.to_json(), indent=2, ensure_ascii=False))
    print("\n✅ CASO 9: PASÓ" if resultado else "\n❌ CASO 9: FALLÓ")
    
    # CASO 10: Tipo de dato incorrecto
    print("\n" + "=" * 70)
    print("CASO 10: Tipo de dato incorrecto (número entero 123)")
    print("=" * 70)
    resultado = service.validar_temperatura_ciudad(123)
    print("\n✅ CASO 10: PASÓ (correctamente retornó None)" if resultado is None else "\n❌ CASO 10: FALLÓ")
    
    print("\n" + "=" * 70)
    print("PRUEBAS COMPLETADAS")
    print("=" * 70)


if __name__ == "__main__":
    ejecutar_pruebas()
