import sys
import os

from mtool.cli import mtool

m = None
counter = 0
items = []
display_format_string = "\t{0}.\t{1} ({2})"


def list_notebook(args):
    global m
    m = mtool.MTool(args)
    m.log.section("List notebooks")

    if (m.list_exist):
        for item in m.get_list:
            m.log.info(display_format_string.format(str(item[0]), item[1], item[2]))
    else:
        m.for_each_notebook(display)
        m.write_list(items)


def display(filename):
    global counter
    global items
    global display_format_string
    counter += 1

    notebook = m.notebook(filename)

    m.log.info(display_format_string.format(str(counter), notebook.name, notebook.library_name))
    items.append([counter, notebook.name, notebook.library_name])

