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
_prediction_root = os.path.join(_root, "prediction")
_prediction_db = os.path.join(_prediction_root, "prediction.db")
_default_scene_name = 'scene'



_query_start = 0
_query_end = 100


def get_current_scene_db(scene_root, history_db):
    """calls the function to get the location of the history db"""
    import os
    from src.mtool.util.sqlite import sqlite_scene
    scene = sqlite_scene.get_current_scene(history_db)
    return os.path.join(scene_root, scene, f"{scene}.db")
    

def init(
        root, 
        library_root, 
        library_db, 
        outfile_root, 
        scene_root, 
        history_db, 
        telemetry_db,
        prediction_root, 
        prediction_db,
        default_scene_name,
        telemetry = True,
        ):
    import os
    from src.mtool.util.entrypoints import entry_environment
    from src.mtool.util.entrypoints import entry_library
    from src.mtool.util.entrypoints import entry_notebook
    from src.mtool.util.entrypoints import entry_scene
    from src.mtool.util.entrypoints import entry_telemetry
    from src.mtool.util.entrypoints import entry_prediction

    if not os.path.exists(root):
        os.mkdir(root)

    #library init
    if not os.path.exists(library_root):
        entry_library.init_library(library_root, library_db)
    
    #outfile init
    if not os.path.exists(outfile_root):
        entry_notebook.init_outfile(outfile_root)

    #scene init
    if not os.path.exists(scene_root):
        entry_scene.init_scene(scene_root, history_db, default_scene_name)

    # telemetry info init
    if not os.path.exists(telemetry_db):
        entry_telemetry.init_telemetry(telemetry_db)

    # predictions init
    if not os.path.exists(prediction_db):
        entry_prediction.init_prediction(prediction_root, prediction_db)


