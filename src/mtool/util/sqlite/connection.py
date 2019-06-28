"""
This file contains the create connection function used by all pf the sqlite files
"""

import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """creates the connection to the database specified"""
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
        return None
