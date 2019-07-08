"""
This file ends the specified scene
"""

##TODO: make all of these strings I return into proper errors.

def end_scene(args, scene_root, history_db, current_scene_db):
    """Ends a scene"""
    from src.mtool.util.sqlite import sqlite_scene
    from src.mtool.display import display_scene
    from src.mtool.display import display_error
    from src.mtool.scene import scene
    
    if hasattr(args, "name"):
        if(args.name == None):
            name = sqlite_scene.get_current_scene(history_db)
        else:
            name = args.name
    else:
        name = args

    tmp_name = scene.get_scene_by_ordinal(args, name, history_db)
    if tmp_name != None:
        name = tmp_name

    allow_end_scene = sqlite_scene.mark_ended_scene(history_db, name)

    if allow_end_scene == -1:
        display_error.scene_does_not_exist_error(name)
        return("scene_not_exist")
    elif allow_end_scene:
        sqlite_scene.end_scene(current_scene_db, name)
        display_scene.display_end_scene_success(name)
        return(name)
    else:
        display_error.last_active_scene_error(name)
        return("last_active_scene")
