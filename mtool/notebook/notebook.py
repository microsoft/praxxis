"""
"""

import json
import ijson
import os

#TODO: refactor for readability / pythonic nature
class Notebook:
    _hasParameters = False
    _environmentVars = []
    
    def __init__(self, path):
        #TODO: add support for reading from a URL
        print(path)
        try:
            f = open(path)
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
    
    def extract_envVars(self, source):
        print(source)
        for line in source:
            if "=" in line and not line.startswith("#"):
                self._environmentVars.append(line.split("=")[0].strip())

    def run(self):
        print("papermill here")

