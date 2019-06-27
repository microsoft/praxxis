"""
This file lists all of the environment variables
"""

def list_env(args, scene_root, history_db, start, end):
    """lists the environment variables by getting them out of the scene"""
    import os
    
    from src.mtool.util import sqlite_util
    from src.mtool.cli import display
    
    scene = sqlite_util.get_current_scene(history_db)

    directory = os.path.join(scene_root, scene)
    db_file = os.path.join(directory, f"{scene}.db")

    display.display_list_env(sqlite_util.list_env(db_file, start, end))


def list_notebook_env(args, library_db, current_scene_db):
    """lists environments set to defaults in the notebook and set in the scene"""
    from src.mtool.util import sqlite_util
    from src.mtool.cli import display
    from src.mtool.notebook import notebook

    name = args.notebook
    tmp_name = notebook.get_notebook_by_ordinal(current_scene_db, name)
    if tmp_name != None:
        name = tmp_name

    sqlite_util.get_all_env(current_scene_db)
    
    display.display_view_env(sqlite_util.list_notebook_env(library_db, name), 
                                      sqlite_util.get_all_env(current_scene_db))


def list_library_env(args, library_db, current_scene_db):
    from src.mtool.util import sqlite_util
    from src.mtool.cli import display
    name = args.name 
    display.display_view_env(sqlite_util.get_library_environments(library_db, name),
                             sqlite_util.get_all_env(current_scene_db))
    
