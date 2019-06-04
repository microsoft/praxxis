import os
import sys
from mtool.cli import mtool

m = None
counter = 0
items = []
search_term = None


def search_notebook(args):
    global m
    global search_term
    
    m = mtool.MTool(args)
    search_term = m.args.search_term
    m.log.section("Search notebook names for", search_term)
    m.for_each_notebook(filter)
    m.write_list(items)


def filter(filename):
    global counter
    global items
    global search_term

    notebook = m.notebook(filename)

    if (notebook.name.lower().find(search_term)) > -1:
        counter += 1
        m.log.info(f"\t{str(counter)}.\t{notebook.name} ({notebook.library_name})")
        items.append([counter, notebook.name, notebook.library_name])

