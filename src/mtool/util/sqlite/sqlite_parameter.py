"""
This file contains all of the sqlite functions for parameters
"""

def set_notebook_parameters(library_db, notebook_name, parameter_name, parameter_value):
    """set or update an parameter variable"""
    from src.mtool.util.sqlite import connection

    conn = connection.create_connection(library_db)
    cur = conn.cursor()
    set_notebook_param = f'INSERT OR IGNORE INTO "NotebookParameter" (ParameterName, NotebookName) VALUES(?, ?)'
    set_param = f'INSERT OR IGNORE INTO "Parameter" (Name, Value) VALUES(?, ?)'    
    update_param = f'UPDATE "Parameter" SET Value = ? WHERE Name = ?'

    cur.execute(set_notebook_param, (parameter_name, notebook_name))

    cur.execute(set_param, (parameter_name, parameter_value))
    cur.execute(update_param, (parameter_name, parameter_value))
    conn.commit()
    conn.close()

def clear_notebook_parameters(library_db):
    """empties the notebook parameter table""" 
    from src.mtool.util.sqlite import connection

    conn = connection.create_connection(library_db)
    cur = conn.cursor()
    clear_parameter = f'DELETE FROM "Parameter"'
    cur.execute(clear_parameter)
    conn.commit()
    conn.close()
    

def get_library_parameters(library_db, library_name):
    from src.mtool.util.sqlite import connection
    from src.mtool.util.sqlite import sqlite_library
    from src.mtool.util import error

    try:
        sqlite_library.check_library_exists(library_db, library_name)
    except error.LibraryNotFoundError as e:
        raise e

    conn = connection.create_connection(library_db)
    cur = conn.cursor()
    get_library_params = f'SELECT Name, Value from "Parameter" WHERE Name in (SELECT ParameterName FROM NotebookParameter WHERE NotebookName IN (SELECT Name FROM "Notebooks" WHERE LibraryName = "{library_name}"))'
    cur.execute(get_library_params)
    parameters = cur.fetchall()
    conn.close()
    return parameters


def list_param(current_scene_db, start, end):
    """returns a list of set parameter variables in the scene"""
    from src.mtool.util.sqlite import connection

    conn = connection.create_connection(current_scene_db)
    cur = conn.cursor()
    list_param = f'SELECT * FROM "Parameters" ORDER BY Parameter DESC LIMIT {start}, {end}'
    cur.execute(list_param)
    conn.commit()
    rows = cur.fetchall()
    conn.close()
    return rows


def get_all_param(current_scene_db):
    """returns a list of set parameter variables in the scene"""
    from src.mtool.util.sqlite import connection

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
    from src.mtool.util.sqlite import connection

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
    from src.mtool.util.sqlite import connection

    conn = connection.create_connection(current_scene_db)
    cur = conn.cursor()
    set_param = f'INSERT OR IGNORE INTO "Parameters"(Parameter, Value) VALUES("{parameter}", "{value}")'
    upate_param = f'UPDATE "Parameters" SET Value = "{value}" WHERE Parameter = "{parameter}"'
    cur.execute(set_param)
    cur.execute(upate_param)
    conn.commit()
    conn.close()


def set_many_params(current_scene_db, parameter_list):
    from src.mtool.util.sqlite import connection

    conn = connection.create_connection(current_scene_db)
    cur = conn.cursor()
    set_many_params = f'INSERT OR IGNORE INTO "Parameters"(Parameter, Value) VALUES(?,?)'
    cur.executemany(set_many_params, parameter_list)
    conn.commit()
    conn.close()

def get_param_by_ord(current_scene_db, ordinal):
    """get an parameter variable by ord"""
    from src.mtool.util.sqlite import connection
    from src.mtool.util import error

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
    """Delete an parameter variable"""
    from src.mtool.util.sqlite import connection
    from src.mtool.util import error

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


def list_notebook_param(library_db, notebook_name):
    from src.mtool.util.sqlite import connection

    conn = connection.create_connection(library_db)
    cur = conn.cursor()
    param = f'SELECT Name, Value from "Parameter" WHERE Name in (SELECT ParameterName from NotebookParameter WHERE NotebookName = "{notebook_name}")'
    cur.execute(param)
    rows = cur.fetchall()
    conn.close()
    return rows