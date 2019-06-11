import sqlite3

from sqlite3 import Error

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        conn.close()

def init_scene(db_file, table_name):
    import uuid

    try:
        conn = sqlite3.connect(db_file)
        c = conn.cursor()
        
        scene_id = str(uuid.uuid4())
        c.execute(f'CREATE TABLE "scene" (ID TEXT PRIMARY KEY)')
        c.execute(f'INSERT INTO "scene" VALUES("{scene_id}")')
    except Error as e:
        print(e)
    finally:
        conn.close()