from src.mtool import app
import sys
import pytest


def test_help_formatter():
    import argparse 
    from src.mtool.app import helpFormatter
    from tests.src.mtool.util import dummy_object

    notebook = dummy_object.make_dummy_action("command", "", "run notebook")
    scene = dummy_object.make_dummy_action("command", "", "new scene")
    parameter = dummy_object.make_dummy_action("command", "", "set parameter variable for current scene")
    library = dummy_object.make_dummy_action("command", "", "install library of notebooks to mtool")

    formatter = helpFormatter(argparse.RawDescriptionHelpFormatter)
    data = formatter._format_action(notebook)
    assert data.split('\n')[0] == "Notebooks: "
    data = formatter._format_action(scene)
    assert data.split('\n')[0] == "Scene: "
    data = formatter._format_action(parameter)
    assert data.split('\n')[0] == "parameter: "
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



def test_view_params():
    view_params(['v', 'test'])
    view_params(['viewparams', 'test'])


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


def test_set_param():
    set_param(['setparam', 'test', 'test'])
    set_param(['se', 'test', 'test'])


def test_search_param():
    search_param(['searchparam', 'test'])
    search_param(['sv', 'test'])


def test_delete_param():
    delete_param(['deleteparam', 'test'])
    delete_param(['de', 'test'])

def test_list_param():
    list_param(['listparam'])
    list_param(['le'])


def test_view_library_param():
    view_library_param(['viewlibparam', 'test'])
    view_library_param(['vl', 'test'])


def test_pull_notebook_param():
    pull_notebook_param(['pullparam', 'test'])
    pull_notebook_param(['p', 'test'])

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


def test_new_ruleset():
    new_ruleset(['newruleset', 'test'])
    new_ruleset(['nr', 'test'])


def test_remove_ruleset():
    remove_ruleset(['removeruleset', 'test'])
    remove_ruleset(['rr', 'test'])


def test_list_rulesets():
    list_rulesets(['listrulesets'])
    list_rulesets(['lr'])


def test_import_ruleset():
    import_ruleset(['importruleset', 'test'])
    import_ruleset(['ir', 'test'])


def test_view_ruleset():
    view_ruleset(['viewruleset', 'test'])
    view_ruleset(['vr', 'test'])


def test_edit_ruleset():
    edit_ruleset(['editruleset', 'test', 'a'])
    edit_ruleset(['editruleset', 'test', 'd'])


def test_activate_ruleset():
    activate_ruleset(['activateruleset', 'test'])
    activate_ruleset(['ar', 'test'])


def test_deactivate_ruleset():
    deactivate_ruleset(['deactivateruleset', 'test'])
    deactivate_ruleset(['dr', 'test'])


def run(command):

    namespace = app.main(command)
    assert namespace.command == 'r' or namespace.command == "run"
    assert namespace.notebook == "test"
    if "html" in command:
        assert namespace.html == "html"
    

def view_params(command):
    namespace = app.main(command)
    
    assert namespace.command == 'v' or namespace.command == 'viewparams'
    assert namespace.notebook == 'test'


def open_notebook(command):
    namespace = app.main(command)
    assert namespace.command == 'o' or namespace.command == "open"
    assert namespace.notebook == "test"
    if "html" in command:
        assert namespace.viewer == "html"


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


def set_param(command):
    """
    tests if the set param command is running properly 
    """
    namespace = app.main(command)
    assert namespace.command == 'se' or namespace.command == "setparam"
    assert namespace.name == "test"
    assert namespace.value == "test"


def search_param(command):
    """
    tests if the set param command is running properly 
    """
    namespace = app.main(command)
    assert namespace.command == 'sv' or namespace.command == "searchparam"
    assert namespace.term == "test"


def delete_param(command):
    """
    tests if the delete param command is running properly 
    """
    namespace = app.main(command)
    assert namespace.command == 'de' or namespace.command == "deleteparam"
    assert namespace.name == "test"


def list_param(command):
    """
    tests if the list param command is running properly 
    """
    namespace = app.main(command)
    assert namespace.command == 'le' or namespace.command == "listparam"


def view_library_param(command):
    """
    tests if the view library param command is running properly 
    """
    namespace = app.main(command)
    assert namespace.command == 'vl' or namespace.command == "viewlibparam"
    assert namespace.name == "test"


def pull_notebook_param(command):
    namespace = app.main(command)
    assert namespace.command == 'p' or namespace.command == "pullparam"
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


def new_ruleset(command):
    """
    tests if the new ruleset command is running properly
    """
    namespace = app.main(command)
    assert namespace.command == 'nr' or namespace.command == "newruleset"
    assert namespace.name == "test"


def remove_ruleset(command):
    """
    tests if the remove ruleset command is running properly
    """
    namespace = app.main(command)
    assert namespace.command == 'rr' or namespace.command == "removeruleset"
    assert namespace.name == "test"


def list_rulesets(command):
    """
    tests if the list rulesets command is running properly
    """
    namespace = app.main(command)
    assert namespace.command == 'lr' or namespace.command == "listrulesets"


def import_ruleset(command):
    """
    tests if the import ruleset command is running properly
    """
    namespace = app.main(command)
    assert namespace.command == 'ir' or namespace.command == "importruleset"
    assert namespace.path == "test"


def view_ruleset(command):
    """
    tests if the view ruleset command is running properly
    """
    namespace = app.main(command)
    assert namespace.command == 'vr' or namespace.command == "viewruleset"
    assert namespace.name == "test"

def edit_ruleset(command):
    """
    tests if the edit ruleset command is running properly
    """
    namespace = app.main(command)
    assert namespace.command == 'er' or namespace.command == "editruleset"
    assert namespace.name == "test"
    assert namespace.action in ['a','d']

def activate_ruleset(command):
    """
    tests if the activate ruleset command is running properly
    """
    namespace = app.main(command)
    assert namespace.command == 'ar' or namespace.command == "activateruleset"
    assert namespace.name == "test"

def deactivate_ruleset(command):
    """
    tests if the deactivate ruleset command is running properly
    """
    namespace = app.main(command)
    assert namespace.command == 'dr' or namespace.command == "deactivateruleset"
    assert namespace.name == "test"

def import_model(command):
    """
    tests if the import model command is running properly
    """
    namespace = app.main(command)
    assert namespace.command == 'im' or namespace.command == "importmodel"
    assert namespace.modelpath == "test1"
    assert namespace.convertpath == "test2"

def update_model(command):
    """
    tests if the update model command is running properly
    """
    namespace = app.main(command)
    assert namespace.command == 'um' or namespace.command == "updatemodel"
    

def test_start(setup, add_test_library, scene_root, library_root, library_db, current_scene_db, start, stop):
    from src.mtool import app
    from src.mtool.sqlite import sqlite_scene
    from src.mtool.notebook import run_notebook
    from src.mtool.util import error
    import sys
    
    assert app.start(["", "2"], True).__class__ == run_notebook.run_notebook.__class__ 

    sys.argv = ["", "r", "1"]
    assert app.start(test=True).__class__ == run_notebook.run_notebook.__class__ 

    try:
        app.start(["", "99"], test=True)
    except error.NotebookNotFoundError:
        assert 1

    try:
        sys.argv = ["", "r", "99"] 
    except error.NotebookNotFoundError:
        assert 1

    sys.argv = [""]
    assert app.start(test=True).__class__ == run_notebook.run_notebook.__class__ 
    