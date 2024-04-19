Aplicación Test
Prueba técnica
Introducción

Esta aplicación es una API RESTful desarrollada con Flask que proporciona funcionalidades CRUD (Crear, Leer, Actualizar y Eliminar) para administrar restaurantes. Permite realizar operaciones como crear nuevos restaurantes, obtener todos los restaurantes, actualizar la información de un restaurante existente y eliminar un restaurante. Esta versión no incluye autenticación básica.
Requisitos

    Docker
    Docker Compose

Instalación y Uso

    Clona o descarga el repositorio en tu máquina local.

    En el directorio raíz del proyecto, ejecuta el siguiente comando para construir y levantar los contenedores de Docker:

bash

docker-compose up --build

    ¡IMPORTANTE! Para utilizar la aplicación, primero debes crear la tabla de restaurantes en la base de datos. Esto se puede hacer ejecutando el siguiente endpoint:

bash

curl -X GET http://localhost:5000/start

    La aplicación estará disponible en http://localhost:5000.

Endpoints Disponibles

    GET /ping: Verifica si la aplicación está en línea.
    GET /start: Crea la tabla de restaurantes en la base de datos.
    GET /get_all: Obtiene todos los restaurantes almacenados.
    POST /insert_restaurant: Inserta un nuevo restaurante.
    PUT /update_restaurant: Actualiza la información de un restaurante existente.
    DELETE /delete_restaurant/<restaurant_id>: Elimina un restaurante por su ID.
    GET /get_one: Obtiene un restaurante por un parámetro específico.
    GET /restaurants/statistics: Calcula estadísticas sobre los restaurantes en un área específica.

Requisitos de Datos

Los datos de los restaurantes deben proporcionarse en formato JSON en el cuerpo de la solicitud para las rutas que requieran datos, como POST /insert_restaurant y PUT /update_restaurant.
Ejemplo de datos de restaurante:

json

{
    "id": "123456",
    "rating": 4.5,
    "name": "Restaurante de Ejemplo",
    "site": "http://www.ejemplo.com",
    "email": "info@ejemplo.com",
    "phone": "+1234567890",
    "street": "123 Calle Principal",
    "city": "Ciudad Ejemplo",
    "state": "Estado Ejemplo",
    "lat": 12.3456,
    "lng": -78.9012
}

Base de Datos

La aplicación utiliza PostgreSQL como base de datos. Se ha configurado un contenedor Docker para ejecutar una instancia de PostGIS.

Ejemplos de Uso
1. Verificar si la aplicación está en línea

    Método: GET
    Ruta: /ping
    Ejemplo de Solicitud:

bash

curl -X GET http://localhost:5000/ping

2. Crear la tabla de restaurantes en la base de datos

    Método: GET
    Ruta: /start
    Ejemplo de Solicitud:

bash

curl -X GET http://localhost:5000/start

3. Obtener todos los restaurantes almacenados

    Método: GET
    Ruta: /get_all
    Ejemplo de Solicitud:

bash

curl -X GET http://localhost:5000/get_all

4. Insertar un nuevo restaurante

    Método: POST
    Ruta: /insert_restaurant
    Datos en el Cuerpo de la Solicitud (JSON):

json

{
    "id": "097f66dd-ca33-4f30-88e4-33193fcf8cda",
    "rating": 1,
    "name": "Briseño - Rodarte",
    "site": "https://fernando javier.com",
    "email": "Mario84@yahoo.com",
    "phone": "5256-976-186",
    "street": "780 Medina Terrenos",
    "city": "Madridland",
    "state": "Sonora",
    "lat": 19.4338572792132,
    "lng": -99.1254273785957
}

    Ejemplo de Solicitud:

bash

curl -X POST -H "Content-Type: application/json" -d '{
    "id": "097f66dd-ca33-4f30-88e4-33193fcf8cda",
    "rating": 1,
    "name": "Briseño - Rodarte",
    "site": "https://fernando javier.com",
    "email": "Mario84@yahoo.com",
    "phone": "5256-976-186",
    "street": "780 Medina Terrenos",
    "city": "Madridland",
    "state": "Sonora",
    "lat": 19.4338572792132,
    "lng": -99.1254273785957
}' http://localhost:5000/insert_restaurant

5. Actualizar la información de un restaurante existente

    Método: PUT
    Ruta: /update_restaurant
    Datos en el Cuerpo de la Solicitud (JSON):

json

{
    "id": "097f66dd-ca33-4f30-88e4-33193fcf8cda",
    "campo": "rating",
    "valor": 4
}


    Ejemplo de Solicitud:

bash

curl -X PUT -H "Content-Type: application/json" -d '{
    "id": "097f66dd-ca33-4f30-88e4-33193fcf8cda",
    "campo": "rating",
    "valor": 4
}' http://localhost:5000/update_restaurant

6. Eliminar un restaurante por su ID

    Método: DELETE
    Ruta: /delete_restaurant/097f66dd-ca33-4f30-88e4-33193fcf8cda
    Ejemplo de Solicitud:

bash

curl -X DELETE http://localhost:5000/delete_restaurant/097f66dd-ca33-4f30-88e4-33193fcf8cda

7. Obtener un restaurante por un parámetro específico

    Método: GET
    Ruta: /get_one?param_name=city&param_value=Madridland
    Ejemplo de Solicitud:

bash

curl -X GET http://localhost:5000/get_one?param_name=city&param_value=Madridland

8. Calcular estadísticas sobre los restaurantes en un área específica

    Método: GET
    Ruta: /restaurants/statistics?latitude=19.4338572792132&longitude=-99.1254273785957&radius=1000
    Ejemplo de Solicitud:

bash

curl -X GET http://localhost:5000/restaurants/statistics?latitude=19.4338572792132&longitude=-99.1254273785957&radius=

