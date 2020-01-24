from movies.database import create_table_database


def create_actors_table():
    query = """CREATE TABLE IF NOT EXISTS actors (
                        actor_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        actor_name TEXT)"""
    create_table_database(query)


create_actors_table()
