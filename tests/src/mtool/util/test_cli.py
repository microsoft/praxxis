from src.mtool.util import cli
from tests.src.mtool.util import dummy_object

def test_command(setup, 
         add_test_library, 
         init_root, 
         library_root, 
         library_db,
         outfile_root,
         scene_root,
         history_db,
         telemetry_db,
         default_scene_name,
         current_scene_db):
    import os
    from src.mtool.util.sqlite import sqlite_scene

    dummy_input = dummy_object.make_dummy_input("run_notebook")

    result = cli.command(dummy_input, init_root, library_root, library_db, outfile_root, scene_root, history_db, telemetry_db, default_scene_name)
    sqlite_scene.clear_history(current_scene_db)
    assert result == 0

    dummy_input = dummy_object.make_dummy_input("view_notebook_env")
    result = cli.command(dummy_input, init_root, library_root, library_db, outfile_root, scene_root, history_db, telemetry_db, default_scene_name)
    assert result == []

    dummy_input = dummy_object.make_dummy_input("open_notebook")
    result = cli.command(dummy_input, init_root, library_root, library_db, outfile_root, scene_root, history_db, telemetry_db, default_scene_name)
    assert result == 0
