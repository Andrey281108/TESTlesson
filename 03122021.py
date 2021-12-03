import sqlite3
from sqlite3 import Error

PATH = 'awdawd.db'

def add_data(connection):
    cursor = connection.cursor()

    add_query = '''
        INSERT INTO python_table
        VALUES(2, 'b', 'd', '2021-11-12 19:16', 647);
        '''

    cursor.execute(add_query)
    connection.commit()
    cursor.close()