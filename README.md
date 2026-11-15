# NASA Bot para Telegram

Bot de Telegram en Python que consulta la API **Astronomy Picture of the Day (APOD)** de la NASA. Permite pedir la imagen astronómica asociada a una fecha y muestra su título, fecha y descripción.

> El bot y sus mensajes están en español. Este proyecto usa la API APOD; no consulta toda la biblioteca de la NASA.

## Funcionalidades

- `/start`: mensaje de bienvenida y resumen de uso.
- `/help`: muestra la ayuda.
- `/imagenNasa`: solicita una fecha con formato `AAAA-MM-DD` (por ejemplo, `2008-01-13`) y busca el contenido APOD de ese día.
- Ante otros mensajes de texto, muestra la ayuda. Los comandos no reconocidos reciben un aviso.

Si la consulta tiene éxito, el bot envía el título, la fecha, la explicación y la URL del contenido como foto. Si la API devuelve un error de fecha o de consulta, muestra un mensaje en español.

## Requisitos

- Python 3.
- Un bot de Telegram y su token, creado mediante [@BotFather](https://t.me/BotFather).
- Una clave de la API de la NASA, disponible en [api.nasa.gov](https://api.nasa.gov/).
- Para ejecutar el modo webhook incluido: un servidor accesible públicamente con HTTPS y un certificado TLS válido. El código inicia Flask en el puerto `443`.

## Instalación

Clona el repositorio y entra en su directorio:

```bash
git clone https://github.com/JuanAnacona15/nasaBotT.git
cd nasaBotT
```

Instala las dependencias utilizadas por el código:

```bash
python -m pip install pyTelegramBotAPI Flask requests
```

`pyTelegramBotAPI` es el paquete que proporciona el módulo importado como `telebot`.

## Configuración de credenciales

El código obtiene el token de Telegram y la clave de NASA mediante `token()` y `apiKey()` en `credentials.py`. Configura allí tus propias credenciales antes de iniciar el bot.

**Seguridad:** no publiques tokens ni claves en el repositorio. Las credenciales incluidas previamente en `credentials.py` deben considerarse expuestas: revoca o regenera el token de Telegram con BotFather y sustituye la clave de NASA. Evita volver a guardar credenciales reales en commits; para un despliegue, es preferible leerlas desde variables de entorno y mantenerlas fuera del control de versiones.

## Ejecución

Desde la raíz del proyecto:

```bash
python nasaBot.py
```

El programa obtiene la IP pública mediante `api.ipify.org`, elimina el webhook anterior, registra uno y levanta Flask en `0.0.0.0:443`.

### Nota sobre el despliegue webhook

La configuración de webhook del código es básica y no completa por sí sola una puesta en producción: Telegram requiere una URL HTTPS pública válida y el servidor debe tener TLS configurado. Antes de desplegar, configura la URL completa del webhook y los certificados según tu infraestructura. Además, revisa `nasaBot.py`: la comprobación actual del encabezado `Content-Type` contiene un error tipográfico (`aplication/json`), por lo que las actualizaciones pueden no procesarse. Corrígelo a `application/json` y prueba el webhook antes de usarlo.

## Estructura del proyecto

| Archivo | Propósito |
| --- | --- |
| `nasaBot.py` | Inicializa el bot y Flask, configura el webhook y gestiona los comandos y mensajes. |
| `functionsForBot.py` | Construye los mensajes de bienvenida y ayuda y consulta el endpoint APOD de la NASA. |
| `credentials.py` | Proporciona el token de Telegram y la clave de la API de NASA. No almacenes secretos reales en el repositorio. |
| `README.md` | Documentación del proyecto. |

## Cómo funciona la consulta

1. El usuario envía `/imagenNasa`.
2. El bot solicita una fecha en formato `AAAA-MM-DD`.
3. `functionsForBot.py` realiza una solicitud al endpoint `https://api.nasa.gov/planetary/apod` con la fecha y la clave de NASA.
4. Si la respuesta es exitosa, el bot envía los datos APOD; si no, responde con un mensaje de error.

## Limitaciones conocidas

- La aplicación depende de los servicios de Telegram y de la API de NASA, así como de una conexión a Internet.
- La fecha se pasa directamente a la API; el código no valida localmente su formato.
- El despliegue webhook requiere configuración HTTPS que no está incluida en el proyecto.
- El manejador de webhook tiene el error de encabezado señalado arriba y debe corregirse para procesar las actualizaciones correctamente.
- La respuesta se envía mediante `send_photo`; el código no distingue otros tipos de contenido que la API pudiera devolver.

## Tecnologías

- Python
- [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI)
- [Flask](https://flask.palletsprojects.com/)
- [Requests](https://requests.readthedocs.io/)
- [NASA APOD API](https://api.nasa.gov/)
