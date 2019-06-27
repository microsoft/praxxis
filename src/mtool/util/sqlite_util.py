"""
This file is responsible for handling all of the sqlite queries throughout mtool
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


def init_scene(db_file, name):
    """initializes the scene db"""
    #TODO: handle strings
    import uuid

    conn=create_connection(db_file)
    cur = conn.cursor()

    scene_id = str(uuid.uuid4())

    create_metadata_table = f'CREATE TABLE "SceneMetadata" (ID TEXT PRIMARY KEY, Ended INTEGER, Name TEXT)'
    create_notebook_list_table=f'CREATE TABLE "NotebookList" (ID INTEGER PRIMARY KEY AUTOINCREMENT, Data TEXT, Path TEXT)'
    create_environment_table=f'CREATE TABLE "Environment" (Name TEXT PRIMARY KEY, Value TEXT)'
    create_history_table=f'CREATE TABLE "History" (Timestamp STRING, Notebook TEXT, Library TEXT)'
    init_metadata_table = f'insert into "SceneMetadata"(ID, Ended, Name) values("{scene_id}", 0, "{name}")'
    
    cur.execute(create_metadata_table)
    cur.execute(create_notebook_list_table)
    cur.execute(create_environment_table)
    cur.execute(create_history_table)
    cur.execute(init_metadata_table)
    conn.commit()
    conn.close()


def init_library_db(db_file):
    """initializes the library database"""
    conn = create_connection(db_file)
    cur = conn.cursor()
    create_metadata_table = f'CREATE TABLE "LibraryMetadata" (Root TEXT PRIMARY KEY, Readme TEXT, Name TEXT)'
    create_notebook_table = f'CREATE TABLE "Notebooks" (Root TEXT PRIMARY KEY, Name TEXT, LibraryName TEXT, FOREIGN KEY(LibraryName) REFERENCES "LibraryMetadata"(Name))'
    create_environment_table = f'CREATE TABLE "Environment" (Name TEXT PRIMARY KEY, Value TEXT, NotebookName TEXT, FOREIGN KEY(NotebookName) REFERENCES "Notebooks"(Name))'
    cur.execute(create_metadata_table)
    cur.execute(create_notebook_table)
    cur.execute(create_environment_table)
    conn.commit()
    conn.close()


def init_current_scene(db_file, scene_name):
    """initializes the current scene database"""
    conn = create_connection(db_file)
    cur = conn.cursor()
    create_current_scene_table = 'CREATE TABLE "SceneHistory" (ID INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT, Ended INTEGER)'
    create_scene_list_table=f'CREATE TABLE "SceneList" (ID INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT)'
    cur.execute(create_scene_list_table)
    cur.execute(create_current_scene_table)
    conn.commit()
    conn.close()


def check_scene_ended(db_file, scene_name):
    """checks if scene has ended"""
    #TODO: handle strings
    conn = create_connection(db_file)
    cur = conn.cursor()
    check_scene_exists = f'SELECT Ended from "SceneHistory" WHERE Name = "{scene_name}"'
    cur.execute(check_scene_exists)
    rows = cur.fetchall()
    conn.close()
    if rows == []:
        return -1
    else:
        return rows[0][0]


def update_current_scene(db_file, scene_name):
    """updates the current scene in the history db"""
    #TODO: handle strings
    conn = create_connection(db_file)
    cur =  conn.cursor()
    add_current_scene = f'INSERT INTO "SceneHistory"(Name, Ended) VALUES("{scene_name}", 0)'
    cur.execute(add_current_scene)
    conn.commit()
    conn.close()


def get_current_scene(db_file):
    """gets the current scene from the history db"""
    conn = create_connection(db_file)
    cur = conn.cursor()
    get_current_scene = 'SELECT Name FROM "SceneHistory" WHERE Ended != 1 ORDER BY ID DESC LIMIT 0, 1'
    cur.execute(get_current_scene)
    rows = cur.fetchall()
    conn.close()
    return rows[0][0]


def get_scene_id(db_file):
    """gets the scene ID from the scene db"""
    conn = create_connection(db_file)
    cur = conn.cursor()
    get_scene_id = 'SELECT ID FROM "SceneMetadata"'
    cur.execute(get_scene_id)
    id = cur.fetchone()[0]
    conn.close()
    return id


def get_notebook_environments(db_file, name):
    """gets the scene ID from the scene db"""
    conn = create_connection(db_file)
    cur = conn.cursor()
    get_notebook_environment = f'SELECT * FROM "Environment" WHERE NotebookName = "{name}"'
    cur.execute(get_notebook_environment)
    id = cur.fetchall()
    conn.close()
    return id


def set_notebook_environments(db_file, notebook_name, environment_name, environment_value):
    """set or update an environment variable"""
    conn = create_connection(db_file)
    cur = conn.cursor()
    set_env = f'INSERT OR IGNORE INTO "Environment" (Name, Value, NotebookName) VALUES(?, ?, ?)'
    update_env = f'UPDATE "Environment" SET Value = ? WHERE Name = ? AND NotebookName = ?'
    cur.execute(set_env, (environment_name, environment_value, notebook_name))
    cur.execute(update_env, (environment_name, environment_value, notebook_name))
    conn.commit()
    conn.close()


def delete_scene(db_file, name):
    """Deletes the specified scene"""
    conn = create_connection(db_file)
    cur = conn.cursor()

    ended = check_ended(db_file, name, conn, cur)
    if ended == -1:
        return 0
        
    active_scenes = get_active_scenes(db_file)
    if len(active_scenes) <= 1 and ended != 1:
        return 0
    else:
        delete_scene = f'DELETE FROM "SceneHistory" WHERE Name = "{name}"'
        cur.execute(delete_scene)
        conn.commit()
        conn.close()
        return 1
    return 0


def end_scene(db_file, name):
    """marks the specified scene as ended"""
    conn = create_connection(db_file)
    cur = conn.cursor()
    end_scene = f'UPDATE "SceneMetadata" SET Ended = 1 WHERE Name = "{name}"'
    cur.execute(end_scene)
    conn.commit()
    conn.close()


def check_ended(db_file, name, conn, cur):
    """checks if a scene has ended"""
    ended = f'SELECT Ended from "SceneHistory" WHERE Name = "{name}"'
    cur.execute(ended)
    ended = cur.fetchall()
    if ended == []:
        return -1
    return ended[0][0]


def mark_ended_scene(db_file, name):
    """marks a scene as ended in the history db"""
    conn = create_connection(db_file)
    cur = conn.cursor()

    ended = check_ended(db_file, name, conn, cur)
    if ended == -1:
        return -1

    active_scenes = get_active_scenes(db_file)
    if len(active_scenes) <= 1 and ended != 1:
        return 0
    else:
        end_scene = f'UPDATE "SceneHistory" SET Ended = 1 WHERE Name = "{name}"'
        cur.execute(end_scene)
        conn.commit()
        conn.close()
        return 1
    return 0


def mark_resumed_scene(db_file, name):
    """mark a scene as resumed in the history db"""
    conn = create_connection(db_file)
    cur = conn.cursor()
    end_scene = f'UPDATE "SceneHistory" SET Ended = 0 WHERE Name = "{name}"'
    cur.execute(end_scene)
    conn.commit()
    conn.close()


def resume_scene(db_file, name):
    """resumes a scene"""
    conn = create_connection(db_file)
    cur = conn.cursor()
    end_scene = f'UPDATE "SceneMetadata" SET Ended = 0 WHERE Name = "{name}"'
    cur.execute(end_scene)
    conn.commit()
    conn.close()


def get_active_scenes(db_file):
    """returns a list of all active scenes"""
    conn = create_connection(db_file)
    cur = conn.cursor()
    get_active_scenes = f'SELECT DISTINCT Name from "SceneHistory" WHERE Ended = 0'
    cur.execute(get_active_scenes)
    rows = cur.fetchall()
    conn.close()
    return rows


def get_ended_scenes(db_file):
    """returns a list of all ended scenes"""
    conn = create_connection(db_file)
    cur = conn.cursor()
    get_ended_scenes = f'SELECT DISTINCT Name from "SceneHistory" WHERE Ended = 1'
    cur.execute(get_ended_scenes)
    rows = cur.fetchall()
    conn.close()
    return rows


def add_to_scene_history(db_file, timestamp, name, library):
    """adds a notebook to the scene history"""
    conn = create_connection(db_file)
    cur = conn.cursor()
    add_to_scene_history = f'INSERT INTO "History"(Timestamp, Notebook, Library) VALUES (?,?,?)'
    cur.execute(add_to_scene_history, (timestamp, name, library))
    conn.commit()
    conn.close()


def get_notebook_history(db_file):
    """gets the notebook history from a scene"""
    conn = create_connection(db_file)
    cur = conn.cursor()
    get_notebook_history = f'SELECT * FROM "History" ORDER BY Timestamp'
    cur.execute(get_notebook_history)
    conn.commit()
    rows = cur.fetchall()
    conn.close()
    return rows


def init_user_info(db_file):
    """From name of database file, creates and initializes user info"""
    import uuid
    import getpass

    conn = create_connection(db_file)
    cur = conn.cursor()
    create_userinfo_table = f'CREATE TABLE "UserInfo" (Key TEXT PRIMARY KEY, Value TEXT)'
    create_user_id = f'INSERT INTO "UserInfo" (Key, Value) VALUES ("ID",?)'
    create_telem_permissions = f'INSERT INTO "UserInfo" (Key, Value) VALUES ("TELEMETRY", 1)'
    create_host = f'INSERT INTO "UserInfo" (Key, Value) VALUES ("Host", ?)'
    create_url = f'INSERT INTO "UserInfo" (Key, Value) VALUES ("URL", ?)'
    create_user = f'INSERT INTO "UserInfo" (Key, Value) VALUES ("Username", ?)'
    create_pswd = f'INSERT INTO "UserInfo" (Key, Value) VALUES ("Password", ?)'
    id_val = str(uuid.uuid4())
    
    cur.execute(create_userinfo_table)
    cur.execute(create_user_id, (id_val,))
    cur.execute(create_telem_permissions)
    #TODO: figure out where to put input of server info (hint: not here)
    host = input("Enter an IP address for the host server: ")
    url = "https://{0}:30443/gateway/default/webhdfs/v1/mtool"
    username = input("Enter your username for connecting to the server: ")
    pswd = getpass.getpass()
    cur.execute(create_host, (host,))
    cur.execute(create_url, (url,))
    cur.execute(create_user, (username,))
    cur.execute(create_pswd, (pswd,))
    conn.commit()
    conn.close()
    

def list_env(db_file, start, end):
    """returns a list of set environment variables in the scene"""
    conn = create_connection(db_file)
    cur = conn.cursor()
    list_env = f'SELECT * FROM "Environment" ORDER BY Name DESC LIMIT {start}, {end}'
    cur.execute(list_env)
    conn.commit()
    rows = cur.fetchall()
    conn.close()
    return rows


def get_env(db_file, var_name):
    """get the value of the specified environment variable""" 
    conn = create_connection(db_file)
    cur = conn.cursor()
    get_env = f'SELECT Value FROM "Environment" WHERE Name = ?'
    cur.execute(get_env, (var_name,))
    conn.commit()
    value = cur.fetchone()   #just a value, not the tuple
    conn.close()
    return value


def set_env(db_file, name, value):
    """set or update an environment variable"""
    conn = create_connection(db_file)
    cur = conn.cursor()
    set_env = f'INSERT OR IGNORE INTO "Environment"(Name, Value) VALUES("{name}", "{value}")'
    upate_env = f'UPDATE "Environment" SET Value = "{value}" WHERE Name = "{name}"'
    cur.execute(set_env)
    cur.execute(upate_env)
    conn.commit()
    conn.close()


def get_env_by_ord(db_file, ordinal):
    """get an environment variable by ord"""
    conn = create_connection(db_file)
    cur = conn.cursor()
    list_env = f'SELECT * FROM "Environment" ORDER BY Name DESC LIMIT {ordinal-1}, {ordinal}'
    cur.execute(list_env)
    conn.commit()
    rows = cur.fetchall()
    conn.close()
    if rows == []:
        return ""
    return rows[0][0]


def delete_env(db_file, name):
    """Delete an environment variable"""
    conn = create_connection(db_file)
    cur = conn.cursor()
    env = f'SELECT * from "Environment" WHERE Name = "{name}"'
    cur.execute(env)
    exists = cur.fetchall()
    if exists == []:
        return 0
    else:
        delete_env = f'DELETE FROM "Environment" where Name = "{name}"'
        cur.execute(delete_env)
        conn.commit()
        conn.close()
        return 1

def clear_loaded_libararies(db_file):
    conn = create_connection(db_file)
    cur = conn.cursor()
    clear_metadata = f'DELETE FROM "LibraryMetadata"'
    clear_notebooks = f'DELETE FROM "Notebooks"'
    cur.execute(clear_metadata)
    cur.execute(clear_notebooks)
    conn.commit()
    conn.close()


def load_library(db_file, root, readme, name):
    """load a library into the library db"""
    conn = create_connection(db_file)
    cur = conn.cursor()
    load_library = f'INSERT OR IGNORE INTO "LibraryMetadata"(Root, Readme, Name) VALUES("{root}", "{readme}", "{name}")'
    update_library = f'UPDATE "LibraryMetadata" SET Readme = "{readme}" WHERE Name = "{name}"'
    cur.execute(load_library)
    cur.execute(update_library)
    conn.commit()
    conn.close()


def load_notebook(db_file, file_root, name, library):
    """load a notebook into the library db"""
    conn = create_connection(db_file)
    cur = conn.cursor()
    load_library = f'INSERT OR IGNORE INTO "Notebooks"(Root, Name, LibraryName) VALUES("{file_root}", "{name}", "{library}")'
    cur.execute(load_library)
    conn.commit()
    conn.close()


def list_libraries(db_file, start, end):
    """returns a list of loaded libraries"""
    conn = create_connection(db_file)
    cur = conn.cursor()
    list_libraries = f'SELECT Name FROM "LibraryMetadata" LIMIT {start}, {end}'
    cur.execute(list_libraries)
    conn.commit()
    rows = cur.fetchall()
    conn.close()
    return rows


def list_notebooks(db_file, start, end):
    """lists all loaded notebooks"""
    conn = create_connection(db_file)
    cur = conn.cursor()
    list_libraries = f'SELECT Name, Root FROM "Notebooks" LIMIT {start}, {end}'
    cur.execute(list_libraries)
    conn.commit()
    rows = cur.fetchall()
    conn.close()
    return rows


def get_notebook(db_file, name):
    """returns a specific notebook"""
    conn = create_connection(db_file)
    cur = conn.cursor()
    get_notebook = f'SELECT * FROM "Notebooks" WHERE Name = "{name}" LIMIT 0, 1'
    cur.execute(get_notebook)
    conn.commit()
    rows = cur.fetchall()
    conn.close()
    return rows[0]


def get_notebook_by_ord(db_file, ordinal):
    """Returns list item referenced by input ordinal"""
    conn = create_connection(db_file)
    cur = conn.cursor()
    query = f'SELECT Data FROM NotebookList WHERE ID = "{ordinal}" LIMIT 0, 1'
    cur.execute(query)
    conn.commit()
    item = cur.fetchone()
    conn.close()
    return item


def write_list(db_file, notebook_list, path_list = []):
    """creates the list of notebooks in list"""
    conn = create_connection(db_file)
    cur = conn.cursor()
    clear_list = f'DELETE FROM "NotebookList"'
    reset_counter = "UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME='NotebookList'"
    insert_line = f'INSERT INTO "NotebookList" (DATA, PATH) VALUES (?,?)'
    cur.execute(clear_list)
    cur.execute(reset_counter)
    if path_list == []:
        cur.executemany(insert_line, notebook_list)
    else:
        cur.executemany(insert_line, (notebook_list, path_list))
    conn.commit()
    conn.close()

def get_notebook_path(db_file, notebook, library):
    """gets notebook path from libraries/notebooks"""
    conn = create_connection(db_file)
    cur = conn.cursor()
    get_notebook_path = f"SELECT ROOT FROM 'Notebooks' WHERE NAME=? AND LIBRARYNAME=?"
    cur.execute(get_notebook_path, (notebook, library))
    conn.commit()
    path = cur.fetchone()[0]
    conn.close()
    return path
    
def get_telemetry_info(db_file, key):
    """gets the telemetry information:"""
    conn = create_connection(db_file)
    cur = conn.cursor()
    query = f'SELECT Value FROM "UserInfo" WHERE Key = ?'
    cur.execute(query, (key,))
    conn.commit()
    item = cur.fetchone()
    if item != None:
        item = item[0] # remove tuple wrapping
    conn.close()
    return item


def dump_scene_list(db_file):
    """empties the scene list table""" 
    conn = create_connection(db_file)
    cur = conn.cursor()
    clear_list = f'DELETE FROM "SceneList"'
    reset_counter = "UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME='SceneList'"
    cur.execute(clear_list)
    cur.execute(reset_counter)
    conn.commit()
    conn.close()


def write_scene_list(db_file, scene_list):
    """writes to scene list table"""
    conn = create_connection(db_file)
    cur = conn.cursor()
    insert_line = f'INSERT INTO "SceneList" (Name) VALUES (?)'
    cur.executemany(insert_line, scene_list)
    conn.commit()
    conn.close()


def get_scene_by_ord(db_file, ordinal):
    """gets scene by ordinal"""
    conn = create_connection(db_file)
    cur = conn.cursor()
    list_env = f'SELECT Name FROM "SceneList" ORDER BY ID LIMIT {ordinal-1}, {ordinal}'
    cur.execute(list_env)
    conn.commit()
    rows = cur.fetchall()
    conn.close()
    if rows == []:
        return ""
    return rows[0][0]


def search_notebooks(db_file, search_term, start, end):
    """searches notebooks for search term"""
    conn = create_connection(db_file)
    cur = conn.cursor()
    list_env = f'SELECT Name, Root FROM "Notebooks" WHERE Name LIKE "%{search_term}%" ORDER BY Name LIMIT {start}, {end}'
    cur.execute(list_env)
    conn.commit()
    rows = cur.fetchall()
    conn.close()
    return rows