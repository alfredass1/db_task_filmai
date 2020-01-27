import sqlite3

def open_connection():
    connection = sqlite3.connect("movies.db")
    cursor = connection.cursor()
    return connection, cursor


def close_connection(connection, cursor):
    cursor.close()
    connection.close()

# apejimas
def insert_query(query, params=None):
    try:
        connection, cursor = open_connection()
        if params:
            cursor.execute(query, params)
            connection.commit()

    except sqlite3.DataError as error:
        print(error)
    finally:
        connection.close()


def get_database(query,params=None):
    try:
        connection, cursor = open_connection()
        if params:
            for row in cursor.execute(query, params):
                print(row)
        else:
            for row in cursor.execute(query):
                print(row)

    except sqlite3.DataError as error:
        print(error)
    finally:
        connection.close()




def create_table_database(query):
    try:
        connection, cursor = open_connection()
        cursor.execute(query)
        connection.commit()
    except sqlite3.DataError as error:
        print(error)
    finally:
        connection.close()


