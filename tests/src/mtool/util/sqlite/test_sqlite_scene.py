"""
Tests the sqlite scene db
"""
from tests.src import global_vars

def test_init_history_db(db_file = global_vars.HISTORY_DB):
    """
    tests the initializing of the history db for columns and tables
    """
    from src.mtool.util.sqlite import connection

    conn = connection.create_connection(db_file)
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
    notebook_columns = [description[0] for description in cur.description]
    conn.close()

    assert set(library_metadata_columns) == set(['ID', 'Name', 'Ended'])
    assert set(notebook_columns) == set(['ID', 'Name'])


def test_init_scene_db(db_file = global_vars.HISTORY_DB, name = global_vars.DEFAULT_SCENE_NAME):
    """
    tests the initalizing of the scene db
    """
    from src.mtool.util.sqlite import connection

    conn = connection.create_connection(db_file)
    cur = conn.cursor()
    check_scene_metadata_table = f"SELECT count(*) FROM sqlite_master WHERE type='table' AND name='SceneMetaData';"
    check_notebook_list_table = f"SELECT count(*) FROM sqlite_master WHERE type='table' AND name='NotebookList';"
    check_environment_table = f"SELECT count(*) FROM sqlite_master WHERE type='table' AND name='Environment';"
    check_history_table = f"SELECT count(*) FROM sqlite_master WHERE type='table' AND name='History';"

    cur.execute(check_scene_metadata_table)
    scene_metadata = bool(cur.fetchone()[0])

    cur.execute(check_notebook_list_table)
    notebook_list = bool(cur.fetchone()[0])

    cur.execute(check_environment_table)
    environment = bool(cur.fetchone()[0])

    cur.execute(check_history_table)
    history = bool(cur.fetchone()[0])

    assert scene_metadata 
    assert notebook_list
    assert environment
    assert history

    check_scene_metadata_columns = f"SELECT * FROM 'SceneHistory';"
    check_notebook_list_columns = f"SELECT * FROM 'SceneList';"
    check_environment_columns = f"SELECT * FROM 'Environment';"
    check_history_columns = f"SELECT * FROM 'History';"

    cur.execute(check_scene_metadata_columns)
    scene_metadata_columns = [description[0] for description in cur.description]

    cur.execute(check_notebook_list_columns)
    notebook_list_columns = [description[0] for description in cur.description]

    cur.execute(check_environment_columns)
    environment_columns = [description[0] for description in cur.description]

    cur.execute(check_history_columns)
    history_columns = [description[0] for description in cur.description]
    conn.close()

    assert set(scene_metadata_columns) == set(['ID', 'Ended', 'Name'])
    assert set(notebook_list_columns) == set(['ID', 'Data', 'Path'])
    assert set(environment_columns) == set(['Name', 'Value'])
    assert set(history_columns) == set(['Timestamp', 'Notebook', 'Library'])
