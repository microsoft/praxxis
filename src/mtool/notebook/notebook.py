"""
This file contains the Notebook class, with methods for loading in a .ipynb
file and checking its parameterization information.

Dependencies within mtool: NONE
"""

import json
import os
import time

import ijson


#TODO: works, but needs cleanup
#TODO: remove all unused parts from yanking 
class Notebook:
    # TODO: only works on Windows, is kinda ugly :(
    _library_loc = "%APPDATA%\\mtool\\library"

    def __init__(self, path, libary_space = _library_loc):
        #TODO: add support for reading from a URL

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
            # TODO: prints to console
            print("Invalid notebook name entered.")

    
    def getpath(self):
        return self._path

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


