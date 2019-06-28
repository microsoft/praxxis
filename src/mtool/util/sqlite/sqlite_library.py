"""
This file contains all of the sqlite functions for libraries
"""

def init_library_db(db_file):
    """initializes the library database"""
    from src.mtool.util.sqlite import connection

    conn = connection.create_connection(db_file)
    cur = conn.cursor()
    create_metadata_table = f'CREATE TABLE "LibraryMetadata" (Root TEXT PRIMARY KEY, Readme TEXT, Name TEXT)'
    create_notebook_table = f'CREATE TABLE "Notebooks" (Root TEXT PRIMARY KEY, Name TEXT, LibraryName TEXT, FOREIGN KEY(LibraryName) REFERENCES "LibraryMetadata"(Name))'
    create_environment_table = f'CREATE TABLE "Environment" (Name TEXT PRIMARY KEY, Value TEXT, NotebookName TEXT, FOREIGN KEY(NotebookName) REFERENCES "Notebooks"(Name))'
    cur.execute(create_metadata_table)
    cur.execute(create_notebook_table)
    cur.execute(create_environment_table)
    conn.commit()
    conn.close()

def clear_loaded_libararies(db_file):
    from src.mtool.util.sqlite import connection

    conn = connection.create_connection(db_file)
    cur = conn.cursor()
    clear_metadata = f'DELETE FROM "LibraryMetadata"'
    clear_notebooks = f'DELETE FROM "Notebooks"'
    cur.execute(clear_metadata)
    cur.execute(clear_notebooks)
    conn.commit()
    conn.close()


def load_library(db_file, root, readme, name):
    """load a library into the library db"""
    from src.mtool.util.sqlite import connection

    conn = connection.create_connection(db_file)
    cur = conn.cursor()
    load_library = f'INSERT OR IGNORE INTO "LibraryMetadata"(Root, Readme, Name) VALUES("{root}", "{readme}", "{name}")'
    update_library = f'UPDATE "LibraryMetadata" SET Readme = "{readme}" WHERE Name = "{name}"'
    cur.execute(load_library)
    cur.execute(update_library)
    conn.commit()
    conn.close()


def load_notebook(db_file, file_root, name, library):
    """load a notebook into the library db"""
    from src.mtool.util.sqlite import connection

    conn = connection.create_connection(db_file)
    cur = conn.cursor()
    load_library = f'INSERT OR IGNORE INTO "Notebooks"(Root, Name, LibraryName) VALUES("{file_root}", "{name}", "{library}")'
    cur.execute(load_library)
    conn.commit()
    conn.close()
    

def list_libraries(db_file, start, end):
    """returns a list of loaded libraries"""
    from src.mtool.util.sqlite import connection

    conn = connection.create_connection(db_file)
    cur = conn.cursor()
    list_libraries = f'SELECT Name FROM "LibraryMetadata" LIMIT {start}, {end}'
    cur.execute(list_libraries)
    conn.commit()
    rows = cur.fetchall()
    conn.close()
    return rows

