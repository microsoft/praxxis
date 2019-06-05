"""
This file implements the json operations for working with files.

Dependencies within mtool: mtool/mtool.py
"""
import json

def load_json(filename):
    """Load a file as a python object"""
    with open(filename, encoding="utf8") as json_file:
        return json.load(json_file)

def save_json(filename, contents):
    """Dump a file as a stream to the outfile"""
    with open(filename, 'w', encoding="utf8") as outfile:
        json.dump(contents, outfile, indent=4)