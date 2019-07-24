"""
This file contains all of the sqlite functions for parameters
"""

def set_notebook_parameters(library_db, notebook_name, parameter_name, parameter_value, library):
    """set or update an parameter variable"""
    from src.praxxis.sqlite import connection

    conn = connection.create_connection(library_db)
    cur = conn.cursor()
    set_notebook_param = f'INSERT OR IGNORE INTO "NotebookDefaultParam" (Parameter, Value, Notebook, Library) VALUES(?, ?, ?, ?)'
    update_notebook_param = f'UPDATE "NotebookDefaultParam" SET Value = ? WHERE Parameter = ? AND Notebook = ? AND Library = ?'

    cur.execute(set_notebook_param, (parameter_name, parameter_value, notebook_name, library,))
    cur.execute(update_notebook_param, (parameter_name, parameter_value, notebook_name, library,))
    conn.commit()
    conn.close()


def clear_notebook_parameters(library_db):
    """empties the notebook parameter table""" 
    from src.praxxis.sqlite import connection

    conn = connection.create_connection(library_db)
    cur = conn.cursor()
    clear_parameter = f'DELETE FROM "NotebookDefaultParam"'
    cur.execute(clear_parameter)
    conn.commit()
    conn.close()
    

def get_library_parameters(library_db, library):
    from src.praxxis.sqlite import connection
    from src.praxxis.sqlite import sqlite_library
    from src.praxxis.util import error

    try:
        sqlite_library.check_library_exists(library_db, library)
    except error.LibraryNotFoundError as e:
        raise e

    conn = connection.create_connection(library_db)
    cur = conn.cursor()
    get_library_params = f'SELECT Parameter, Value from "NotebookDefaultParam" WHERE Library = ?'
    cur.execute(get_library_params, (library,))
    parameters = cur.fetchall()
    conn.close()
    return parameters


def list_param(current_scene_db, start, end):
    """returns a list of set parameters in the scene"""
    from src.praxxis.sqlite import connection

    conn = connection.create_connection(current_scene_db)
    cur = conn.cursor()
    list_param = f'SELECT * FROM "Parameters" ORDER BY Parameter DESC LIMIT {start}, {end}'
    cur.execute(list_param)
    conn.commit()
    rows = cur.fetchall()
    conn.close()
    return rows


def get_all_param(current_scene_db):
    """returns a list of set parameters in the scene"""
    from src.praxxis.sqlite import connection

    conn = connection.create_connection(current_scene_db)
    cur = conn.cursor()
    list_param = f'SELECT * FROM "Parameters" ORDER BY Parameter DESC'
    cur.execute(list_param)
    conn.commit()
    rows = cur.fetchall()
    conn.close()
    return rows


def get_param(current_scene_db, parameter):
    """get the value of the specified parameter variable""" 
    from src.praxxis.sqlite import connection

    conn = connection.create_connection(current_scene_db)
    cur = conn.cursor()
    get_param = f'SELECT Value FROM "Parameters" WHERE Parameter = ?'
    cur.execute(get_param, (parameter,))
    conn.commit()
    value = cur.fetchone()
    conn.close()
    return value


def set_param(current_scene_db, parameter, value):
    """set or update an parameter variable"""
    from src.praxxis.sqlite import connection

    conn = connection.create_connection(current_scene_db)
    cur = conn.cursor()
    set_param = f'INSERT OR IGNORE INTO "Parameters"(Parameter, Value) VALUES("{parameter}", "{value}")'
    upate_param = f'UPDATE "Parameters" SET Value = "{value}" WHERE Parameter = "{parameter}"'
    cur.execute(set_param)
    cur.execute(upate_param)
    conn.commit()
    conn.close()


def set_many_params(current_scene_db, parameter_list):
    from src.praxxis.sqlite import connection

    conn = connection.create_connection(current_scene_db)
    cur = conn.cursor()
    set_many_params = f'INSERT OR IGNORE INTO "Parameters"(Parameter, Value) VALUES(?,?)'
    cur.executemany(set_many_params, parameter_list)
    conn.commit()
    conn.close()

def get_param_by_ord(current_scene_db, ordinal):
    """get an parameter variable by ord"""
    from src.praxxis.sqlite import connection
    from src.praxxis.util import error

    conn = connection.create_connection(current_scene_db)
    cur = conn.cursor()
    list_param = f'SELECT * FROM "Parameters" ORDER BY Name DESC LIMIT {ordinal-1}, {ordinal}'
    cur.execute(list_param)
    conn.commit()
    rows = cur.fetchall()
    conn.close()
    if rows == []:
        raise error.ParamNotFoundError(ordinal)
    return rows[0][0]


def delete_param(current_scene_db, parameter):
    """Delete an parameter"""
    from src.praxxis.sqlite import connection
    from src.praxxis.util import error

    conn = connection.create_connection(current_scene_db)
    cur = conn.cursor()
    param = f'SELECT * from "Parameters" WHERE Parameter = "{parameter}"'
    cur.execute(param)
    exists = cur.fetchall()
    if exists == []:
        raise error.ParamNotFoundError(parameter)
    else:
        delete_param = f'DELETE FROM "Parameters" where Parameter = "{parameter}"'
        cur.execute(delete_param)
        conn.commit()
        return 1
    conn.close()


def list_notebook_param(library_db, notebook, library):
    from src.praxxis.sqlite import connection
    
    conn = connection.create_connection(library_db)
    cur = conn.cursor()
    param = f'SELECT Parameter, Value from "NotebookDefaultParam" WHERE Notebook = "{notebook}" AND Library = "{library}"'
    cur.execute(param)
    rows = cur.fetchall()
    conn.close()
    return rows