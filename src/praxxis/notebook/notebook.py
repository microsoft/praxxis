"""
This file contains the Notebook class, with methods for loading in a .ipynb
file and checking its parameterization information.
"""


def get_notebook(current_scene_db, library_db, name):
    """gets a notebook path from name and library name"""
    from src.praxxis.notebook import notebook
    from src.praxxis.util import error
    from src.praxxis.sqlite import sqlite_notebook

    tmp_name = notebook.get_notebook_by_ordinal(current_scene_db, name)[0]

    if tmp_name is not None:
        name = tmp_name

    notebook_data = sqlite_notebook.get_notebook(library_db, name)

    if not len(notebook_data) == 1:
        notebook_data = [notebook.handle_duplicate_notebook(library_db, notebook_data, name)]

    return notebook_data[0]


def get_notebook_by_ordinal(current_scene_db, name):
    """gets notebook by ordinal using the sqlite history db"""
    from src.praxxis.sqlite import sqlite_notebook
    from src.praxxis.util import error

    if str(name).isdigit():
        try:
            name = sqlite_notebook.get_notebook_by_ord(current_scene_db, name)
        except error.NotebookNotFoundError as e:
            raise e
    else:
        library = sqlite_notebook.get_notebook_library(current_scene_db, name)
        name = (name, library)
    return (name)


def get_output_from_filename(filename):
    """gets only cell outputs from filename"""
    import json

    linelist = []
    with open(filename) as f:
        info = json.load(f)
        cells = info["cells"]
        for cell in cells:
            if (cell["cell_type"] == "code"):
                if (len(cell["outputs"]) != 0):
                    linelist += (cell["outputs"][0]["text"])

        f.close()

    return ''.join(linelist)


def handle_duplicate_notebook(library_db, notebook_data, name):
    """prompts user to resolve duplicate notebook problem"""
    from src.praxxis.display import display_error
    from src.praxxis.library import list_library
    from src.praxxis.library import library
    from src.praxxis.sqlite import sqlite_notebook
    from src.praxxis.sqlite import sqlite_library
    from src.praxxis.notebook import notebook
    from src.praxxis.display import display_notebook
    from src.praxxis.util import error

    library_list = []
    for element in notebook_data:
        library_list.append(element[2])

    display_error.duplicate_notebook_error(name, library_list)
    selection = display_notebook.get_notebook_selection()

    if selection.isdigit():
        if int(selection) <= len(library_list):
            selection = library_list[int(selection) - 1]
        else:
            raise error.LibraryNotFoundError(selection)
    else:
        sqlite_library.check_library_exists(library_db, selection)
    return sqlite_notebook.get_notebook(library_db, name, selection)[0]


class Notebook:
    """this is the notebook class, which is an instance of a notebook"""

    def __init__(self, notebook_data):
        """creates a notebook as set of parameters, path, and library name"""
        from src.praxxis.display import display_error
        import os

        # TODO: add support for reading from a URL
        self.name = notebook_data[1]
        notebook_path = notebook_data[0]

        self._hasParameters = False
        self._parameters = []
        self._path = os.path.join(notebook_path)
        self.library_name = notebook_data[2]

        try:
            f = open(self._path, encoding='utf-8')
            self.extract_params(f)
            f.close()
        except(FileNotFoundError):
            print(display_error.notebook_not_found_error(self.name))

    def getpath(self):
        """returns the path of the notebook"""
        return self._path

    def extract_params(self, openFile):
        """extracts the parameters from the file"""
        import ijson
        objects = ijson.items(openFile, 'cells.item')
        code_cells = (o for o in objects if o['cell_type'] == 'code')
        for cell in code_cells:
            metadata = cell.get("metadata")
            if metadata and "parameters" in metadata.get("tags"):
                self._hasParameters = True
                self.extract_from_cell(cell.get("source"))
                return

    def extract_from_cell(self, source):
        """extracts the parameters"""
        if (isinstance(source, list)):
            lines = source
        else:
            lines = source.splitlines()
        for line in lines:
            if "=" in line and not line.startswith("#"):
                parameter = line.split("=")
                name = parameter[0].strip()
                value = parameter[1].split("#")[0].strip()
                if value == "\"\"":
                    value = None
                self._parameters.append([name, value])
