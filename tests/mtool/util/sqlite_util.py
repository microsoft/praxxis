from src.mtool.util import sqlite_util

def test_create_connection(db_file):
    sqlite_util.create_connection(db_file)


def test_init_scene(db_file, name):
    sqlite_util.init_scene(db_file, name)


def test_init_library_db(db_file):
    sqlite_util.init_library_db(db_file)


def test_init_current_scene(db_file, scene_name):
    sqlite_util.init_current_scene(db_file, scene_name)


def test_check_scene_ended(db_file, scene_name):
    sqlite_util.check_scene_ended(db_file, scene_name)


def test_update_current_scene(db_file, scene_name):
    sqlite_util.update_current_scene(db_file, scene_name)


def test_get_current_scene(db_file):
    sqlite_util.get_current_scene(db_file)


def test_get_scene_id(db_file):
    sqlite_util.get_scene_id(db_file)


def test_delete_scene(db_file, name):
    sqlite_util.delete_scene(db_file, name)


def test_end_scene(db_file, name):
    sqlite_util.end_scene(db_file, name)


def test_check_ended(db_file, name, conn, cur):
    sqlite_util.check_ended(db_file, name, conn, cur)


def test_mark_ended_scene(db_file, name):
    sqlite_util.mark_ended_scene(db_file, name)


def test_mark_resumed_scene(db_file, name):
    sqlite_util.mark_resumed_scene(db_file, name)


def test_resume_scene(db_file, name):
    sqlite_util.resume_scene(db_file, name)


def test_get_active_scenes(db_file):
    sqlite_util.get_active_scenes(db_file)


def test_get_ended_scenes(db_file):
    sqlite_util.get_ended_scenes(db_file)


def test_add_to_scene_history(db_file, timestamp, name, library):
    sqlite_util.add_to_scene_history(db_file, timestamp, name, library)


def test_get_notebook_history(db_file):
    sqlite_util.get_notebook_history(db_file)


def test_init_user_info(db_file):
    sqlite_util.init_user_info(db_file)


def test_list_env(db_file, start, end):
    sqlite_util.list_env(db_file, start, end)


def test_set_env(db_file, name, value):
    sqlite_util.set_env(db_file, name, value)


def test_get_env_by_ord(db_file, ordinal):
    sqlite_util.get_env_by_ord


def test_delete_env(db_file, name):
    sqlite_util.delete_env(db_file, name)


def test_clear_loaded_libraries(db_file):
    sqlite_util.clear_loaded_libararies(db_file)


def test_load_library(db_file, root, readme, name):
    sqlite_util.load_library(db_file, root, readme, name)


def test_load_notebook(db_file, root, name, library):
    sqlite_util.load_notebook(db_file, root, name, library)


def test_list_libraries(db_file, start, end):
    sqlite_util.list_libraries(db_file, start, end)


def test_list_notebooks(db_file, start, end):
    sqlite_util.list_notebooks(db_file, start, end)


def test_get_notebook(db_file, name):
    sqlite_util.get_notebook(db_file, name)


def test_get_notebook_by_ord(db_file, ordinal):
    sqlite_util.get_notebook_by_ord(db_file, ordinal)


def test_write_list(db_file, notebook_list):
    sqlite_util.write_list(db_file, notebook_list)


def test_get_telemetry_info(db_file, key):
    sqlite_util.get_telemetry_info(db_file, key)

def test_dump_scene_list(db_file):
    sqlite_util.dump_scene_list(db_file)


def test_write_scene_list(db_file, scene_list):
    sqlite_util.write_scene_list(db_file, scene_list)


def test_get_scene_by_ord(db_file, ordinal):
    sqlite_util.get_scene_by_ord(db_file, ordinal)


def test_search_notebooks(db_file, search_term, start, end): 
    sqlite_util.search_notebooks(db_file, search_term, start, end)