"""
This file contains all of the sqlite functions for environments
"""

def set_notebook_environments(library_db, notebook_name, environment_name, environment_value):
    """set or update an environment variable"""
    from src.mtool.util.sqlite import connection

    conn = connection.create_connection(library_db)
    cur = conn.cursor()
    set_notebook_env = f'INSERT OR IGNORE INTO "NotebookEnvironment" (EnvironmentName, NotebookName) VALUES(?, ?)'
    set_env = f'INSERT OR IGNORE INTO "Environment" (Name, Value) VALUES(?, ?)'    
    update_env = f'UPDATE "Environment" SET Value = ? WHERE Name = ?'

    cur.execute(set_notebook_env, (environment_name, notebook_name))
    cur.execute(set_env, (environment_name, environment_value))
    cur.execute(update_env, (environment_name, environment_value))
    conn.commit()
    conn.close()

def clear_notebook_environments(library_db):
    """empties the notebook environment table""" 
    from src.mtool.util.sqlite import connection

    conn = connection.create_connection(library_db)
    cur = conn.cursor()
    clear_environment = f'DELETE FROM "Environment"'
    cur.execute(clear_environment)
    conn.commit()
    conn.close()
    

def get_library_environments(library_db, library_name):
    from src.mtool.util.sqlite import connection

    conn = connection.create_connection(library_db)
    cur = conn.cursor()
    get_library_envs = f'SELECT Name, Value from "Environment" WHERE Name in (SELECT EnvironmentName FROM NotebookEnvironment WHERE NotebookName IN (SELECT Name FROM "Notebooks" WHERE LibraryName = "{library_name}"))'
    cur.execute(get_library_envs)
    environments = cur.fetchall()
    conn.close()
    return environments


def list_env(current_scene_db, start, end):
    """returns a list of set environment variables in the scene"""
    from src.mtool.util.sqlite import connection

    conn = connection.create_connection(current_scene_db)
    cur = conn.cursor()
    list_env = f'SELECT * FROM "Environment" ORDER BY Name DESC LIMIT {start}, {end}'
    cur.execute(list_env)
    conn.commit()
    rows = cur.fetchall()
    conn.close()
    return rows


def get_all_env(current_scene_db):
    """returns a list of set environment variables in the scene"""
    from src.mtool.util.sqlite import connection

    conn = connection.create_connection(current_scene_db)
    cur = conn.cursor()
    list_env = f'SELECT * FROM "Environment" ORDER BY Name DESC'
    cur.execute(list_env)
    conn.commit()
    rows = cur.fetchall()
    conn.close()
    return rows


def get_env(current_scene_db, var_name):
    """get the value of the specified environment variable""" 
    from src.mtool.util.sqlite import connection

    conn = connection.create_connection(current_scene_db)
    cur = conn.cursor()
    get_env = f'SELECT Value FROM "Environment" WHERE Name = ?'
    cur.execute(get_env, (var_name,))
    conn.commit()
    value = cur.fetchone()
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

def list_notebook_env(library_db, notebook_name):
    from src.mtool.util.sqlite import connection

    conn = connection.create_connection(library_db)
    cur = conn.cursor()
    env = f'SELECT Name, Value from "Environment" WHERE Name in (SELECT EnvironmentName from NotebookEnvironment WHERE NotebookName = "{notebook_name}")'
    cur.execute(env)
    rows = cur.fetchall()
    conn.close()
    return rows