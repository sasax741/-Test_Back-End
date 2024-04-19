from services.services import conectionDb 
from flask import jsonify  

def insert_restaurant(params):
    try:
        # Establece la conexión a la base de datos
        conn_db = conectionDb()
        cursor = conn_db.conn.cursor()

        # Construye la sentencia SQL de inserción
        insert_query = '''
        INSERT INTO restaurants.public.restaurants (id, rating, name, site, email, phone, street, city, state, lat, lng)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        '''

        # Ejecuta la sentencia SQL de inserción con los parámetros proporcionados
        cursor.execute(insert_query, (
            params['id'],
            params['rating'],
            params['name'],
            params['site'],
            params['email'],
            params['phone'],
            params['street'],
            params['city'],
            params['state'],
            params['lat'],
            params['lng']
        ))

        # Confirma la transacción
        conn_db.conn.commit()

        # Devuelve un mensaje de éxito en formato JSON
        return jsonify({'message': 'Registro insertado exitosamente'})

    except Exception as e:
        # Maneja cualquier excepción que pueda ocurrir durante la inserción
        return jsonify({'error': str(e)})
    
    finally:
        # Cierra el cursor y la conexión a la base de datos al finalizar
        if cursor:
            cursor.close()

        if conn_db:
            conn_db.close()
