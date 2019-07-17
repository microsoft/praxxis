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
    from src.mtool.scene import history
    from src.mtool.notebook import add_notebook
    from src.mtool.notebook import remove_notebook
    from src.mtool.scene import new_scene
    from src.mtool.scene import end_scene
    from src.mtool.scene import change_scene
    from src.mtool.scene import resume_scene
    from src.mtool.scene import delete_scene
    from src.mtool.scene import list_scene
    from src.mtool.library import add_library 
    from src.mtool.library import remove_library 
    from src.mtool.library import list_library 
    from src.mtool.environment import delete_env
    from src.mtool.environment import set_env
    from src.mtool.environment import list_env
    from src.mtool.environment import pull_env
    from src.mtool.library import sync_library
    from src.mtool.telemetry import update_settings 


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

    dummy_input = dummy_object.make_dummy_input("list_notebooks")
    result = cli.command(dummy_input, init_root, library_root, library_db, outfile_root, scene_root, history_db, telemetry_db, default_scene_name, True)
    assert result.__class__ == list_notebook.list_notebook.__class__

    dummy_input = dummy_object.make_dummy_input("history")
    result = cli.command(dummy_input, init_root, library_root, library_db, outfile_root, scene_root, history_db, telemetry_db, default_scene_name, True)
    assert result.__class__ == history.history.__class__

    dummy_input = dummy_object.make_dummy_input("add_notebook")
    result = cli.command(dummy_input, init_root, library_root, library_db, outfile_root, scene_root, history_db, telemetry_db, default_scene_name, True)
    assert result.__class__ == add_notebook.add_notebook.__class__

    dummy_input = dummy_object.make_dummy_input("remove_notebook")
    result = cli.command(dummy_input, init_root, library_root, library_db, outfile_root, scene_root, history_db, telemetry_db, default_scene_name, True)
    assert result.__class__ == remove_notebook.remove_notebook.__class__

    dummy_input = dummy_object.make_dummy_input("new_scene")
    result = cli.command(dummy_input, init_root, library_root, library_db, outfile_root, scene_root, history_db, telemetry_db, default_scene_name, True)
    assert result.__class__ == new_scene.new_scene.__class__

    dummy_input = dummy_object.make_dummy_input("end_scene")
    result = cli.command(dummy_input, init_root, library_root, library_db, outfile_root, scene_root, history_db, telemetry_db, default_scene_name, True)
    assert result.__class__ == end_scene.end_scene.__class__

    dummy_input = dummy_object.make_dummy_input("change_scene")
    result = cli.command(dummy_input, init_root, library_root, library_db, outfile_root, scene_root, history_db, telemetry_db, default_scene_name, True)
    assert result.__class__ == change_scene.change_scene.__class__

    dummy_input = dummy_object.make_dummy_input("resume_scene")
    result = cli.command(dummy_input, init_root, library_root, library_db, outfile_root, scene_root, history_db, telemetry_db, default_scene_name, True)
    assert result.__class__ == resume_scene.resume_scene.__class__

    dummy_input = dummy_object.make_dummy_input("delete_scene")
    result = cli.command(dummy_input, init_root, library_root, library_db, outfile_root, scene_root, history_db, telemetry_db, default_scene_name, True)
    assert result.__class__ == delete_scene.delete_scene.__class__

    dummy_input = dummy_object.make_dummy_input("list_scene")
    result = cli.command(dummy_input, init_root, library_root, library_db, outfile_root, scene_root, history_db, telemetry_db, default_scene_name, True)
    assert result.__class__ == list_scene.list_scene.__class__

    dummy_input = dummy_object.make_dummy_input("add_library")
    result = cli.command(dummy_input, init_root, library_root, library_db, outfile_root, scene_root, history_db, telemetry_db, default_scene_name, True)
    assert result.__class__ == add_library.add_library.__class__

    dummy_input = dummy_object.make_dummy_input("remove_library")
    result = cli.command(dummy_input, init_root, library_root, library_db, outfile_root, scene_root, history_db, telemetry_db, default_scene_name, True)
    assert result.__class__ == remove_library.remove_library.__class__

    dummy_input = dummy_object.make_dummy_input("list_library")
    result = cli.command(dummy_input, init_root, library_root, library_db, outfile_root, scene_root, history_db, telemetry_db, default_scene_name, True)
    assert result.__class__ == list_library.list_library.__class__

    dummy_input = dummy_object.make_dummy_input("set_env")
    result = cli.command(dummy_input, init_root, library_root, library_db, outfile_root, scene_root, history_db, telemetry_db, default_scene_name, True)
    assert result.__class__ == set_env.set_env.__class__

    dummy_input = dummy_object.make_dummy_input("delete_env")
    result = cli.command(dummy_input, init_root, library_root, library_db, outfile_root, scene_root, history_db, telemetry_db, default_scene_name, True)
    assert result.__class__ == delete_env.delete_env.__class__

    dummy_input = dummy_object.make_dummy_input("list_env")
    result = cli.command(dummy_input, init_root, library_root, library_db, outfile_root, scene_root, history_db, telemetry_db, default_scene_name, True)
    assert result.__class__ == list_env.list_env.__class__

    dummy_input = dummy_object.make_dummy_input("view_library_env")
    result = cli.command(dummy_input, init_root, library_root, library_db, outfile_root, scene_root, history_db, telemetry_db, default_scene_name, True)
    assert result.__class__ == list_env.list_library_env.__class__

    dummy_input = dummy_object.make_dummy_input("pull_notebook_env")
    result = cli.command(dummy_input, init_root, library_root, library_db, outfile_root, scene_root, history_db, telemetry_db, default_scene_name, True)
    assert result.__class__ == pull_env.pull_notebook_environment.__class__

    dummy_input = dummy_object.make_dummy_input("pull_library_env")
    result = cli.command(dummy_input, init_root, library_root, library_db, outfile_root, scene_root, history_db, telemetry_db, default_scene_name, True)
    assert result.__class__ == pull_env.pull_library_environment.__class__

    dummy_input = dummy_object.make_dummy_input("sync_library")
    result = cli.command(dummy_input, init_root, library_root, library_db, outfile_root, scene_root, history_db, telemetry_db, default_scene_name, True)
    assert result.__class__ == sync_library.sync_library.__class__

    dummy_input = dummy_object.make_dummy_input("update_settings")
    result = cli.command(dummy_input, init_root, library_root, library_db, outfile_root, scene_root, history_db, telemetry_db, default_scene_name, True)
    assert result.__class__ == update_settings.update_settings.__class__
 
