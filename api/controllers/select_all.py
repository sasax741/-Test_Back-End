from services.services import conectionDb  
from flask import jsonify  

def get_all():
    try:
        # Establece la conexión a la base de datos
        conn_db = conectionDb()

        # Crea un cursor para ejecutar consultas SQL
        cursor = conn_db.conn.cursor()
        
        # Ejecuta la consulta SQL para obtener todos los registros de la tabla
        cursor.execute("SELECT * FROM restaurants.public.restaurants r")

        # Obtiene todos los resultados de la consulta
        result = cursor.fetchall()

        # Convierte los resultados a formato JSON
        result_json = [
            {
                'id': resultado[0],
                'rating': resultado[1],
                'name': resultado[2],
                'site': resultado[3],
                'email': resultado[4],
                'phone': resultado[5],
                'street': resultado[6],
                'city': resultado[7],
                'state': resultado[8],
                'lat': resultado[9],
                'lng': resultado[10]
            }
            for resultado in result
        ]

        # Devuelve los datos en formato JSON utilizando la función jsonify
        return jsonify(result_json)

    except Exception as e:
        # Maneja cualquier excepción que pueda ocurrir durante la consulta
        return jsonify({'error': str(e)})
    
    finally:
        # Cierra el cursor y la conexión a la base de datos al finalizar
        if cursor:
            cursor.close()

        if conn_db:
            conn_db.close()  
