Aplicación Test

Prueba tecnica
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