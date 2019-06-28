"""
This file runs a notebook. Results are either printed to the console or 
opened as an html output in the web browser, depending on user input.
"""

def run_notebook(args, root, outfile_root, current_scene_db, library_root, library_db):
    """runs a single notebook specified in args and sends telemetry"""
    from src.mtool.display import display_notebook
    from src.mtool.notebook import notebook
    from src.mtool.notebook import open_notebook 
    from src.mtool.util.sqlite import sqlite_notebook
    from src.mtool.util.sqlite import sqlite_scene
    from src.mtool.util import telemetry
    from datetime import datetime

    name = args.notebook

    tmp_name = notebook.get_notebook_by_ordinal(current_scene_db, name)
    if tmp_name != None:
        name = tmp_name

    notebook_data = sqlite_notebook.get_notebook(library_db, name)
    notebook = notebook.Notebook(notebook_data)

    display_notebook.display_run_notebook_start(notebook.name)

    local_copy = execute(current_scene_db, notebook, outfile_root)
    if args.html == "html":
        html_outputfile = f"{local_copy.split('.')[0]}.html"
        open_notebook.display_as_html(local_copy, html_outputfile)
    else:
        display_notebook.display_run_notebook(local_copy)

    timestamp = datetime.today().strftime("%Y-%m-%d %H:%M.%S")
<<<<<<< HEAD
<<<<<<< HEAD
    sqlite_scene.add_to_scene_history(current_scene_db, timestamp, notebook.name, notebook.library_name)
    telemetry.send(root, local_copy, current_scene_db)
=======
    sqlite_util.add_to_scene_history(current_scene_db, timestamp, notebook.name, notebook.library_name)
>>>>>>> telemetry runs as subprocess
=======
    sqlite_util.add_to_scene_history(current_scene_db, timestamp, notebook.name, notebook.library_name)
>>>>>>> 5fc18740ac68f1c1874b30f2d7c7d838a48d8a5c

    import subprocess
    import os
    import sys
    f = os.path.join(os.path.dirname(__file__),  "..\\util")
    os.chdir(f)
    subprocess.Popen([sys.executable, "telemetry.py", root, local_copy, current_scene_db])
    

def execute(db_file, notebook, outfile_root):
    """Handles papermill execution for notebook"""
    import papermill
    from src.mtool.display import display_error

    local_copy = get_outputname(notebook, outfile_root)

    if (notebook._hasParameters): 
        injects = pull_params(db_file, notebook._environmentVars)
        try:
            papermill.execute_notebook(notebook.getpath(), local_copy, injects)
        except Exception as e:
            display_error.papermill_error(e)
    else:
        display_error.no_tagged_cell_warning()
        try:
            papermill.execute_notebook(notebook.getpath(), local_copy)
        except Exception as e:
            display_error.papermill_error(e)

    #need local output -- temp? or just send it directly to HDFS
    return local_copy


def pull_params(db_file, environmentVars):
    """Returns a dictionary of all overridden parameters for notebook"""
    from src.mtool.util.sqlite import sqlite_environment

    injects = {}
    for var in environmentVars:
        value = sqlite_environment.get_env(db_file, var[0])
        if value != None:
            value = value[0] # want just the value, currently a tuple
            injects[var] = value
    return injects


def get_outputname(notebook, outfile_root):
    """Returns name of output file for notebook"""
    import os
    from datetime import datetime

    timestamp = datetime.today().strftime("%Y%m%d-%H%M%S")
    filename = f"{timestamp}-{notebook.library_name}-{notebook.name}.ipynb"
    
    outputname = os.path.join(outfile_root, filename)
    return outputname
