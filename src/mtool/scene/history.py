"""
This file displays the history in the current scene.

TODO: should give warning/error when notebook can't be found in current libraries?
"""

def history(args, history_db, library_db, current_scene_db):
    """displays the notebook history of the sceen"""
    from src.mtool.util import sqlite_util
    from src.mtool.cli import display

    curr_scene = sqlite_util.get_current_scene(history_db)
    
    notebook_history = sqlite_util.get_notebook_history(current_scene_db)
    display.display_history(curr_scene, notebook_history)

    # get paths and format for writing into notebooklist
    notebooks = []
    for notebook_info in notebook_history:
        # pass the library_db, notebook name, notebook library
        path = sqlite_util.get_notebook_path(library_db, notebook_info[1], notebook_info[2])
        notebooks.insert(0, (notebook_info[1], path))
    sqlite_util.write_list(current_scene_db, notebooks)
        
