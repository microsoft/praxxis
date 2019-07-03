"""
This file contains all of the sqlite functions for scenes
"""

def get_scene_id(db_file):
    """gets the scene ID from the scene db"""
    from src.mtool.util.sqlite import connection

    conn = connection.create_connection(db_file)
    cur = conn.cursor()
    get_scene_id = 'SELECT ID FROM "SceneMetadata"'
    cur.execute(get_scene_id)
    id = cur.fetchone()[0]
    conn.close()
    return id


def init_user_info(db_file):
    """From name of database file, creates and initializes user info"""
    import uuid
    import getpass

    from src.mtool.util.sqlite import connection

    conn = connection.create_connection(db_file)
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


def telem_on(db_file):
    """returns boolean of whether telemetry is enabled"""
    from src.mtool.util.sqlite import connection

    conn = connection.create_connection(db_file)
    cur = conn.cursor()
    query = f'SELECT Value FROM "UserInfo" WHERE Key = "TELEMETRY"'
    cur.execute(query)
    conn.commit()
    response = cur.fetchone()[0]
    return str(response) == str(1) # True if telemetry is on 

def get_telemetry_info(db_file):
    """gets the telemetry information:"""
    from src.mtool.util.sqlite import connection
    conn = connection.create_connection(db_file)
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

def get_settings(db_file, settings):
    """gets the current value of each setting"""
    from src.mtool.util.sqlite import connection

    values = {}
    conn = connection.create_connection(db_file)
    cur = conn.cursor()
    query = f'SELECT Value FROM "UserInfo" WHERE Key=?'
    for setting in settings:
        cur.execute(query, (setting,))
        conn.commit()
        values[setting] = cur.fetchone()[0]
    return values

def write_setting(db_file, setting, value):
    """changes the value of setting"""
    from src.mtool.util.sqlite import connection

    conn = connection.create_connection(db_file)
    cur = conn.cursor()
    update = f'UPDATE "UserInfo" SET Value = ? WHERE Key = ?'
    cur.execute(update, (value, setting))
    conn.commit()
    conn.close()
    return 
     
def write_settings(db_file, settings, values):
    for setting in settings:
        write_setting(db_file, setting, values[setting])