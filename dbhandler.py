import dbcreds
import mariadb as db


class dbInteraction:
    # Connect function that starts a DB connection and creates a cursor
    def db_connect(self):
        conn = None
        cursor = None
        try:
            conn = db.connect(user=dbcreds.user, password=dbcreds.password,
                              host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
            cursor = conn.cursor()
        except db.OperationalError:
            print('Something is wrong with the DB')
        except:
            print('Something went wrong connecting to the DB')
        return conn, cursor
# Disconnect function that takes in the conn and cursor and attempts to close both

    def db_disconnect(self, conn, cursor):
        try:
            cursor.close()
        except:
            print('Error closing cursor')
        try:
            conn.close()
        except:
            print('Error closing connection')

    def get_items(self):
        items = []
        conn, cursor = self.db_connect()
        try:
            cursor.execute(
                "SELECT name, description, created_at, quantity FROM item")
            items = cursor.fetchall()
        except db.OperationalError:
            print('Something went  wrong with the db!')
        except db.ProgrammingError:
            print('Error running DB query')
        self.db_disconnect(conn, cursor)
        return items
