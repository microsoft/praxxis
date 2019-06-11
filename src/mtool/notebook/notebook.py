"""
"""

import json
import ijson
import os
import papermill
import time
import pypandoc


#TODO: refactor for readability / pythonic nature
class Notebook:
    # TODO: only works on Windows, is kinda ugly :(
    _library_loc = "%APPDATA%\\mtool\\library"
    _output_loc  = "%APPDATA%\\mtool\\output"

    def __init__(self, path, libary_space = _library_loc):
        #TODO: add support for reading from a URL
        self._output_loc  = os.path.join(os.getenv('APPDATA'),"mtool","output")

        self._hasParameters = False
        self._environmentVars = []

        self._path = os.path.join(os.path.expandvars(self._library_loc), path)
        split = os.path.split(path)
        self.name = split[-1]
        self.library_name = os.path.split(split[0])[-1]
        try:
            f = open(self._path)
            self.extract_params(f)
        except(FileNotFoundError):
            print("Invalid notebook name entered.")

    def extract_params(self, openFile):
        objects = ijson.items(openFile, 'cells.item')
        code_cells = (o for o in objects if o['cell_type'] == 'code')
        for cell in code_cells:
            metadata = cell.get("metadata")
            if metadata and "parameters" in metadata.get("tags"):
                self._hasParameters = True
                self.extract_envVars(cell.get("source"))
                return
    
    def convert_to_html(self, local_copy, html_outputfile):
        return pypandoc.convert_file(self._path, 'html')
    
    
    def display_to_console(self):
        return pypandoc.convert_file(self._path, 'asciidoc')
       

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
        local_copy = os.path.join(os.path.expandvars(self._output_loc), "20190607" + str(time.time()) + self.name.split(".")[0] + "-"  + ".ipynb")
        papermill.execute_notebook(self._path, local_copy)
        return local_copy

    def pull_params(self):
        
        return


    @staticmethod
    def for_each_notebook_in_library(library_path, fn):
        for item in os.listdir():
            if(item.endswith(".ipynb")):
                fn(os.path.join(library_path, item))


