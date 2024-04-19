import psycopg2


class conectionDb:
    def __init__(self):
        self.conn = self.connected()
    
    def connected(self):
        return  psycopg2.connect(
                    database="restaurants",
                    user="root",
                    password="T3mp0r4l",
                    host="db",
                    port="5432"
                )
    def close(self):
        if self.conn:
            self.conn.close()