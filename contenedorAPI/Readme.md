## CONSTRUIR IMAGEN API 🔧

	docker build -t flaskapp .

### PARA CONTENEDOR API  ✒️
	docker run --restart always --name docker_api -d -p 3000:3000 flaskapp

### INGRESAR AL CONTENEDOR

	docker exec -it docker_api bash

### EXPLICACION DOCKERFILE ⚙️

**Indicamos que utilizaremos la imagen de ubuntu 16.04 para instalar nuestra api**

```bash
FROM ubuntu:16.04
```

Corremos los comandos para actualizar e instalar pip de python
```bash
RUN apt-get update -y && \
    apt-get install -y python-pip --upgrade python-pip python-dev
```
Copiamos el archivo de requerimientos donde estan las librerias que necesitamos para la api.

```
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app
```
**Comando para instalar las librerias necesarias, encontradas en el archivo de #requirments.txt**
**Después copiamos la carpeta app que es donde se encuentra nuestra aplicacion.**

```bash
RUN pip install -r requirements.txt

COPY . /app
```
**Corremos nuestra aplicacion**

```bash
CMD [ "python","src/app.py" ]

```
