from database.database import create_table_database, insert_query, get_database
from entities.actor import actor


def create_actors_table():
    query = """CREATE TABLE IF NOT EXISTS actors (
                        actor_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        actor_name TEXT)"""
    create_table_database(query)


def create_actors_movies_table():
    query = """CREATE TABLE IF NOT EXISTS actors_movies (
                        actor_movie_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        actor_id  FOREIGN KEY (actor_id) REFERENCES actors(actor_id),
                        movie_id FOREIGN KEY (movie_id) REFERENCES movies(movie_id))"""
    create_table_database(query)


create_actors_table()


# create_actors_movies_table()

# create_table_database('DROP TABLE actors')

# get_database('PRAGMA table_info(actors)')

def create_actor(actor):
    query = "INSERT INTO actors VALUES (? ,?)"
    params = (actor.actor_id, actor.actor_name)
    insert_query(query, params)


actor1 = actor(None, "Bet kas")


def get_actor(actor):
    query = "SELECT * FROM actors WHERE actor_id = (?) OR actor_name = (?)"
    params = (actor.actor_id, actor.actor_name)
    get_database(query, params)


def update_actor(actor):
    query = "UPDATE actors SET actor_name = 'Bet kas' WHERE actor_name = (?)"
    params = (actor.actor_name,)
    insert_query(query, params)


get_actor(actor1)
update_actor(actor1)
create_actor(actor1)
