import pytest 
import sys 
import os

from src.mtool.util import function_switcher

def test_scene_initializer(setup, init_root, default_scene_name, scene_root, history_db):
    from tests.src.mtool.util.sqlite import test_sqlite_scene
    from tests.src.mtool.scene import test_new_scene
    from tests.src.mtool.scene import test_scene


