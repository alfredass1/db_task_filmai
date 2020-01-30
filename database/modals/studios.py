from database.database import create_table_database, insert_query, get_database
from entities.studio import studio

def create_studios_table():
    query = """CREATE TABLE IF NOT EXISTS studios (
                        studio_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        studio_name TEXT)"""
    create_table_database(query)

create_studios_table()


# create_table_database('DROP TABLE studios')

# get_database('PRAGMA table_info(studios)')

def create_studio(studio):
    query = "INSERT INTO studios VALUES (? ,?)"
    params = (studio.studio_id, studio.studio_name)
    insert_query(query, params)


studio2 = studio(None, "Warner bros")

def get_studio(studio):
    query = "SELECT * FROM studios WHERE studio_id = (?) OR studio_name = (?)"
    params = (studio.studio_id, studio.studio_name)
    get_database(query, params)

def update_studio(studio):
    query = "UPDATE studios SET studio_name = 'Picture' WHERE studio_name = (?)"
    params = (studio.studio_name,)
    insert_query(query, params)

def delete_studio(studio):
    query = "DELETE FROM studios WHERE studio_id = (?) OR studio_name = (?)"
    params = (studio.studio_id, studio.studio_name)
    insert_query(query, params)



# create_studio(studio2)
# get_studio(studio2)
# update_studio(studio2)
# delete_studio(studio2)