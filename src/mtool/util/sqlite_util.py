import sqlite3

from sqlite3 import Error

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
        return None


def init_scene(db_file, name):
    import uuid

    conn=create_connection(db_file)
    cur = conn.cursor()

    scene_id = str(uuid.uuid4())

    create_metadata_table = f'CREATE TABLE "SceneMetadata" (ID TEXT PRIMARY KEY, Ended INTEGER, Name TEXT)'
    create_list_table=f'CREATE TABLE "List" (ID INTEGER PRIMARY KEY AUTOINCREMENT, Timestamp INTEGER, Data TEXT)'
    create_environment_table=f'CREATE TABLE "Environment" (Name TEXT PRIMARY KEY, Value TEXT)'
    create_history_table=f'CREATE TABLE "History" (Timestamp INTEGER, Notebook, TEXT, Library TEXT)'
    init_metadata_table = f'insert into "SceneMetadata"(ID, Ended, Name) values("{scene_id}", 0, "{name}")'
    
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
    create_current_scene_table = 'CREATE TABLE "CurrentScene" (ID INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT)'
    init_current_scene_table = f'insert into "CurrentScene"(Name) values ("{scene_name}")'
    cur.execute(create_current_scene_table)
    cur.execute(init_current_scene_table)
    conn.commit()
    conn.close()


def update_current_scene(db_file, scene_name):
    conn = create_connection(db_file)
    cur =  conn.cursor()
    add_current_scene = f'INSERT INTO "CurrentScene"(Name) VALUES("{scene_name}")'
    cur.execute(add_current_scene)
    conn.commit()
    conn.close()


def get_current_scene(db_file):
    conn = create_connection(db_file)
    cur = conn.cursor()
    get_current_scene = 'SELECT Name FROM "CurrentScene" ORDER BY id DESC LIMIT 0, 1'
    cur.execute(get_current_scene)
    rows = cur.fetchall()
    conn.close()
    return rows[0][0]


def get_next_scene(db_file, name):
    conn = create_connection(db_file)
    cur = conn.cursor()
    get_next_scene = f'SELECT Name FROM "CurrentScene" WHERE Name != "{name}" ORDER BY id DESC LIMIT 0, 1'
    cur.execute(get_next_scene)
    rows = cur.fetchall()
    conn.close()
    return rows[0][0]


def delete_scene(db_file, name):
    conn = create_connection(db_file)
    cur = conn.cursor()
    delete_scene = f'DELETE FROM "CurrentScene" WHERE Name = "{name}"'
    cur.execute(delete_scene)
    conn.commit()
    conn.close()


def end_scene(db_file, name):
    conn = create_connection(db_file)
    cur = conn.cursor()
    end_scene = f'UPDATE "SceneMetadata" SET Ended = 1 WHERE Name = "{name}"'
    cur.execute(end_scene)
    conn.commit()
    conn.close()


def resume_scene(db_file, name):
    conn = create_connection(db_file)
    cur = conn.cursor()
    end_scene = f'UPDATE "SceneMetadata" SET Ended = 0 WHERE Name = "{name}"'
    cur.execute(end_scene)
    conn.commit()
    conn.close()


def get_scene_id(db_file):
    conn = create_connection(db_file)
    cur = conn.cursor()

