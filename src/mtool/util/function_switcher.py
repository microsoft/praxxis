"""
This file is responsible for running all of the functions identified by app.py
"""

import os
import sys

#checks what platform you're on to see where to put mtool root
if(sys.platform == "linux"):
    _root = os.path.join (os.path.expanduser('~/mtool'))
    _azure_data_studio_location = os.path.join('/usr', 'share', 'azuredatastudio', 'azuredatastudio')

else:
    _root = os.path.join(os.getenv('APPDATA'), "mtool")
    _azure_data_studio_location = os.path.join(os.getenv('LOCALAPPDATA'), 'Programs', 'Azure Data Studio', 'azuredatastudio')


_user_info_db = os.path.join(_root, "user_id.db")
_library_root = os.path.join(_root, "library")
_library_db = os.path.join(_library_root, "libraries.db")
_scene_root = os.path.join(_root, "scene")
_outfile_root = os.path.join(_root, "output")
_history_db = os.path.join(_scene_root, "current_scene.db")
_telemetry_db = os.path.join(_root, "user_id.db")
_default_scene_name = 'scene'


_query_start = 0
_query_end = 100

def get_current_scene_db(scene_root, history_db):
    """calls the function to get the location of the history db"""
    from src.mtool.util.sqlite import sqlite_scene
    scene = sqlite_scene.get_current_scene(history_db)
    return os.path.join(scene_root, scene, f"{scene}.db")


def update_settings(arg,
                    user_info_db = _user_info_db):
    """calls the function to open the settings utility"""
    from src.mtool.util import update_settings
    settings = update_settings.update_settings(user_info_db)
    return settings


def default(arg, 
            scene_root = _scene_root,
            history_db = _history_db):
    """calls the default function, which is to display the current scene."""
    ##TODO:set up running notebook as default 
    from src.mtool.scene import current_scene
    current_scene = current_scene.current_scene(scene_root, history_db)
    return current_scene


def run_notebook(args):
    from src.mtool.util.entrypoints import notebook
    
    notebook.run_notebook(args, 
                 _user_info_db, 
                 _outfile_root, 
                 _library_root, 
                 _library_db, 
                 _scene_root,
                 _history_db)


def open_notebook(args):
    from src.mtool.util.entrypoints import notebook
    
    notebook.open_notebook(args, 
                           _scene_root,
                           _history_db,
                           _library_db,
                           _azure_data_studio_location)


def search_notebooks(args):
    from src.mtool.util.entrypoints import notebook


    notebook.search_notebook(args, 
                             _scene_root,
                             _history_db,
                             _library_db,
                             _query_start,
                             _query_end,
                             _azure_data_studio_location)


def list_notebooks(args):
    from src.mtool.util.entrypoints import notebook

    notebook.list_notebook(args,
                  _scene_root,
                  _history_db,
                  _library_root,
                  _library_db,
                  _query_start,
                  _query_end)


def next_notebook(args): 
    from src.mtool.util.entrypoints import notebook

    notebook.next_notebook(args)


def history(args): 
    from src.mtool.util.entrypoints import scene

    scene.history(args, 
                  _scene_root,
                  _history_db,
                  _library_db)
def new_scene(args): 
    from src.mtool.util.entrypoints import scene

    scene.new_scene(args, 
                    _scene_root,
                    _history_db)

                
def end_scene(args): 
    from src.mtool.util.entrypoints import scene

    scene.end_scene(args,
                    _scene_root,
                    _history_db)

                
def change_scene(args):
    from src.mtool.util.entrypoints import scene

    scene.change_scene(args,
                       _scene_root,
                       _history_db)


def resume_scene(args):
    from src.mtool.util.entrypoints import scene

    scene.resume_scene(args,
                       _scene_root, 
                       _history_db)



def delete_scene(args):
    from src.mtool.util.entrypoints import scene

    scene.delete_scene(args,
                       _scene_root, 
                       _history_db),


def list_scene(args): 
    from src.mtool.util.entrypoints import scene

    scene.list_scene(args,
                     _scene_root,
                     _history_db)


def add_library(args):
    from src.mtool.util.entrypoints import library

    library.add_library (args)


def list_library(args): 
    from src.mtool.util.entrypoints import library

    library.list_library(args,
                         _library_root,
                         _library_db)


def sync_library(args): 
    from src.mtool.util.entrypoints import library

    library.sync_library(args, 
                         _library_root,
                         _library_db)


def set_env(args): 
    from src.mtool.util.entrypoints import environment

    environment.set_env(args, 
                        _scene_root,
                        _history_db)


def delete_env(args): 
    from src.mtool.util.entrypoints import environment
    
    environment.delete_env(args,
                           _scene_root, 
                           _history_db)

                    
def list_env(args): 
    from src.mtool.util.entrypoints import environment

    environment.list_env(args,
             _scene_root,
             _history_db,
             _query_start,
             _query_end)


def view_notebook_env(args): 
    from src.mtool.util.entrypoints import environment

    environment.view_notebook_env(args, 
                      _scene_root,
                      _library_db,
                      _history_db,)


def view_library_env(args): 
    from src.mtool.util.entrypoints import environment

    environment.view_library_env(args, 
                                  _scene_root,
                                  _history_db,
                                  _library_db)


def init(
        root, 
        library_root, 
        library_db, 
        outfile_root, 
        scene_root, 
        history_db, 
        telemetry_db,
        default_scene_name,
        telemetry = True,
        ):
    from src.mtool.util.entrypoints import environment
    from src.mtool.util.entrypoints import library
    from src.mtool.util.entrypoints import notebook
    from src.mtool.util.entrypoints import scene
    from src.mtool.util.entrypoints import telemetry

    if not os.path.exists(root):
        os.mkdir(root)

    #library init
    if not os.path.exists(library_root):
        library.init_library(library_root, library_db)
    
    #outfile init
    if not os.path.exists(outfile_root):
        notebook.init_outfile(outfile_root)

    #scene init
    if not os.path.exists(scene_root):
        scene.init_scene(scene_root, history_db, default_scene_name)

    # telemetry info init
    if not os.path.exists(telemetry_db):
        telemetry.init_telemetry(telemetry_db)


def command(argument,
            root = _root,
            library_root = _library_root, 
            library_db = _library_db,
            outfile_root = _outfile_root,
            scene_root = _scene_root,
            history_db = _history_db,
            telemetry_db = _telemetry_db,
            default_scene_name = _default_scene_name):
    """uses a dictionary as a switch statement to determine which funciton to run."""
    from src.mtool.util.entrypoints import environment
    from src.mtool.util.entrypoints import library
    from src.mtool.util.entrypoints import notebook
    from src.mtool.util.entrypoints import scene
    from src.mtool.util.entrypoints import telemetry

    init(root, 
         library_root, 
         library_db,
         outfile_root,
         scene_root,
         history_db,
         telemetry_db,
         default_scene_name)

    switcher = {
        "run_notebook": run_notebook,
        "view_notebook_env": view_notebook_env,
        "open_notebook": open_notebook,
        "search_notebooks": search_notebooks,
        "list_notebooks": list_notebooks,
        "history": history,
        "next_notebook": next_notebook,
        "new_scene": new_scene,
        "end_scene": end_scene,
        "change_scene": change_scene,
        "resume_scene": resume_scene,
        "delete_scene": delete_scene,
        "list_scene": list_scene,
        "add_library": add_library,
        "list_library": list_library,
        "set_env": set_env,
        "delete_env": delete_env,
        "list_env": list_env,
        "view_library_env": view_library_env,
        "sync_library": sync_library,
        "update_settings": update_settings
    }
    if hasattr(argument, "which"):
        func = switcher.get(argument.which)
    else:
        func = default

    try:
        func(argument)
    except Exception as e:
        print(e)
    