# Proyecto 1 Seminario de Sistemas 1

## PAGINAS WEB S3
Existe una pagina web en S3. Cuenta con un login realizado en Cognito de AWS. Al loggearse se puede tener acceso a los trabajos que estan en proceso.

## API SITIO WEB S3
* HTTP POST
- Recibe como parametros el nombre del trabajo, las instrucciones y archivos opcionales.

* HTTP GET
- Retorna el cuerpo de un html con la información de los trabajos que estan almacenados en DynamoDB. La función se encuentra en Lambda de AWS.

## MAQUINA EC2
- En las maquinas EC2 se encuentra con 3 contenedores docker.
- Se realizo con docker-compose para poner en marcha los contenedores.
- Cada Contenedor se ejecuta con dockerfile. 

## ARCHIVO DOCKERFILE
Es donde se encuentran las instrucciones de construccion de las magenes necesarias para el proyecto.

## API PARA EC2
* HTTP POST
- Recibe como parametros una imagen en cualquier formato y la fecha en que es subida.

* HTTP GET
- Retorna el cuerpo de un html con los nombres y las direcciones de las imagenes para que sean mostradas en la pagina web principal.

## ENTREGA CONTINUA
* En una maquina EC2 se encuentra Jenkins escuchando los eventos de github que es donde se encuentra el proyecto para ponerlos en marcha.

Jenkins se encuentra en un contenedor docker.
Se ejecuta en los puertos 8080 o 50000.


## Usuarios y Roles 🛠️
- Rol para acceder a Lambda y DynamoDB
- Rol para acceso a reconocimiento de objetos
- Usuario con Acceso a Bucket de Pagina Web
- Usuario con Acceso a EC2
- Usuario con Acceso a los usuarios de Cognito

## Construido con 🛠️

* [FLASK](https://www.fullstackpython.com) - Python 
* [AWS S3](https://aws.amazon.com/s3/)  - Servicio de Almacenamiento
* [AWS DynamoDB](https://aws.amazon.com/rds/) - Bases de Datos No SQL
* [AWS Lambda](https://aws.amazon.com/lambda/) - Lambda
* [AWS API GATEWAY](https://aws.amazon.com/apigateway/) - API GATEWAY
* [AWS COGNITO](https://aws.amazon.com/cognito/) - COGNITO

## DOCKER
Imagenes utilizados

* Jenkins
* MySQL
* Ubuntu Para Ejecutar Flask
* NGINX 

#### *Los archivos docker-compose y dockerfile se encuentran cada uno en la carpeta respectiva.*

## Autor ✒️

* **Sergio Geovany Guoz Tubac** 🤓
