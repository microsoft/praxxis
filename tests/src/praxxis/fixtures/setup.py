"""
This file sets up the parameter for the rest of the tests
"""
import pytest
import os

@pytest.fixture(scope="session")
def setup(init_root, library_root, telemetry_db, library_db, outfile_root, scene_root, history_db, default_scene_name, start, stop, rulesengine_root, rulesengine_db):
    """
    sets up directories in the temp dir
    """
    from src.praxxis.sqlite import sqlite_init
    from src.praxxis.sqlite import sqlite_scene
    from src.praxxis.sqlite import sqlite_library
    from src.praxxis.sqlite import sqlite_rulesengine
    from src.praxxis.util import roots
    from src.praxxis.scene import new_scene
    from src.praxxis.scene import list_scene
    from src.praxxis.parameter import list_param
    from src.praxxis.library import list_library
    from src.praxxis.notebook import list_notebook
    from src.praxxis.sqlite import sqlite_telemetry


    if not os.path.exists(init_root):
        os.mkdir(init_root)
        assert os.path.exists(init_root)

    if not os.path.exists(library_root):
        os.mkdir(library_root)
        assert os.path.exists(library_root)

    if not os.path.exists(library_db):
        sqlite_init.init_library_db(library_db)
        assert os.path.exists(library_db)
    
    if not os.path.exists(outfile_root):
        os.mkdir(outfile_root)
        assert os.path.exists(outfile_root)

    if not os.path.exists(scene_root):
        os.mkdir(scene_root)
        assert os.path.exists(scene_root)
    
    if not os.path.exists(history_db):
        sqlite_init.init_history(history_db, default_scene_name)
        assert os.path.exists(history_db)

    if not os.path.exists(telemetry_db):
        sqlite_init.init_user_info(telemetry_db, 0)

    
    if not os.path.exists(rulesengine_root):
        os.mkdir(rulesengine_root)
        assert os.path.exists(rulesengine_root)
    
    
    if not os.path.exists(rulesengine_db):
        sqlite_init.init_rulesengine_db(rulesengine_db)
    

    new_scene.new_scene(default_scene_name, scene_root, history_db)
    yield 
    current_scene_db = roots.get_current_scene_db(scene_root, history_db)
    assert len(list_scene.list_scene(init_root, history_db)) == 1
    assert len(list_param.list_param(current_scene_db, start, stop)) == 0
    assert len(list_library.list_library(library_db, start, stop)) == 0
    assert len(list_notebook.list_notebook(library_db, current_scene_db, start, stop)) == 0
    