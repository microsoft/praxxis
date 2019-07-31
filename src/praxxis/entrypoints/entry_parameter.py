"""
handles the parameter functions for the CLI
"""
from src.praxxis.util.roots import _scene_root
from src.praxxis.util.roots import _history_db
from src.praxxis.util.roots import _query_start
from src.praxxis.util.roots import _query_end
from src.praxxis.util.roots import _library_db

def set_param(arg, 
            scene_root = _scene_root,
            history_db = _history_db,
            current_scene_db = None):
    """calls the function to set an parameter"""
    from src.praxxis.parameter import set_param
    from src.praxxis.util import roots
    
    if current_scene_db == None:
        current_scene_db = roots.get_current_scene_db(scene_root, history_db)

    set_param.set_param(arg, scene_root, history_db, current_scene_db)


def delete_param(arg, 
               scene_root = _scene_root,
               history_db = _history_db,
               current_scene_db = None):
    """calls the function to delete an parameter"""
    from src.praxxis.parameter import delete_param
    from src.praxxis.util import roots
    
    if current_scene_db == None:
        current_scene_db = roots.get_current_scene_db(scene_root, history_db)

    delete_param.delete_parameter(arg, scene_root, history_db, current_scene_db)
    

def list_param(arg,
             scene_root = _scene_root,
             history_db = _history_db,
             query_start = _query_start,
             query_end = _query_end, 
             current_scene_db = None):
    """calls the function to list parameters in current scene"""
    from src.praxxis.parameter import list_param   
    from src.praxxis.util import roots
    
    if current_scene_db == None:
        current_scene_db = roots.get_current_scene_db(scene_root, history_db)

    list_param.list_param(current_scene_db, query_start, query_end)


def view_library_param(arg, 
                     scene_root = _scene_root,
                     history_db = _history_db,
                     library_db = _library_db,
                     start = _query_start,
                     end = _query_end,
                     current_scene_db = None):
    """ handles viewing library parameters from the CLI """
    from src.praxxis.parameter import list_param
    from src.praxxis.util import roots
    
    if current_scene_db == None:
        current_scene_db = roots.get_current_scene_db(scene_root, history_db)

    list_param.list_library_param(arg, library_db, current_scene_db, start, end)


def view_notebook_param(arg, 
                      scene_root = _scene_root,
                      library_db = _library_db,
                      history_db = _history_db,
                      current_scene_db = None):
    """ handles viewing notebook parameters from the CLI """
    from src.praxxis.parameter import list_param
    from src.praxxis.util import roots
    
    if current_scene_db == None:
        current_scene_db = roots.get_current_scene_db(scene_root, history_db)

    list_param.list_notebook_param(arg, library_db, current_scene_db)
 

def pull_notebook_param(arg,
                      library_db = _library_db,
                      scene_root = _scene_root,
                      history_db = _history_db,
                      current_scene_db = None):
    """ handles pulling parameters out of a notebook through the CLI """
    from src.praxxis.parameter import pull_param
    from src.praxxis.util import roots

    if current_scene_db == None:
        current_scene_db = roots.get_current_scene_db(scene_root, history_db)

    pull_param.pull_notebook_parameter(arg, library_db, current_scene_db)


def pull_library_param(arg,
                      library_db = _library_db,
                      scene_root = _scene_root,
                      history_db = _history_db,
                      current_scene_db = None,
                      start = _query_start,
                      stop = _query_end):
    """ handles pulling parameters out of a library through the CLI. """
    from src.praxxis.parameter import pull_param
    from src.praxxis.util import roots

    if current_scene_db == None:
        current_scene_db = roots.get_current_scene_db(scene_root, history_db)

    pull_param.pull_library_parameter(arg, library_db, current_scene_db, start, stop)
