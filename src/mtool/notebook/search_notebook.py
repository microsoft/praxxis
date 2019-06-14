import os

from src.mtool.notebook.notebook import Notebook
from src.mtool.util import sqlite_util
from src.mtool.cli import display


def search_notebook(args, library_db):
    search_term = args.term

    notebooks = sqlite_util.list_notebooks(library_db, 0, 100)

    display.display_search(search_term, filter(notebooks, search_term))
   

def filter(notebook_filenames, search_term):
    results = []
    
    for i in range(len(notebook_filenames)):
        notebook = Notebook(notebook_filenames[i][1])
        if (notebook.name.lower().find(search_term)) > -1:
            results.append([notebook.name, notebook.library_name])

    return results 

