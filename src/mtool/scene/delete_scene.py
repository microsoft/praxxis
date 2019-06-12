"""
This file calls the function to delete the current scene.

Dependencies within mtool: mtool/mtool.py
"""

import os
import shutil

def delete_scene(args, root, history_db):
    from src.mtool.scene import current_scene
    from src.mtool.util import sqlite_util
    """Deletes a scene"""
    if hasattr(args, "name"):
        name = args.name
    else:
        name = args

    directory = os.path.join(root, name)
    
    if os.path.exists(directory):
        if sqlite_util.delete_scene(history_db, name):
            shutil.rmtree(directory)
    else:
        ##TODO: give proper print
        print("scene does not exist")
    

            
