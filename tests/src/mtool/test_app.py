from src.mtool import app
import sys
import pytest

def test_0_args():
    """
    this tests the 0 args command.
    this should have no command, since the 0 args case gets handled manually
    """
    namespace = app.main([])
    assert namespace.command == None

#//TODO: finish commenting and writing tests for app.py

def test_run():
    run(['r', "test"])
    run(["run", "test"])
    run(["run", "test", "html"])

def test_view_envs():
    view_envs(['v', 'test'])
    view_envs(['viewenvs', 'test'])


def test_open_notebook():
    open_notebook(['o', 'test'])
    open_notebook(['open', 'test'])
    open_notebook(['open', 'test', 'html'])


def test_search_notebook():
    search_notebook(['s', 'test'])
    search_notebook(['search', 'test'])


def run(command):
    namespace = app.main(command)
    assert namespace.command == 'r' or namespace.command == "run"
    assert namespace.which == "run_notebook"
    assert namespace.notebook == "test"
    if "html" in command:
        assert namespace.html == "html"


def view_envs(command):
    namespace = app.main(command)
    assert namespace.command == 'v' or namespace.command == 'viewenvs'
    assert namespace.which == "view_notebook_env"
    assert namespace.notebook == 'test'


def open_notebook(command):
    namespace = app.main(command)
    assert namespace.command == 'o' or namespace.command == "open"
    assert namespace.which == "open_notebook"
    assert namespace.notebook == "test"
    if "html" in command:
        assert namespace.html == "html"

def search_notebook(command):
    namespace = app.main(command)
    assert namespace.command == 's' or namespace.command == "search"
    assert namespace.which == 'search_notebooks'
    assert namespace.term == "test"


def test_list():
    """
    tests if the list command is running properly 
    """
    namespace = app.main(['l'])
    assert namespace.command == 'l'
    assert namespace.which == "list_notebooks"
