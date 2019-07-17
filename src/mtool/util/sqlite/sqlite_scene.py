
"""
This file contains all of the sqlite functions for scenes
"""

def init_scene(scene_db, name):
    """initializes the scene db"""
    #TODO: handle strings
    import uuid
    from src.mtool.util.sqlite import connection

    conn = connection.create_connection(scene_db)
    cur = conn.cursor()
    scene_id = str(uuid.uuid4())

    create_metadata_table = f'CREATE TABLE "SceneMetadata" (ID TEXT PRIMARY KEY, Ended INTEGER, Name TEXT)'
    create_notebook_list_table=f'CREATE TABLE "NotebookList" (ID INTEGER PRIMARY KEY AUTOINCREMENT, Data TEXT, Path TEXT)'
    create_environment_table=f'CREATE TABLE "Environment" (Name TEXT PRIMARY KEY, Value TEXT)'
    create_history_table=f'CREATE TABLE "History" (Timestamp STRING, Notebook TEXT, Library TEXT, OutputPath TEXT)'
    init_metadata_table = f'insert into "SceneMetadata"(ID, Ended, Name) values("{scene_id}", 0, "{name}")'
    cur.execute(create_metadata_table)
    cur.execute(create_notebook_list_table)
    cur.execute(create_environment_table)
    cur.execute(create_history_table)
    cur.execute(init_metadata_table)
    conn.commit()
    conn.close()


def check_ended(history_db, name, conn, cur):
    """checks if a scene has ended"""
    from src.mtool.util import error
     
    ended = f'SELECT Ended from "SceneHistory" WHERE Name = "{name}"'
    cur.execute(ended)
    ended = cur.fetchone()
    if ended == None:
        raise error.SceneNotFoundError(name)
    elif ended[0]:
        raise error.EndEndedSceneError(name)
    return ended


def init_current_scene(history_db, scene_name):
    """initializes the current scene database"""
    from src.mtool.util.sqlite import connection

    conn = connection.create_connection(history_db)
    cur = conn.cursor()
    create_current_scene_table = 'CREATE TABLE "SceneHistory" (ID INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT, Ended INTEGER)'
    create_scene_list_table=f'CREATE TABLE "SceneList" (ID INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT)'
    cur.execute(create_scene_list_table)
    cur.execute(create_current_scene_table)
    conn.commit()
    conn.close()


def check_scene_ended(history_db, scene_name):
    """checks if scene has ended"""
    #TODO: handle strings
    from src.mtool.util.sqlite import connection
    from src.mtool.util import error

    conn = connection.create_connection(history_db)
    cur = conn.cursor()
    check_scene_exists = f'SELECT Ended from "SceneHistory" WHERE Name = "{scene_name}"'
    cur.execute(check_scene_exists)
    rows = cur.fetchall()
    conn.close()
    if rows == []:
        raise error.SceneNotFoundError(scene_name)
    elif rows[0][0]:
        raise error.SceneEndedError(scene_name)


def update_current_scene(history_db, scene_name):
    """updates the current scene in the history db"""
    #TODO: handle strings
    from src.mtool.util.sqlite import connection

    conn = connection.create_connection(history_db)
    cur =  conn.cursor()
    add_current_scene = f'INSERT INTO "SceneHistory"(Name, Ended) VALUES("{scene_name}", 0)'
    cur.execute(add_current_scene)
    conn.commit()
    conn.close()


def get_current_scene(history_db):
    """gets the current scene from the history db"""
    from src.mtool.util.sqlite import connection

    conn = connection.create_connection(history_db)
    cur = conn.cursor()
    get_current_scene = 'SELECT Name FROM "SceneHistory" WHERE Ended != 1 ORDER BY ID DESC LIMIT 0, 1'
    cur.execute(get_current_scene)
    rows = cur.fetchall()
    conn.close()
    return rows[0][0]


def delete_scene(history_db, name):
    """Deletes the specified scene"""
    import itertools
    from src.mtool.util.sqlite import connection
    from src.mtool.util import error

    conn = connection.create_connection(history_db)
    cur = conn.cursor()

    try:
        check_ended(history_db, name, conn, cur)
    except error.SceneNotFoundError as e:
        raise e
    except error.EndEndedSceneError:
        pass
        
    active_scenes = get_active_scenes(history_db)

    if len(active_scenes) <= 1 and name in list(itertools.chain(*active_scenes)):
        raise error.LastActiveSceneError(name)
    else:
        delete_scene = f'DELETE FROM "SceneHistory" WHERE Name = "{name}"'
        cur.execute(delete_scene)
        conn.commit()
        conn.close()
        return 0


def end_scene(current_scene_db, name):
    """marks the specified scene as ended"""
    from src.mtool.util.sqlite import connection

    conn = connection.create_connection(current_scene_db)
    cur = conn.cursor()
    end_scene = f'UPDATE "SceneMetadata" SET Ended = 1 WHERE Name = "{name}"'
    cur.execute(end_scene)
    conn.commit()
    conn.close()


def mark_ended_scene(history_db, name):
    """marks a scene as ended in the history db"""
    from src.mtool.util.sqlite import connection
    from src.mtool.util import error
    import itertools

    conn = connection.create_connection(history_db)
    cur = conn.cursor()

    try:
        check_ended(history_db, name, conn, cur)
    except error.SceneNotFoundError as e:
        raise e
    except error.EndEndedSceneError as e:
        raise e

    active_scenes = get_active_scenes(history_db)
    if len(active_scenes) <= 1 and name in list(itertools.chain(*active_scenes)) :
        raise error.LastActiveSceneError(name)
    else:
        end_scene = f'UPDATE "SceneHistory" SET Ended = 1 WHERE Name = "{name}"'
        cur.execute(end_scene)
        conn.commit()
        conn.close()
        return 0


def mark_resumed_scene(history_db, name):
    """mark a scene as resumed in the history db"""
    from src.mtool.util.sqlite import connection

    conn = connection.create_connection(history_db)
    cur = conn.cursor()
    end_scene = f'UPDATE "SceneHistory" SET Ended = 0 WHERE Name = "{name}"'
    cur.execute(end_scene)
    conn.commit()
    conn.close()


def resume_scene(scene_db, name):
    """resumes a scene"""
    from src.mtool.util.sqlite import connection

    conn = connection.create_connection(scene_db)
    cur = conn.cursor()
    end_scene = f'UPDATE "SceneMetadata" SET Ended = 0 WHERE Name = "{name}"'
    cur.execute(end_scene)
    conn.commit()
    conn.close()


def get_active_scenes(history_db):
    """returns a list of all active scenes"""
    from src.mtool.util.sqlite import connection

    conn = connection.create_connection(history_db)
    cur = conn.cursor()
    get_active_scenes = f'SELECT DISTINCT Name from "SceneHistory" WHERE Ended = 0'
    cur.execute(get_active_scenes)
    rows = cur.fetchall()
    conn.close()
    return rows


def get_ended_scenes(history_db):
    """returns a list of all ended scenes"""
    from src.mtool.util.sqlite import connection

    conn = connection.create_connection(history_db)
    cur = conn.cursor()
    get_ended_scenes = f'SELECT DISTINCT Name from "SceneHistory" WHERE Ended = 1'
    cur.execute(get_ended_scenes)
    rows = cur.fetchall()
    conn.close()
    return rows


def add_to_scene_history(current_scene_db, timestamp, name, library, outputpath):
    """adds a notebook to the scene history"""
    from src.mtool.util.sqlite import connection

    conn = connection.create_connection(current_scene_db)
    cur = conn.cursor()
    add_to_scene_history = f'INSERT INTO "History"(Timestamp, Notebook, Library, OutputPath) VALUES (?,?,?, ?)'
    cur.execute(add_to_scene_history, (timestamp, name, library, outputpath))
    conn.commit()
    conn.close()


def get_notebook_history(current_scene_db):
    """gets the notebook history from a scene"""
    from src.mtool.util.sqlite import connection

    conn = connection.create_connection(current_scene_db)
    cur = conn.cursor()
    get_notebook_history = f'SELECT * FROM "History" ORDER BY Timestamp'
    cur.execute(get_notebook_history)
    conn.commit()
    rows = cur.fetchall()
    conn.close()
    return rows


def get_recent_history(db_file, seq_length):
    """Gets last <seq_length> file names from a scene"""
    from src.mtool.util.sqlite import connection

    conn = connection.create_connection(db_file)
    cur = conn.cursor()
    get_recent_history = f'SELECT Notebook, Path FROM (SELECT * FROM "History" ORDER BY Timestamp DESC LIMIT ?) ORDER BY Timestamp ASC'
    cur.execute(get_recent_history, (seq_length,))
    conn.commit()
    rows = cur.fetchall()
    conn.close()
    return rows

def dump_scene_list(history_db):
    """empties the scene list table""" 
    from src.mtool.util.sqlite import connection

    conn = connection.create_connection(history_db)
    cur = conn.cursor()
    clear_list = f'DELETE FROM "SceneList"'
    reset_counter = "UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME='SceneList'"
    cur.execute(clear_list)
    cur.execute(reset_counter)
    conn.commit()
    conn.close()


def write_scene_list(history_db, scene_list):
    """writes to scene list table"""
    from src.mtool.util.sqlite import connection

    conn = connection.create_connection(history_db)
    cur = conn.cursor()
    insert_line = f'INSERT INTO "SceneList" (Name) VALUES (?)'
    cur.executemany(insert_line, scene_list)
    conn.commit()
    conn.close()


def get_scene_by_ord(history_db, ordinal):
    """gets scene by ordinal"""
    from src.mtool.util.sqlite import connection
    from src.mtool.util import error

    conn = connection.create_connection(history_db)
    cur = conn.cursor()
    list_env = f'SELECT Name FROM "SceneList" ORDER BY ID LIMIT {ordinal-1}, {ordinal}'
    cur.execute(list_env)
    conn.commit()
    rows = cur.fetchall()
    conn.close()
    if rows == []:
        raise error.SceneNotFoundError(ordinal)
    return rows[0][0]


def clear_history(current_scene_db):
    """empties the history table""" 
    from src.mtool.util.sqlite import connection

    conn = connection.create_connection(current_scene_db)
    cur = conn.cursor()
    clear_history = f'DELETE FROM "History"'
    cur.execute(clear_history)
    conn.commit()
    conn.close()
