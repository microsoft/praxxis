"""
This file opens a notebook in Azure Data Studio.
"""

def open_notebook(args, current_scene_db, ads_location):
    """Opens a notebook, by getting the filename and then opening from the ads binary location"""
    import subprocess
    from src.mtool.util import sqlite_util
    
    notebook_filename = sqlite_util.ordinal_to_list_item(current_scene_db, args.notebook)[1]
    subprocess.Popen([ads_location, notebook_filename])


def display_as_html(filename, html_outputfile):
    """opens the file as html in the web browser"""
    import pypandoc
    import webbrowser

    pypandoc.convert_file(filename, 'html', outputfile=html_outputfile)
    webbrowser.open(html_outputfile)
