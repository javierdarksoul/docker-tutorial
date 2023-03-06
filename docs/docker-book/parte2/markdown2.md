# Definiendo un archivo yaml de docker compose


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