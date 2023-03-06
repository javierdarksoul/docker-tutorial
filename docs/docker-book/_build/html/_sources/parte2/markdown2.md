# Definiendo un archivo yaml de docker compose

Un archivo yml tiene la siguiente estructura 


``` 
services:       
  nombre_del_servicio: #definicion de servicio, cada aplicación docker debe definirse aqui
    variable_de_configuracion: ## configuraciones para cada aplicación
      valores
    variable_de_configuracion:
      valores
  nombre_de_otro_servicio:
    variable_de_configuracion:
      valores
``` 

Veremos un ejemplo sencillo de un docker-compose.yml que utiliza una imagen de dockerhub postgres

``` 
services:
  db:
    image: postgres
``` 

Si necesitamos una imagen personalizada, podemos usar un archivo Dockerfile junto con la opción build. 

``` 
services:
  my-service:
    build: dockers-examples/numpy-test
``` 

Si queremos modificar el comando ejecutado por defecto por el contenedor , podemos usar la opcion command de docker compose

``` 
services:
  my-service:
    build:  dockers-examples/numpy-test
    command: echo "hola mundo"
``` 

Si alguno de nuestros servicios necesita utilizar un puerto, con la opcion port se puede hacer un mapeo HOST:CONTENEDOR(recordar bien el orden)

``` 
services:
  my-service:
    build:  dockers-examples/numpy-test
    command: echo "hola mundo"
    ports:
    - 6000:6000
``` 

Si alguno de nuestros servicios depende de la ejecución de otro, podemos utilizar la opcion "depends_on: servicio"

``` 
services:
  my-service:
    build:  dockers-examples/numpy-test
    command: echo "hola mundo"
    ports:
    - 6000:6000
    depends_on:
      - servicio_del_que_dependo
``` 

Si necesitamos definir variables de entorno, utilizamos la opcion "environment"

``` 
services:
  my-service:
    build:  dockers-examples/numpy-test
    command: echo "hola mundo"
    ports:
    - 6000:6000
    environment:
    - VAR: valor
``` 

En caso de que queramos configurar la red a la que los servicios se conectan, utilizaremos la opcion "network"

```
services:
  flask:
    build:  dockers-examples/numpy-test
    command: echo "hola mundo"
    ports:
    - "6001:6001"
    networks:
     network: #nombre de la red
      ipv4_address: 192.168.0.10  #definimos ip estatica en caso de ser necesario
networks:
  network:
    ipam:
        config:
          - subnet: "192.168.0.0/24"
            gateway: 192.168.0.1
```
