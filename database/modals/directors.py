from database.database import create_table_database, insert_query, get_database
from entities.director import director


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


# create_directors_movies_table()

# get_database('PRAGMA table_info(directors)')

# create_table_database('DROP TABLE directors')

def create_director(director):
    query = "INSERT INTO directors VALUES (? ,?)"
    params = (director.director_id, director.name)
    insert_query(query, params)


def get_director(director):
    query = "SELECT * FROM directors WHERE director_id = (?) OR name = (?)"
    params = (director.director_id, director.name)
    get_database(query, params)


def update_director(director):
    query = "UPDATE directors SET name = 'johnAS' WHERE name = (?)"
    params = (director.name,)
    insert_query(query, params)


def delete_director(director):
    query = "DELETE FROM directors WHERE director_id = (?) OR name = (?)"
    params = (director.director_id, director.name)
    insert_query(query, params)



# create_director(director1)

# get_director(director1)

# update_director(director1)

# delete_director(director1)
director1 = director(None, "Bet kaS")
