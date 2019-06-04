"""
This file searches the notebooks for a search term. 

Dependencies within mtool: mtool/mtool.py
"""
import os
import sys

# Include the mtool subfolder folder
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), "mtool"))

import mtool

m = mtool.MTool(sys.argv)

search_term = m.args.search_term

counter = 0
items = []

def filter(filename):
    """Filters out notebooks that do not meet search term"""
    global counter
    global items
    global search_term

    notebook = m.notebook(filename)

    if (notebook.name.lower().find(search_term)) > -1:
        counter += 1
        m.log.info(f"\t{str(counter)}.\t{notebook.name} ({notebook.library_name})")
        items.append([counter, notebook.name, notebook.library_name])

m.log.section("Search notebook names for", search_term)
m.for_each_notebook(filter)
m.write_list(items)