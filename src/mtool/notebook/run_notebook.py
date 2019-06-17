"""
This file runs a notebook. Results are either printed to the console or 
opened as an html output in the web browser, depending on user input.

Dependencies within mtool:  notebook.py, scene.py, open_notebook.py,
    telemetry.py
"""

"""
TIMING INFO: notebook runs 
avg without injection, without telemetry: 3.904 s (4 runs)
avg with    injection, without telemetry: 3.881 s (3 runs)
avg with    injection, with    telemetry: 5.556 s (4 runs)

injection does not appear to add substantial processing time; the difference 
between injection enabled and disabled does not appear to be statistically
significant. 

telemetry is a huge time drag, adding an average of 1.675 seconds simply to 
send the data to HDFS. At this rate, might be easier to thread that process?
Also check string concat and other optimizers.
"""


#TODO: want to print defaults and overridden vals before execution
#TODO: should have a way to view all defaults in a notebook 
#TODO: have a way to load all environment variables for a library?

import os
import webbrowser
from datetime import datetime

from src.mtool.notebook import open_notebook 
from src.mtool.util import telemetry
from src.mtool.util import sqlite_util

import papermill

def run_notebook(args, root, outfile_root, current_scene_db, library_root):
    from src.mtool.cli import display
    from src.mtool.notebook import notebook
    """Runs one notebook specified"""    
    notebook.init_notebook_run(outfile_root)

    filename = sqlite_util.ordinal_to_list_item(current_scene_db, args.notebook)[1]
    notebook = notebook.Notebook(filename, library_root)
    display.display_run_notebook_start(notebook.name)
    local_copy = execute(current_scene_db, notebook)

    if args.html == "html":
        html_outputfile = f"{local_copy.split('.')[0]}.html"
        open_notebook.display_as_html(local_copy, html_outputfile)
    else:
        display.display_run_notebook(local_copy)


    timestamp = datetime.today().strftime("%Y-%m-%d %H:%M.%S")
    sqlite_util.add_to_scene_history(current_scene_db, timestamp, notebook.name, notebook.library_name)
    telemetry.send(root, local_copy, current_scene_db)


def execute(db_file, notebook):
    from src.mtool.cli import display
    """Handles papermill execution for notebook"""
    local_copy = get_outputname(notebook)
    if (notebook._hasParameters): 
        injects = pull_params(db_file, notebook._environmentVars)
        try:
            papermill.execute_notebook(notebook.getpath(), local_copy, injects)
        except Exception as e:
            print("PAPERMILL ERROR")
            print(e)
    else:
        display.no_tagged_cell_warning()
        try:
            papermill.execute_notebook(notebook.getpath(), local_copy)
        except Exception as e:
            print("PAPERMILL ERROR")
            print(e)
    
    #need local output -- temp? or just send it directly to HDFS
    return local_copy

def pull_params(db_file, environmentVars):
    """Returns a dictionary of all overridden parameters for notebook"""
    injects = {}
    for var in environmentVars:
        value = sqlite_util.get_env(db_file, var)
        if value != None:
            value = value[0] # want just the value, currently a tuple
            injects[var] = value
    return injects

def get_outputname(notebook):
    """Returns name of output file for notebook"""
    appdata = os.path.expandvars("%APPDATA%")
    output_folder = os.path.join(appdata, "mtool", "output")

    timestamp = datetime.today().strftime("%Y%m%d-%H%M%S")
    filename = f"{timestamp}-{notebook.library_name}-{notebook.name}"
    
    outputname = os.path.join(output_folder, filename)
    return outputname
