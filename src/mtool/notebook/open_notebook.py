"""
This file opens a notebook in Azure Data Studio.
"""

def open_notebook(args, current_scene_db, library_db, ads_location):
    """Opens a notebook, by getting the filename and then opening from the ads binary location"""
    import subprocess
    from src.mtool.util.sqlite import sqlite_notebook
    from src.mtool.notebook import notebook

    name = args.notebook
    
    tmp_name = notebook.get_notebook_by_ordinal(current_scene_db, name)
    if tmp_name != None:
        name = tmp_name
    notebook_data = sqlite_notebook.get_notebook(library_db, name)

    notebook_filename = notebook_data[0]
    if args.html == "html":
        display_as_html(notebook_filename)
    else:
        subprocess.Popen([ads_location, notebook_filename])


def display_as_html(filename, html_outputfile = None):
    """opens the file as html in the web browser"""
    import nbconvert
    import webbrowser

    output = nbconvert.exporters.export(nbconvert.HTMLExporter(), filename)[0]
    if html_outputfile == None:
        import tempfile
        # create temporary file
        temp = tempfile.NamedTemporaryFile(mode="w+t", suffix=".html", delete=False)
        temp.write(output)
        temp.seek(0)
        webbrowser.open(temp.name)
    
    else:
        with open(html_outputfile, 'w+') as f:
            f.write(output)
        webbrowser.open(html_outputfile)
