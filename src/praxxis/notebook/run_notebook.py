"""
This file runs a notebook. Results are either printed to the console or 
opened as an html output in the web browser, depending on user input.
"""

from src.praxxis.sqlite import sqlite_telemetry 

def run_notebook(args, user_info_db, output_root, current_scene_db, library_root, library_db, query_start, query_end):
    """runs a single notebook specified in args and sends telemetry"""
    from src.praxxis.display import display_notebook
    from src.praxxis.notebook import notebook
    from src.praxxis.notebook import open_notebook 
    from src.praxxis.sqlite import sqlite_notebook
    from src.praxxis.sqlite import sqlite_scene
    from datetime import datetime
    import os

    name = args.notebook

    if os.path.isfile(name):
        pass
        ## TODO: handle running notebooks from path

    notebook_data = notebook.get_notebook(current_scene_db, library_db, name)
    notebook = notebook.Notebook(notebook_data)

    display_notebook.display_run_notebook_start(notebook.name)

    try:
        local_copy = execute(current_scene_db, notebook, output_root)
    except Exception as e:
        raise e
    
    if args.html == "html":
        html_outputfile = "%s.html" %(local_copy.split('.')[0])
        open_notebook.display_as_html(local_copy, html_outputfile)
    else:
        display_notebook.display_run_notebook(local_copy)

    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M.%S")
    sqlite_scene.add_to_scene_history(current_scene_db, timestamp, notebook.name, notebook.library_name, local_copy)

    telemetry(user_info_db, local_copy, sqlite_telemetry.get_scene_id(current_scene_db))


def telemetry(user_info_db, local_copy, current_scene_id):
    """sets up telemetry subprocess and calls it"""
    if not sqlite_telemetry.telem_init(user_info_db):
        from src.praxxis.display import display_error
        display_error.telem_not_init_warning() 
    elif not sqlite_telemetry.telem_on(user_info_db):
        from src.praxxis.display import display_error
        display_error.telem_off_warning()    

    else: # telemetry initalized and on     
        backlog = sqlite_telemetry.backlog_size(user_info_db) 
        if backlog != 0:        
            from src.praxxis.display import display_error
            display_error.display_telem_unsent(backlog)
            
        import subprocess
        import os
        import sys
        
        subprocess.Popen([sys.executable, os.path.join(os.path.dirname(__file__),  ".." , "telemetry", "telemetry.py"), user_info_db, local_copy, current_scene_id])


def execute(current_scene_db, notebook, output_root):
    """handles papermill execution for notebook"""
    import papermill
    from src.praxxis.display import display_error

    local_copy = get_outputname(notebook, output_root)

    if (notebook._hasParameters): 
        injects = pull_params(current_scene_db, notebook._parameters)
        try:
            papermill.execute_notebook(notebook.getpath(), local_copy, injects)
        except Exception as e:
            raise e
    else:
        display_error.no_tagged_cell_warning()
        try:
            papermill.execute_notebook(notebook.getpath(), local_copy)
        except Exception as e:
            raise e

    return local_copy


def pull_params(current_scene_db, parameters):
    """returns a dictionary of all overridden parameters for notebook"""
    from src.praxxis.sqlite import sqlite_parameter

    injects = {}
    for var in parameters:
        value = sqlite_parameter.get_param(current_scene_db, var[0])
        if value != None:
            value = value[0] # want just the value, currently a tuple
            injects[var[0]] = value
    return injects


def get_outputname(notebook, output_root):
    """returns name of output file for notebook"""
    import os
    from datetime import datetime

    timestamp = datetime.utcnow().strftime("%Y%m%d-%H%M%S")
    filename = "%s-%s-%s.ipynb" %(timestamp, notebook.library_name, notebook.name)
    
    outputname = os.path.join(output_root, filename)
    return outputname
