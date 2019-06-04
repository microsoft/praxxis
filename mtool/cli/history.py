import os
import sys
from mtool.cli import mtool

counter = 0
items = []
uniquify = False
m = None

def history(args):
    global m
    m = mtool.MTool(args)

    m.log.header("History for scene", m.current_scene)

    m.for_each_notebook_in_scene_history(uniquify, display)
    m.write_list(items)

def display(notebook_name, library_name):
    global counter
    global items

    counter += 1
    m.log.indent("{0}. {1} ({2})".format(str(counter), notebook_name, library_name))
    items.append([counter, notebook_name, library_name])



