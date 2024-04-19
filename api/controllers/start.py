import csv
from services.services import conectionDb

def createTable():
    try:
        # Definir el nombre del archivo CSV y la tabla
        csv_file = '/app/files/restaurantes.csv'
        table_name = 'Restaurants'

        # Definir la consulta SQL para crear la tabla si no existe
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS {} (
            id TEXT PRIMARY KEY,
            rating INTEGER,
            name TEXT,
            site TEXT,
            email TEXT,
            phone TEXT,
            street TEXT,
            city TEXT,
            state TEXT,
            lat FLOAT,
            lng FLOAT
        );
        '''.format(table_name)

        # Conexión a la base de datos
        conn_db = conectionDb()
        cursor = conn_db.conn.cursor()
        
        # Ejecutar la consulta para crear la tabla
        cursor.execute(create_table_query)
        conn_db.conn.commit()
        print("Se creó la tabla Restaurants")

        # Abrir el archivo CSV y leer los datos
        with open(csv_file, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Saltar la fila de encabezado
            for row in reader:
                # Insertar cada fila en la tabla
                insert_query = '''
                INSERT INTO {} (id, rating, name, site, email, phone, street, city, state, lat, lng)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
                '''.format(table_name)
                cursor.execute(insert_query, row)

        conn_db.conn.commit()

    except Exception as e:
        # Manejar cualquier excepción que pueda ocurrir durante la consulta
        print("Error:", str(e))
        return {'error': str(e)}
    
    finally:
        # Cerrar el cursor y la conexión a la base de datos
        if cursor:
            cursor.close()

        if conn_db:
            conn_db.close()

if __name__ == "__main__":
    createTable()
