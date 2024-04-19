from services.services import conectionDb
from flask import jsonify

def update_restaurant(restaurant_data):
    try:
        # Establecemos la conexión a la base de datos
        conn_db = conectionDb()
        cursor = conn_db.conn.cursor()

        # Comprobamos si restaurant_data tiene solo un campo a actualizar
        if len(restaurant_data) == 2 and 'id' in restaurant_data and 'update_field' in restaurant_data:
            # Construimos la sentencia SQL de actualización para actualizar un solo campo
            update_query = f'''
            UPDATE restaurants.public.restaurants
            SET {restaurant_data['update_field']} = %s
            WHERE id = %s
            '''
            # Ejecutamos la sentencia SQL de actualización
            cursor.execute(update_query, (restaurant_data['value'], restaurant_data['id']))
        else:
            # Construimos la sentencia SQL de actualización para actualizar todos los campos
            update_query = '''
            UPDATE restaurants.public.restaurants
            SET rating = %s, name = %s, site = %s, email = %s, phone = %s,
                street = %s, city = %s, state = %s, lat = %s, lng = %s
            WHERE id = %s
            '''
            # Ejecutamos la sentencia SQL de actualización
            cursor.execute(update_query, (
                restaurant_data['rating'],
                restaurant_data['name'],
                restaurant_data['site'],
                restaurant_data['email'],
                restaurant_data['phone'],
                restaurant_data['street'],
                restaurant_data['city'],
                restaurant_data['state'],
                restaurant_data['lat'],
                restaurant_data['lng'],
                restaurant_data['id']
            ))

        # Confirmamos la transacción
        conn_db.conn.commit()

        # Retornamos un mensaje de éxito
        return jsonify({'message': 'Registro actualizado exitosamente'})

    except Exception as e:
        # Manejamos cualquier excepción que pueda ocurrir durante la actualización
        return jsonify({'error': str(e)})
    
    finally:
        # Cerramos el cursor y la conexión a la base de datos
        if cursor:
            cursor.close()

        if conn_db:
            conn_db.close()
