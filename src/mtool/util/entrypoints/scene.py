def init_scene(scene_root, history_db, default_scene_name):
    import os
    from src.mtool.display import display_scene
    from src.mtool.util.sqlite import sqlite_scene
    from src.mtool.scene import new_scene

    os.mkdir(scene_root)
    display_scene.display_init_scene_folder(scene_root)
    sqlite_scene.init_current_scene(history_db, default_scene_name)
    new_scene.new_scene(default_scene_name, scene_root, history_db)
    display_scene.display_init_scene_db(history_db)


def new_scene(arg,
              scene_root,
              history_db):
    """calls the function to create a new scene"""
    from src.mtool.scene import new_scene
    from src.mtool.scene import scene
    new_scene = new_scene.new_scene(arg, scene_root, history_db)
    return new_scene


def end_scene(arg, 
              scene_root,
              history_db,
              current_scene_db = None):
    """calls the function to end a scene"""
    from src.mtool.scene import end_scene
    from src.mtool.util import function_switcher
    
    if current_scene_db == None:
        current_scene_db = function_switcher.get_current_scene_db(scene_root, history_db)

    ended = end_scene.end_scene(arg, scene_root, history_db, current_scene_db)
    return ended


def change_scene(arg,
                 scene_root,
                 history_db):
    """calls the function to change the current scene"""
    from src.mtool.scene import change_scene

    try:
        scene = change_scene.change_scene(arg, scene_root, history_db)
    except Exception as e:
        raise e
    else:
        return scene
     

def resume_scene(arg, 
                 scene_root,
                 history_db):
    """calls the function to resume an ended scene"""
    from src.mtool.scene import resume_scene
    
    try:
        resumed = resume_scene.resume_scene(arg, scene_root, history_db)
    except Exception as e:
        raise e
    return resumed
 

def delete_scene(arg, 
                 scene_root,
                 history_db):
    """ calls the function to delete a scene"""
    from src.mtool.scene import delete_scene
    
    try:
        deleted = delete_scene.delete_scene(arg, scene_root, history_db)
    except Exception as e:
        raise e
    return deleted


def list_scene(arg, 
               scene_root, 
               history_db):
    """calls the function to list scenes"""
    from src.mtool.scene import list_scene
    list_scene.list_scene(scene_root, history_db)
    return



def history(arg, 
            scene_root,
            history_db,
            library_db, 
            current_scene_db = None):
    """calls the function to display scene history"""
    from src.mtool.scene import history
    from src.mtool.util import function_switcher
    
    if current_scene_db == None:
        current_scene_db = function_switcher.get_current_scene_db(scene_root, history_db)

    history_list = history.history(history_db, library_db, current_scene_db)
    return history_list
