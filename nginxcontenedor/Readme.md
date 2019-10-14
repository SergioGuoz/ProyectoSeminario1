## CREAR SERVIDOR NGINX 

Esto se ejecutara en el puerto 80, el nombre del contenedor sera ## server_nginx

	docker run --name server_nginx -d -p 80:80 nginx 

### ENTRAR AL CONTENEDOR DOCKER 
	docker exec -it server_nginx /bin/bash

### ARCHIVO DE PAGINA DE INICIO
  
	/usr/share/nginx/html
			--! REINICIAR NGINX /etc/init.d/nginx restart
