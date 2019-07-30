"""
This file contains all of the sqlite functions for telemetry
"""

def get_scene_id(current_scene_db):
    """gets the scene ID from the scene db"""
    from src.praxxis.sqlite import connection

    conn = connection.create_connection(current_scene_db)
    cur = conn.cursor()
    get_scene_id = 'SELECT ID FROM "SceneMetadata"'
    cur.execute(get_scene_id)
    id = str(cur.fetchone()[0])
    conn.close()
    return id


def telem_init(user_info_db):
    """returns boolean of whether telemetry was ever set up
    (checks whether Host has a value) 
    """
    from src.praxxis.sqlite import connection

    conn = connection.create_connection(user_info_db)
    cur = conn.cursor()
    query = f'SELECT Value FROM "UserInfo" WHERE Key = "Host"'
    cur.execute(query)
    conn.commit()
    response = cur.fetchone()[0]
    return response != None # True if telemetry is initialized


def telem_on(user_info_db):
    """returns boolean of whether telemetry is enabled"""
    from src.praxxis.sqlite import connection

    conn = connection.create_connection(user_info_db)
    cur = conn.cursor()
    query = f'SELECT Value FROM "UserInfo" WHERE Key = "TELEMETRY"'
    cur.execute(query)
    conn.commit()
    response = cur.fetchone()[0]
    return str(response) == str(1) # True if telemetry is on 


def get_telemetry_info(user_info_db):
    """gets the telemetry information:"""
    from src.praxxis.sqlite import connection
    conn = connection.create_connection(user_info_db)
    cur = conn.cursor()
    query = f'SELECT Value FROM "UserInfo" WHERE Key in ("URL", "Host", "Username", "Password", "ID") ORDER BY Key="ID", Key="Password", Key="Username", Key="URL", Key="Host"'
    cur.execute(query)
    conn.commit()
    info = cur.fetchall()
    if info != None:
        for i in range(len(info)):
            info[i] = info[i][0]
    conn.close()
    return info


def get_settings(user_info_db, settings):
    """gets the current value of each setting"""
    from src.praxxis.sqlite import connection

    values = {}
    conn = connection.create_connection(user_info_db)
    cur = conn.cursor()
    query = f'SELECT Value FROM "UserInfo" WHERE Key=?'
    for setting in settings:
        cur.execute(query, (setting,))
        conn.commit()
        values[setting] = cur.fetchone()[0]
    return values


def write_setting(user_info_db, setting, value):
    """changes the value of setting"""
    from src.praxxis.sqlite import connection

    conn = connection.create_connection(user_info_db)
    cur = conn.cursor()
    update = f'UPDATE "UserInfo" SET Value = ? WHERE Key = ?'
    cur.execute(update, (value, setting))
    conn.commit()
    conn.close()
    return 
     

def write_settings(user_info_db, settings, values):
    for setting in settings:
        write_setting(user_info_db, setting, values[setting])


def add_to_backlog(user_info_db, local_copy, scene_id, error):
    """adds this file to the telemetry backlog"""
    from src.praxxis.sqlite import connection

    conn = connection.create_connection(user_info_db)
    cur = conn.cursor()
    add = f'INSERT INTO "TelemBacklog" (LocalCopy, SceneID, Error) VALUES (?,?,?)'
    cur.execute(add, (local_copy, scene_id, error))
    conn.commit()
    conn.close()
    return


def backlog_size(user_info_db):
    """returns current size of telemetry backlog"""
    from src.praxxis.sqlite import connection

    conn = connection.create_connection(user_info_db)
    cur = conn.cursor()
    getcount = f'SELECT COUNT(*) FROM "TelemBacklog"'
    cur.execute(getcount)
    conn.commit()
    count = cur.fetchone()[0]
    conn.close()
    return count


def get_backlog(user_info_db):
    """returns the backlog"""
    from src.praxxis.sqlite import connection

    conn = connection.create_connection(user_info_db)
    cur = conn.cursor()
    getbacklog = f'SELECT * FROM "TelemBacklog"'
    cur.execute(getbacklog)
    conn.commit()
    toSend = cur.fetchall()
    conn.close()
    return toSend


def delete_from_backlog(user_info_db, local_copy):
    """deletes sent telemetry from backlog, if in backlog"""
    from src.praxxis.sqlite import connection

    conn = connection.create_connection(user_info_db)
    cur = conn.cursor()
    cleanup = f'DELETE FROM "TelemBacklog" WHERE LocalCopy = ?'
    cur.execute(cleanup, (local_copy,))
    conn.commit()
    conn.close()

def clear_backlog(user_info_db):
    """clears backlog completely (for testing purposes)"""
    from src.praxxis.sqlite import connection

    conn = connection.create_connection(user_info_db)
    cur = conn.cursor()
    cleanup = 'DELETE FROM "TelemBacklog"'
    cur.execute(cleanup)
    conn.commit()
    conn.close()
