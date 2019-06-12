"""
This file calls the function to delete the current scene.

Dependencies within mtool: mtool/mtool.py
"""

import os
import shutil

def delete_scene(args, root):
    from src.mtool.scene import current_scene
    from src.mtool.util import sqlite_util
    """Deletes a scene"""
    if hasattr(args, "name"):
        name = args.name
    else:
        name = args

    directory = os.path.join(root, name)
    
    if os.path.exists(directory):
        shutil.rmtree(directory)
        current_scene = os.path.join(root, "current_scene.db")
        sqlite_util.delete_scene(current_scene, name)
    else:
        ##TODO: give proper print
        print("that doesn't exist :((")
    

            
