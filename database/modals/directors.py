from database.database import create_table_database


def create_directors_table():
    query = """CREATE TABLE IF NOT EXISTS directors (
                        director_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT)"""
    create_table_database(query)


def create_directors_movies_table():
    query = """CREATE TABLE IF NOT EXISTS actors_movies (
                        director_movie_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        movie_id  FOREIGN KEY (movie_id) REFERENCES actors(movie_id),
                        director_id  FOREIGN KEY (director_id) REFERENCES actors(director_id)"""
    create_table_database(query)



create_directors_table()
create_directors_movies_table()