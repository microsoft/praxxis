import os
import sys
from mtool.cli import mtool

m = mtool.MTool(sys.argv)

search_term = m.args.search_term

counter = 0
items = []

def filter(filename):
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