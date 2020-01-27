from database.database import create_table_database


def create_genres_table():
    query = """CREATE TABLE IF NOT EXISTS genres (
                        genre_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT)"""
    create_table_database(query)


def create_movies_genres_table():
    query = """CREATE TABLE IF NOT EXISTS movie_genres (
                        genre_movie_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        genre_id  FOREIGN KEY (genre_id) REFERENCES actors(genre_id),
                        movie_id  FOREIGN KEY (movie_id) REFERENCES actors(movie_id)"""
    create_table_database(query)


create_genres_table()
create_movies_genres_table()
