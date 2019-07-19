"""
This file handles the argument parsing, and is the entry point of the app
"""

import argparse
import os
import sys
from colorama import init, Fore, Style
init(autoreset=True)

## these are the commands passed into cli.py
run_notebook_command = "run_notebook"
view_notebook_param_command="view_notebook_param"
list_notebooks_command="list_notebooks"
search_notebooks_command="search_notebooks"
open_notebook_command="open_notebook"
history_command="history"
next_notebook_command="next_notebook"
remove_notebook_command = "remove_notebook"
add_notebook_command = "add_notebook"

new_scene_command = "new_scene"
end_scene_command="end_scene"
change_scene_command="change_scene"
resume_scene_command="resume_scene"
delete_scene_command="delete_scene"
list_scene_command="list_scene"

add_library_command="add_library"
list_library_command="list_library"
remove_library_command="remove_library"
sync_library_command="sync_library"

set_param_command="set_param"
delete_param_command="delete_param"
list_param_command="list_param"
view_library_param_command="view_library_param"
pull_notebook_param_command = "pull_notebook_param"
pull_library_param_command = "pull_library_param"
search_param_command="search_param"

update_settings_command="update_settings"
new_ruleset_command="new_ruleset"
remove_ruleset_command="remove_ruleset"
list_rulesets_command="list_rulesets"
view_ruleset_command="view_ruleset"
edit_ruleset_command="edit_ruleset"
import_ruleset_command="import_ruleset"
activate_ruleset_command="activate_ruleset"
deactivate_ruleset_command="deactivate_ruleset"
import_model_command="import_model"
update_model_command="update_model"

## notebook help strings
run_notebook_help="run notebook"
run_notebook_notebook_help="notebook to run"
run_notebook_parameter_help="html flag for opening in web"
view_notebook_param_help="displays the parameters for the notebook"
view_notebook_param_notebook_help="the notebook to view parameter for"
open_notebook_help="open notebook in Azure Data Studio"
open_notebook_notebook_help="notebook to open"
open_notebook_parameter_help="open notebook in jupyter ads or html"
list_notebooks_help="list notebooks to run, by ordinal."
search_notebooks_help="search for notebooks matching search term"
search_notebooks_term_help ="search term for notebooks"
next_notebook_help="model based prediction of what to do next in the current scene"
remove_notebook_help = "remove notebook by name"
remove_notebook_name_help = "name of notebook to remove"
add_notebook_help = "add a notebook to mtool"
add_notebook_path_help = "the path of the notebook you want to load"
## scene help strings 
new_scene_help="new scene"
new_scene_name_help="name of new scene"
end_scene_help="end scene"
end_scene_name_help="name of scene to end"
change_scene_help="change scene"
change_scene_parameter_help="parameter for scene"
change_scene_name_help="name of scene to change to"
resume_scene_help="resume scene"
resume_scene_name_help="name of scene to resume"
delete_scene_help="delete scene"
delete_scene_name_help="name of scene to delete"
list_scene_help="list scenes"
## parameter help strings
set_param_help="set parameter variable for current scene"
set_param_name_help="name of the parameter variable to set"
set_param_value_help="value of the parameter variable to set"
delete_param_help="delete parameter variable for current scene"
delete_param_name_help="name of the parameter variable to delete"
search_param_help="search for parameter variable names"
search_param_term_help="search term for parameter variable"
list_param_help="list parameter variables"
view_library_param_help="list all parameters in a library of notebooks"
view_library_param_name_help="the name of the library you want to list for"
pull_notebook_param_help = "pull parameters out of a notebook into your current scene"
pull_notebook_param_name_help = "the name of the notebook to pull parameters from"
pull_library_param_help = "pull parameters out of a library into your current scene"
pull_library_param_name_help = "the name of the library to pull the parameters from"
## library help strings
add_library_help="install library of notebooks to mtool"
add_library_path_help="the path to the library you want to add"
remove_library_help="remove library of notebooks mtool"
remove_library_name_help="name of the library you want to remove"
list_libraries_help="list libraries currently installed"
sync_library_help="load libraries into mtool. Default loads from predefined library path"
sync_library_path_help="load library from a specific directory into mtool"
## misc help strings
history_help="history of what you've done in the current scene"
update_settings_help="update telemetry and security settings"
#prediction help strings
new_ruleset_help="create a ruleset for the rules engine"
new_ruleset_name_help="the name of the new ruleset to create"
new_ruleset_path_help="(optional) path to location to save ruleset at"
remove_ruleset_help="remove a ruleset from your machine"
remove_ruleset_name_help="the name of the ruleset to remove"
list_rulesets_help="list all rulesets available for the rules engine"
view_ruleset_help="view all rules in a ruleset"
view_ruleset_name_help="the name of the ruleset to view rules in"
edit_ruleset_help="make changes to a ruleset"
edit_ruleset_name_help="the name of the ruleset to edit"
edit_ruleset_action_help="'a' to add a rule, 'd' to delete a rule, 'm' to modify a rule"
import_ruleset_help="import a ruleset file from outside mtool"
import_ruleset_path_help="the path to the file to import"
activate_ruleset_help="activate ruleset(s) to use when making predictions"
activate_ruleset_name_help="name of the ruleset to activate"
deactivate_ruleset_name_help="name of the ruleset to deactivate"
deactivate_ruleset_help="deactivate ruleset(s) to keep them on your machine, but not use them in predictions"
import_model_help="import a model file and converter from outside mtool"
import_model_modelpath_help="the path to the model file"
import_model_converterpath_help="the path to the converter"
update_model_help="fetch newest version of model from storage pool"


mtool_ascii_art = r"""
               ▒▒ |                        ▒▒ |
▒▒▒▒▒▒\▒▒▒▒\ ▒▒▒▒▒▒\    ▒▒▒▒▒▒\   ▒▒▒▒▒▒\  ▒▒ |
▒▒  _▒▒  _▒▒\\_▒▒  _|  ▒▒  __▒▒\ ▒▒  __▒▒\ ▒▒ |
▒▒ / ▒▒ / ▒▒ | ▒▒ |    ▒▒ /  ▒▒ |▒▒ /  ▒▒ |▒▒ |
▒▒ | ▒▒ | ▒▒ | ▒▒ |▒▒\ ▒▒ |  ▒▒ |▒▒ |  ▒▒ |▒▒ |
▒▒ | ▒▒ | ▒▒ | \▒▒▒▒  |\▒▒▒▒▒▒  |\▒▒▒▒▒▒  |▒▒ |
\__| \__| \__|  \____/  \______/  \______/ \__|
"""

class helpFormatter (argparse.RawDescriptionHelpFormatter):
    def _format_action(self, action):
        import re
        if action.dest == "command":
            new_choices = []
            for choice in action.choices:
                if len(choice) <= 2:
                    new_choices.append(choice)
            action.choices = new_choices
        parts = super()._format_action(action)  
        if action.help == run_notebook_help:
            parts = f"""Notebooks: \n    [n]                 runs nth notebook in list\n{parts}"""
        elif action.help == new_scene_help:
            parts = f'Scene: \n{parts}'
        elif action.help == set_param_help:
            parts = f'parameter: \n{parts}'
        elif action.help == add_library_help:
            parts = f'Library: \n{parts}'
        elif action.help == new_ruleset_help:
            parts = f'Rules Engine: \n{parts}'
        elif action.help == import_model_help:
            parts = f'Model: \n{parts}'

        return parts

def main(command_line=None):
    """creates all of the argparse parsers and returns the args passed in""" 
    parser = argparse.ArgumentParser(description=mtool_ascii_art, 
                                    formatter_class=helpFormatter, 
                                    usage="Notebooks: r, o, s, l, h, v, Scene: ns, es, cs, rs, ds, ls, Library: al, rl, ll, sl, parameter:se , sv, de, le")
                                    
    subparsers = parser.add_subparsers(dest='command')
    
    run_notebook = subparsers.add_parser('run', aliases=["r"], help=run_notebook_help)
    run_notebook.add_argument('notebook', help=run_notebook_notebook_help)
    run_notebook.add_argument('html', nargs="?", help=run_notebook_parameter_help)
    run_notebook.set_defaults(which=run_notebook_command)

    view_notebook_params = subparsers.add_parser('viewparams', aliases=["v"], help=view_notebook_param_help)
    view_notebook_params.add_argument('notebook', help=view_notebook_param_notebook_help)
    view_notebook_params.set_defaults(which=view_notebook_param_command)

    open_notebook = subparsers.add_parser('open', aliases=["o"], help=open_notebook_help)
    open_notebook.add_argument('notebook', help=open_notebook_notebook_help)
    open_notebook.add_argument('parameter', nargs="?", help=open_notebook_parameter_help)
    open_notebook.set_defaults(which=open_notebook_command)
    
    search_notebooks = subparsers.add_parser('search', aliases=["s"], help=search_notebooks_help)
    search_notebooks.add_argument('term', help=search_notebooks_term_help)
    search_notebooks.set_defaults(which=search_notebooks_command)

    list_notebooks = subparsers.add_parser('list', aliases=["l"], help=list_notebooks_help)
    list_notebooks.set_defaults(which=list_notebooks_command)

    history = subparsers.add_parser('history', aliases=["h"], help=history_help)
    history.set_defaults(which=history_command)

    next_notebook = subparsers.add_parser('whatnext', aliases=["n"], help=next_notebook_help)
    next_notebook.set_defaults(which=next_notebook_command)


    add_notebook = subparsers.add_parser('addnotebook', aliases=["a"], help=add_notebook_help)
    add_notebook.add_argument('path', help=add_notebook_path_help)
    add_notebook.set_defaults(which=add_notebook_command)

    remove_notebook = subparsers.add_parser('removenotebook', aliases=["rm"], help=remove_notebook_help)
    remove_notebook.add_argument('name', help=remove_notebook_name_help)
    remove_notebook.set_defaults(which=remove_notebook_command)

    new_scene = subparsers.add_parser('newscene', aliases=["ns"], help=new_scene_help)
    new_scene.add_argument('name', help=new_scene_name_help)
    new_scene.set_defaults(which=new_scene_command)

    end_scene = subparsers.add_parser('endscene', aliases=["es"], help=end_scene_help)
    end_scene.add_argument('name', nargs="?", help=end_scene_name_help)
    end_scene.set_defaults(which=end_scene_command)

    change_scene = subparsers.add_parser('changescene', aliases=["cs"], help=change_scene_help)
    change_scene.add_argument('name', help=change_scene_name_help)
    change_scene.set_defaults(which=change_scene_command)

    resume_scene = subparsers.add_parser('resumescene', aliases=["rs"], help=resume_scene_help)
    resume_scene.add_argument('name', help=resume_scene_name_help)
    resume_scene.set_defaults(which=resume_scene_command)

    delete_scene = subparsers.add_parser('deletescene', aliases=["ds"], help=delete_scene_help)
    delete_scene.add_argument('name', nargs="?", help=delete_scene_name_help)
    delete_scene.set_defaults(which=delete_scene_command)

    list_scene = subparsers.add_parser('listscenes', aliases=["ls"], help=list_scene_help)
    list_scene.set_defaults(which=list_scene_command)

    set_param = subparsers.add_parser('setparam', aliases=["se"], help=set_param_help)
    set_param.add_argument('name', help=set_param_name_help)
    set_param.add_argument('value', help=set_param_value_help)
    set_param.set_defaults(which=set_param_command)

    search_param = subparsers.add_parser('searchparam', aliases=["sv"], help=search_param_help)
    search_param.add_argument('term', help=search_param_term_help)
    search_param.set_defaults(which=search_param_command)

    delete_param = subparsers.add_parser('deleteparam', aliases=["de"], help=delete_param_help)
    delete_param.add_argument('name', help=delete_param_name_help)
    delete_param.set_defaults(which=delete_param_command)

    list_param = subparsers.add_parser('listparam', aliases=["le"], help=list_param_help)
    list_param.set_defaults(which=list_param_command)

    view_library_param = subparsers.add_parser('viewlibparam', aliases=["vl"], help=view_library_param_help)
    view_library_param.add_argument('name', help=view_library_param_name_help)
    view_library_param.set_defaults(which=view_library_param_command)

    pull_notebook_param = subparsers.add_parser('pullparam', aliases=['p'], help=pull_notebook_param_help)
    pull_notebook_param.add_argument('notebook', help = pull_notebook_param_name_help)
    pull_notebook_param.set_defaults(which = pull_notebook_param_command)

    pull_library_param = subparsers.add_parser('pullparamlib', aliases=['pl'], help=pull_library_param_help)
    pull_library_param.add_argument('name', help = pull_library_param_name_help)
    pull_library_param.set_defaults(which = pull_library_param_command)

    add_library = subparsers.add_parser('addlibrary', aliases=["al"], help=add_library_help)
    add_library.add_argument('path', help=add_library_path_help)
    add_library.set_defaults(which=add_library_command)

    remove_library = subparsers.add_parser('removelibrary', aliases=["rl"], help=remove_library_help)
    remove_library.add_argument('name', help=remove_library_name_help)
    remove_library.set_defaults(which=remove_library_command)

    list_libraries = subparsers.add_parser('listlibrary', aliases=["ll"], help=list_libraries_help)
    list_libraries.set_defaults(which=list_library_command)

    sync_library = subparsers.add_parser('synclibrary', aliases=["sl"], help=sync_library_help)
    sync_library.add_argument('path', nargs="?", help=sync_library_path_help)
    sync_library.set_defaults(which=sync_library_command)

    update_settings = subparsers.add_parser('updatesettings', aliases=['u'], help=update_settings_help)
    update_settings.set_defaults(which=update_settings_command)

    new_ruleset = subparsers.add_parser('newruleset', aliases=['nr'], help=new_ruleset_help)
    new_ruleset.add_argument('name', help=new_ruleset_name_help)
    new_ruleset.add_argument('path', nargs="?", help=new_ruleset_path_help)
    new_ruleset.set_defaults(which=new_ruleset_command)

    remove_ruleset = subparsers.add_parser('removeruleset', aliases=['rr'], help=remove_ruleset_help)
    remove_ruleset.add_argument('name', help=remove_ruleset_name_help)
    remove_ruleset.set_defaults(which=remove_ruleset_command)

    list_rulesets = subparsers.add_parser('listrulesets', aliases=['lr'], help=list_rulesets_help)
    list_rulesets.set_defaults(which=list_rulesets_command)

    import_ruleset = subparsers.add_parser('importruleset', aliases=['ir'], help=import_ruleset_help)
    import_ruleset.add_argument('path', help=import_ruleset_path_help)
    import_ruleset.set_defaults(which=import_ruleset_command)

    view_ruleset = subparsers.add_parser('viewruleset', aliases=['vr'], help=view_ruleset_help)
    view_ruleset.add_argument('name', help=view_ruleset_name_help)
    view_ruleset.set_defaults(which=view_ruleset_command)

    edit_ruleset = subparsers.add_parser('editruleset', aliases=['er'], help=edit_ruleset_help)
    edit_ruleset.add_argument('name', help=edit_ruleset_name_help)
    edit_ruleset.add_argument('action', choices=['a','d','m'], help=edit_ruleset_action_help)
    edit_ruleset.set_defaults(which=edit_ruleset_command)

    activate_ruleset = subparsers.add_parser('activateruleset', aliases=['ar'], help=activate_ruleset_help)
    activate_ruleset.add_argument('name', help=activate_ruleset_name_help)
    activate_ruleset.set_defaults(which=activate_ruleset_command)

    deactivate_ruleset = subparsers.add_parser('deactivateruleset', aliases=['dr'], help=deactivate_ruleset_help)
    deactivate_ruleset.add_argument('name', help=deactivate_ruleset_name_help)
    deactivate_ruleset.set_defaults(which=deactivate_ruleset_command)

    import_model = subparsers.add_parser('importmodel', aliases=['im'], help=import_model_help)
    import_model.add_argument('modelpath', help=import_model_modelpath_help)
    import_model.add_argument('converterpath', help=import_model_converterpath_help)
    import_model.set_defaults(which=import_model_command)

    update_model = subparsers.add_parser('updatemodel', aliases=['um'], help=update_model_help)
    update_model.set_defaults(which=update_model_command)

    args = parser.parse_args(command_line)

    if len(sys.argv[1:])==0:
        parser.print_help()
        print()
    
    return args


def start(args=None, test = False):
    """the runner of mtool from the cli. makes a call to the switcher with the output of main"""
    from src.mtool.util import cli
    from src.mtool.util import error
    
    if args == None:
        args = sys.argv

    # prevents mtool from running on an out of date version of python
    if sys.version_info.major < 3 and sys.version_info.minor < 6:
        print("mtool requires python 3.6. Your version is " + str(sys.version_info.major)+ "." + str(sys.version_info.minor), "which is incompatable. Please update python.")
        return 1
    """
    This should be somewhere less annoying
    # warns if tensorflow is turbo broken
    elif sys.version_info.major == 3 and sys.version_info.minor > 6:
        print("mtool's model is built with tensorflow, which requires python <=3.6. Your version is " + str(sys.version_info.major)+ "." + str(sys.version_info.minor), "which is incompatable." +
        " Consider changing your python version or running in a virtual parameter to get model-based predictions for next actions.")
    """

    if len(args) > 1:
        arg1 = args[1]
        if arg1.isnumeric():
            arg = argparse.Namespace

            if len(args) > 2:
                arg.html = args[2]
            else:
                arg.html = None

            arg.command = 'r'
            arg.notebook = arg1
            arg.which = run_notebook_command
            func = 0
            try:
                func = cli.command(arg, test=test)
            except error.NotebookNotFoundError as e:
                print(e)
                return 1
            return func
        
    func = 0
    try:
        func = cli.command(main(), test=test)
    except (error.EndEndedSceneError, 
            error.ParamNotFoundError, 
            error.LastActiveSceneError, 
            error.LibraryNotFoundError, 
            error.NotebookNotFoundError, 
            error.SceneEndedError, 
            error.SceneNotFoundError, 
            error.RulesetNotFoundError,
            error.RulesetActiveError,
            error.RulesetNotActiveError,
            error.SceneNotFoundError,
            error.NotDirectoryError,
            error.NotFileError, 
            error.NotNotebookError,
            error.EditorNotFoundError,
            error.ADSNotFoundError,
            error.NotValidRuleset)as e:
        print(e)
        return 1
    
    if test:
        return func


if __name__ == "__main__":
    """the runner of mtool. makes a call to start"""
    start()
