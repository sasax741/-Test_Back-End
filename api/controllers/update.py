from services.services import conectionDb
from flask import jsonify

def update_restaurant(restaurant_data):
    try:
        # Establecemos la conexión a la base de datos
        conn_db = conectionDb()
        cursor = conn_db.conn.cursor()

        # Comprobamos si restaurant_data tiene los campos necesarios
        if 'id' in restaurant_data and 'campo' in restaurant_data and 'valor' in restaurant_data:
            # Construimos la sentencia SQL de actualización
            update_query = f'''
            UPDATE restaurants.public.restaurants
            SET {restaurant_data['campo']} = %s
            WHERE id = %s
            '''
            # Ejecutamos la sentencia SQL de actualización
            cursor.execute(update_query, (restaurant_data['valor'], restaurant_data['id']))

            # Confirmamos la transacción
            conn_db.conn.commit()

            # Retornamos un mensaje de éxito
            return jsonify({'message': 'Registro actualizado exitosamente'})
        else:
            # Retornamos un mensaje de error si falta algún campo
            return jsonify({'error': 'Faltan campos obligatorios en los datos proporcionados'})

    except Exception as e:
        # Manejamos cualquier excepción que pueda ocurrir durante la actualización
        return jsonify({'error': str(e)})
    
    finally:
        # Cerramos el cursor y la conexión a la base de datos
        if cursor:
            cursor.close()

        if conn_db:
            conn_db.close()
