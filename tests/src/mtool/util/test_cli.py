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
         current_scene_db,
         start,
         stop):
    import os
    from src.mtool.util.sqlite import sqlite_scene
    from src.mtool.notebook import list_notebook
    from src.mtool.notebook import run_notebook
    from src.mtool.environment import list_env
    from src.mtool.notebook import open_notebook
    from src.mtool.notebook import search_notebook

    list_notebook.list_notebook(library_db, current_scene_db, start, stop)

    dummy_input = dummy_object.make_dummy_input("run_notebook")

    result = cli.command(dummy_input, init_root, library_root, library_db, outfile_root, scene_root, history_db, telemetry_db, default_scene_name, True)
    sqlite_scene.clear_history(current_scene_db)
    assert result.__class__ == run_notebook.run_notebook.__class__

    dummy_input = dummy_object.make_dummy_input("view_notebook_env")
    result = cli.command(dummy_input, init_root, library_root, library_db, outfile_root, scene_root, history_db, telemetry_db, default_scene_name, True)
    assert result.__class__ == list_env.list_notebook_env.__class__

    dummy_input = dummy_object.make_dummy_input("open_notebook")
    result = cli.command(dummy_input, init_root, library_root, library_db, outfile_root, scene_root, history_db, telemetry_db, default_scene_name, True)
    assert result.__class__ == open_notebook.open_notebook.__class__

    dummy_input = dummy_object.make_dummy_input("search_notebooks")
    result = cli.command(dummy_input, init_root, library_root, library_db, outfile_root, scene_root, history_db, telemetry_db, default_scene_name, True)
    assert result.__class__ == search_notebook.search_notebook.__class__

    