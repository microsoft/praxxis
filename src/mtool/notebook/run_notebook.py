"""
This file runs a notebook. Results are either printed to the console or 
opened as an html output in the web browser, depending on user input.

Dependencies within mtool: log.py, notebook.py, scene.py, open_notebook.py,
    telemetry.py
"""

import os
import sys
import webbrowser
from datetime import datetime

from src.mtool.util.log import Log
from src.mtool.notebook.notebook import Notebook
from src.mtool.scene.scene import Scene
from src.mtool.notebook import open_notebook 
from src.mtool.util import telemetry

import papermill

def run_notebook(args):
    """Runs one notebook specified"""
    run(Scene.ordinal_to_list_item(args.notebook))

def execute(notebook):
    """Handles papermill execution for notebook"""
    local_copy = get_outputname(notebook)
    if (notebook._hasParameters):
        injects = pull_params(notebook)
        papermill.execute_notebook(notebook.path, local_copy, injects)
    else:
        print("Warning: no tagged cell located. No parameters will be " +
            "injected for this notebook.")
        papermill.execute_notebook(notebook.getpath(), local_copy)
    
    #need local output -- temp? or just send it directly to HDFS
    # need to pull params from toml and send to papermill as dict
    
    return local_copy

def pull_params(environmentVars):
    """Returns a dictionary of all overridden parameters for notebook"""
    return {}

def get_outputname(notebook):
    """Returns name of output file for notebook"""
    appdata = os.path.expandvars("%APPDATA%")
    output_folder = os.path.join(appdata, "mtool", "output")

    timestamp = datetime.today().strftime("%Y%m%d-%H%M%S")
    filename = f"{timestamp}-{notebook.library_name}-{notebook.name}"
    
    outputname = os.path.join(output_folder, filename)
    return outputname

def run(filename):
    """Run a notebook, given a filename.

    Keyword arguments:
    filename -- the name of a notebook to run
    """
    
    notebook = Notebook(filename)
    log = Log()


    log.header("Running")
    log.indent_no_new_line("{0}... ".format(notebook.name))

    local_copy = execute(notebook)

    # TODO: html flag
    if False:
        html_outputfile = f"{local_copy.split('.')[0]}.html"
        log.complete()

        log.header("View HTML output from notebook runs here")
        log.indent("%APPDATA%/mtool/output")
        log.header("Launching result file in web browser")
        log.indent(html_outputfile)
        open_notebook.display_as_html(local_copy, html_outputfile)
    else:
        log.info("")
        log.header("Notebook output")
        open_notebook.display_to_console(local_copy)

    send_telemetry(local_copy)

def send_telemetry(local_copy):
    """Sends telemetry to HDFS"""
    basedir = os.path.expandvars("%APPDATA%/mtool")
    with open(os.path.join(basedir, "id.json")) as infile:
        id = infile.read()
    infile.close()
    with open(os.path.join(basedir, "scene", "current_scene.json")) as infile:
        curr_scene = infile.read()
    infile.close()
    with open(os.path.join(basedir, "scene", curr_scene, "id.json")) as infile:
        scene_id = infile.read()
    infile.close()

    telemetry.send(id, scene_id, local_copy)