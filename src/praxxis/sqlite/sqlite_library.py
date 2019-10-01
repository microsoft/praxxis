"""
This file contains all of the sqlite functions for libraries
"""


def clear_loaded_libararies(library_db):
    from src.praxxis.sqlite import connection

    conn = connection.create_connection(library_db)
    cur = conn.cursor()
    clear_metadata = 'DELETE FROM "LibraryMetadata"'
    clear_notebooks = 'DELETE FROM "Notebooks"'
    cur.execute(clear_metadata)
    cur.execute(clear_notebooks)
    conn.commit()
    conn.close()


def get_library_by_name(library_db, library):
    """returns a list of loaded libraries"""
    from src.praxxis.sqlite import connection

    conn = connection.create_connection(library_db)
    cur = conn.cursor()
    get_library = 'SELECT * FROM "LibraryMetadata" WHERE Library = ?'
    cur.execute(get_library, (library,))
    conn.commit()
    rows = cur.fetchall()
    conn.close()
    return rows


def get_library_by_root(library_db, path):
    """returns a list of loaded libraries"""
    from src.praxxis.sqlite import connection

    conn = connection.create_connection(library_db)
    cur = conn.cursor()
    get_library = 'SELECT * FROM "LibraryMetadata" WHERE Path = ?'
    cur.execute(get_library, (path,))
    conn.commit()
    rows = cur.fetchall()
    conn.close()
    return rows


def load_library(library_db, path, readme, library, remote=None):
    """load a library into the library db"""
    from src.praxxis.sqlite import connection

    conn = connection.create_connection(library_db)
    cur = conn.cursor()
    load_library = 'INSERT OR IGNORE INTO "LibraryMetadata"(Path, Readme, Library, Remote) VALUES(?,?,?,?)'
    update_library = 'UPDATE "LibraryMetadata" SET Readme = ? WHERE Library = ?'
    cur.execute(load_library, (path, readme, library, remote))
    cur.execute(update_library, (readme, library))
    conn.commit()
    conn.close()


def load_notebook(library_db, path, notebook, library, raw_url=None):
    """load a notebook into the library db"""
    from src.praxxis.sqlite import connection

    conn = connection.create_connection(library_db)
    cur = conn.cursor()
    load_library = 'INSERT OR IGNORE INTO "Notebooks"(Path, Notebook, Library, RawUrl) VALUES(?, ?, ?, ?)'
    cur.execute(load_library, (path, notebook, library, raw_url))
    conn.commit()
    conn.close()


def sync_library(library_db, path, readme, library, remote=None):
    """load a library into the library db"""
    from src.praxxis.sqlite import connection

    conn = connection.create_connection(library_db)
    cur = conn.cursor()
    load_library = 'INSERT OR IGNORE INTO "LibraryMetadata"(Path, Readme, Library, Remote) VALUES(?, ?, ?, ?)'
    update_library = 'UPDATE "LibraryMetadata" SET Readme = ? WHERE Library = ?'
    cur.execute(load_library, (path, readme, library, remote))
    cur.execute(update_library, (readme, library))
    conn.commit()
    conn.close()
    

def list_libraries(library_db, query_start, query_end):
    """returns a list of loaded libraries"""
    from src.praxxis.sqlite import connection

    conn = connection.create_connection(library_db)
    cur = conn.cursor()
    list_libraries = 'SELECT Library FROM "LibraryMetadata" ORDER BY Library LIMIT ?, ?'
    cur.execute(list_libraries, (query_start, query_end))
    conn.commit()
    rows = cur.fetchall()
    conn.close()
    return rows


def check_library_exists(library_db, library):
    from src.praxxis.sqlite import connection
    from src.praxxis.util import error

    conn = connection.create_connection(library_db)
    cur = conn.cursor()
    get_library = 'SELECT * FROM "LibraryMetadata" WHERE Library = ? LIMIT 0, 1'
    cur.execute(get_library, (library,))
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
    clear_library = 'DELETE FROM "LibraryMetadata" WHERE Library = ?'
    clear_notebooks = 'DELETE FROM "Notebooks" WHERE Library = ?'
    clear_parameter = 'DELETE FROM NotebookDefaultParam Where Library = ?'
    cur.execute(clear_library, (library,))
    cur.execute(clear_notebooks, (library,))
    cur.execute(clear_parameter, (library,))
    conn.commit()
    conn.close()


def remove_notebook(library_db, notebook, library):
    from src.praxxis.sqlite import connection

    conn = connection.create_connection(library_db)
    cur = conn.cursor()
    clear_parameter = 'DELETE FROM NotebookDefaultParam Where Notebook = ? AND Library = ?'
    clear_notebook = 'DELETE FROM Notebooks WHERE Notebook = ? AND Library = ?'
    cur.execute(clear_parameter, (notebook, library))
    cur.execute(clear_notebook, (notebook, library))
    conn.commit()
    conn.close()
