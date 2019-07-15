from src.mtool.util.roots import _outfile_root
from src.mtool.util.roots import _user_info_db
from src.mtool.util.roots import _library_root
from src.mtool.util.roots import _library_db
from src.mtool.util.roots import _scene_root
from src.mtool.util.roots import _history_db
from src.mtool.util.roots import _azure_data_studio_location
from src.mtool.util.roots import _query_start
from src.mtool.util.roots import _query_end

def init_outfile(outfile_root):
    import os
    from src.mtool.display import display_notebook

    os.mkdir(outfile_root)
    display_notebook.display_init_run_notebook(outfile_root)
    

def run_notebook(arg, 
                 user_info_db = _user_info_db, 
                 outfile_root = _outfile_root, 
                 library_root = _library_root, 
                 library_db = _library_db, 
                 scene_root = _scene_root,
                 history_db = _history_db,
                 current_scene_db = None):
    """calls the function to run a notebook"""
    from src.mtool.notebook import run_notebook
    from src.mtool.util import roots
    
    if current_scene_db == None:
        current_scene_db = roots.get_current_scene_db(scene_root, history_db)
    
    try:
        run_notebook.run_notebook(arg, user_info_db, outfile_root, current_scene_db, library_root, library_db)
    except Exception as e:
        raise e
    return 0


def open_notebook(arg, 
                  scene_root = _scene_root,
                  history_db = _history_db, 
                  library_db = _library_db,
                  azure_data_studio_location = _azure_data_studio_location,
                  current_scene_db = None,
                  test = False):
    """calls the function to open a notebook"""
    from src.mtool.notebook import open_notebook
    from src.mtool.util import roots
    
    if current_scene_db == None:
        current_scene_db = roots.get_current_scene_db(scene_root, history_db)

    try:
        open_notebook.open_notebook(arg, current_scene_db, library_db, azure_data_studio_location, True)
    except Exception as e:
        raise e
    return 0
 

def search_notebook(arg,
                    scene_root = _scene_root,
                    history_db = _history_db,
                    library_db = _library_db,
                    query_start = _query_start,
                    query_end = _query_end,
                    current_scene_db = None
                    ):
    """calls the function to search a notebook"""
    from src.mtool.notebook import search_notebook

    notebooks = search_notebook.search_notebook(arg, library_db, current_scene_db, query_start, query_end)
    return notebooks


def list_notebook(arg,
                  scene_root = _scene_root,
                  history_db = _history_db,
                  library_root = _library_root,
                  library_db = _library_db,
                  query_start = _query_start,
                  query_end = _query_end, 
                  current_scene_db = None):
    """calls the function to list notebooks"""
    from src.mtool.notebook import list_notebook
    from src.mtool.util import roots
    
    if current_scene_db == None:
        current_scene_db = roots.get_current_scene_db(scene_root, history_db)

    notebook_list = list_notebook.list_notebook(library_db, current_scene_db, query_start, query_end)
    return notebook_list


def next_notebook(arg, 
                    user_info_db=_user_info_db,
                    scene_root = _scene_root,
                    history_db = _history_db, 
                    current_scene_db = None):
    """calls the function to get the next notebook"""
    from src.mtool.notebook import what_next

    if current_scene_db == None:
        from src.mtool.util.roots import get_current_scene_db
        current_scene_db = get_current_scene_db(scene_root, history_db)

    what_next.what_next(arg, user_info_db, current_scene_db)



def add_notebook(arg, 
                library_db = _library_db):
    from src.mtool.notebook import add_notebook

    try:
        add_notebook.add_notebook(arg, library_db)
    except Exception as e:
        raise e


def remove_notebook(arg, 
                    scene_root = _scene_root,
                    history_db = _history_db,
                    library_db = _library_db, 
                    current_scene_db = None):
    from src.mtool.notebook import remove_notebook
    from src.mtool.util import roots

    if current_scene_db == None:
        current_scene_db = roots.get_current_scene_db(scene_root, history_db)

    remove_notebook.remove_notebook(arg, library_db, current_scene_db)
