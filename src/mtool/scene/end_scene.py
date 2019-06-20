"""
This file ends the specified scene
"""

def end_scene(args, scene_root, history_db, current_scene_db):
    """Ends a scene"""
    from src.mtool.util import sqlite_util
    from src.mtool.cli import display
    from src.mtool.scene import scene
    
   if hasattr(args, "name"):
        if(args.name == None):
            name = sqlite_util.get_current_scene(history_db)
        else:
            name = args.name
    else:
        name = args

    tmp_name = scene.get_scene_by_ordinal(args, name, history_db)
    if tmp_name != None:
        name = tmp_name

    if args.name == None and tmp_name == None:
        name = sqlite_util.get_current_scene(history_db)

    allow_end_scene = sqlite_util.mark_ended_scene(history_db, name)

    if allow_end_scene == -1:
        display.scene_does_not_exist_error(name)
    elif allow_end_scene:
        sqlite_util.end_scene(current_scene_db, name)
        display.display_end_scene_success(name)
    else:
        display.last_active_scene_error(name)

        
    