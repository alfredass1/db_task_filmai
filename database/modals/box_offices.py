from database.database import create_table_database, insert_query, get_database
from entities.box_office import box_office

def create_box_offices_table():
    query = """CREATE TABLE IF NOT EXISTS box_offices (
                        box_office_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        box_office_gross REAL)"""
    create_table_database(query)


def create_box_office(box_office):
    query = """INSERT INTO box_offices (box_office_id, box_office_gross) 
                          VALUES(?, ?)"""
    params = (box_office.box_office_id, box_office.box_office_gross)
    insert_query(query, params)

def get_box_office():
    query = "SELECT * FROM box_office"
    get_database(query)

def update_box_office(box_office):
    query = "UPDATE box_offices SET box_office_gross = ? WHERE box_office_id = ?"
    params = (box_office.box_office_gross, box_office.box_office_id)
    insert_query(query, params)

def delete_box_office(box_office):
    query =  "DELETE FROM box_offices WHERE box_office_id = ?"
    params = (box_office.box_office_id)
    insert_query(query, params)


boxoffices1 = box_office(None, 35000)
