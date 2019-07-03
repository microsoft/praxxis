"""
This file sets up the environment for the rest of the tests
"""
import pytest
import os

@pytest.fixture(scope="session")
def setup(init_root, library_root, library_db, outfile_root, scene_root, history_db, default_scene_name, start, stop):
    """
    sets up directories in the temp dir
    """
    from src.mtool.util.sqlite import sqlite_library
    from src.mtool.util.sqlite import sqlite_scene
    from src.mtool.scene import new_scene

    if not os.path.exists(init_root):
        os.mkdir(init_root)
        assert os.path.exists(init_root)

    if not os.path.exists(library_root):
        os.mkdir(library_root)
        assert os.path.exists(library_root)

    if not os.path.exists(library_db):
        sqlite_library.init_library_db(library_db)
        assert os.path.exists(library_db)
    
    if not os.path.exists(outfile_root):
        os.mkdir(outfile_root)
        assert os.path.exists(outfile_root)

    if not os.path.exists(scene_root):
        os.mkdir(scene_root)
        assert os.path.exists(scene_root)
    
    if not os.path.exists(history_db):
        sqlite_scene.init_current_scene(history_db, default_scene_name)
        assert os.path.exists(history_db)

    new_scene.new_scene(default_scene_name, scene_root, history_db)
    yield 
    from src.mtool.scene import list_scene
    from src.mtool.environment import list_env
    from src.mtool.util import function_switcher
    from src.mtool.library import list_library
    
    current_scene_db = function_switcher.get_current_scene_db(scene_root, history_db)

    assert len(list_scene.list_scene(init_root, history_db)) == 1
    assert len(list_env.list_env(current_scene_db, start, stop)) == 0
    assert len(list_library.list_library(library_root, library_db)) == 0
