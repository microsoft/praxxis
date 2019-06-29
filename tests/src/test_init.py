import pytest 
import sys 
import os

from src.mtool.util import function_switcher

def test_initializer():
    from src.mtool.util.sqlite import sqlite_library
    from src.mtool.util.sqlite import sqlite_scene
    from tests.src.mtool.util.sqlite import test_sqlite_scene
    from tests.src import global_vars

    if not os.path.exists(global_vars.ROOT):
        os.mkdir(global_vars.ROOT)
        assert os.path.exists(global_vars.ROOT)

    if not os.path.exists(global_vars.LIBRARY_ROOT):
        os.mkdir(global_vars.LIBRARY_ROOT)
        assert os.path.exists(global_vars.LIBRARY_ROOT)

    if not os.path.exists(global_vars.LIBRARY_DB):
        sqlite_library.init_library_db(global_vars.LIBRARY_DB)
        test_sqlite_scene.test_init_library_db(global_vars.LIBRARY_DB)
        assert os.path.exists(global_vars.LIBRARY_DB)
    
    if not os.path.exists(global_vars.OUTFILE_ROOT):
        os.mkdir(global_vars.OUTFILE_ROOT)
        assert os.path.exists(global_vars.OUTFILE_ROOT)

    if not os.path.exists(global_vars.SCENE_ROOT):
        os.mkdir(global_vars.SCENE_ROOT)
        assert os.path.exists(global_vars.SCENE_ROOT)
    
    if not os.path.exists(global_vars.HISTORY_DB):
        sqlite_scene.init_current_scene(global_vars.HISTORY_DB, global_vars.DEFAULT_SCENE_NAME)
        assert os.path.exists(global_vars.HISTORY_DB)
