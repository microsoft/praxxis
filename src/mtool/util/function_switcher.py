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


def run_notebook(arg, 
                 user_info_db = _user_info_db, 
                 outfile_root = _outfile_root, 
                 library_root = _library_root, 
                 library_db = _library_db, 
                 scene_root = _scene_root,
                 history_db = _history_db,
                 current_scene_db = None):
    """calls the function to run a notebook"""
    from src.mtool.notebook import run_notebook
    
    if current_scene_db == None:
        current_scene_db = get_current_scene_db(scene_root, history_db)

    current_scene_db = get_current_scene_db(scene_root, history_db)
    run_notebook.run_notebook(arg, user_info_db, outfile_root, current_scene_db, library_root, library_db)
    return 0


def view_notebook_env(arg, 
                      library_db = _library_db, 
                      current_scene_db = None):
    from src.mtool.environment import list_env

    if current_scene_db == None:
        current_scene_db = get_current_scene_db(_scene_root, _history_db)

    envs = list_env.list_notebook_env(arg, library_db, current_scene_db)
    return envs
 

def open_notebook(arg, 
                  scene_root = _scene_root,
                  history_db = _history_db,
                  library_db = _library_db,
                  azure_data_studio_location = _azure_data_studio_location,
                  current_scene_db = None):
    """calls the function to open a notebook"""
    from src.mtool.notebook import open_notebook

    open_notebook.open_notebook(arg, current_scene_db, library_db, azure_data_studio_location)
    return 0
 

def search_notebook(arg,
                    scene_root = _scene_root,
                    history_db = _history_db,
                    library_db = _library_db,
                    query_start = _query_start,
                    query_end = _query_end,
                    current_scene_db = None
                    ):
    """calls the function to search a notebook"""
    from src.mtool.notebook import search_notebook



    notebooks = search_notebook.search_notebook(arg, library_db, current_scene_db, query_start, query_end)
    return notebooks


def list_notebook(arg,
                  scene_root = _scene_root,
                  history_db = _history_db,
                  library_root = _library_root,
                  library_db = _library_db,
                  query_start = _query_start,
                  query_end = _query_end,
                  current_scene_db = None):
    """calls the function to list notebooks"""
    from src.mtool.notebook import list_notebook

    if current_scene_db == None:
        current_scene_db = get_current_scene_db(scene_root, history_db)
    
    notebook_list = list_notebook.list_notebook(scene_root, library_root, library_db, current_scene_db, query_start, query_end)
    return notebook_list


def next_notebook(arg):
    """calls the function to get the next notebook"""
    ##TODO  implement this
    return "coming soon"


def history(arg, 
            scene_root = _scene_root,
            history_db = _history_db,
            library_db = _library_db, 
            current_scene_db = None):
    """calls the function to display scene history"""
    from src.mtool.scene import history

    if current_scene_db == None:
        current_scene_db = get_current_scene_db(scene_root, history_db)

    history_list = history.history(history_db, library_db, current_scene_db)
    return history_list


def new_scene(arg,
              scene_root = _scene_root,
              history_db = _history_db):
    """calls the function to create a new scene"""
    from src.mtool.scene import new_scene
    from src.mtool.scene import scene
    new_scene = new_scene.new_scene(arg, scene_root, history_db)
    return new_scene
 

def end_scene(arg, 
              scene_root = _scene_root,
              history_db = _history_db,
              current_scene_db = None):
    """calls the function to end a scene"""
    from src.mtool.scene import end_scene

    if current_scene_db == None:
        current_scene_db = get_current_scene_db(scene_root, history_db)

    current_scene = get_current_scene_db(scene_root, history_db)
    ended = end_scene.end_scene(arg, scene_root, history_db, current_scene)
    return ended
 

def change_scene(arg,
                 scene_root = _scene_root,
                 history_db = _history_db):
    """calls the function to change the current scene"""
    from src.mtool.scene import change_scene
    scene = change_scene.change_scene(arg, scene_root, history_db)
    return scene
 

def resume_scene(arg, 
                 scene_root = _scene_root,
                 history_db = _history_db):
    """calls the function to resume an ended scene"""
    from src.mtool.scene import resume_scene
    
    resumed = resume_scene.resume_scene(arg, scene_root, history_db)
    return resumed
 

def delete_scene(arg, 
                 scene_root = _scene_root,
                 history_db = _history_db):
    """ calls the function to delete a scene"""
    from src.mtool.scene import delete_scene
    
    deleted = delete_scene.delete_scene(arg, scene_root, history_db)
    return deleted


def list_scene(arg, 
               scene_root = _scene_root, 
               history_db = _history_db):
    """calls the function to list scenes"""
    from src.mtool.scene import list_scene
    list_scene.list_scene(_scene_root, _history_db)
    return


def set_env(arg, 
            scene_root = _scene_root,
            history_db = _history_db,
            current_scene_db = None):
    """calls the function to set an environment"""
    from src.mtool.environment import set_env

    if current_scene_db == None:
        current_scene_db = get_current_scene_db(scene_root, history_db)

    current_scene_db = get_current_scene_db(scene_root, history_db)
    env = set_env.set_env(arg, scene_root, history_db, current_scene_db)
    return env


def delete_env(arg, 
               scene_root = _scene_root,
               history_db = _history_db,
               current_scene_db = None):
    """calls the function to delete an environment"""
    from src.mtool.environment import delete_env

    env = delete_env.delete_env(arg, scene_root, history_db, current_scene_db)
    return env


def list_env(arg,
             scene_root = _scene_root,
             history_db = _history_db,
             query_start = _query_start,
             query_end = _query_end, 
             current_scene_db = None):
    """calls the function to list environments in current scene"""
    from src.mtool.environment import list_env   

    env = list_env.list_env(current_scene_db, query_start, query_end)
    return env


def view_library_env(arg, 
                     scene_root = _scene_root,
                     history_db = _history_db,
                     library_db = _library_db,
                     current_scene_db = None):
    from src.mtool.environment import list_env
    
    if current_scene_db == None:
        current_scene_db = get_current_scene_db(scene_root, history_db)

    envs = list_env.list_library_env(arg, library_db, current_scene_db)
    return envs

def add_library(arg):
    """calls the function to add a library"""
    ##TODO: implement this
    return "coming soon"


def list_library(arg, 
                 library_root = _library_root,
                 library_db = _library_db):
    """calls the function to list loaded libraries"""
    from src.mtool.library import list_library
    libraries = list_library.list_library(library_root, library_db)
    return libraries


def sync_library(arg, 
                 library_root = _library_root,
                 library_db = _library_db):
    """calls the function to load libraries"""
    from src.mtool.library import sync_library
    libraries = sync_library.sync_libraries(library_root, library_db)
    return libraries

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

    if not os.path.exists(root):
        os.mkdir(root)

    #library init
    if not os.path.exists(library_root):
        init_library(library_root, library_db)
    
    #outfile init
    if not os.path.exists(outfile_root):
        init_outfile(outfile_root)

    #scene init
    if not os.path.exists(scene_root):
        init_scene(scene_root, history_db, default_scene_name)

    # telemetry info init
    if not os.path.exists(telemetry_db):
        init_telemetry(telemetry_db)


def init_library(library_root, library_db):
    from src.mtool.util.sqlite import sqlite_library
    from src.mtool.display import display_library
    
    os.mkdir(library_root)
    display_library.display_init_libraries_folder(library_root)
    sqlite_library.init_library_db(library_db)
    display_library.display_init_libraries_db(library_db)


def init_outfile(outfile_root):
    from src.mtool.display import display_notebook

    os.mkdir(outfile_root)
    display_notebook.display_init_run_notebook(outfile_root)


def init_scene(scene_root, history_db, default_scene_name):
    from src.mtool.display import display_scene
    from src.mtool.util.sqlite import sqlite_scene
    from src.mtool.scene import new_scene

    os.mkdir(scene_root)
    display_scene.display_init_scene_folder(scene_root)
    sqlite_scene.init_current_scene(history_db, default_scene_name)
    new_scene.new_scene(default_scene_name, scene_root, history_db)
    display_scene.display_init_scene_db(history_db)


def init_telemetry(telemetry_db, send_telemetry = 1):
    from src.mtool.util.sqlite import sqlite_telemetry
    from src.mtool.display import display_error

    sqlite_telemetry.init_user_info(telemetry_db, send_telemetry)
    display_error.display_telem_not_init()



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
    ##Creates the mtool folder if it doesn't exist

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
        "search_notebooks": search_notebook,
        "list_notebooks": list_notebook,
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
    
    return func(argument)
    