"""
This file contains all init functions to be run at the first 
instantiation of praxxis (or if something from the data is deleted
unexpectedly)
"""

def init_library_db(library_db):  
    """initializes the library database"""
    from src.praxxis.sqlite import connection

    conn = connection.create_connection(library_db)
    cur = conn.cursor()
    create_metadata_table = f'CREATE TABLE "LibraryMetadata" (Path TEXT PRIMARY KEY, Readme TEXT, Library TEXT, Remote TEXT)'
    create_notebook_table = f'CREATE TABLE "Notebooks" (Path TEXT PRIMARY KEY, Notebook TEXT, Library TEXT, RawUrl TEXT, FOREIGN KEY(Library) REFERENCES "LibraryMetadata"(Library))'
    create_parameter_table = f'CREATE TABLE "Parameters" (Parameter TEXT PRIMARY KEY, Value TEXT)'
    create_notebook_parameter_table = f'CREATE TABLE "NotebookDefaultParam" (Parameter TEXT, Value TEXT, Notebook TEXT, Library TEXT,  PRIMARY KEY(Parameter, Library, Notebook), FOREIGN KEY(Notebook) REFERENCES "Notebooks"(Notebook), FOREIGN KEY(Parameter) REFERENCES "Parameters"(Parameter), FOREIGN KEY(Library) REFERENCES "Library"(Library))'
    cur.execute(create_metadata_table)
    cur.execute(create_notebook_table)
    cur.execute(create_parameter_table)
    cur.execute(create_notebook_parameter_table)
    conn.commit()
    conn.close()


def init_model_db(model_db):
    """initializes the base model database"""
    from src.praxxis.sqlite import connection

    conn = connection.create_connection(model_db)
    cur = conn.cursor()
    create_models_table = f'CREATE TABLE "Models" (Name TEXT PRIMARY KEY, Info TEXT, Date TEXT, Path TEXT, ConverterPath TEXT)'
    cur.execute(create_models_table)
    conn.commit()
    conn.close()


def init_rulesengine_db(rulesengine_db):
    """initializes the base rules engine database"""
    from src.praxxis.sqlite import connection

    conn = connection.create_connection(rulesengine_db)
    cur = conn.cursor()
    create_rules_table = f'CREATE TABLE "RulesEngine" (ID INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT, Path TEXT, Active INTEGER)'
    cur.execute(create_rules_table)
    conn.commit()
    conn.close()


def init_history(history_db, scene_name):
    """initializes the current scene database"""
    from src.praxxis.sqlite import connection

    conn = connection.create_connection(history_db)
    cur = conn.cursor()
    create_scene_history_table = 'CREATE TABLE "SceneHistory" (ID INTEGER PRIMARY KEY AUTOINCREMENT, Scene TEXT, Ended INTEGER)'
    create_scene_list_table=f'CREATE TABLE "SceneList" (ID INTEGER PRIMARY KEY AUTOINCREMENT, Scene TEXT)'
    cur.execute(create_scene_list_table)
    cur.execute(create_scene_history_table)
    conn.commit()
    conn.close()


def init_user_info(telemetry_db, send_telemetry=1):
    """From name of database file, creates and initializes user info"""
    import uuid
    import getpass

    from src.praxxis.sqlite import connection

    conn = connection.create_connection(telemetry_db)
    cur = conn.cursor()
    create_userinfo_table = f'CREATE TABLE "UserInfo" (Key TEXT PRIMARY KEY, Value TEXT)'
    create_user_id = f'INSERT INTO "UserInfo" (Key, Value) VALUES ("ID",?)'
    create_telem_permissions = f'INSERT INTO "UserInfo" (Key, Value) VALUES ("TELEMETRY", {send_telemetry})'
    create_host = f'INSERT INTO "UserInfo" (Key) VALUES ("Host")'
    create_url = f'INSERT INTO "UserInfo" (Key, Value) VALUES ("URL", ?)'
    create_user = f'INSERT INTO "UserInfo" (Key) VALUES ("Username")'
    create_pswd = f'INSERT INTO "UserInfo" (Key) VALUES ("Password")'
    create_telemetry_table = f'CREATE TABLE "TelemBacklog" (LocalCopy TEXT PRIMARY KEY, SceneID TEXT, Error TEXT, Operation INTEGER)'
    id_val = str(uuid.uuid4())
    
    cur.execute(create_userinfo_table)
    cur.execute(create_user_id, (id_val,))
    cur.execute(create_telem_permissions)
    url = "https://{0}:30443/gateway/default/webhdfs/v1/praxxis"
    cur.execute(create_host)
    cur.execute(create_url, (url,))
    cur.execute(create_user)
    cur.execute(create_pswd)
    cur.execute(create_telemetry_table)
    conn.commit()
    conn.close()

