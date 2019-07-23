"""
This file contains all of the sqlite functions for libraries
"""

def clear_loaded_libararies(library_db):
    from src.mtool.sqlite import connection

    conn = connection.create_connection(library_db)
    cur = conn.cursor()
    clear_metadata = f'DELETE FROM "LibraryMetadata"'
    clear_notebooks = f'DELETE FROM "Notebooks"'
    cur.execute(clear_metadata)
    cur.execute(clear_notebooks)
    conn.commit()
    conn.close()


def load_library(library_db, path, readme, library):
    """load a library into the library db"""
    from src.mtool.sqlite import connection

    conn = connection.create_connection(library_db)
    cur = conn.cursor()
    load_library = f'INSERT OR IGNORE INTO "LibraryMetadata"(Path, Readme, Library) VALUES("{path}", "{readme}", "{library}")'
    update_library = f'UPDATE "LibraryMetadata" SET Readme = "{readme}" WHERE Library = "{library}"'
    cur.execute(load_library)
    cur.execute(update_library)
    conn.commit()
    conn.close()


def load_notebook(library_db, file_root, notebook, library):
    """load a notebook into the library db"""
    from src.mtool.sqlite import connection

    conn = connection.create_connection(library_db)
    cur = conn.cursor()
    load_library = f'INSERT OR IGNORE INTO "Notebooks"(Path, Notebook, Library) VALUES("{file_root}", "{notebook}", "{library}")'
    cur.execute(load_library)
    conn.commit()
    conn.close()
    

def list_libraries(library_db, start, end):
    """returns a list of loaded libraries"""
    from src.mtool.sqlite import connection

    conn = connection.create_connection(library_db)
    cur = conn.cursor()
    list_libraries = f'SELECT Library FROM "LibraryMetadata" ORDER BY Library LIMIT {start}, {end}'
    cur.execute(list_libraries)
    conn.commit()
    rows = cur.fetchall()
    conn.close()
    return rows


def check_library_exists(library_db, library):
    from src.mtool.sqlite import connection
    from src.mtool.util import error

    conn = connection.create_connection(library_db)
    cur = conn.cursor()
    get_library = f'SELECT * FROM "LibraryMetadata" WHERE Library = "{library}" LIMIT 0, 1'
    cur.execute(get_library)
    conn.commit()
    rows = cur.fetchall()
    conn.close()
    if rows == []:
        raise error.LibraryNotFoundError(library)
    return True


def remove_library(library_db, library):
    from src.mtool.sqlite import connection

    conn = connection.create_connection(library_db)
    cur = conn.cursor()
    clear_library = f'DELETE FROM "LibraryMetadata" WHERE Library = "{library}"'
    clear_notebooks = f'DELETE FROM "Notebooks" WHERE Library = "{library}"'
    clear_parameter = f'DELETE FROM NotebookDefaultParam Where Library = "{library}"'
    cur.execute(clear_library)
    cur.execute(clear_notebooks)
    cur.execute(clear_parameter)
    conn.commit()
    conn.close()


def remove_notebook(library_db, notebook):
    from src.mtool.sqlite import connection
    
    conn = connection.create_connection(library_db)
    cur = conn.cursor()
    clear_parameter = f'DELETE FROM NotebookDefaultParam Where Notebook = "{notebook}"'
    clear_notebook = f'DELETE FROM Notebooks WHERE Notebook = "{notebook}"'
    cur.execute(clear_parameter)
    cur.execute(clear_notebook)
    conn.commit()
    conn.close()
