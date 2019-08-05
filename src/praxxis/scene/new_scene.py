"""
This file creates a new scene
"""

def new_scene(args, scene_root, history_db):
    """creates a new scene db file""" 
    import os
    from src.praxxis.display import display_scene
    from src.praxxis.scene import scene 
    
    if hasattr(args, "name"):
        name = args.name
    else:
        name = args
        
    name = name.lower()
    directory = os.path.join(scene_root, name)
    if os.path.exists(directory):
        i=1
        while os.path.exists("%s-%s" %(directory, i)):
            i+= 1
        directory = "%s-%s" %(directory, i)
        name = "%s-%s" %(name, i)
    os.mkdir(directory)
    scene_db = os.path.join(directory, "%s.db" %(name))
        
    display_scene.display_new_scene(name)
    scene.init_scene(scene_db, history_db, name)
    
    return (scene_db, name)
