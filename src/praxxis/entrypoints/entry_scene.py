"""
This file handles all of the scene functions for the CLI
"""

from src.praxxis.util.roots import _scene_root
from src.praxxis.util.roots import _history_db
from src.praxxis.util.roots import _default_scene_name
from src.praxxis.util.roots import _library_db

def init_scene(scene_root = _scene_root, 
               history_db = _history_db, 
               default_scene_name = _default_scene_name):
    """handles initializing the scene db and directory"""
    import os
    from src.praxxis.display import display_scene
    from src.praxxis.sqlite import sqlite_init
    from src.praxxis.scene import new_scene

    os.mkdir(scene_root)
    display_scene.display_init_scene_folder(scene_root)
    sqlite_init.init_history(history_db, default_scene_name)
    new_scene.new_scene(default_scene_name, scene_root, history_db)
    display_scene.display_init_scene_db(history_db)


def new_scene(arg,
              scene_root = _scene_root,
              history_db = _history_db):
    """handles creating a new scene"""
    from src.praxxis.scene import new_scene
    from src.praxxis.scene import scene

    new_scene.new_scene(arg, scene_root, history_db)


def end_scene(arg, 
              scene_root = _scene_root,
              history_db = _history_db,
              current_scene_db = None):
    """handles ending a scene"""
    from src.praxxis.scene import end_scene
    from src.praxxis.util import roots
    
    if current_scene_db == None:
        current_scene_db = roots.get_current_scene_db(scene_root, history_db)

    end_scene.end_scene(arg, scene_root, history_db, current_scene_db)


def change_scene(arg,
                 scene_root = _scene_root,
                 history_db = _history_db):
    """handles changing the current scene"""
    from src.praxxis.scene import change_scene

    change_scene.change_scene(arg, scene_root, history_db)
     

def resume_scene(arg, 
                 scene_root = _scene_root,
                 history_db = _history_db):
    """handles resuming an ended scene"""
    from src.praxxis.scene import resume_scene

    resume_scene.resume_scene(arg, scene_root, history_db)

 
def delete_scene(arg, 
                 scene_root = _scene_root,
                 history_db = _history_db):
    """handles deleting a scene"""
    from src.praxxis.scene import delete_scene
    
    delete_scene.delete_scene(arg, scene_root, history_db)


def list_scene(arg, 
               scene_root = _scene_root, 
               history_db = _history_db):
    """handles listing scenes"""
    from src.praxxis.scene import list_scene

    list_scene.list_scene(scene_root, history_db)


def history(arg, 
            scene_root = _scene_root,
            history_db = _history_db,
            library_db = _library_db, 
            current_scene_db = None):
    """handles displaying scene history"""
    from src.praxxis.scene import history
    from src.praxxis.util import roots
    
    if current_scene_db == None:
        current_scene_db = roots.get_current_scene_db(scene_root, history_db)

    history.history(history_db, library_db, current_scene_db)


def current_scene(arg, 
            scene_root = _scene_root,
            history_db = _history_db):
    """handles the default function, which displays the current scene"""
    from src.praxxis.scene import current_scene
    
    current_scene = current_scene.current_scene(scene_root, history_db)
