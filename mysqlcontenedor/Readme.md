## CONSTRUCCION DE CONTENEDOR MYSQL

	docker build -t mysql_f:0.1 .

#### PARA EJECUTAR .SH
	sudo chmod +x init.sh 
	./init.sh

### INGRESAR AL CONTENEDOR

	docker exec -it docker_mysql bash

### FUNCIONAMIENTO DE DOCKERFILE

Con este comando hacemos referencia a que vamos a utilizar mysql en su version 8, bajada de dockerhub.
	
	FROM mysql:8

Sera nuestra base de datos
	
	ENV MYSQL_DATABASE flores

Copiamos la carpeta de scripts para ejecutarlo después.
	
	COPY ./scripts/ /docker-entrypoint-initdb.d/


### Archivo init.sh

Creamos el contenedor de nombre docker_mysql, con MYSQL_ROOT_PASSWORD como admin.

	docker run --name docker_mysql \
	-e MYSQL_ROOT_PASSWORD=admin \
	-d mysql_f:0.1 \
	--character-set-server=utf8mb4 \
	--collation-server=utf8mb4_unicode_ci \
	--default-authentication-plugin=mysql_native_password
