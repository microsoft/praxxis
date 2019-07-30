"""
This file contains all of the sqlite functions for libraries
"""

def clear_loaded_libararies(library_db):
    from src.praxxis.sqlite import connection

    conn = connection.create_connection(library_db)
    cur = conn.cursor()
    clear_metadata = f'DELETE FROM "LibraryMetadata"'
    clear_notebooks = f'DELETE FROM "Notebooks"'
    cur.execute(clear_metadata)
    cur.execute(clear_notebooks)
    conn.commit()
    conn.close()


def get_library_by_name(library_db, library):
    """returns a list of loaded libraries"""
    from src.praxxis.sqlite import connection

    conn = connection.create_connection(library_db)
    cur = conn.cursor()
    get_library = f'SELECT * FROM "LibraryMetadata" WHERE Library = "{library}"'
    cur.execute(get_library)
    conn.commit()
    rows = cur.fetchall()
    conn.close()
    return rows


def get_library_by_root(library_db, path):
    """returns a list of loaded libraries"""
    from src.praxxis.sqlite import connection

    conn = connection.create_connection(library_db)
    cur = conn.cursor()
    get_library = f'SELECT * FROM "LibraryMetadata" WHERE Path = "{path}"'
    cur.execute(get_library)
    conn.commit()
    rows = cur.fetchall()
    conn.close()
    return rows


def load_library(library_db, path, readme, library, remote=None):
    """load a library into the library db"""
    from src.praxxis.sqlite import connection

    conn = connection.create_connection(library_db)
    cur = conn.cursor()
    load_library = f'INSERT OR IGNORE INTO "LibraryMetadata"(Path, Readme, Library, Remote) VALUES("{path}", "{readme}", "{library}", {remote})'
    update_library = f'UPDATE "LibraryMetadata" SET Readme = "{readme}" WHERE Library = "{library}"'
    cur.execute(load_library)
    cur.execute(update_library)
    conn.commit()
    conn.close()


def load_notebook(library_db, path, notebook, library, raw_url=None):
    """load a notebook into the library db"""
    from src.praxxis.sqlite import connection

    conn = connection.create_connection(library_db)
    cur = conn.cursor()
    load_library = f'INSERT OR IGNORE INTO "Notebooks"(Path, Notebook, Library, RawUrl) VALUES("{path}", "{notebook}", "{library}", "{raw_url}")'
    cur.execute(load_library)
    conn.commit()
    conn.close()


def sync_library(library_db, path, readme, library, remote=None):
    """load a library into the library db"""
    from src.praxxis.sqlite import connection

    conn = connection.create_connection(library_db)
    cur = conn.cursor()
    load_library = f'INSERT OR IGNORE INTO "LibraryMetadata"(Path, Readme, Library, Remote) VALUES("{path}", "{readme}", "{library}", "{remote}")'
    update_library = f'UPDATE "LibraryMetadata" SET Readme = "{readme}" WHERE Library = "{library}"'
    cur.execute(load_library)
    cur.execute(update_library)
    conn.commit()
    conn.close()

    

def list_libraries(library_db, start, end):
    """returns a list of loaded libraries"""
    from src.praxxis.sqlite import connection

    conn = connection.create_connection(library_db)
    cur = conn.cursor()
    list_libraries = f'SELECT Library FROM "LibraryMetadata" ORDER BY Library LIMIT {start}, {end}'
    cur.execute(list_libraries)
    conn.commit()
    rows = cur.fetchall()
    conn.close()
    return rows


def check_library_exists(library_db, library):
    from src.praxxis.sqlite import connection
    from src.praxxis.util import error

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
    from src.praxxis.sqlite import connection

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


def remove_notebook(library_db, notebook, library):
    from src.praxxis.sqlite import connection

    conn = connection.create_connection(library_db)
    cur = conn.cursor()
    clear_parameter = f'DELETE FROM NotebookDefaultParam Where Notebook = "{notebook}" AND Library = "{library}"'
    clear_notebook = f'DELETE FROM Notebooks WHERE Notebook = "{notebook}" AND Library = "{library}"'
    cur.execute(clear_parameter)
    cur.execute(clear_notebook)
    conn.commit()
    conn.close()
