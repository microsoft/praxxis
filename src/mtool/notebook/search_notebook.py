import os
import sys

from src.mtool.cli import mtool

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
    m.write_list(items)


def filter(filename):
    global counter
    global items
    global search_term

