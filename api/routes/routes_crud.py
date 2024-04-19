from flask import Blueprint, request
from controllers.start import createTable
from controllers.select_all import get_all
from controllers.select import get_by_param
from controllers.add import insert_restaurant
from controllers.update import update_restaurant
from controllers.delete import delete_restaurant
from controllers.statistics import calculate_statistics

# Crear un Blueprint para las rutas CRUD
bp = Blueprint('routes_crud', __name__)

# Ruta para verificar la conexión
@bp.route('/ping', methods=['GET'])
def ping():
    return 'pong'

# Ruta para iniciar la creación de la tabla de restaurantes
@bp.route('/start', methods=['GET'])
def start():
    createTable()
    return 'La tabla Restaurants ha sido creada exitosamente.'

# Ruta para obtener todos los restaurantes
@bp.route('/get_all', methods=['GET'])
def getAll():
    return get_all()

# Ruta para insertar un restaurante
@bp.route('/insert_restaurant', methods=['POST'])
def insertRestaurant():
    # Obtener los datos del restaurante del cuerpo de la solicitud en formato JSON
    restaurant_data = request.json

    # Llamar a la función insert_restaurant para realizar la inserción
    return insert_restaurant(restaurant_data)

# Ruta para actualizar un restaurante
@bp.route('/update_restaurant', methods=['PUT'])
def updateRestaurant():
    # Obtener los datos de actualización del restaurante del cuerpo de la solicitud en formato JSON
    restaurant_data = request.json

    # Llamar a la función update_restaurant para realizar la actualización
    return update_restaurant(restaurant_data)

# Ruta para eliminar un restaurante
@bp.route('/delete_restaurant/<restaurant_id>', methods=['DELETE'])
def deleteRestaurant(restaurant_id):
    # Llamar a la función delete_restaurant para realizar la eliminación
    return delete_restaurant(restaurant_id)

# Ruta para obtener un restaurante por parámetro
@bp.route('/get_one', methods=['GET'])
def getOne():
    # Obtener el nombre del parámetro y su valor de la solicitud
    param_name = request.args.get('param_name')
    param_value = request.args.get('param_value')

    # Obtener un restaurante por parámetro
    return get_by_param(param_name, param_value)

# Ruta para obtener estadísticas de restaurantes
@bp.route('/restaurants/statistics', methods=['GET'])
def restaurantsStatistics():
    # Obtener los parámetros de la solicitud: latitud, longitud y radio
    latitude = float(request.args.get('latitude'))
    longitude = float(request.args.get('longitude'))
    radius = float(request.args.get('radius'))

    # Calcular y devolver las estadísticas
    return calculate_statistics(latitude, longitude, radius)
