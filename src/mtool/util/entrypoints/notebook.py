def init_outfile(outfile_root):
    import os
    from src.mtool.display import display_notebook

    os.mkdir(outfile_root)
    display_notebook.display_init_run_notebook(outfile_root)
    

def run_notebook(arg, 
                 user_info_db, 
                 outfile_root, 
                 library_root, 
                 library_db, 
                 scene_root,
                 history_db,
                 current_scene_db = None):
    """calls the function to run a notebook"""
    from src.mtool.notebook import run_notebook
    from src.mtool.util import function_switcher
    
    if current_scene_db == None:
        current_scene_db = function_switcher.get_current_scene_db(scene_root, history_db)

    try:
        run_notebook.run_notebook(arg, user_info_db, outfile_root, current_scene_db, library_root, library_db)
    except Exception as e:
        raise e
    return 0


def open_notebook(arg, 
                  scene_root,
                  history_db,
                  library_db,
                  azure_data_studio_location,
                  current_scene_db = None):
    """calls the function to open a notebook"""
    from src.mtool.notebook import open_notebook
    from src.mtool.util import function_switcher
    
    if current_scene_db == None:
        current_scene_db = function_switcher.get_current_scene_db(scene_root, history_db)

    try:
        open_notebook.open_notebook(arg, current_scene_db, library_db, azure_data_studio_location)
    except Exception as e:
        raise e
    return 0
 

def search_notebook(arg,
                    scene_root,
                    history_db,
                    library_db ,
                    query_start,
                    query_end,
                    current_scene_db = None
                    ):
    """calls the function to search a notebook"""
    from src.mtool.notebook import search_notebook

    notebooks = search_notebook.search_notebook(arg, library_db, current_scene_db, query_start, query_end)
    return notebooks


def list_notebook(arg,
                  scene_root,
                  history_db,
                  library_root,
                  library_db,
                  query_start,
                  query_end, 
                  current_scene_db = None):
    """calls the function to list notebooks"""
    from src.mtool.notebook import list_notebook
    from src.mtool.util import function_switcher
    
    if current_scene_db == None:
        current_scene_db = function_switcher.get_current_scene_db(scene_root, history_db)

    notebook_list = list_notebook.list_notebook(scene_root, library_root, library_db, current_scene_db, query_start, query_end)
    return notebook_list


def next_notebook(arg):
    """calls the function to get the next notebook"""
    ##TODO  implement this
    return "coming soon"