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
from src.mtool.util.roots import _rulesengine_root
from src.mtool.util.roots import _rulesengine_db
from src.mtool.util.roots import _model_root
from src.mtool.util.roots import _model_db

def command(argument,
            root = _root,
            library_root = _library_root, 
            library_db = _library_db,
            outfile_root = _outfile_root,
            scene_root = _scene_root,
            history_db = _history_db,
            telemetry_db = _telemetry_db,
            rulesengine_root = _rulesengine_root,
            rulesengine_db = _rulesengine_db,
            model_root = _model_root,
            model_db = _model_db,
            default_scene_name = _default_scene_name,
            test = False):
    """uses a dictionary as a switch statement to determine which funciton to run."""
    from src.mtool.util.entrypoints import entry_parameter
    from src.mtool.util.entrypoints import entry_library
    from src.mtool.util.entrypoints import entry_notebook
    from src.mtool.util.entrypoints import entry_scene
    from src.mtool.util.entrypoints import entry_telemetry
    from src.mtool.util.entrypoints import entry_rulesengine
    from src.mtool.util.entrypoints import entry_model
    from src.mtool.util import roots

    roots.init(root, 
         library_root, 
         library_db,
         outfile_root,
         scene_root,
         history_db,
         telemetry_db,
         rulesengine_root,
         rulesengine_db,
         model_root,
         model_db,
         default_scene_name,
         )
    
    switcher = {
        "run_notebook": entry_notebook.run_notebook,
        "view_notebook_param": entry_parameter.view_notebook_param,
        "open_notebook": entry_notebook.open_notebook,
        "search_notebooks": entry_notebook.search_notebook,
        "list_notebooks": entry_notebook.list_notebook,
        "history": entry_scene.history,
        "next_notebook": entry_notebook.next_notebook,
        "add_notebook": entry_notebook.add_notebook,
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
        "set_param": entry_parameter.set_param,
        "delete_param": entry_parameter.delete_param,
        "list_param": entry_parameter.list_param,
        "view_library_param": entry_parameter.view_library_param,
        "pull_notebook_param": entry_parameter.pull_notebook_param,
        "pull_library_param": entry_parameter.pull_library_param,
        "sync_library": entry_library.sync_library,
        "update_settings": entry_telemetry.update_settings,
        "new_ruleset": entry_rulesengine.new_ruleset,
        "remove_ruleset": entry_rulesengine.remove_ruleset,
        "list_rulesets": entry_rulesengine.list_rulesets,
        "view_ruleset": entry_rulesengine.view_ruleset,
        "edit_ruleset": entry_rulesengine.edit_ruleset,
        "import_ruleset": entry_rulesengine.import_ruleset,
        "activate_ruleset": entry_rulesengine.activate_ruleset,
        "deactivate_ruleset": entry_rulesengine.deactivate_ruleset,
        "import_model": entry_model.import_model,
        "update_model": entry_model.update_model
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

    