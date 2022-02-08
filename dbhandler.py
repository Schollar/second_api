import dbcreds
import mariadb as db

# Connect function that starts a DB connection and creates a cursor


def db_connect():
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


def db_disconnect(conn, cursor):
    try:
        cursor.close()
    except:
        print('Error closing cursor')
    try:
        conn.close()
    except:
        print('Error closing connection')

# Function that takes in an optional limit argument. If the limit comes through as None, we dont limit the results and grab all items from DB
# If user sends a limit param, we use fetchmany and use limit as the number  for fetchmany


def get_items(limit):
    limit = int(limit)
    items = []
    conn, cursor = db_connect()
    try:
        cursor.execute(
            "SELECT name, description, created_at, quantity FROM item")
        if(limit == None):
            items = cursor.fetchall()
        else:
            items = cursor.fetchmany(limit)
    except db.OperationalError:
        print('Something went  wrong with the db!')
    except db.ProgrammingError:
        print('Error running DB query')
    db_disconnect(conn, cursor)
    return items

# Function that expects an id to be passed to it, and it selects user from DB corresponding to id it is given


def get_employee(id):
    employee = []
    conn, cursor = db_connect()
    try:
        cursor.execute(
            "SELECT name, hired_at, hourly_wage FROM employee WHERE id = ?", [id, ])
        employee = cursor.fetchone()
    except db.OperationalError:
        print('Something went  wrong with the db!')
    except db.ProgrammingError:
        print('Error running DB query')
    db_disconnect(conn, cursor)

    return True, employee

# Function that takes in item name, description and quantity and adds a new item to the DB


def add_item(name, description, quantity):
    conn, cursor = db_connect()
    try:
        cursor.execute(
            "INSERT INTO item (name, description, quantity) VALUES (?, ?, ?)", [name, description, quantity])

    except db.OperationalError:
        print('Something is wrong with the db!')
    except db.ProgrammingError:
        print('Error running DB query')
    conn.commit()
    db_disconnect(conn, cursor)

    return True

# Function that takes in  name, and wage and adds a new employee to the DB


def add_employee(name, hourly_wage):
    conn, cursor = db_connect()
    try:
        cursor.execute(
            "INSERT INTO employee (name, hourly_wage) VALUES (?, ?)", [name, hourly_wage])

    except db.OperationalError:
        print('Something is wrong with the db!')
    except db.ProgrammingError:
        print('Error running DB query')
    conn.commit()
    db_disconnect(conn, cursor)

    return True

# Function that takes in item ID,  and quantity, changes item's quantity where the ID matches the ID passed to function


def change_item(id, quantity):
    conn, cursor = db_connect()
    try:
        cursor.execute(
            "UPDATE item SET quantity = ? WHERE id = ?", [quantity, id])

    except db.OperationalError:
        print('Something is wrong with the db!')
    except db.ProgrammingError:
        print('Error running DB query')
    conn.commit()
    db_disconnect(conn, cursor)

    return True

# Function that takes in employee ID, and wage then changes employee's wage where the ID matches the ID passed to function


def change_employee(id, wage):
    conn, cursor = db_connect()
    try:
        cursor.execute(
            "UPDATE employee SET hourly_wage = ? WHERE id = ?", [wage, id])

    except db.OperationalError:
        print('Something is wrong with the db!')
    except db.ProgrammingError:
        print('Error running DB query')
    conn.commit()
    db_disconnect(conn, cursor)

    return True

# Function that takes in a employee ID number and deletes that employee from the DB


def delete_employee(id):
    conn, cursor = db_connect()
    try:
        cursor.execute(
            "DELETE FROM employee WHERE id = ?", [id, ])

    except db.OperationalError:
        print('Something is wrong with the db!')
    except db.ProgrammingError:
        print('Error running DB query')
    conn.commit()
    db_disconnect(conn, cursor)

    return True

# Function that takes in a item ID number and deletes that item from the DB


def delete_item(id):
    conn, cursor = db_connect()
    try:
        cursor.execute(
            "DELETE FROM item WHERE id = ?", [id, ])

    except db.OperationalError:
        print('Something is wrong with the db!')
    except db.ProgrammingError:
        print('Error running DB query')
    conn.commit()
    db_disconnect(conn, cursor)

    return True
