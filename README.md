# 🌤️ Weather App

Aplicación de consola en Python para consultar el clima actual de cualquier ciudad del mundo utilizando la API gratuita de Open-Meteo.

## 📋 Descripción

Weather App es una aplicación de línea de comandos que permite obtener información meteorológica en tiempo real de cualquier ciudad. La aplicación:

- 🌍 Busca coordenadas geográficas de la ciudad ingresada
- 🌡️ Obtiene la temperatura actual en Celsius y Fahrenheit
- 📍 Muestra las coordenadas exactas (latitud y longitud)
- 🕐 Proporciona la marca de tiempo de la medición
- 📊 Exporta los resultados en formato JSON
- 💾 **Sistema de caché inteligente** que almacena datos por 3 horas para mejorar el rendimiento

La aplicación está construida con una arquitectura modular que separa responsabilidades en capas (API, servicios, modelos, UI y utilidades), facilitando el mantenimiento y las pruebas.

## 🚀 Instalación

### Requisitos previos

- Python 3.7 o superior
- pip (gestor de paquetes de Python)
- Conexión a Internet

### Pasos de instalación

1. **Clonar el repositorio:**

```bash
git clone https://github.com/EdwarLe/ai-weather-app.git
cd weather-app
```

> 💡 **Alternativa**: Si no tienes Git instalado, puedes descargar el proyecto como archivo ZIP desde el repositorio y descomprimirlo.

2. **Crear un entorno virtual (recomendado):**

Un entorno virtual aísla las dependencias del proyecto y evita conflictos con otros proyectos Python.

**En Linux/macOS:**
```bash
python3 -m venv venv
```

**En Windows:**
```bash
python -m venv venv
```

3. **Activar el entorno virtual:**

**En Linux/macOS:**
```bash
source venv/bin/activate
```

**En Windows (CMD):**
```bash
venv\Scripts\activate.bat
```

**En Windows (PowerShell):**
```bash
venv\Scripts\Activate.ps1
```

> 💡 **Nota**: Cuando el entorno virtual está activado, verás `(venv)` al inicio de tu línea de comandos.

4. **Instalar dependencias:**
```bash
pip install -r requirements.txt
```

5. **Para desactivar el entorno virtual (cuando termines):**
```bash
deactivate
```

### Dependencias

El proyecto utiliza las siguientes dependencias:

- **requests==2.31.0**: Librería para realizar peticiones HTTP a las APIs de Open-Meteo

## 💻 Uso

### Ejecución básica

Para ejecutar la aplicación, simplemente ejecuta:

```bash
python main.py
```

### Flujo de uso

1. La aplicación mostrará un mensaje de bienvenida
2. Solicitará el nombre de una ciudad
3. Validará la entrada y buscará las coordenadas
4. Consultará la temperatura actual
5. Mostrará los resultados en formato legible y JSON

### Ejemplo de uso

```bash
$ python main.py
==================================================
🌤️  APLICACIÓN DE CLIMA - Open-Meteo
==================================================

Ingresa el nombre de la ciudad: Madrid
🔍 Iniciando validación para: 'Madrid'
✅ Validación exitosa
🌍 Buscando coordenadas de 'Madrid'...
✅ Coordenadas: (40.4165, -3.70256)
🌡️  Obteniendo temperatura...
✅ Temperatura: 15.2°C / 59.4°F
💾 Datos almacenados en caché (válidos por 3 horas)

🌍 Ciudad: Madrid
🌡️  Temperatura: 15.2°C / 59.4°F
📍 Coordenadas: (40.4165, -3.70256)
🕐 Hora: 2024-03-25T10:00

📊 Formato JSON:
{
  "success": true,
  "city": "Madrid",
  "temperature": {
    "celsius": 15.2,
    "fahrenheit": 59.4
  },
  "coordinates": {
    "latitude": 40.4165,
    "longitude": -3.70256
  },
  "timestamp": "2024-03-25T10:00"
}
```

### Ejemplo con caché

Si consultas la misma ciudad dentro de 3 horas:

```bash
$ python main.py
Ingresa el nombre de la ciudad: Madrid
🔍 Iniciando validación para: 'Madrid'
✅ Validación exitosa
💾 Datos obtenidos del caché (actualizados hace menos de 3 horas)

🌍 Ciudad: Madrid
🌡️  Temperatura: 15.2°C / 59.4°F
...
```

## 🧠 Sistema de Caché

La aplicación incluye un sistema de caché inteligente que mejora el rendimiento:

### Características

- ⏱️ **Expiración automática**: Los datos se almacenan por 3 horas
- 🚀 **Mejora de rendimiento**: Reduce peticiones HTTP innecesarias
- 💾 **Almacenamiento en memoria**: Rápido acceso a datos recientes
- 🔄 **Actualización automática**: Después de 3 horas, consulta nuevamente la API
- 🎯 **Normalización de claves**: "Madrid", "madrid" y "MADRID" usan el mismo caché

### Demostración del caché

Puedes ejecutar una demostración del sistema de caché:

```bash
python demo_cache.py
```

Este script muestra:
- Primera consulta (va a la API)
- Segunda consulta inmediata (usa caché)
- Consultas con diferentes mayúsculas (usa caché)
- Estadísticas del caché

### Configuración

Puedes modificar el tiempo de expiración en `config.py`:

```python
CACHE_EXPIRATION_HOURS = 3  # Cambiar a las horas deseadas
```

## 🧪 Pruebas

El proyecto incluye dos tipos de pruebas:

### 1. Tests unitarios (unittest)

Ejecutar los tests unitarios con cobertura completa:

```bash
python -m unittest tests/test_weather.py -v
```

Los tests incluyen:
- ✅ Validación de ciudades válidas
- ✅ Manejo de ciudades inexistentes
- ✅ Validación de entradas vacías, None y solo números
- ✅ Conversión de temperaturas Celsius a Fahrenheit
- ✅ Creación y serialización del modelo de datos
- ✅ Formato de salida

### 2. Tests del sistema de caché

Ejecutar tests específicos del caché:

```bash
python -m unittest tests/test_cache.py -v
```

Los tests incluyen:
- ✅ Almacenamiento y recuperación de datos
- ✅ Normalización de claves (mayúsculas/minúsculas)
- ✅ Expiración automática después de 3 horas
- ✅ Limpieza de entradas expiradas
- ✅ Estadísticas del caché

### 3. Casos de prueba funcionales

Ejecutar casos de prueba con ciudades reales:

```bash
python casos_de_prueba.py
```

Este script ejecuta 10 casos de prueba que incluyen:
- Ciudades válidas (Madrid, Barcelona, Tokyo)
- Ciudades con espacios extra
- Ciudades inexistentes
- Entradas vacías y None
- Solo números
- Nombres muy cortos
- Ciudades con caracteres especiales (São Paulo)
- Tipos de datos incorrectos

## ⚠️ Manejo de Errores

La aplicación implementa un robusto sistema de manejo de errores:

### Validación de entrada

- ❌ **Entrada None**: "El nombre no puede ser None"
- ❌ **Tipo incorrecto**: "Debe ser texto, recibí: [tipo]"
- ❌ **Entrada vacía**: "El nombre no puede estar vacío"
- ❌ **Nombre muy corto**: "Nombre demasiado corto (mínimo 2 caracteres)"
- ❌ **Solo números**: "El nombre no puede ser solo números"

### Errores de API

- ❌ **Ciudad no encontrada**: "No se encontró la ciudad '[nombre]'"
- ❌ **Timeout**: "Petición tardó demasiado (timeout)"
- ❌ **Error de conexión**: "No se pudo conectar a la API"
- ❌ **Código de estado HTTP**: "API respondió con código [código]"
- ❌ **Datos inválidos**: "Datos inválidos: [detalle]"

### Características de seguridad

- ⏱️ Timeout de 10 segundos en todas las peticiones HTTP
- 🔒 Manejo de excepciones específicas (Timeout, ConnectionError, JSONDecodeError)
- ✅ Validación exhaustiva de datos antes de procesarlos
- 🛡️ Protección contra inyección de código

## 📊 Ejemplo de Resultados

### Resultado exitoso

```json
{
  "success": true,
  "city": "Barcelona",
  "temperature": {
    "celsius": 18.5,
    "fahrenheit": 65.3
  },
  "coordinates": {
    "latitude": 41.3851,
    "longitude": 2.1734
  },
  "timestamp": "2024-03-25T14:30"
}
```

### Resultado con error

```
❌ No se encontró la ciudad 'CiudadInventada'
   Sugerencia: Verifica la ortografía

❌ No se pudo obtener la temperatura
```

## 🏗️ Estructura del Proyecto

```
weather-app/
├── app/
│   ├── api/
│   │   └── weather_api.py      # Cliente de API Open-Meteo
│   ├── models/
│   │   └── weather_model.py    # Modelo de datos WeatherData
│   ├── services/
│   │   └── weather_service.py  # Lógica de negocio y validación
│   ├── ui/
│   │   └── cli.py              # Interfaz de línea de comandos
│   └── utils/
│       ├── cache.py            # Sistema de caché con expiración
│       └── formatters.py       # Utilidades de formato
├── tests/
│   ├── test_cache.py           # Tests del sistema de caché
│   └── test_weather.py         # Tests unitarios
├── casos_de_prueba.py          # Casos de prueba funcionales
├── demo_cache.py               # Demostración del caché
├── config.py                   # Configuración de URLs y timeouts
├── main.py                     # Punto de entrada
├── requirements.txt            # Dependencias
└── README.md                   # Documentación
```

## 🔮 Mejoras Futuras

### Funcionalidades

- [ ] **Pronóstico extendido**: Mostrar predicción de 7 días
- [ ] **Más datos meteorológicos**: Humedad, velocidad del viento, presión atmosférica
- [ ] **Historial de búsquedas**: Guardar ciudades consultadas recientemente
- [ ] **Modo interactivo**: Permitir múltiples consultas sin reiniciar
- [ ] **Comparación de ciudades**: Comparar clima entre varias ciudades
- [ ] **Alertas meteorológicas**: Notificar condiciones extremas

### Interfaz

- [ ] **Interfaz gráfica (GUI)**: Versión con Tkinter o PyQt
- [ ] **API REST**: Crear servidor web con Flask/FastAPI
- [ ] **Aplicación web**: Frontend con HTML/CSS/JavaScript
- [ ] **Aplicación móvil**: Versión para Android/iOS

### Datos y almacenamiento

- [x] **Caché**: Guardar resultados temporalmente para reducir peticiones (implementado - 3 horas)
- [ ] **Base de datos**: Almacenar historial en SQLite
- [ ] **Exportación**: Guardar resultados en CSV o Excel
- [ ] **Gráficos**: Visualizar tendencias de temperatura
- [ ] **Caché persistente**: Guardar caché en disco para mantenerlo entre ejecuciones

### Calidad y rendimiento

- [ ] **Logging**: Sistema de logs para debugging
- [ ] **Configuración**: Archivo de configuración personalizable
- [ ] **Internacionalización**: Soporte para múltiples idiomas
- [ ] **Peticiones asíncronas**: Mejorar rendimiento con asyncio
- [ ] **Cobertura de tests**: Aumentar a 100%
- [ ] **CI/CD**: Integración continua con GitHub Actions

### Experiencia de usuario

- [ ] **Autocompletado**: Sugerencias de ciudades mientras se escribe
- [ ] **Geolocalización**: Detectar ubicación automáticamente
- [ ] **Temas**: Modo claro/oscuro para la interfaz
- [ ] **Notificaciones**: Alertas de cambios significativos

## 📝 Licencia

Este proyecto es de código abierto y está disponible para uso educativo.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Haz un fork del proyecto
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -m 'Agregar nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

## 📧 Contacto

Para preguntas o sugerencias sobre el proyecto, por favor abre un issue en el repositorio.

---

**Desarrollado con ❤️ usando Python y Open-Meteo API**
