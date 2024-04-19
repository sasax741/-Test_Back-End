from services.services import conectionDb
from flask import jsonify

def delete_restaurant(restaurant_id):
    try:
        # Establece la conexión a la base de datos
        conn_db = conectionDb()
        cursor = conn_db.conn.cursor()

        # Construye la sentencia SQL de eliminación
        delete_query = '''
        DELETE FROM restaurants.public.restaurants
        WHERE id = %s
        '''

        # Ejecuta la sentencia SQL de eliminación
        cursor.execute(delete_query, (restaurant_id,))

        # Confirma la transacción
        conn_db.conn.commit()

        # Devuelve un mensaje de éxito en formato JSON
        return jsonify({'message': 'Registro eliminado exitosamente'})

    except Exception as e:
        # Maneja cualquier excepción que pueda ocurrir durante la eliminación
        return jsonify({'error': str(e)})
    
    finally:
        # Cierra el cursor y la conexión a la base de datos al finalizar
        if cursor:
            cursor.close()

        if conn_db:
            conn_db.close()
