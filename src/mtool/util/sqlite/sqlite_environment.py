"""
This file contains all of the sqlite functions for environments
"""

def get_notebook_environments(db_file, name):
    """gets the scene ID from the scene db"""
    from src.mtool.util.sqlite import connection

    conn = connection.create_connection(db_file)
    cur = conn.cursor()
    get_notebook_environment = f'SELECT * FROM "Environment" WHERE NotebookName = "{name}"'
    cur.execute(get_notebook_environment)
    id = cur.fetchall()
    conn.close()
    return id

def set_notebook_environments(library_db, notebook_name, environment_name, environment_value):
    """set or update an environment variable"""
    from src.mtool.util.sqlite import connection

    conn = connection.create_connection(library_db)
    cur = conn.cursor()
    set_env = f'INSERT OR IGNORE INTO "Environment" (Name, Value, NotebookName) VALUES(?, ?, ?)'
    update_env = f'UPDATE "Environment" SET Value = ? WHERE Name = ? AND NotebookName = ?'
    cur.execute(set_env, (environment_name, environment_value, notebook_name))
    cur.execute(update_env, (environment_name, environment_value, notebook_name))
    conn.commit()
    conn.close()

def clear_notebook_environments(db_file):
    """empties the notebook environment table""" 
    from src.mtool.util.sqlite import connection

    conn = connection.create_connection(db_file)
    cur = conn.cursor()
    clear_environment = f'DELETE FROM "Environment"'
    cur.execute(clear_environment)
    conn.commit()
    conn.close()
    

def get_library_environments(db_file, library_name):
    from src.mtool.util.sqlite import connection

    conn = connection.create_connection(db_file)
    cur = conn.cursor()
    get_library_envs = f'SELECT Name, Value from "Environment" Where NotebookName IN (SELECT Name FROM "Notebooks" WHERE LibraryName = "{library_name}")'
    cur.execute(get_library_envs)
    environments = cur.fetchall()
    conn.close()
    return environments


def list_env(db_file, start, end):
    """returns a list of set environment variables in the scene"""
    from src.mtool.util.sqlite import connection

    conn = connection.create_connection(db_file)
    cur = conn.cursor()
    list_env = f'SELECT * FROM "Environment" ORDER BY Name DESC LIMIT {start}, {end}'
    cur.execute(list_env)
    conn.commit()
    rows = cur.fetchall()
    conn.close()
    return rows


def get_all_env(db_file):
    """returns a list of set environment variables in the scene"""
    from src.mtool.util.sqlite import connection

    conn = connection.create_connection(db_file)
    cur = conn.cursor()
    list_env = f'SELECT * FROM "Environment" ORDER BY Name DESC'
    cur.execute(list_env)
    conn.commit()
    rows = cur.fetchall()
    conn.close()
    return rows


def get_env(db_file, var_name):
    """get the value of the specified environment variable""" 
    from src.mtool.util.sqlite import connection

    conn = connection.create_connection(db_file)
    cur = conn.cursor()
    get_env = f'SELECT Value FROM "Environment" WHERE Name = ?'
    cur.execute(get_env, (var_name,))
    conn.commit()
    value = cur.fetchone()   #just a value, not the tuple
    conn.close()
    return value

def set_env(current_scene_db, name, value):
    """set or update an environment variable"""
    from src.mtool.util.sqlite import connection

    conn = connection.create_connection(current_scene_db)
    cur = conn.cursor()
    set_env = f'INSERT OR IGNORE INTO "Environment"(Name, Value) VALUES("{name}", "{value}")'
    upate_env = f'UPDATE "Environment" SET Value = "{value}" WHERE Name = "{name}"'
    cur.execute(set_env)
    cur.execute(upate_env)
    conn.commit()
    conn.close()


def get_env_by_ord(current_scene_db, ordinal):
    """get an environment variable by ord"""
    from src.mtool.util.sqlite import connection
    from src.mtool.util import error

    conn = connection.create_connection(current_scene_db)
    cur = conn.cursor()
    list_env = f'SELECT * FROM "Environment" ORDER BY Name DESC LIMIT {ordinal-1}, {ordinal}'
    cur.execute(list_env)
    conn.commit()
    rows = cur.fetchall()
    conn.close()
    if rows == []:
        raise error.EnvNotFoundError(ordinal)
    return rows[0][0]


def delete_env(current_scene_db, name):
    """Delete an environment variable"""
    from src.mtool.util.sqlite import connection
    from src.mtool.util import error

    conn = connection.create_connection(current_scene_db)
    cur = conn.cursor()
    env = f'SELECT * from "Environment" WHERE Name = "{name}"'
    cur.execute(env)
    exists = cur.fetchall()
    if exists == []:
        conn.close()
        raise error.EnvNotFoundError(name)
    else:
        delete_env = f'DELETE FROM "Environment" where Name = "{name}"'
        cur.execute(delete_env)
        conn.commit()
        conn.close()
        return 1

def list_notebook_env(db_file, notebook_name):
    from src.mtool.util.sqlite import connection

    conn = connection.create_connection(db_file)
    cur = conn.cursor()
    env = f'SELECT Name, Value from "Environment" WHERE NotebookName = "{notebook_name}"'
    cur.execute(env)
    rows = cur.fetchall()
    conn.close()
    return rows