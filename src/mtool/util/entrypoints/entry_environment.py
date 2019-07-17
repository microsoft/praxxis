from src.mtool.util.roots import _scene_root
from src.mtool.util.roots import _history_db
from src.mtool.util.roots import _query_start
from src.mtool.util.roots import _query_end
from src.mtool.util.roots import _library_db

def set_env(arg, 
            scene_root = _scene_root,
            history_db = _history_db,
            current_scene_db = None):
    """calls the function to set an environment"""
    from src.mtool.environment import set_env
    from src.mtool.util import roots
    
    if current_scene_db == None:
        current_scene_db = roots.get_current_scene_db(scene_root, history_db)

    set_env.set_env(arg, scene_root, history_db, current_scene_db)


def delete_env(arg, 
               scene_root = _scene_root,
               history_db = _history_db,
               current_scene_db = None):
    """calls the function to delete an environment"""
    from src.mtool.environment import delete_env
    from src.mtool.util import roots
    
    if current_scene_db == None:
        current_scene_db = roots.get_current_scene_db(scene_root, history_db)

    delete_env.delete_env(arg, scene_root, history_db, current_scene_db)
    

def list_env(arg,
             scene_root = _scene_root,
             history_db = _history_db,
             query_start = _query_start,
             query_end = _query_end, 
             current_scene_db = None):
    """calls the function to list environments in current scene"""
    from src.mtool.environment import list_env   
    from src.mtool.util import roots
    
    if current_scene_db == None:
        current_scene_db = roots.get_current_scene_db(scene_root, history_db)

    list_env.list_env(current_scene_db, query_start, query_end)


def view_library_env(arg, 
                     scene_root = _scene_root,
                     history_db = _history_db,
                     library_db = _library_db,
                     current_scene_db = None):
    from src.mtool.environment import list_env
    from src.mtool.util import roots
    
    if current_scene_db == None:
        current_scene_db = roots.get_current_scene_db(scene_root, history_db)

    list_env.list_library_env(arg, library_db, current_scene_db)


def view_notebook_env(arg, 
                      scene_root = _scene_root,
                      library_db = _library_db,
                      history_db = _history_db,
                      current_scene_db = None):
    from src.mtool.environment import list_env
    from src.mtool.util import roots
    
    if current_scene_db == None:
        current_scene_db = roots.get_current_scene_db(scene_root, history_db)

    list_env.list_notebook_env(arg, library_db, current_scene_db)
 

def pull_notebook_env(arg,
                      library_db = _library_db,
                      scene_root = _scene_root,
                      history_db = _history_db,
                      current_scene_db = None):
    from src.mtool.environment import pull_env
    from src.mtool.util import roots


    if current_scene_db == None:
        current_scene_db = roots.get_current_scene_db(scene_root, history_db)

    pull_env.pull_notebook_environment(arg, library_db, current_scene_db)


def pull_library_env(arg,
                      library_db = _library_db,
                      scene_root = _scene_root,
                      history_db = _history_db,
                      current_scene_db = None):
    from src.mtool.environment import pull_env
    from src.mtool.util import roots


    if current_scene_db == None:
        current_scene_db = roots.get_current_scene_db(scene_root, history_db)

    pull_env.pull_library_environment(arg, library_db, current_scene_db)