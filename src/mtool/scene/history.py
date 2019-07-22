"""
This file displays the history in the current scene.

TODO: should give warning/error when notebook can't be found in current libraries?
"""

def history(history_db, library_db, current_scene_db):
    """displays the notebook history of the sceen"""
    from src.mtool.sqlite import sqlite_scene
    from src.mtool.sqlite import sqlite_notebook
    from src.mtool.display import display_scene
    from src.mtool.util import error

    curr_scene = sqlite_scene.get_current_scene(history_db)
    
    notebook_history = sqlite_scene.get_notebook_history(current_scene_db)
    display_scene.display_history(curr_scene, notebook_history)

    # get paths and format for writing into notebooklist
    notebooks = []
    for notebook_info in notebook_history:
        # pass the library_db, notebook name, notebook library
        notebook_data = sqlite_notebook.get_notebook(library_db, notebook_info[1])[0]


        notebooks.insert(0, (notebook_data))
    sqlite_notebook.write_list(current_scene_db, notebooks)
    return notebooks
        