"""
This file is responsible for running all of the functions identified by app.py
"""

from src.mtool.util.roots import _default_scene_name
from src.mtool.util.roots import _history_db
from src.mtool.util.roots import _library_db
from src.mtool.util.roots import _library_root
from src.mtool.util.roots import _outfile_root
from src.mtool.util.roots import _root
from src.mtool.util.roots import _scene_root
from src.mtool.util.roots import _telemetry_db

def command(argument,
            root = _root,
            library_root = _library_root, 
            library_db = _library_db,
            outfile_root = _outfile_root,
            scene_root = _scene_root,
            history_db = _history_db,
            telemetry_db = _telemetry_db,
            default_scene_name = _default_scene_name,
            test = False):
    """uses a dictionary as a switch statement to determine which funciton to run."""
    from src.mtool.util.entrypoints import entry_environment
    from src.mtool.util.entrypoints import entry_library
    from src.mtool.util.entrypoints import entry_notebook
    from src.mtool.util.entrypoints import entry_scene
    from src.mtool.util.entrypoints import entry_telemetry
    from src.mtool.util import roots

    roots.init(root, 
         library_root, 
         library_db,
         outfile_root,
         scene_root,
         history_db,
         telemetry_db,
         default_scene_name)

    switcher = {
        "run_notebook": entry_notebook.run_notebook,
        "view_notebook_env": entry_environment.view_notebook_env,
        "open_notebook": entry_notebook.open_notebook,
        "search_notebooks": entry_notebook.search_notebook,
        "list_notebooks": entry_notebook.list_notebook,
        "history": entry_scene.history,
        "next_notebook": entry_notebook.next_notebook,
        "remove_notebook": entry_notebook.remove_notebook,
        "new_scene": entry_scene.new_scene,
        "end_scene": entry_scene.end_scene,
        "change_scene": entry_scene.change_scene,
        "resume_scene": entry_scene.resume_scene,
        "delete_scene": entry_scene.delete_scene,
        "list_scene": entry_scene.list_scene,
        "add_library": entry_library.add_library,
        "remove_library": entry_library.remove_library,
        "list_library": entry_library.list_library,
        "set_env": entry_environment.set_env,
        "delete_env": entry_environment.delete_env,
        "list_env": entry_environment.list_env,
        "view_library_env": entry_environment.view_library_env,
        "pull_notebook_env": entry_environment.pull_notebook_env,
        "pull_library_env": entry_environment.pull_library_env,
        "sync_library": entry_library.sync_library,
        "update_settings": entry_telemetry.update_settings
    }

    if hasattr(argument, "which"):
        func = switcher.get(argument.which)
    else:
        func = entry_scene.current_scene
    
    if(test):
        return func
        
    try:
        output = func(argument)
    except Exception as e:
        raise e
    return output

    