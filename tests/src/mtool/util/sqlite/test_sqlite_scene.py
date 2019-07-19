"""
Tests the sqlite scene db
"""

def test_init_history_db(setup, history_db):
    """
    tests the initializing of the history db for columns and tables
    """

    from src.mtool.util.sqlite import connection

    conn = connection.create_connection(history_db)
    cur = conn.cursor()
    check_scene_history_table = f"SELECT count(*) FROM sqlite_master WHERE type='table' AND name='SceneHistory';"
    check_scene_list_table = f"SELECT count(*) FROM sqlite_master WHERE type='table' AND name='SceneList';"

    cur.execute(check_scene_history_table)
    history = bool(cur.fetchone()[0])

    cur.execute(check_scene_list_table)
    scene_list = bool(cur.fetchone()[0])

    assert history
    assert scene_list

    check_scene_history_columns = f"SELECT * FROM 'SceneHistory';"
    check_scene_list_columns = f"SELECT * FROM 'SceneList';"

    cur.execute(check_scene_history_columns)
    library_metadata_columns = [description[0] for description in cur.description]

    cur.execute(check_scene_list_columns)
    scene_list_columns = [description[0] for description in cur.description]
    conn.close()

    assert set(library_metadata_columns) == set(['ID', 'Scene', 'Ended'])
    assert set(scene_list_columns) == set(['ID', 'Scene'])


def init_scene_db(setup, scene_db=""):
    """
    tests the initalizing of the scene db
    """
    from src.mtool.util.sqlite import connection

    conn = connection.create_connection(scene_db)
    cur = conn.cursor()
    check_scene_metadata_table = f"SELECT count(*) FROM sqlite_master WHERE type='table' AND name='SceneMetadata';"
    check_notebook_list_table = f"SELECT count(*) FROM sqlite_master WHERE type='table' AND name='NotebookList';"
    check_parameter_table = f"SELECT count(*) FROM sqlite_master WHERE type='table' AND name='parameter';"
    check_history_table = f"SELECT count(*) FROM sqlite_master WHERE type='table' AND name='History';"

    cur.execute(check_scene_metadata_table)
    scene_metadata = bool(cur.fetchone()[0])

    cur.execute(check_notebook_list_table)
    notebook_list = bool(cur.fetchone()[0])

    cur.execute(check_parameter_table)
    parameter = bool(cur.fetchone()[0])

    cur.execute(check_history_table)
    history = bool(cur.fetchone()[0])

    assert scene_metadata 
    assert notebook_list
    assert parameter
    assert history

    check_scene_metadata_columns = f"SELECT * FROM 'SceneMetadata';"
    check_notebook_list_columns = f"SELECT * FROM 'NotebookList';"
    check_parameter_columns = f"SELECT * FROM 'parameter';"
    check_history_columns = f"SELECT * FROM 'History';"

    cur.execute(check_scene_metadata_columns)
    scene_metadata_columns = [description[0] for description in cur.description]

    cur.execute(check_notebook_list_columns)
    notebook_list_columns = [description[0] for description in cur.description]

    cur.execute(check_parameter_columns)
    parameter_columns = [description[0] for description in cur.description]

    cur.execute(check_history_columns)
    history_columns = [description[0] for description in cur.description]
    conn.close()

    assert set(scene_metadata_columns) == set(['ID', 'Ended', 'Scene']) 
    assert set(notebook_list_columns) == set(['ID', 'Data', 'Path'])
    assert set(parameter_columns) == set(['Scene', 'Value'])
    assert set(history_columns) == set(['Timestamp', 'Notebook', 'Library', 'OutputPath'])
