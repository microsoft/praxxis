"""
This file runs a notebook. Results are either printed to the console or 
opened as an html output in the web browser, depending on user input.

Dependencies within mtool: mtool/mtool.py
"""

import os
import sys
import webbrowser
from mtool.cli import mtool

m = None

def run_notebook(args):
    """Runs one or more notebooks specified"""
    global m
    m = mtool.MTool(args)
    m.set_environment_overrides_for_scene()
    m.for_each_notebook_specified_on_command_line(run_notebook)


def run(filename):
    """Run a notebook.

    Keyword arguments:
    filename -- the name of a notebook to run
    Keyword exceptions:
    if notebook fails to execute correctly (raises error in running)
    """
   
    notebook = m.notebook(filename)
    log = m.log
    spinner = m.spinner

    local_copy = notebook.get_local_copy_filename('.ipynb')
    html_outputfile = notebook.get_local_copy_filename('.html')

    log.header("Running")
    log.indent_no_new_line("{0}... ".format(notebook.name))

    spinner.start()

    notebook.execute(local_copy, allow_errors=False)

    # BUGBUG: There appears to be a bug in jupyter nbconvert where you can't
    # save the results of a notebook if an error was raised in one of the cells!
    # 
    # This is frustrating, because it means we can't get any telemetry on notebooks
    # that partially completed!  We need to find a fix for this!
    #
    # Of course, we could pass in 'allow_errors' = True above, but we don't
    # want to do this (without the user expressly allowing us to) because we
    # might do something really bad, by running cells in a notebook that presume
    # the cells above have run successfully!
    #
    if not os.path.isfile(local_copy):
        raise Exception("\n\nNotebook execution raised an error, please 'm open' this notebook and execute the cells to view the error.")

    if m.show_notebook_in_web_browser:
        notebook.convert_to_html(local_copy, html_outputfile)

    spinner.stop()

    if not m.show_notebook_in_web_browser:
        log.info("")
        log.header("Notebook output")
        notebook.display_to_console(local_copy)
    else:
        log.complete()

        log.header("View HTML output from notebook runs here")
        log.indent("start", m.working_dir)
        log.header("Launching result file in web browser")
        log.indent(html_outputfile)

        webbrowser.open(html_outputfile)

    m.send_telemetry(local_copy)

