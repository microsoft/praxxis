import sqlite3

from sqlite3 import Error

#TODO: sql injection is scary and bad

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
    create_list_table=f'CREATE TABLE "List" (ID INTEGER PRIMARY KEY, Data TEXT, Path TEXT)'
    create_environment_table=f'CREATE TABLE "Environment" (Name TEXT PRIMARY KEY, Value TEXT)'
    create_history_table=f'CREATE TABLE "History" (Timestamp INTEGER, Notebook TEXT, Library TEXT)'
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

    ended = check_ended(db_file, name, conn, cur)
    if ended == -1:
        return 0
        
    active_scenes = get_active_scenes(db_file)
    if len(active_scenes) <= 1 and ended != 1:
        #TODO: make this print a good print
        print("Can't delete current scene, it's the only active scene you have. Make a new scene or restart an old one")
        return 0
    else:
        delete_scene = f'DELETE FROM "CurrentScene" WHERE Name = "{name}"'
        cur.execute(delete_scene)
        conn.commit()
        conn.close()
        return 1
    return 0

def end_scene(db_file, name):
    conn = create_connection(db_file)
    cur = conn.cursor()
    end_scene = f'UPDATE "SceneMetadata" SET Ended = 1 WHERE Name = "{name}"'
    cur.execute(end_scene)
    conn.commit()
    conn.close()

def check_ended(db_file, name, conn, cur):
    ended = f'SELECT Ended from "CurrentScene" WHERE Name = "{name}"'
    cur.execute(ended)
    ended = cur.fetchall()
    if ended == []:
        print("scene does not exist")
        return -1
    return ended[0][0]

def mark_ended_scene(db_file, name):
    conn = create_connection(db_file)
    cur = conn.cursor()

    ended = check_ended(db_file, name, conn, cur)
    if ended == -1:
        return 0

    active_scenes = get_active_scenes(db_file)
    if len(active_scenes) <= 1 and ended != 1:
        #TODO: make this print a good print
        print("Can't end current scene, it's the only active scene you have. Make a new scene or restart an old one")
        return 0
    else:
        end_scene = f'UPDATE "CurrentScene" SET Ended = 1 WHERE Name = "{name}"'
        cur.execute(end_scene)
        conn.commit()
        conn.close()
        return 1
    return 0

def mark_resumed_scene(db_file, name):
    conn = create_connection(db_file)
    cur = conn.cursor()
    end_scene = f'UPDATE "CurrentScene" SET Ended = 0 WHERE Name = "{name}"'
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

def list_env(db_file):
    conn = create_connection(db_file)
    cur = conn.cursor()
    list_env = f'SELECT * FROM "Environment"'
    cur.execute(list_env)
    conn.commit()
    rows = cur.fetchall()
    conn.close()
    return rows

def get_env(db_file, var_name):
    conn = create_connection(db_file)
    cur = conn.cursor()
    get_env = f'SELECT Value FROM "Environment" WHERE Name = ?'
    cur.execute(get_env, (var_name,))
    conn.commit()
    value = cur.fetchone()   #just a value, not the tuple
    conn.close()
    return value

def set_env(db_file, name, value):
    conn = create_connection(db_file)
    cur = conn.cursor()
    set_env = f'INSERT INTO "Environment"(Name, Value) VALUES("{name}", "{value}")'
    cur.execute(set_env)
    conn.commit()
    conn.close()

def delete_env(db_file, name):
    conn = create_connection(db_file)
    cur = conn.cursor()
    delete_env = f'DELETE FROM "Environment" where Name = "{name}"'
    cur.execute(delete_env)
    conn.commit()
    conn.close()

def get_scene_id(db_file):
    conn = create_connection(db_file)
    cur = conn.cursor()

def write_scene_list(db_file, input):
    conn = create_connection(db_file)
    cur = conn.cursor()
    clear_list = f'DELETE FROM "List"'
    insert_line = f'INSERT INTO "List" (ID, DATA, PATH) VALUES (?,?,?)'
    cur.execute(clear_list)
    cur.executemany(insert_line, input)
    conn.commit()
    conn.close()

    
def ordinal_to_list_item(db_file, ordinal):
    """Returns list item referenced by input ordinal"""
    conn = create_connection(db_file)
    cur = conn.cursor()
    if str.isnumeric(ordinal):
        query = f'SELECT DATA, PATH FROM List WHERE ID = ?'
    else:
        query = f'SELECT DATA, PATH FROM LIST WHERE DATA = ?'
    cur.execute(query, ordinal)
    conn.commit()
    item = cur.fetchone()
    conn.close()
    return item