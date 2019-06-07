"""
"""

import json
import ijson
import os
import papermill
import time

#TODO: refactor for readability / pythonic nature
class Notebook:
    _path = ""
    _hasParameters = False
    _environmentVars = []
    name = ""
    library_name = ""
    
    def __init__(self, path):
        #TODO: add support for reading from a URL
        curr = os.getcwd()
        curr = os.path.split(curr)[0]
        curr = os.path.join(curr, "library")
        self._path = os.path.join(curr, path)
        split = os.path.split(path)
        self.name = split[-1]
        self.library_name = os.path.split(split[0])[-1]
        try:
            f = open(path)
            self.extract_params(f)
        except(FileNotFoundError):
            # BUG: notebooks being run aren't opening correctly
            print()
            #print("Invalid notebook name entered.")

    def extract_params(self, openFile):
        objects = ijson.items(openFile, 'cells.item')
        code_cells = (o for o in objects if o['cell_type'] == 'code')
        for cell in code_cells:
            metadata = cell.get("metadata")
            if metadata and "parameters" in metadata.get("tags"):
                self._hasParameters = True
                self.extract_envVars(cell.get("source"))
                return
    
    def extract_envVars(self, source):
        for line in source:
            if "=" in line and not line.startswith("#"):
                self._environmentVars.append(line.split("=")[0].strip())

    def execute(self):
        if not(self._hasParameters):
            print("Warning: no tagged cell located. No parameters will be " +
                "injected for this notebook.")
        #need local output -- temp? or just send it directly to HDFS
        # need to pull params from toml and send to papermill as dict
        local_copy = os.path.join(os.path.split(self._path)[0], "..", "..", "..", "output", self.name.split(".")[0] + "-" + str(time.time()) + ".ipynb")
        papermill.execute_notebook(self._path, local_copy)
        return local_copy

    def pull_params(self):
        return

    @staticmethod
    def for_each_notebook(root, fn):
        """Calls fn on every notebook in directory"""
        os.chdir(root)
        currDir = os.listdir()
        subDirs = []
        for item in currDir:
            if os.path.isfile(item) and item.endswith(".ipynb"):
                path = os.getcwd()
                nb = Notebook(os.path.join(path, item))
                fn(nb)
            elif os.path.isdir(item):
                subDirs.append(item)
        while subDirs != []:
            thisSubDir = subDirs.pop()
            Notebook.for_each_notebook(os.path.join(root, thisSubDir), fn)

    @staticmethod
    def for_each_notebook_in_library(library_path, fn):
        for item in os.listdir():
            if(item.endswith(".ipynb")):
                fn(os.path.join(library_path, item))


