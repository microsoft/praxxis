
"""
Tests the sqlite library db
"""
from tests.src import global_vars

def test_init_library_db(db_file = global_vars.LIBRARY_DB):
    """
    tests the initializing of the library db for columns and tables
    """
    from src.mtool.util.sqlite import connection

    conn = connection.create_connection(db_file)
    cur = conn.cursor()
    check_library_metadata_table = f"SELECT count(*) FROM sqlite_master WHERE type='table' AND name='LibraryMetadata';"
    check_notebooks_table = f"SELECT count(*) FROM sqlite_master WHERE type='table' AND name='Notebooks';"
    check_environment_table = f"SELECT count(*) FROM sqlite_master WHERE type='table' AND name='Environment';"

    cur.execute(check_library_metadata_table)
    library_metadata = bool(cur.fetchone()[0])

    cur.execute(check_notebooks_table)
    notebooks = bool(cur.fetchone()[0])

    cur.execute(check_environment_table)
    environment = bool(cur.fetchone()[0])

    assert library_metadata
    assert notebooks
    assert environment

    check_library_metadata_columns = f"SELECT * FROM'LibraryMetadata';"
    check_notebooks_columns = f"SELECT * FROM 'Notebooks';"
    check_environment_columns = f"SELECT * FROM 'Environment';"

    cur.execute(check_library_metadata_columns)
    library_metadata_columns = [description[0] for description in cur.description]

    cur.execute(check_notebooks_columns)
    notebook_columns = [description[0] for description in cur.description]

    cur.execute(check_environment_columns)
    environment_columns = [description[0] for description in cur.description]

    assert library_metadata_columns == ['Root', 'Readme', 'Name']
    assert notebook_columns == ['Root', 'Name', 'LibraryName']
    assert environment_columns == ['Name', 'Value', 'NotebookName']