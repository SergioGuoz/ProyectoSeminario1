## JENKINS 

#### COMPOSE 

Para construir la imagen ejecutamos el siguiente comando:
```bash
docker-compose build
```
Para arrancar el contenedor con Jenkins ejecutamos el siguiente comando:
```bash
docker-compose up –d
```
Accedemos a la direccion de nuestra maquina http://localhost:8080  e ingresaremos al panel de administración de Jenkins.

Para obtener la contraseña del usuario admin de Jenkins ejecutamos el siguiente comando:

```bash
docker exec -it jenkinssemi1_master_1 cat /var/jenkins_home/secrets/initialAdminPassword
```
