from src.mtool import app
import sys
import pytest


def test_help_formatter():
    import argparse 
    from src.mtool.app import helpFormatter
    from tests.src.mtool.util import dummy_object

    notebook = dummy_object.make_dummy_action("command", "", "run notebook")
    scene = dummy_object.make_dummy_action("command", "", "new scene")
    environment = dummy_object.make_dummy_action("command", "", "set environment variable for current scene")
    library = dummy_object.make_dummy_action("command", "", "install library of notebooks to mtool")

    formatter = helpFormatter(argparse.RawDescriptionHelpFormatter)
    data = formatter._format_action(notebook)
    assert data.split('\n')[0] == "Notebooks: "
    data = formatter._format_action(scene)
    assert data.split('\n')[0] == "Scene: "
    data = formatter._format_action(environment)
    assert data.split('\n')[0] == "Environment: "
    data = formatter._format_action(library)
    assert data.split('\n')[0] == "Library: "

def test_0_args(library_db):
    """
    this tests the 0 args command.
    this should have no command, since the 0 args case gets handled manually
    """
    import argparse

    namespace = app.main([])
    assert namespace.__class__ == argparse.Namespace


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


def test_list_notebooks():
    list_notebooks(['list'])
    list_notebooks(['l'])


def test_history():
    history(['history'])
    history(['h'])


def test_next_notebook():
    next_notebook(['whatnext'])
    next_notebook(['n'])


def test_new_scene():
    new_scene(['newscene', 'test'])
    new_scene(['ns', 'test'])


def test_end_scene():
    end_scene(['endscene', 'test'])
    end_scene(['es', 'test'])
    end_scene(['endscene'])
    end_scene(['es'])


def test_change_scene():
    change_scene(['changescene', 'test'])
    change_scene(['cs', 'test'])


def test_resume_scene():
    resume_scene(['resumescene', 'test'])
    resume_scene(['rs', 'test'])


def test_delete_scene():
    delete_scene(['deletescene', 'test'])
    delete_scene(['ds', 'test'])
    delete_scene(['deletescene'])
    delete_scene(['ds'])


def test_list_scene():
    list_scene(['listscenes'])
    list_scene(['ls'])


def test_set_env():
    set_env(['setenv', 'test', 'test'])
    set_env(['se', 'test', 'test'])


def test_search_env():
    search_env(['searchenv', 'test'])
    search_env(['sv', 'test'])


def test_delete_env():
    delete_env(['deleteenv', 'test'])
    delete_env(['de', 'test'])

def test_list_env():
    list_env(['listenv'])
    list_env(['le'])


def test_view_library_env():
    view_library_env(['viewlibenv', 'test'])
    view_library_env(['vl', 'test'])


def test_pull_notebook_env():
    pull_notebook_env(['pullenv', 'test'])
    pull_notebook_env(['p', 'test'])

def test_add_library():
    add_library(['addlibrary', 'test'])
    add_library(['al', 'test'])


def test_remove_library():
    remove_library(['removelibrary', 'test'])
    remove_library(['rl', 'test'])


def test_list_library():
    list_library(['listlibrary'])
    list_library(['ll'])


def test_sync_library():
    sync_library(['synclibrary', 'test'])
    sync_library(['sl', 'test'])
    sync_library(['synclibrary'])
    sync_library(['sl'])


def test_update_settings():
    update_settings(['updatesettings'])
    update_settings(['u'])


def run(command):

    namespace = app.main(command)
    assert namespace.command == 'r' or namespace.command == "run"
    assert namespace.notebook == "test"
    if "html" in command:
        assert namespace.html == "html"
    

def view_envs(command):
    namespace = app.main(command)
    
    assert namespace.command == 'v' or namespace.command == 'viewenvs'
    assert namespace.notebook == 'test'


def open_notebook(command):
    namespace = app.main(command)
    assert namespace.command == 'o' or namespace.command == "open"
    assert namespace.notebook == "test"
    if "html" in command:
        assert namespace.environment == "html"


def search_notebook(command):
    namespace = app.main(command)
    assert namespace.command == 's' or namespace.command == "search"
    assert namespace.term == "test"


def list_notebooks(command):
    """
    tests if the list command is running properly 
    """
    namespace = app.main(command)
    assert namespace.command == 'l' or namespace.command == "list"


def history(command):
    """
    tests if the history command is running properly 
    """
    namespace = app.main(command)
    assert namespace.command == 'h' or namespace.command == "history"


def next_notebook(command):
    """
    tests if the notebook command is running properly 
    """
    namespace = app.main(command)
    assert namespace.command == 'n' or namespace.command == "whatnext"


def new_scene(command):
    """
    tests if the new scene command is running properly 
    """
    namespace = app.main(command)
    assert namespace.command == 'ns' or namespace.command == "newscene"
    assert namespace.name == "test"


def end_scene(command):
    """
    tests if the end scene command is running properly 
    """
    namespace = app.main(command)
    assert namespace.command == 'es' or namespace.command == "endscene"
    if "test" in command:
        assert namespace.name == "test"


def change_scene(command):
    """
    tests if the change scene command is running properly 
    """
    namespace = app.main(command)
    assert namespace.command == 'cs' or namespace.command == "changescene"
    assert namespace.name == "test"


def resume_scene(command):
    """
    tests if the resume scene command is running properly 
    """
    namespace = app.main(command)
    assert namespace.command == 'rs' or namespace.command == "resumescene"
    assert namespace.name == "test"


def delete_scene(command):
    """
    tests if the delete scene command is running properly 
    """
    namespace = app.main(command)
    assert namespace.command == 'ds' or namespace.command == "deletescene"
    if "test" in command:
        assert namespace.name == "test"


def list_scene(command):
    """
    tests if the list scene command is running properly 
    """
    namespace = app.main(command)
    assert namespace.command == 'ls' or namespace.command == "listscenes"


def set_env(command):
    """
    tests if the set env command is running properly 
    """
    namespace = app.main(command)
    assert namespace.command == 'se' or namespace.command == "setenv"
    assert namespace.name == "test"
    assert namespace.value == "test"


def search_env(command):
    """
    tests if the set env command is running properly 
    """
    namespace = app.main(command)
    assert namespace.command == 'sv' or namespace.command == "searchenv"
    assert namespace.term == "test"


def delete_env(command):
    """
    tests if the delete env command is running properly 
    """
    namespace = app.main(command)
    assert namespace.command == 'de' or namespace.command == "deleteenv"
    assert namespace.name == "test"


def list_env(command):
    """
    tests if the list env command is running properly 
    """
    namespace = app.main(command)
    assert namespace.command == 'le' or namespace.command == "listenv"


def view_library_env(command):
    """
    tests if the view library env command is running properly 
    """
    namespace = app.main(command)
    assert namespace.command == 'vl' or namespace.command == "viewlibenv"
    assert namespace.name == "test"


def pull_notebook_env(command):
    namespace = app.main(command)
    assert namespace.command == 'p' or namespace.command == "pullenv"
    assert namespace.notebook == "test"


def add_library(command):
    """
    tests if the add library command is running properly 
    """
    from src.mtool.library import list_library

    namespace = app.main(command)
    assert namespace.command == 'al' or namespace.command == "addlibrary"
    assert namespace.path == "test"


def remove_library(command):
    """
    tests if the remove library command is running properly 
    """
    namespace = app.main(command)
    assert namespace.command == 'rl' or namespace.command == "removelibrary"
    assert namespace.name == "test"


def list_library(command):
    """
    tests if the list library command is running properly 
    """
    namespace = app.main(command)
    assert namespace.command == 'll' or namespace.command == "listlibrary"


def sync_library(command):
    """
    tests if the sync library command is running properly 
    """
    namespace = app.main(command)
    assert namespace.command == 'sl' or namespace.command == "synclibrary"
    if "path" in command:
        assert namespace.path == "test"


def update_settings(command):
    """
    tests if the update setting command is running properly 
    """
    namespace = app.main(command)
    assert namespace.command == 'u' or namespace.command == "updatesettings"


def test_start(setup, add_test_library, scene_root, library_root, library_db, current_scene_db, start, stop):
    from src.mtool import app
    from src.mtool.util.sqlite import sqlite_scene
    from src.mtool.notebook import run_notebook
    from src.mtool.util import error
    import sys
    
    assert app.start(["", "2"], True).__class__ == run_notebook.run_notebook.__class__ 

    sys.argv = ["", "r", "1"]
    assert app.start(test=True).__class__ == run_notebook.run_notebook.__class__ 

    try:
        app.start(["", "99"])
    except error.NotebookNotFoundError:
        assert 1

    try:
        sys.argv = ["", "r", "99"]
    except error.NotebookNotFoundError:
        assert 1

    sys.argv = [""]
    assert app.start(test=True).__class__ == run_notebook.run_notebook.__class__ 
    