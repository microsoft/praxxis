"""
This file opens a notebook in Azure Data Studio.
"""

def open_notebook(args, current_scene_db, library_db, ads_location):
    """Opens a notebook, by getting the filename and then opening from the ads binary location"""
    import subprocess
    from src.mtool.util import sqlite_util
    from src.mtool.notebook import notebook

    name = args.notebook
    
    tmp_name = notebook.get_notebook_by_ordinal(current_scene_db, name)
    if tmp_name != None:
        name = tmp_name
    notebook_data = sqlite_util.get_notebook(library_db, name)

    notebook_filename = notebook_data[1]
    subprocess.Popen([ads_location, notebook_filename])


def display_as_html(filename, html_outputfile):
    """opens the file as html in the web browser"""
    from nbconvert import HTMLExporter
    import webbrowser

    #pypandoc.convert_file(filename, 'html', outputfile=html_outputfile)
    webbrowser.open(html_outputfile)
