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
            default_scene_name = _default_scene_name):
    """uses a dictionary as a switch statement to determine which funciton to run."""
    from src.mtool.util.entrypoints import environment
    from src.mtool.util.entrypoints import library
    from src.mtool.util.entrypoints import notebook
    from src.mtool.util.entrypoints import scene
    from src.mtool.util.entrypoints import telemetry
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
        "run_notebook": notebook.run_notebook,
        "view_notebook_env": environment.view_notebook_env,
        "open_notebook": notebook.open_notebook,
        "search_notebooks": notebook.search_notebook,
        "list_notebooks": notebook.list_notebook,
        "history": scene.history,
        "next_notebook": notebook.next_notebook,
        "new_scene": scene.new_scene,
        "end_scene": scene.end_scene,
        "change_scene": scene.change_scene,
        "resume_scene": scene.resume_scene,
        "delete_scene": scene.delete_scene,
        "list_scene": scene.list_scene,
        "add_library": library.add_library,
        "list_library": library.list_library,
        "set_env": environment.set_env,
        "delete_env": environment.delete_env,
        "list_env": environment.list_env,
        "view_library_env": environment.view_library_env,
        "sync_library": library.sync_library,
        "update_settings": telemetry.update_settings
    }
    if hasattr(argument, "which"):
        func = switcher.get(argument.which)
    else:
        func = scene.current_scene

    try:
        func(argument)
    except Exception as e:
        print(e)
    