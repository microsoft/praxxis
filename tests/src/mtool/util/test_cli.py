from src.mtool.util import cli
from tests.src.mtool.util import dummy_object

def test_command(setup, init_root, 
         library_root, 
         library_db,
         outfile_root,
         scene_root,
         history_db,
         telemetry_db,
         default_scene_name):
    import os

    input = dummy_object.make_dummy_input("run_notebook")
    result = cli.command(input, init_root, library_root, library_db, outfile_root, scene_root, history_db, telemetry_db, default_scene_name)
    assert result == 0

    input = dummy_object.make_dummy_input("view_notebook_env")
    result = cli.command(input, init_root, library_root, library_db, outfile_root, scene_root, history_db, telemetry_db, default_scene_name)
    assert result == []


    input = dummy_object.make_dummy_input("open_notebook")
    result = cli.command(input, init_root, library_root, library_db, outfile_root, scene_root, history_db, telemetry_db, default_scene_name)
    assert result == []

    assert 0