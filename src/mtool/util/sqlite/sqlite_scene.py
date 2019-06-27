def init_scene(db_file, name):
    """initializes the scene db"""
    #TODO: handle strings
    import uuid
    from src.mtool.util.sqlite import connection

    conn = connection.create_connection(db_file)
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

def check_ended(db_file, name, conn, cur):
    """checks if a scene has ended"""
    ended = f'SELECT Ended from "SceneHistory" WHERE Name = "{name}"'
    cur.execute(ended)
    ended = cur.fetchall()
    if ended == []:
        return -1
    return ended[0][0]


def init_current_scene(db_file, scene_name):
    """initializes the current scene database"""
    from src.mtool.util.sqlite import connection

    conn = connection.create_connection(db_file)
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
    from src.mtool.util.sqlite import connection

    conn = connection.create_connection(db_file)
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
    from src.mtool.util.sqlite import connection

    conn = connection.create_connection(db_file)
    cur =  conn.cursor()
    add_current_scene = f'INSERT INTO "SceneHistory"(Name, Ended) VALUES("{scene_name}", 0)'
    cur.execute(add_current_scene)
    conn.commit()
    conn.close()


def get_current_scene(db_file):
    """gets the current scene from the history db"""
    from src.mtool.util.sqlite import connection

    conn = connection.create_connection(db_file)
    cur = conn.cursor()
    get_current_scene = 'SELECT Name FROM "SceneHistory" WHERE Ended != 1 ORDER BY ID DESC LIMIT 0, 1'
    cur.execute(get_current_scene)
    rows = cur.fetchall()
    conn.close()
    return rows[0][0]


def delete_scene(db_file, name):
    """Deletes the specified scene"""
    from src.mtool.util.sqlite import connection

    conn = connection.create_connection(db_file)
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
    from src.mtool.util.sqlite import connection

    conn = connection.create_connection(db_file)
    cur = conn.cursor()
    end_scene = f'UPDATE "SceneMetadata" SET Ended = 1 WHERE Name = "{name}"'
    cur.execute(end_scene)
    conn.commit()
    conn.close()


def mark_ended_scene(db_file, name):
    """marks a scene as ended in the history db"""
    from src.mtool.util.sqlite import connection

    conn = connection.create_connection(db_file)
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
    from src.mtool.util.sqlite import connection

    conn = connection.create_connection(db_file)
    cur = conn.cursor()
    end_scene = f'UPDATE "SceneHistory" SET Ended = 0 WHERE Name = "{name}"'
    cur.execute(end_scene)
    conn.commit()
    conn.close()


def resume_scene(db_file, name):
    """resumes a scene"""
    from src.mtool.util.sqlite import connection

    conn = connection.create_connection(db_file)
    cur = conn.cursor()
    end_scene = f'UPDATE "SceneMetadata" SET Ended = 0 WHERE Name = "{name}"'
    cur.execute(end_scene)
    conn.commit()
    conn.close()


def get_active_scenes(db_file):
    """returns a list of all active scenes"""
    from src.mtool.util.sqlite import connection

    conn = connection.create_connection(db_file)
    cur = conn.cursor()
    get_active_scenes = f'SELECT DISTINCT Name from "SceneHistory" WHERE Ended = 0'
    cur.execute(get_active_scenes)
    rows = cur.fetchall()
    conn.close()
    return rows


def get_ended_scenes(db_file):
    """returns a list of all ended scenes"""
    from src.mtool.util.sqlite import connection

    conn = connection.create_connection(db_file)
    cur = conn.cursor()
    get_ended_scenes = f'SELECT DISTINCT Name from "SceneHistory" WHERE Ended = 1'
    cur.execute(get_ended_scenes)
    rows = cur.fetchall()
    conn.close()
    return rows


def add_to_scene_history(db_file, timestamp, name, library):
    """adds a notebook to the scene history"""
    from src.mtool.util.sqlite import connection

    conn = connection.create_connection(db_file)
    cur = conn.cursor()
    add_to_scene_history = f'INSERT INTO "History"(Timestamp, Notebook, Library) VALUES (?,?,?)'
    cur.execute(add_to_scene_history, (timestamp, name, library))
    conn.commit()
    conn.close()


def get_notebook_history(db_file):
    """gets the notebook history from a scene"""
    from src.mtool.util.sqlite import connection

    conn = connection.create_connection(db_file)
    cur = conn.cursor()
    get_notebook_history = f'SELECT * FROM "History" ORDER BY Timestamp'
    cur.execute(get_notebook_history)
    conn.commit()
    rows = cur.fetchall()
    conn.close()
    return rows


def dump_scene_list(db_file):
    """empties the scene list table""" 
    from src.mtool.util.sqlite import connection

    conn = connection.create_connection(db_file)
    cur = conn.cursor()
    clear_list = f'DELETE FROM "SceneList"'
    reset_counter = "UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME='SceneList'"
    cur.execute(clear_list)
    cur.execute(reset_counter)
    conn.commit()
    conn.close()

def write_scene_list(db_file, scene_list):
    """writes to scene list table"""
    from src.mtool.util.sqlite import connection

    conn = connection.create_connection(db_file)
    cur = conn.cursor()
    insert_line = f'INSERT INTO "SceneList" (Name) VALUES (?)'
    cur.executemany(insert_line, scene_list)
    conn.commit()
    conn.close()


def get_scene_by_ord(db_file, ordinal):
    """gets scene by ordinal"""
    from src.mtool.util.sqlite import connection

    conn = connection.create_connection(db_file)
    cur = conn.cursor()
    list_env = f'SELECT Name FROM "SceneList" ORDER BY ID LIMIT {ordinal-1}, {ordinal}'
    cur.execute(list_env)
    conn.commit()
    rows = cur.fetchall()
    conn.close()
    if rows == []:
        return ""
    return rows[0][0]
