"""
This file opens a notebook in ADS, HTML, jupyter or vim
"""

def open_notebook(args, current_scene_db, library_db, ads_location, editor="vim", test = False):
    """Opens a notebook, by getting the filename and then opening from the ads binary location"""
    import subprocess
    from src.praxxis.sqlite import sqlite_notebook
    from src.praxxis.notebook import notebook
    from src.praxxis.util import error

    name = args.notebook
    
    notebook_data = notebook.get_notebook(current_scene_db, library_db, name)
    
    notebook_filename = notebook_data[0]
    if args.viewer == "html":
        display_as_html(notebook_filename)
    elif args.viewer == "jupyter":
        open_jupyter(notebook_filename, test)
    elif args.viewer == "ads":
        try:
            subprocess.Popen([ads_location, notebook_filename])
        except Exception:
            raise error.ADSNotFoundError(ads_location)
    else:
        open_editor(notebook_filename, editor)
    return 0


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


def open_jupyter(filepath, test):
    import subprocess
    import os
    import sys    

    process = subprocess.Popen([sys.executable, os.path.join(os.path.dirname(__file__),  ".." , "util", "open_jupyter.py"), filepath], stdout=subprocess.PIPE)

    if test:
        return

    try:
        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                print (output.strip())
        rc = process.poll()
        return rc
    except KeyboardInterrupt:
        sys.exit(0)


def open_editor(notebook_filename, editor):
    import sys, tempfile, os
    from subprocess import call
    from src.praxxis.display import display_error
    from src.praxxis.util import error
    EDITOR = os.environ.get('EDITOR', editor)

    try:
        call([EDITOR, notebook_filename])
    except FileNotFoundError:
        raise error.EditorNotFoundError(editor)
