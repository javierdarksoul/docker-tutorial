# Primeros pasos con Docker Compose

## ¿Qué es docker compose?

Docker compose es una herramienta que permite la integración de múltiples contenedores docker de manera sencilla. Análogo a docker con el archivo Dockerfile, la definición de la orquestación con docker compose se realiza a través del archivo docker-compose.yml. Un ejemplo bastante común es el uso de docker compose para orquestar aplicaciones web, ya que, normalmente se tienen dos componentes dockerizables: front end y back end. Ambos componentes deben interactuar entre si a través de una API.

![](frontback.jpg "")

Para levantar servicios con docker compose, utilizamos 

´´´
docker compose up

´´´

donde la definición y configuración de los servicios están en el archivo docker-compose.yml (ya veremos como escribir este tipo de archivos)

Para dar de baja los servicios levantados, utilizamos

´´´
docker compose down

´´´









