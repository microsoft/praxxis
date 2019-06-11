import sqlite3

from sqlite3 import Error

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
        return None

def init_scene(db_file):
    import uuid

    conn=create_connection(db_file)
    cur = conn.cursor()

    scene_id = str(uuid.uuid4())

    create_metadata_table = f'CREATE TABLE "scene_metadata" (ID TEXT PRIMARY KEY, Ended INTEGER)'
    create_list_table=f'CREATE TABLE "List" (ID INTEGER PRIMARY KEY AUTOINCREMENT, Timestamp INTEGER, Data TEXT)'
    create_environment_table=f'CREATE TABLE "Environment" (Name TEXT PRIMARY KEY, Value TEXT)'
    create_history_table=f'CREATE TABLE "History" (Timestamp INTEGER, Notebook, TEXT, Library TEXT)'
    init_metadata_table = f'insert into "scene_metadata"(ID, ended) values("{scene_id}", 0)'
    
    cur.execute(create_metadata_table)
    cur.execute(create_list_table)
    cur.execute(create_environment_table)
    cur.execute(create_history_table)
    cur.execute(init_metadata_table)
    conn.commit()
    conn.close()

def init_current_scene(db_file, scene_name):
    conn = create_connection(db_file)
    cur = conn.cursor()
    create_current_scene_table = 'CREATE TABLE "CurrentScene" (ID INTEGER, Name TEXT PRIMARY KEY)'
    init_current_scene_table = f'insert into "CurrentScene"(ID, Name) values (0, "{scene_name}")'
    cur.execute(create_current_scene_table)
    cur.execute(init_current_scene_table)
    conn.commit()
    conn.close()


def update_current_scene(db_file, scene_name):
    conn = create_connection(db_file)
    cur =  conn.cursor()
    update_current_scene = f'UPDATE "CurrentScene" SET Name = {scene_name} WHERE "ID" = 0' 
    cur.execute(update_current_scene)
    conn.commit()
    conn.close()

def get_current_scene(db_file):
    conn = create_connection(db_file)
    cur = conn.cursor()
    get_current_scene = 'SELECT Name FROM "CurrentScene" WHERE ID = 0'
    name = cur.execute(get_current_scene)
    rows = cur.fetchall()
    conn.close()
    return rows[0][0]


def get_scene_id(db_file):
    conn = create_connection(db_file)
    cur = conn.cursor()

