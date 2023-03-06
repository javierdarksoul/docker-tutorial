# Primeros pasos con Docker: definicion, instalación y utilización

## ¿Qué es docker?

Docker es una herramienta que permite a los desarrolladores, administradores de sistemas, etc. implementar fácilmente sus aplicaciones en un espacio aislado (llamado contenedores) para ejecutarlas en el sistema operativo host, es decir, Linux. 

## Diferencias con maquinas virtuales

![](EN-docker-tutorial.png "")

Para poder encapsular las aplicaciones con un hardware de virtualización clásico es necesario un elemento conocido como hipervisor, que funciona como una capa de abstracción entre el sistema anfitrión y los sistemas huéspedes virtuales. Cada sistema invitado emula a una máquina completa con un kernel de sistema operativo separado, al que el hipervisor asigna los componentes de hardware del host (CPU, memoria, espacio en disco duro y periféricos disponibles) de forma proporcional.

Por el contrario, en la virtualización basada en contenedores no se crea un sistema huésped completo, sino que las aplicaciones se inician en contenedores que, aun compartiendo el mismo kernel, es decir, el del sistema anfitrión, se ejecutan como procesos aislados en el espacio de usuario.

## Definiciones básicas

Docker se compone de dos componentes principales

Imagen: Corresponde a una plantilla de solo lectura que define su contenedor. La imagen contiene el código que se ejecutará, incluida cualquier definición para cualquier biblioteca o dependencia que el código necesite. Un contenedor de Docker es una imagen de Docker instanciada (en ejecución).

Contenedor: Corresponde a una imagen de docker instanciada

## Quickstart

Para instalar docker en sistemas basados en linux

```
$ sudo pacman -S docker
```


Para ubuntu
```
$ sudo apt-get install ca-certificates curl gnupg lsb-release
$ sudo mkdir -m 0755 -p /etc/apt/keyrings
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

$ echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

$ sudo apt-get update
$ sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```
La instalacion en Windows / MacOS se debe realizar descargando la aplicación docker desktop desde [https://www.docker.com/products/docker-desktop/]

## Comandos básicos de docker

Para descargar una imagen existente en dockerhub, ejecutamos 

`$ docker pull [image_name:version]`

Para listar las imagenes pulleadas o buildeadas, ejecutamos

`$ docker images`

Para instanciar una imagen en un contenedor y ejecutar un comando  

`$ docker run [image_name] [command]`

Para listar los contenedores

`$ docker ps -a`

Para ejecutar una consola dentro del contenedor

`$ docker run -it [image_name] bash`

Para eliminar una imagen

`$docker rmi [image_name]`

Para detener un contenedor en ejecución

`$ docker stop [container_id]`

 