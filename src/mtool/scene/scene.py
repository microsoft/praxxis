import os 

def init_scene(root, history_db):
    from src.mtool.util import sqlite_util
    from src.mtool.scene import new_scene
    from src.mtool.cli import display

    default_scene_name = 'scene'
    if not os.path.exists(root):
        os.mkdir(root)
        display.display_init_scene_folder(root)

    if not os.path.exists(history_db):
        sqlite_util.init_current_scene(history_db, default_scene_name)
        new_scene.new_scene(default_scene_name, root, history_db)
        display.display_init_scene_db(history_db)
        display.display_new_scene(default_scene_name)