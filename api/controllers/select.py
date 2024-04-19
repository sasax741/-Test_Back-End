from services.services import conectionDb  # Importa la función de conexión a la base de datos
from flask import jsonify  # Importa la función jsonify desde Flask

def get_by_param(param_name, param_value):
    try:
        # Establece la conexión a la base de datos
        conn_db = conectionDb()
        cursor = conn_db.conn.cursor()

        # Define la consulta SQL dinámica para seleccionar un registro que coincida con el criterio de búsqueda
        select_query = f"SELECT * FROM restaurants.public.restaurants WHERE {param_name} = %s"

        # Ejecuta la consulta SQL con el valor del parámetro
        cursor.execute(select_query, (param_value,))
        result = cursor.fetchone()

        # Si se encuentra un resultado, convierte los datos a formato JSON y los devuelve
        if result:
            result_json = {
                'id': result[0],
                'rating': result[1],
                'name': result[2],
                'site': result[3],
                'email': result[4],
                'phone': result[5],
                'street': result[6],
                'city': result[7],
                'state': result[8],
                'lat': result[9],
                'lng': result[10]
            }
            return jsonify(result_json)
        else:
            # Si no se encuentra ningún registro, devuelve un mensaje indicando que no se encontró ningún resultado
            return jsonify({'message': f"No se encontró ningún registro con el parámetro {param_name} igual a {param_value}"})

    except Exception as e:
        # Maneja cualquier excepción que pueda ocurrir durante la consulta
        return jsonify({'error': str(e)})
    
    finally:
        # Cierra el cursor y la conexión a la base de datos al finalizar
        if cursor:
            cursor.close()

        if conn_db:
            conn_db.close()
