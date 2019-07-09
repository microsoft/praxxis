"""
This file contains the sqlite functions for notebooks
"""

def list_notebooks(library_db, start, end):
    """lists all loaded notebooks"""
    from src.mtool.util.sqlite import connection

    conn = connection.create_connection(library_db)
    cur = conn.cursor()
    list_libraries = f'SELECT Name, Root FROM "Notebooks" LIMIT {start}, {end}'
    cur.execute(list_libraries)
    conn.commit()
    rows = cur.fetchall()
    conn.close()
    return rows


def get_notebook(library_db, name):
    """returns a specific notebook"""
    from src.mtool.util.sqlite import connection
    from src.mtool.util import error

    conn = connection.create_connection(library_db)
    cur = conn.cursor()
    get_notebook = f'SELECT * FROM "Notebooks" WHERE Name = "{name}" LIMIT 0, 1'
    cur.execute(get_notebook)
    conn.commit()
    rows = cur.fetchall()
    conn.close()
    if rows == []:
        raise error.NotebookNotFoundError(name)
    return rows[0]


def get_notebook_by_ord(current_scene_db, ordinal):
    """Returns list item referenced by input ordinal"""
    from src.mtool.util.sqlite import connection
    from src.mtool.util import error

    conn = connection.create_connection(current_scene_db)
    cur = conn.cursor()
    query = f'SELECT Data FROM NotebookList WHERE ID = "{ordinal}" LIMIT 0, 1'
    cur.execute(query)
    conn.commit()
    item = cur.fetchone()
    conn.close()
    if item == None:
        raise error.NotebookNotFoundError
    return item


def write_list(current_scene_db, notebook_list, path_list = []):
    """creates the list of notebooks in list"""
    from src.mtool.util.sqlite import connection

    conn = connection.create_connection(current_scene_db)
    cur = conn.cursor()
    clear_list = f'DELETE FROM "NotebookList"'
    reset_counter = "UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME='NotebookList'"
    insert_line = f'INSERT INTO "NotebookList" (DATA, PATH) VALUES (?,?)'
    cur.execute(clear_list)
    cur.execute(reset_counter)
    if path_list == []:
        cur.executemany(insert_line, notebook_list)
    else:
        cur.executemany(insert_line, (notebook_list, path_list))
    conn.commit()
    conn.close()


def get_notebook_path(library_db, notebook, library):
    """gets notebook path from libraries/notebooks"""
    from src.mtool.util.sqlite import connection

    conn = connection.create_connection(library_db)
    cur = conn.cursor()
    get_notebook_path = f"SELECT ROOT FROM 'Notebooks' WHERE NAME=? AND LIBRARYNAME=?"
    cur.execute(get_notebook_path, (notebook, library))
    conn.commit()
    path = cur.fetchone()
    conn.close()
    if path == None:
        return None
    return path[0]
    

def search_notebooks(library_db, search_term, start, end):
    """searches notebooks for search term"""
    from src.mtool.util.sqlite import connection

    conn = connection.create_connection(library_db)
    cur = conn.cursor()
    list_env = f'SELECT Name, Root FROM "Notebooks" WHERE Name LIKE "%{search_term}%" ORDER BY Name LIMIT {start}, {end}'
    cur.execute(list_env)
    conn.commit()
    rows = cur.fetchall()
    conn.close()
    return rows
