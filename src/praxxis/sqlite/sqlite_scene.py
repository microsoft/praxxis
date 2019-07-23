
"""
This file contains all of the sqlite functions for scenes
"""

def init_scene(scene_db, name):
    """initializes the scene db"""
    #TODO: handle strings
    import uuid
    from src.praxxis.sqlite import connection

    conn = connection.create_connection(scene_db)
    cur = conn.cursor()
    scene_id = str(uuid.uuid4())

    create_metadata_table = f'CREATE TABLE "SceneMetadata" (ID TEXT PRIMARY KEY, Ended INTEGER, Scene TEXT)'
    create_notebook_list_table=f'CREATE TABLE "NotebookList" (ID INTEGER PRIMARY KEY AUTOINCREMENT, Notebook TEXT, Library TEXT, Path TEXT, RawUrl TEXT)'
    create_parameter_table=f'CREATE TABLE "Parameters" (Parameter TEXT PRIMARY KEY, Value TEXT)'
    create_history_table=f'CREATE TABLE "History" (Timestamp STRING, Notebook TEXT, Library TEXT, OutputPath TEXT)'
    init_metadata_table = f'insert into "SceneMetadata"(ID, Ended, Scene) values("{scene_id}", 0, "{name}")'
    cur.execute(create_metadata_table)
    cur.execute(create_notebook_list_table)
    cur.execute(create_parameter_table)
    cur.execute(create_history_table)
    cur.execute(init_metadata_table)
    conn.commit()
    conn.close()

def check_ended(history_db, scene, conn, cur):
    """checks if a scene has ended"""
    from src.praxxis.util import error
     
    ended = f'SELECT Ended from "SceneHistory" WHERE Scene = "{scene}"'
    cur.execute(ended)
    ended = cur.fetchone()
    if ended == None:
        raise error.SceneNotFoundError(scene)
    elif ended[0]:
        raise error.EndEndedSceneError(scene)
    return ended


def check_scene_ended(history_db, scene):
    """checks if scene has ended"""
    #TODO: handle strings
    from src.praxxis.sqlite import connection
    from src.praxxis.util import error

    conn = connection.create_connection(history_db)
    cur = conn.cursor()
    check_scene_exists = f'SELECT Ended from "SceneHistory" WHERE Scene = "{scene}"'
    cur.execute(check_scene_exists)
    rows = cur.fetchall()
    conn.close()
    if rows == []:
        raise error.SceneNotFoundError(scene)
    elif rows[0][0]:
        raise error.SceneEndedError(scene)


def update_current_scene(history_db, scene):
    """updates the current scene in the history db"""
    #TODO: handle strings
    from src.praxxis.sqlite import connection

    conn = connection.create_connection(history_db)
    cur =  conn.cursor()
    add_current_scene = f'INSERT INTO "SceneHistory"(Scene, Ended) VALUES("{scene}", 0)'
    cur.execute(add_current_scene)
    conn.commit()
    conn.close()


def get_current_scene(history_db):
    """gets the current scene from the history db"""
    from src.praxxis.sqlite import connection

    conn = connection.create_connection(history_db)
    cur = conn.cursor()
    get_current_scene = 'SELECT Scene FROM "SceneHistory" WHERE Ended != 1 ORDER BY ID DESC LIMIT 0, 1'
    cur.execute(get_current_scene)
    rows = cur.fetchall()
    conn.close()
    return rows[0][0]


def delete_scene(history_db, scene):
    """Deletes the specified scene"""
    import itertools
    from src.praxxis.sqlite import connection
    from src.praxxis.util import error

    conn = connection.create_connection(history_db)
    cur = conn.cursor()

    try:
        check_ended(history_db, scene, conn, cur)
    except error.SceneNotFoundError as e:
        raise e
    except error.EndEndedSceneError:
        pass
        
    active_scenes = get_active_scenes(history_db)

    if len(active_scenes) <= 1 and scene in list(itertools.chain(*active_scenes)):
        raise error.LastActiveSceneError(scene)
    else:
        delete_scene = f'DELETE FROM "SceneHistory" WHERE Scene = "{scene}"'
        cur.execute(delete_scene)
        conn.commit()
        conn.close()
        return 0


def end_scene(current_scene_db, scene):
    """marks the specified scene as ended"""
    from src.praxxis.sqlite import connection

    conn = connection.create_connection(current_scene_db)
    cur = conn.cursor()
    end_scene = f'UPDATE "SceneMetadata" SET Ended = 1 WHERE Scene = "{scene}"'
    cur.execute(end_scene)
    conn.commit()
    conn.close()


def mark_ended_scene(history_db, scene):
    """marks a scene as ended in the history db"""
    from src.praxxis.sqlite import connection
    from src.praxxis.util import error
    import itertools

    conn = connection.create_connection(history_db)
    cur = conn.cursor()

    try:
        check_ended(history_db, scene, conn, cur)
    except error.SceneNotFoundError as e:
        raise e
    except error.EndEndedSceneError as e:
        raise e

    active_scenes = get_active_scenes(history_db)
    if len(active_scenes) <= 1 and scene in list(itertools.chain(*active_scenes)) :
        raise error.LastActiveSceneError(scene)
    else:
        end_scene = f'UPDATE "SceneHistory" SET Ended = 1 WHERE Scene = "{scene}"'
        cur.execute(end_scene)
        conn.commit()
        conn.close()
        return 0


def mark_resumed_scene(history_db, scene):
    """mark a scene as resumed in the history db"""
    from src.praxxis.sqlite import connection

    conn = connection.create_connection(history_db)
    cur = conn.cursor()
    end_scene = f'UPDATE "SceneHistory" SET Ended = 0 WHERE Scene = "{scene}"'
    cur.execute(end_scene)
    conn.commit()
    conn.close()


def resume_scene(scene_db, scene):
    """resumes a scene"""
    from src.praxxis.sqlite import connection

    conn = connection.create_connection(scene_db)
    cur = conn.cursor()
    end_scene = f'UPDATE "SceneMetadata" SET Ended = 0 WHERE Scene = "{scene}"'
    cur.execute(end_scene)
    conn.commit()
    conn.close()


def get_active_scenes(history_db):
    """returns a list of all active scenes"""
    from src.praxxis.sqlite import connection

    conn = connection.create_connection(history_db)
    cur = conn.cursor()
    get_active_scenes = f'SELECT DISTINCT Scene from "SceneHistory" WHERE Ended = 0'
    cur.execute(get_active_scenes)
    rows = cur.fetchall()
    conn.close()
    return rows


def get_ended_scenes(history_db):
    """returns a list of all ended scenes"""
    from src.praxxis.sqlite import connection

    conn = connection.create_connection(history_db)
    cur = conn.cursor()
    get_ended_scenes = f'SELECT DISTINCT Scene from "SceneHistory" WHERE Ended = 1'
    cur.execute(get_ended_scenes)
    rows = cur.fetchall()
    conn.close()
    return rows


def add_to_scene_history(current_scene_db, timestamp, notebook, library, outputpath):
    """adds a notebook to the scene history"""
    from src.praxxis.sqlite import connection

    conn = connection.create_connection(current_scene_db)
    cur = conn.cursor()
    add_to_scene_history = f'INSERT INTO "History"(Timestamp, Notebook, Library, OutputPath) VALUES (?,?,?, ?)'
    cur.execute(add_to_scene_history, (timestamp, notebook, library, outputpath))
    conn.commit()
    conn.close()


def get_notebook_history(current_scene_db):
    """gets the notebook history from a scene"""
    from src.praxxis.sqlite import connection

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
    from src.praxxis.sqlite import connection

    conn = connection.create_connection(db_file)
    cur = conn.cursor()
    get_recent_history = f'SELECT Notebook, OutputPath FROM (SELECT * FROM "History" ORDER BY Timestamp DESC LIMIT ?) ORDER BY Timestamp ASC'
    cur.execute(get_recent_history, (seq_length,))
    conn.commit()
    rows = cur.fetchall()
    conn.close()
    return rows

def dump_scene_list(history_db):
    """empties the scene list table""" 
    from src.praxxis.sqlite import connection

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
    from src.praxxis.sqlite import connection

    conn = connection.create_connection(history_db)
    cur = conn.cursor()
    insert_line = f'INSERT INTO "SceneList" (Scene) VALUES (?)'
    cur.executemany(insert_line, scene_list)
    conn.commit()
    conn.close()


def get_scene_by_ord(history_db, ordinal):
    """gets scene by ordinal"""
    from src.praxxis.sqlite import connection
    from src.praxxis.util import error

    conn = connection.create_connection(history_db)
    cur = conn.cursor()
    get_scene = f'SELECT Scene FROM "SceneList" ORDER BY ID LIMIT {ordinal-1}, {ordinal}'
    cur.execute(get_scene)
    conn.commit()
    rows = cur.fetchall()
    conn.close()
    if rows == []:
        raise error.SceneNotFoundError(ordinal)
    return rows[0][0]


def clear_history(current_scene_db):
    """empties the history table""" 
    from src.praxxis.sqlite import connection

    conn = connection.create_connection(current_scene_db)
    cur = conn.cursor()
    clear_history = f'DELETE FROM "History"'
    cur.execute(clear_history)
    conn.commit()
    conn.close()


def get_notebook_path(current_scene_db, notebook_name):
    """returns the path given a valid notebook name"""
    from src.praxxis.sqlite import connection

    conn = connection.create_connection(current_scene_db)
    cur = conn.cursor()
    get_path = f'SELECT Path FROM "NotebookList" WHERE Data = ?'

    cur.execute(get_path, (notebook_name,))
    conn.commit()
    path = cur.fetchone()
    conn.close()
    
    return path