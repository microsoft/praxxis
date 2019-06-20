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

    notebook_filename = notebook_data[0]
    subprocess.Popen([ads_location, notebook_filename])


def display_as_html(filename, html_outputfile):
    """opens the file as html in the web browser"""
    import nbconvert
    import webbrowser

    output = nbconvert.exporters.export(nbconvert.HTMLExporter(), filename)[0]
    with open(html_outputfile, 'w+') as f:
        f.write(output)

    webbrowser.open(html_outputfile)
