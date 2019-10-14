## DOCKERCOMPOSE 🚀

Se crean 3 servicios que son:
* mysql_database
* web
* flaskapp

*Cada servicio contiene el campo .build en donde le indicamos la carpeta en donde se encuentra nuestro archivo ### Dockerfile en donde se encuentran las instrucciones para construir nuestra imagen.*

Cada servicio tiene su respectivo puerto en el que trabaja.

### ARCHIVO  🔧
Al inicio indicamos version del docker-compose. E iniciamos con la etiqueta services.

    version: '3'
      services:
      
Imagen de la Basede Datos

        mysql_database:
          build: ./mysql_docker/
          command: --default-authentication-plugin=mysql_native_password --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci
          environment:
            - MYSQL_ROOT_PASSWORD="admin"
          restart: always
          ports: 
            - "3306:33060"
Imagen WEB

      web:
        #image: nginx
        build: ./nginx_docker/
        ports:
          - "8080:80"
        environment:
          - NGINX_HOST=sitio.com
          - NGINX_PORT=80
          
IMAGEN DE LA API

      flaskapp:
        build: ./api_docker/
        ports:
          - "3000:3000"
        restart: always 

