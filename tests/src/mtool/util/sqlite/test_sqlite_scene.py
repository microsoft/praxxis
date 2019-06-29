"""
Tests the sqlite scene db
"""
from tests.src import global_vars

# def test_init_scene(db_file):
#     from src.mtool.util.sqlite import connection

#     conn = connection.create_connection(db_file)
#     cur = conn.cursor()
#     check_scene_metadata_table = f"SELECT count(*) FROM sqlite_master WHERE type='table' AND name='SceneMetadata';"
#     check_notebook_list_table = f"SELECT count(*) FROM sqlite_master WHERE type='table' AND name='NotebookList';"
#     check_environment_table = f"SELECT count(*) FROM sqlite_master WHERE type='table' AND name='Environment';"
#     check_history_table = f"SELECT count(*) FROM sqlite_master WHERE type='table' AND name='History';"

#     cur.execute(check_scene_metadata_table)
#     scene_metadata = bool(cur.fetchone()[0])


#     cur.execute(check_notebook_list_table)
#     notebook_list = bool(cur.fetchone()[0])

#     cur.execute(check_environment_table)
#     environment = bool(cur.fetchone()[0])

#     cur.execute(check_history_table)
#     history = bool(cur.fetchone()[0])
    
#     assert scene_metadata
#     assert notebook_list
#     assert environment
#     assert history


def test_init_history_db(db_file = global_vars.HISTORY_DB):
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


def test_init_library_db(db_file = global_vars.LIBRARY_DB):
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
