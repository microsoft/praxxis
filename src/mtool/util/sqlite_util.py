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
    create_current_scene_table = 'CREATE TABLE "CurrentScene" (ID INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT, Ended INTEGER)'
    cur.execute(create_current_scene_table)
    conn.commit()
    conn.close()


def update_current_scene(db_file, scene_name):
    conn = create_connection(db_file)
    cur =  conn.cursor()
    add_current_scene = f'INSERT INTO "CurrentScene"(Name, Ended) VALUES("{scene_name}", 0)'
    cur.execute(add_current_scene)
    conn.commit()
    conn.close()


def get_current_scene(db_file):
    conn = create_connection(db_file)
    cur = conn.cursor()
    get_current_scene = 'SELECT Name FROM "CurrentScene" WHERE Ended != 1 ORDER BY ID DESC LIMIT 0, 1'
    cur.execute(get_current_scene)
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


def mark_ended_scene(db_file, name):
    rows = get_active_scenes(db_file)
    if len(rows) <= 1:
        #TODO: make this print a good print
        print("Can't end current scene, it's the only active scene you have. Make a new scene.")
        return 0
    else:
        conn = create_connection(db_file)
        cur = conn.cursor()
        end_scene = f'UPDATE "CurrentScene" SET Ended = 1 WHERE Name = "{name}"'
        cur.execute(end_scene)
        conn.commit()
        conn.close()
        return 1
    return 0


def resume_scene(db_file, name):
    conn = create_connection(db_file)
    cur = conn.cursor()
    end_scene = f'UPDATE "SceneMetadata" SET Ended = 0 WHERE Name = "{name}"'
    cur.execute(end_scene)
    conn.commit()
    conn.close()


def get_active_scenes(db_file):
    conn = create_connection(db_file)
    cur = conn.cursor()
    get_active_scenes = f'SELECT DISTINCT Name from "CurrentScene" WHERE Ended = 0'
    cur.execute(get_active_scenes)
    rows = cur.fetchall()
    conn.close()
    return rows

def get_ended_scenes(db_file):
    conn = create_connection(db_file)
    cur = conn.cursor()
    get_ended_scenes = f'SELECT DISTINCT Name from "CurrentScene" WHERE Ended = 1'
    cur.execute(get_ended_scenes)
    rows = cur.fetchall()
    conn.close()
    return rows


def get_scene_id(db_file):
    conn = create_connection(db_file)
    cur = conn.cursor()

