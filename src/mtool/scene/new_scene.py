"""
This file creates a new scene
"""

def new_scene(args, scene_root, history_db):
    """ creates a new scene, and sets that scene to the current scene""" 
    import os
    from src.mtool.util.sqlite import sqlite_scene
    from src.mtool.display import display_scene
    from src.mtool.scene import scene 
    
    if hasattr(args, "name"):
        name = args.name
    else:
        name = args
        
    name = name.lower()
    directory = os.path.join(scene_root, name)
    if os.path.exists(directory):
        i=1
        while os.path.exists(f"{directory}-{i}"):
            i+= 1
        directory = f"{directory}-{i}"
        name = f"{name}-{i}"
    os.mkdir(directory)
    db_file = os.path.join(directory, f"{name}.db")
    
    sqlite_scene.init_scene(db_file, name)
    sqlite_scene.update_current_scene(history_db, name)
    
    display_scene.display_new_scene(name)
    