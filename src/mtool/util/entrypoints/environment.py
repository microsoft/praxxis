def set_env(arg, 
            scene_root,
            history_db,
            current_scene_db = None):
    """calls the function to set an environment"""
    from src.mtool.environment import set_env
    from src.mtool.util import function_switcher
    
    if current_scene_db == None:
        current_scene_db = function_switcher.get_current_scene_db(scene_root, history_db)

    env = set_env.set_env(arg, scene_root, history_db, current_scene_db)
    return env


def delete_env(arg, 
               scene_root,
               history_db,
               current_scene_db = None):
    """calls the function to delete an environment"""
    from src.mtool.environment import delete_env
    from src.mtool.util import function_switcher
    
    if current_scene_db == None:
        current_scene_db = function_switcher.get_current_scene_db(scene_root, history_db)


    env = delete_env.delete_env(arg, scene_root, history_db, current_scene_db)
    return env


def list_env(arg,
             scene_root,
             history_db,
             query_start,
             query_end, 
             current_scene_db = None):
    """calls the function to list environments in current scene"""
    from src.mtool.environment import list_env   
    from src.mtool.util import function_switcher
    
    if current_scene_db == None:
        current_scene_db = function_switcher.get_current_scene_db(scene_root, history_db)

    env = list_env.list_env(current_scene_db, query_start, query_end)
    return env


def view_library_env(arg, 
                     scene_root,
                     history_db,
                     library_db,
                     current_scene_db = None):
    from src.mtool.environment import list_env
    from src.mtool.util import function_switcher
    
    if current_scene_db == None:
        current_scene_db = function_switcher.get_current_scene_db(scene_root, history_db)


    envs = list_env.list_library_env(arg, library_db, current_scene_db)
    return envs


def view_notebook_env(arg, 
                      scene_root,
                      library_db,
                      history_db,
                      current_scene_db = None):
    from src.mtool.environment import list_env
    from src.mtool.util import function_switcher
    
    if current_scene_db == None:
        current_scene_db = function_switcher.get_current_scene_db(scene_root, history_db)

    envs = list_env.list_notebook_env(arg, library_db, current_scene_db)
    return envs
 