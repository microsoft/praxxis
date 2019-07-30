"""
handles the notebook functions of the CLI
"""

from src.praxxis.util.roots import _outfile_root
from src.praxxis.util.roots import _user_info_db
from src.praxxis.util.roots import _library_root
from src.praxxis.util.roots import _library_db
from src.praxxis.util.roots import _scene_root
from src.praxxis.util.roots import _history_db
from src.praxxis.util.roots import _azure_data_studio_location
from src.praxxis.util.roots import _query_start
from src.praxxis.util.roots import _query_end
from src.praxxis.util.roots import _rulesengine_db

def init_outfile(outfile_root):
    """ initializes the outfile for running notebooks """
    import os
    from src.praxxis.display import display_notebook

    os.mkdir(outfile_root)
    display_notebook.display_init_run_notebook(outfile_root)
    

def run_notebook(arg, 
                 user_info_db = _user_info_db, 
                 outfile_root = _outfile_root, 
                 library_root = _library_root, 
                 library_db = _library_db, 
                 scene_root = _scene_root,
                 history_db = _history_db,
                 current_scene_db = None,
                 query_start = _query_start,
                 query_end = _query_end):
    """calls the function to run a notebook"""
    from src.praxxis.notebook import run_notebook
    from src.praxxis.util import roots
    
    if current_scene_db == None:
        current_scene_db = roots.get_current_scene_db(scene_root, history_db)
    
    run_notebook.run_notebook(arg, user_info_db, outfile_root, current_scene_db, library_root, library_db, query_start, query_end)


def open_notebook(arg, 
                  scene_root = _scene_root,
                  history_db = _history_db, 
                  library_db = _library_db,
                  azure_data_studio_location = _azure_data_studio_location,
                  current_scene_db = None,
                  test = False):
    """calls the function to open a notebook"""
    from src.praxxis.notebook import open_notebook
    from src.praxxis.util import roots

    #TODO: allow for selecting your own editor on first run
    editor = "vim"
    
    if current_scene_db == None:
        current_scene_db = roots.get_current_scene_db(scene_root, history_db)
    
    open_notebook.open_notebook(arg, current_scene_db, library_db, azure_data_studio_location, editor, True)


def search_notebook(arg,
                    scene_root = _scene_root,
                    history_db = _history_db,
                    library_db = _library_db,
                    query_start = _query_start,
                    query_end = _query_end,
                    current_scene_db = None
                    ):
    """calls the function to search a notebook"""
    from src.praxxis.notebook import search_notebook
    from src.praxxis.util import roots

    if current_scene_db == None:
        current_scene_db = roots.get_current_scene_db(scene_root, history_db)
    
    search_notebook.search_notebook(arg, library_db, current_scene_db, query_start, query_end)


def list_notebook(arg,
                  scene_root = _scene_root,
                  history_db = _history_db,
                  library_root = _library_root,
                  library_db = _library_db,
                  query_start = _query_start,
                  query_end = _query_end, 
                  current_scene_db = None):
    """calls the function to list notebooks"""
    from src.praxxis.notebook import list_notebook
    from src.praxxis.util import roots
    
    if current_scene_db == None:
        current_scene_db = roots.get_current_scene_db(scene_root, history_db)

    list_notebook.list_notebook(library_db, current_scene_db, query_start, query_end)


def next_notebook(arg, 
                    user_info_db=_user_info_db,
                    scene_root = _scene_root,
                    history_db = _history_db, 
                    current_scene_db = None,
                    library_db = _library_db,
                    rulesengine_db = _rulesengine_db,
                    start = _query_start,
                    end = _query_end):
    """calls the function to get the next notebook"""
    from src.praxxis.notebook import what_next
    from src.praxxis.util import roots

    if current_scene_db == None:
        current_scene_db = roots.get_current_scene_db(scene_root, history_db)

    what_next.what_next(arg, user_info_db, current_scene_db, library_db, rulesengine_db, start, end)



def add_notebook(arg, 
                library_db = _library_db):
    """ handles adding a notebook from the CLI """
    from src.praxxis.notebook import add_notebook

    add_notebook.add_notebook(arg, library_db)


def remove_notebook(arg, 
                    scene_root = _scene_root,
                    history_db = _history_db,
                    library_db = _library_db, 
                    current_scene_db = None):
    """handles removing a notebook from the cli"""
    from src.praxxis.notebook import remove_notebook
    from src.praxxis.util import roots

    if current_scene_db == None:
        current_scene_db = roots.get_current_scene_db(scene_root, history_db)

    remove_notebook.remove_notebook(arg, library_db, current_scene_db)
