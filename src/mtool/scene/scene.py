"""This file contains scene utilities, like initializing scenes and getting by ord"""

def init_scene(scene_root, history_db):
    """ initializes the scene db and directory"""
    import os 

    default_scene_name = 'scene'
    if not os.path.exists(scene_root):
        """importing is done in the if statements to increase speed"""
        from src.mtool.cli import display
        os.mkdir(scene_root)
        display.display_init_scene_folder(scene_root)

    if not os.path.exists(history_db):
        from src.mtool.cli import display
        from src.mtool.scene import new_scene
        from src.mtool.util import sqlite_util
        sqlite_util.init_current_scene(history_db, default_scene_name)
        new_scene.new_scene(default_scene_name, scene_root, history_db)
        display.display_init_scene_db(history_db)


def get_scene_by_ordinal(args, name, history_db):
    """gets scene by ordinal using the sqlite history db"""
    from src.mtool.util import sqlite_util

    if f"{name}".isdigit():
        name = sqlite_util.get_scene_by_ord(history_db, int(name))
        if name == "":
            from src.mtool.cli import display
            display.scene_does_not_exist_error(args.name)
            return ""
        return(name)