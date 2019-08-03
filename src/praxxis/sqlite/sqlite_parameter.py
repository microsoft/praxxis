"""
This file contains all of the sqlite functions for parameters
"""

def set_notebook_parameters(library_db, notebook_name, parameter_name, parameter_value, library):
    """set or update an parameter variable"""
    from src.praxxis.sqlite import connection

    conn = connection.create_connection(library_db)
    cur = conn.cursor()
    set_notebook_param = 'INSERT OR IGNORE INTO "NotebookDefaultParam" (Parameter, Value, Notebook, Library) VALUES(?, ?, ?, ?)'
    update_notebook_param = 'UPDATE "NotebookDefaultParam" SET Value = ? WHERE Parameter = ? AND Notebook = ? AND Library = ?'
    cur.execute(set_notebook_param, (parameter_name, parameter_value, notebook_name, library,))
    cur.execute(update_notebook_param, (parameter_value, parameter_name, notebook_name, library,))
    conn.commit()
    conn.close()


def clear_notebook_parameters(library_db):
    """empties the notebook parameter table""" 
    from src.praxxis.sqlite import connection

    conn = connection.create_connection(library_db)
    cur = conn.cursor()
    clear_parameter = 'DELETE FROM "NotebookDefaultParam"'
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
    get_library_params = 'SELECT Parameter, Value from "NotebookDefaultParam" WHERE Library = ?'
    cur.execute(get_library_params, (library,))
    parameters = cur.fetchall()
    conn.close()
    return parameters


def list_param(current_scene_db, query_start, query_end):
    """returns a list of set parameters in the scene"""
    from src.praxxis.sqlite import connection

    conn = connection.create_connection(current_scene_db)
    cur = conn.cursor()
    list_param = 'SELECT * FROM "Parameters" ORDER BY Parameter DESC LIMIT ?,?'
    cur.execute(list_param, (query_start, query_end))
    conn.commit()
    rows = cur.fetchall()
    conn.close()
    return rows


def get_all_param(current_scene_db):
    """returns a list of set parameters in the scene"""
    from src.praxxis.sqlite import connection

    conn = connection.create_connection(current_scene_db)
    cur = conn.cursor()
    list_param = 'SELECT * FROM "Parameters" ORDER BY Parameter DESC'
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
    get_param = 'SELECT Value FROM "Parameters" WHERE Parameter = ?'
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
    set_param = 'INSERT OR IGNORE INTO "Parameters"(Parameter, Value) VALUES(?,?)'
    upate_param = 'UPDATE "Parameters" SET Value = ? WHERE Parameter = ?'
    cur.execute(set_param, (parameter, value))
    cur.execute(upate_param, (value, parameter))
    conn.commit()
    conn.close()


def set_many_params(current_scene_db, parameter_list):
    from src.praxxis.sqlite import connection

    conn = connection.create_connection(current_scene_db)
    cur = conn.cursor()
    set_many_params = 'INSERT OR IGNORE INTO "Parameters"(Parameter, Value) VALUES(?,?)'
    cur.executemany(set_many_params, parameter_list)
    conn.commit()
    conn.close()

def get_param_by_ord(current_scene_db, ordinal):
    """get an parameter variable by ord"""
    from src.praxxis.sqlite import connection
    from src.praxxis.util import error

    conn = connection.create_connection(current_scene_db)
    cur = conn.cursor()
    list_param = 'SELECT * FROM "Parameters" ORDER BY Parameter DESC LIMIT ?,?'
    cur.execute(list_param, (ordinal-1, ordinal))
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
    param = 'SELECT * from "Parameters" WHERE Parameter = ?'
    cur.execute(param, (parameter,))
    exists = cur.fetchall()
    if exists == []:
        raise error.ParamNotFoundError(parameter)
    else:
        delete_param = 'DELETE FROM "Parameters" where Parameter = ?'
        cur.execute(delete_param, (parameter,))
        conn.commit()
        return 1
    conn.close()


def list_notebook_param(library_db, notebook, library):
    from src.praxxis.sqlite import connection
    conn = connection.create_connection(library_db)
    cur = conn.cursor()
    param = 'SELECT Parameter, Value from "NotebookDefaultParam" WHERE Notebook = ? AND Library = ?'
    cur.execute(param, (notebook, library))
    rows = cur.fetchall()
    conn.close()
    return rows