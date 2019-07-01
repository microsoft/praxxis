import pytest 
import sys 
import os

from src.mtool.util import function_switcher
from tests.src import global_vars

def test_initializer(init_root, library_root, library_db, outfile_root, scene_root, history_db, default_scene_name):
    from src.mtool.util.sqlite import sqlite_library
    from src.mtool.util.sqlite import sqlite_scene
    from tests.src.mtool.util.sqlite import test_sqlite_scene
    from tests.src.mtool.util.sqlite import test_sqlite_library

    if not os.path.exists(init_root):
        os.mkdir(init_root)
        assert os.path.exists(init_root)

    if not os.path.exists(library_root):
        os.mkdir(library_root)
        assert os.path.exists(library_root)

    if not os.path.exists(library_db):
        sqlite_library.init_library_db(library_db)
        test_sqlite_library.test_init_library_db(library_db)
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


def test_scene_initializer(init_root, default_scene_name, scene_root, history_db):
    from tests.src import global_vars
    from tests.src.mtool.util.sqlite import test_sqlite_scene
    from tests.src.mtool.scene import test_new_scene
    from tests.src.mtool.scene import test_scene

    scene_db = test_new_scene.test_new_scene(init_root, default_scene_name, scene_root, history_db)
    test_scene.test_init_scene(init_root, history_db, default_scene_name, scene_db)

    test_sqlite_scene.test_init_scene_db(history_db)

