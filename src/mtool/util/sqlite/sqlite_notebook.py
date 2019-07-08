"""
This file contains the sqlite functions for notebooks
"""

def list_notebooks(db_file, start, end):
    """lists all loaded notebooks"""
    from src.mtool.util.sqlite import connection

    conn = connection.create_connection(db_file)
    cur = conn.cursor()
    list_libraries = f'SELECT Name, Root FROM "Notebooks" LIMIT {start}, {end}'
    cur.execute(list_libraries)
    conn.commit()
    rows = cur.fetchall()
    conn.close()
    return rows


def get_notebook(db_file, name):
    """returns a specific notebook"""
    from src.mtool.util.sqlite import connection

    conn = connection.create_connection(db_file)
    cur = conn.cursor()
    get_notebook = f'SELECT * FROM "Notebooks" WHERE Name = "{name}" LIMIT 0, 1'
    cur.execute(get_notebook)
    conn.commit()
    rows = cur.fetchall()
    conn.close()
    if rows == []:
        return 1
    return rows[0]


def get_notebook_by_ord(db_file, ordinal):
    """Returns list item referenced by input ordinal"""
    from src.mtool.util.sqlite import connection

    conn = connection.create_connection(db_file)
    cur = conn.cursor()
    query = f'SELECT Data FROM NotebookList WHERE ID = "{ordinal}" LIMIT 0, 1'
    cur.execute(query)
    conn.commit()
    item = cur.fetchone()
    conn.close()
    return item


def write_list(db_file, notebook_list, path_list = []):
    """creates the list of notebooks in list"""
    from src.mtool.util.sqlite import connection

    conn = connection.create_connection(db_file)
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


def get_notebook_path(db_file, notebook, library):
    """gets notebook path from libraries/notebooks"""
    from src.mtool.util.sqlite import connection

    conn = connection.create_connection(db_file)
    cur = conn.cursor()
    get_notebook_path = f"SELECT ROOT FROM 'Notebooks' WHERE NAME=? AND LIBRARYNAME=?"
    cur.execute(get_notebook_path, (notebook, library))
    conn.commit()
    path = cur.fetchone()
    conn.close()
    if path == None:
        return None
    return path[0]
    

def search_notebooks(db_file, search_term, start, end):
    """searches notebooks for search term"""
    from src.mtool.util.sqlite import connection

    conn = connection.create_connection(db_file)
    cur = conn.cursor()
    list_env = f'SELECT Name, Root FROM "Notebooks" WHERE Name LIKE "%{search_term}%" ORDER BY Name LIMIT {start}, {end}'
    cur.execute(list_env)
    conn.commit()
    rows = cur.fetchall()
    conn.close()
    return rows
