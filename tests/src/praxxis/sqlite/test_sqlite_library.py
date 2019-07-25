"""
Tests the sqlite library db
"""

def test_init_library_db(setup, library_db):
    """
    tests the initializing of the library db for columns and tables
    """
    from src.praxxis.sqlite import connection

    conn = connection.create_connection(library_db)
    cur = conn.cursor()
    check_library_metadata_table = f"SELECT count(*) FROM sqlite_master WHERE type='table' AND name='LibraryMetadata';"
    check_notebooks_table = f"SELECT count(*) FROM sqlite_master WHERE type='table' AND name='Notebooks';"
    check_parameter_table = f"SELECT count(*) FROM sqlite_master WHERE type='table' AND name='Parameters';"
    check_notebook_parameter_table = f"SELECT count(*) FROM sqlite_master WHERE type='table' AND name='NotebookDefaultParam';"


    cur.execute(check_library_metadata_table)
    library_metadata = bool(cur.fetchone()[0])

    cur.execute(check_notebooks_table)
    notebooks = bool(cur.fetchone()[0])

    cur.execute(check_parameter_table)
    parameter = bool(cur.fetchone()[0])

    cur.execute(check_notebook_parameter_table)
    notebook_parameter = bool(cur.fetchone()[0])

    assert library_metadata
    assert notebooks
    assert parameter
    assert notebook_parameter

    check_library_metadata_columns = f"SELECT * FROM'LibraryMetadata';"
    check_notebooks_columns = f"SELECT * FROM 'Notebooks';"
    check_parameter_columns = f"SELECT * FROM 'Parameters';"
    check_notebook_parameter_columns = f"SELECT * FROM 'NotebookDefaultParam'"

    cur.execute(check_library_metadata_columns)
    library_metadata_columns = [description[0] for description in cur.description]

    cur.execute(check_notebooks_columns)
    notebook_columns = [description[0] for description in cur.description]

    cur.execute(check_parameter_columns)
    parameter_columns = [description[0] for description in cur.description]

    cur.execute(check_notebook_parameter_columns)
    notebook_parameter_columns = [description[0] for description in cur.description]

    assert library_metadata_columns == ['Path', 'Readme', 'Library', 'Remote']
    assert notebook_columns == ['Path', 'Notebook', 'Library', 'RawUrl']
    assert parameter_columns == ['Parameter', 'Value']
    assert notebook_parameter_columns == ['Parameter', 'Value', 'Notebook', 'Library']
    conn.close()