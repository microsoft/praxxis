from src.mtool.util import function_switcher
from tests.src.mtool.util import dummy_object

def test_get_current_scene_db(setup, scene_root, history_db):
    import os

    current_scene_db = function_switcher.get_current_scene_db(scene_root, history_db)
    assert os.path.basename(current_scene_db) == "scene.db"


def test_run_notebook(setup, telemetry_db, outfile_root, library_root, library_db, scene_root, history_db, current_scene_db):
    notebook = dummy_object.make_dummy_notebook()

    assert function_switcher.run_notebook(notebook, telemetry_db, outfile_root, library_root, library_db, scene_root, history_db, current_scene_db) == 0


def test_view_notebook_env(setup, add_test_library, library_db):
    import os

    notebook = dummy_object.make_dummy_notebook_params()
    envs = function_switcher.view_notebook_env(notebook, library_db)
    
    assert len(envs) == 2


def test_open_notebook(setup, add_test_library, scene_root, history_db, library_db, ads_location, current_scene_db):
    notebook = dummy_object.make_dummy_notebook()

    assert function_switcher.open_notebook(notebook, scene_root, history_db, library_db, ads_location, current_scene_db) == 0


def test_search_notebook(setup, add_test_library, scene_root, history_db, library_db, start, stop, current_scene_db):
    search = dummy_object.make_dummy_search()

    notebooks = function_switcher.search_notebook(search, scene_root, history_db, library_db, start, stop, current_scene_db)
    assert len(notebooks) == 2


def test_list_notebook(setup, add_test_library, scene_root, history_db, library_root, library_db, start, stop, current_scene_db):
    notebook = dummy_object.make_dummy_notebook()

    notebook_list = function_switcher.list_notebook(notebook, scene_root, history_db, library_root, library_db, start, stop, current_scene_db)
    assert len(notebook_list) == 3


def test_next_notebook():    
    notebook = dummy_object.make_dummy_notebook()
    assert function_switcher.next_notebook(notebook) == "coming soon"


def test_history(setup, setup_telemetry, generate_short_history, scene_root, history_db, library_db, current_scene_db):
    assert len(function_switcher.history("", scene_root, history_db, library_db, current_scene_db)) == 1


def test_new_scene(setup, scene_root, history_db):
    from src.mtool.scene import delete_scene

    scene = dummy_object.make_dummy_scene("generated_new_scene")

    new_scene = function_switcher.new_scene(scene, scene_root, history_db)
    assert new_scene[1] == "generated_new_scene"

    delete_scene.delete_scene("generated_new_scene", scene_root, history_db)


def test_end_scene(setup, create_one_scene, scene_root, history_db, current_scene_db):
    ended = function_switcher.end_scene("generated_one_scene", scene_root, history_db, current_scene_db)

    assert ended == "generated_one_scene"


def test_change_scene(setup, create_one_scene, scene_root, history_db):
    scene = dummy_object.make_dummy_scene("scene")

    change_scene = function_switcher.change_scene(scene, scene_root, history_db)
    assert change_scene == "scene"


def test_resume_scene(setup, create_ended_scene, scene_root, history_db):
    resume_scene = function_switcher.resume_scene("generated_ended_scene", scene_root, history_db)

    assert resume_scene == "generated_ended_scene"


def test_delete_scene(setup, create_one_scene, scene_root, history_db):
    delete_scene = function_switcher.delete_scene("generated_one_scene", scene_root, history_db)

    assert delete_scene == "generated_one_scene"


def test_set_env(setup, scene_root, history_db, current_scene_db):
    from src.mtool.environment import delete_env
    env = dummy_object.make_dummy_environment("test_set_env", "test")

    set_env = function_switcher.set_env(env, scene_root, history_db)
    assert set_env.name == "test_set_env"
    delete_env.delete_env(env, scene_root, history_db, current_scene_db)


def test_delete_env(setup, set_one_env, scene_root, history_db, current_scene_db):
    assert function_switcher.delete_env("generated_single_env", scene_root, history_db, current_scene_db) == "generated_single_env"


def test_list_env(setup, set_one_env, scene_root, history_db, start, stop, current_scene_db):
    envs = function_switcher.list_env("", scene_root, history_db, start, stop, current_scene_db)
    
    assert len(envs) == 1


def test_view_library_env(setup, add_test_library, scene_root, history_db, library_db, current_scene_db):
    envs = function_switcher.view_library_env("test_notebooks", scene_root, history_db, library_db, current_scene_db)
    assert len(envs) == 2


def test_add_library():
    assert function_switcher.add_library("") == "coming soon"


def test_list_library(setup, add_test_library, library_root, library_db):
    libraries = function_switcher.list_library("", library_root, library_db)
    assert len(libraries) == 1


def test_sync_library(setup, library_root, library_db):
    libraries = function_switcher.sync_library("", library_root, library_db)
    assert libraries == 0


def test_init(setup, init_root, library_root, library_db, outfile_root, scene_root, history_db, telemetry_db, default_scene_name):
    pass
    import shutil 
    import os 
    
    assert os.path.exists(init_root)
    shutil.rmtree(init_root)
    assert not os.path.exists(init_root)
    function_switcher.init(init_root, library_root, library_db, outfile_root, scene_root, history_db, telemetry_db, default_scene_name, False)
    
    assert os.path.exists(init_root)
    assert os.path.exists(library_root)
    assert os.path.exists(library_db)
    assert os.path.exists(outfile_root)
    assert os.path.exists(scene_root)
    assert os.path.exists(history_db)
    assert os.path.exists(telemetry_db)

    os.remove(telemetry_db)

def test_init_library(setup, library_root, library_db):
    import shutil 
    import os 
    
    assert os.path.exists(library_root)
    assert os.path.exists(library_db)
    shutil.rmtree(library_root)
    assert not os.path.exists(library_root)
    
    function_switcher.init_library(library_root, library_db)
    
    assert os.path.exists(library_root)
    assert os.path.exists(library_db)


def test_init_outfile(setup, outfile_root):
    import shutil 
    import os 

    assert os.path.exists(outfile_root)
    shutil.rmtree(outfile_root)
    assert not os.path.exists(outfile_root)

    function_switcher.init_outfile(outfile_root)

    assert os.path.exists(outfile_root)


def test_init_scene(setup, scene_root, history_db, default_scene_name):
    import shutil 
    import os 

    assert os.path.exists(scene_root)
    assert os.path.exists(history_db)
    shutil.rmtree(scene_root)
    os.remove(history_db)
    assert not os.path.exists(scene_root)
    
    function_switcher.init_scene(scene_root, history_db, default_scene_name)

    assert os.path.exists(scene_root)


def test_init_telemetry(setup, telemetry_db):
    import os 

    if os.path.exists(telemetry_db):
        os.remove(telemetry_db)
    assert not os.path.exists(telemetry_db)
    
    function_switcher.init_telemetry(telemetry_db, 0)

    assert os.path.exists(telemetry_db)
    os.remove(telemetry_db)


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
    result = function_switcher.command(input, init_root, library_root, library_db, outfile_root, scene_root, history_db, telemetry_db, default_scene_name)
    assert result == 0

    input = dummy_object.make_dummy_input("view_notebook_env")
    result = function_switcher.command(input, init_root, library_root, library_db, outfile_root, scene_root, history_db, telemetry_db, default_scene_name)
    assert result == []


    input = dummy_object.make_dummy_input("open_notebook")
    result = function_switcher.command(input, init_root, library_root, library_db, outfile_root, scene_root, history_db, telemetry_db, default_scene_name)
    print(result)
    assert result == []

    os.remove(telemetry_db)
    assert 0