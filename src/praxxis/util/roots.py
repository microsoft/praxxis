import os
import sys

#checks what platform you're on to see where to put praxxis root
if(sys.platform == "linux"):
    _root = os.path.join (os.path.expanduser('~/praxxis'))
    _azure_data_studio_location = os.path.join('/usr', 'share', 'azuredatastudio', 'azuredatastudio')

else:
    _root = os.path.join(os.getenv('APPDATA'), "praxxis")
    _azure_data_studio_location = os.path.join(os.getenv('LOCALAPPDATA'), 'Programs', 'Azure Data Studio', 'azuredatastudio')

_user_info_db = os.path.join(_root, "user_id.db")
_library_root = os.path.join(_root, "library")
_library_db = os.path.join(_library_root, "libraries.db")
_scene_root = os.path.join(_root, "scene")
_output_root = os.path.join(_root, "output")
_history_db = os.path.join(_scene_root, "history.db")
_telemetry_db = os.path.join(_root, "user_id.db")
_rulesengine_root = os.path.join(_root, "rulesengine")
_rulesengine_db = os.path.join(_rulesengine_root, "rulesengine.db")
_model_root = os.path.join(_root, "model")
_model_db = os.path.join(_model_root, "model.db")
_default_scene_name = 'scene'
_git_root = os.path.join(_library_root, "git_libraries")

_query_start = 0
_query_end = 100

def get_current_scene_db(scene_root, history_db):
    """calls the function to get the location of the history db"""
    import os
    from src.praxxis.sqlite import sqlite_scene
    scene = sqlite_scene.get_current_scene(history_db)
    return os.path.join(scene_root, scene, f"{scene}.db")

def init(
        root, 
        library_root, 
        library_db, 
        output_root, 
        scene_root, 
        history_db, 
        telemetry_db,
        rulesengine_root, 
        rulesengine_db,
        model_root,
        model_db,
        default_scene_name,
        telemetry = True,
        ):
    import os
    from src.praxxis.entrypoints import entry_parameter
    from src.praxxis.entrypoints import entry_library
    from src.praxxis.entrypoints import entry_notebook
    from src.praxxis.entrypoints import entry_scene
    from src.praxxis.entrypoints import entry_telemetry
    from src.praxxis.entrypoints import entry_rulesengine
    from src.praxxis.entrypoints import entry_model

    if not os.path.exists(root):
        os.mkdir(root)

    #library init
    if not os.path.exists(library_root):
        entry_library.init_library(library_root, library_db)
    
    #output init
    if not os.path.exists(output_root):
        entry_notebook.init_output(output_root)

    #scene init
    if not os.path.exists(scene_root):
        entry_scene.init_scene(scene_root, history_db, default_scene_name)

    # telemetry info init
    if not os.path.exists(telemetry_db):
        entry_telemetry.init_telemetry(telemetry_db)

    # rules engine init
    if not os.path.exists(rulesengine_db):
        entry_rulesengine.init_rulesengine(rulesengine_root, rulesengine_db)

    # model init
    if not os.path.exists(model_db):
        entry_model.init_model(model_root, model_db)

