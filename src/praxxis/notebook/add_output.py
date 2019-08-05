"""
This file adds output to the last executed notbeook.
"""

def add_output(args, output_root, current_scene_db, user_info_db):
    """insert output into previously executed notebook json"""
    import json
    from src.praxxis.sqlite import sqlite_scene
    from src.praxxis.display import display_notebook

    CELL_FORMAT = {'cell_type': 'code', 'execution_count': None, 'metadata': {}, 'outputs': [{"name": "stdout", "output_type": "stream", "text": []}],  'source': ['OUTPUT ADDED AFTER EXECUTION:']}
    
    CELL_FORMAT['outputs'][0]['text'].append(args.string)

    last_notebook = sqlite_scene.get_recent_history(current_scene_db, 1)
    if last_notebook == []:
        from src.praxxis.util import error
        raise error.EmptyHistoryError()
        
    with open(last_notebook[0][1]) as f:
        notebook_data = json.load(f)
        notebook_data["cells"].append(CELL_FORMAT)
        f.close()
    with open(last_notebook[0][1], 'w') as f1:
        json.dump(notebook_data, f1)
        f1.close()
        
    display_notebook.display_adding_output(last_notebook[0][0], args.string)

    update_telemetry(user_info_db, last_notebook[0][1], current_scene_db)

    return args.string
    

def update_telemetry(user_info_db, local_copy, current_scene_db):
    """sets up a telemetry update operation as a subprocess"""
    from src.praxxis.sqlite import sqlite_telemetry

    current_scene_id = sqlite_telemetry.get_scene_id(current_scene_db)

    if not sqlite_telemetry.telem_init(user_info_db):
        from src.praxxis.display import display_error
        display_error.telem_not_init_warning() 
    elif not sqlite_telemetry.telem_on(user_info_db):
        from src.praxxis.display import display_error
        display_error.telem_off_warning()    
    else: # telemetry initalized and on     
        import subprocess
        import os
        import sys
        
        subprocess.Popen([sys.executable, os.path.join(os.path.dirname(__file__),  ".." , "telemetry", "update_file_output.py"), user_info_db, local_copy, current_scene_id])
