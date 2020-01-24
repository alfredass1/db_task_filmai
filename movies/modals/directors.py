from movies.database import create_table_database


def create_directors_table():
    query = """CREATE TABLE IF NOT EXISTS directors (
                        director_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        director_name TEXT)"""
    create_table_database(query)


create_directors_table()
