from flask import request, jsonify
from services.services import conectionDb
import numpy as np

def calculate_statistics(latitude, longitude, radius):
    try:
        # Conexión a la base de datos
        conn_db = conectionDb()
        cursor = conn_db.conn.cursor()

        # Calcular el radio en grados de latitud y longitud
        radius_degrees = radius / 111000  # Aproximadamente 111 km por grado de latitud o longitud

        # Calcular el área cuadrada cubierta por el círculo
        min_lat = latitude - radius_degrees
        max_lat = latitude + radius_degrees
        min_lng = longitude - radius_degrees
        max_lng = longitude + radius_degrees

        # Consulta SQL para obtener restaurantes dentro del área cuadrada
        query = '''
        SELECT rating
        FROM Restaurants
        WHERE lat BETWEEN %s AND %s
        AND lng BETWEEN %s AND %s;
        '''
        cursor.execute(query, (min_lat, max_lat, min_lng, max_lng))

        # Obtener calificaciones de restaurantes dentro del área cuadrada
        ratings = [row[0] for row in cursor.fetchall()]

        # Calcular el número de restaurantes dentro del círculo
        count = len(ratings)

        # Calcular la calificación promedio
        avg_rating = np.mean(ratings) if count > 0 else None

        # Calcular la desviación estándar de las calificaciones
        std_deviation = np.std(ratings) if count > 0 else None

        # Crear el JSON de respuesta
        response = {
            'count': count,
            'avg': avg_rating,
            'std': std_deviation
        }

        return jsonify(response)

    except Exception as e:
        # Manejar cualquier excepción que pueda ocurrir durante el cálculo de estadísticas
        return jsonify({'error': str(e)})

    finally:
        # Cerrar el cursor y la conexión a la base de datos
        if cursor:
            cursor.close()

        if conn_db:
            conn_db.close()
