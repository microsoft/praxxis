"""
This file handles the argument parsing, and is the entry point of the app
"""

import argparse
import os
import sys

## these are the commands passed into cli.py
run_notebook_command = "run_notebook"
view_notebook_env_command="view_notebook_env"
list_notebooks_command="list_notebooks"
search_notebooks_command="search_notebooks"
open_notebook_command="open_notebook"
history_command="history"
next_notebook_command="next_notebook"
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
set_env_command="set_env"
delete_env_command="delete_env"
list_env_command="list_env"
view_library_env_command="view_library_env"
pull_notebook_env_command = "pull_notebook_env"
pull_library_env_command = "pull_library_env"
search_env_command="search_env"
update_settings_command="update_settings"
new_ruleset_command="new_ruleset"
remove_ruleset_command="remove_ruleset"
list_rulesets_command="list_rulesets"
view_ruleset_command="view_ruleset"
edit_ruleset_command="edit_ruleset"
import_ruleset_command="import_ruleset"
activate_ruleset_command="activate_ruleset"
deactivate_ruleset_command="deactivate_ruleset"
update_model_command="update_model"

## notebook help strings
run_notebook_help="run notebook"
run_notebook_notebook_help="notebook to run"
run_notebook_environment_help="html flag for opening in web"
view_notebook_env_help="displays the environments for the notebook"
view_notebook_env_notebook_help="the notebook to view environment for"
open_notebook_help="open notebook in Azure Data Studio"
open_notebook_notebook_help="notebook to open"
list_notebooks_help="list notebooks to run, by ordinal."
search_notebooks_help="search for notebooks matching search term"
search_notebooks_term_help ="search term for notebooks"
next_notebook_help="model based prediction of what to do next in the current scene"
## scene help strings 
new_scene_help="new scene"
new_scene_name_help="name of new scene"
end_scene_help="end scene"
end_scene_name_help="name of scene to end"
change_scene_help="change scene"
change_scene_environment_help="environment for scene"
change_scene_name_help="name of scene to change to"
resume_scene_help="resume scene"
resume_scene_name_help="name of scene to resume"
delete_scene_help="delete scene"
delete_scene_name_help="name of scene to delete"
list_scene_help="list scenes"
## environment help strings
set_env_help="set environment variable for current scene"
set_env_name_help="name of the environment variable to set"
set_env_value_help="value of the environment variable to set"
delete_env_help="delete environment variable for current scene"
delete_env_name_help="name of the environment variable to delete"
search_env_help="search for environment variable names"
search_env_term_help="search term for environment variable"
list_env_help="list environment variables"
view_library_env_help="list all environments in a library of notebooks"
view_library_env_name_help="the name of the library you want to list for"
pull_notebook_env_help = "pull environments out of a notebook into your current scene"
pull_notebook_env_name_help = "the name of the notebook to pull environments from"
pull_library_env_help = "pull environments out of a library into your current scene"
pull_library_env_name_help = "the name of the library to pull the environments from"
## library help strings
add_library_help="install library of notebooks to mtool"
add_library_path_help="the path to the library you want to add"
remove_library_help="remove library of notebooks mtool"
remove_library_path_help="path of the library you want to remove"
list_libraries_help="list libraries currently installed"
sync_library_help="load libraries into mtool. Default loads from predefined library path"
sync_library_path_help="load library from a specific directory into mtool"
## misc help strings
history_help="history of what you've done in the current scene"
update_settings_help="update telemetry and security settings"
#prediction help strings
new_ruleset_help="create a ruleset for the prediction rules engine"
new_ruleset_name_help="the name of the new ruleset to create"
remove_ruleset_help="remove a ruleset from the prediction rules engine"
list_rulesets_help="list all rulesets available for the prediction rules engine"
view_ruleset_help="view all rules in a ruleset"
edit_ruleset_help="make changes to a ruleset"
import_ruleset_help="import a ruleset file from outside mtool"
activate_ruleset_help="activate ruleset(s) to use when making predictions"
deactivate_ruleset_help="deactivate ruleset(s) to keep them on your machine, but not use them in predictions"
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
            parts = f"""\nNotebooks: \n    [n]                 runs nth notebook in list\n{parts}"""
        elif action.help == new_scene_help:
            parts = f'\nScene: \n{parts}'
        elif action.help == set_env_help:
            parts = f'\nEnvironment: \n{parts}'
        elif action.help == add_library_help:
            parts = f'\nLibrary: \n{parts}'
        elif action.help == new_ruleset_help:
            parts = f'\nPredictions: \n{parts}'

        return parts

def main(command_line=None):
    """creates all of the argparse parsers and returns the args passed in""" 
    parser = argparse.ArgumentParser(description=mtool_ascii_art, 
                                    formatter_class=helpFormatter, 
                                    usage="Notebooks: r, o, s, l, h, v, Scene: ns, es, cs, rs, ds, ls, Library: al, rl, ll, sl, Environment:se , sv, de, le")
                                    
    subparsers = parser.add_subparsers(dest='command')
    
    run_notebook = subparsers.add_parser('run', aliases=["r"], help=run_notebook_help)
    run_notebook.add_argument('notebook', help=run_notebook_notebook_help)
    run_notebook.add_argument('html', nargs="?", help=run_notebook_environment_help)
    run_notebook.set_defaults(which=run_notebook_command)

    view_notebook_envs = subparsers.add_parser('viewenvs', aliases=["v"], help=view_notebook_env_help)
    view_notebook_envs.add_argument('notebook', help=view_notebook_env_notebook_help)
    view_notebook_envs.set_defaults(which=view_notebook_env_command)

    open_notebook = subparsers.add_parser('open', aliases=["o"], help=open_notebook_help)
    open_notebook.add_argument('notebook', help=open_notebook_notebook_help)
    open_notebook.add_argument('html', nargs="?", help=run_notebook_environment_help)
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

    set_env = subparsers.add_parser('setenv', aliases=["se"], help=set_env_help)
    set_env.add_argument('name', help=set_env_name_help)
    set_env.add_argument('value', help=set_env_value_help)
    set_env.set_defaults(which=set_env_command)

    search_env = subparsers.add_parser('searchenv', aliases=["sv"], help=search_env_help)
    search_env.add_argument('term', help=search_env_term_help)
    search_env.set_defaults(which=search_env_command)

    delete_env = subparsers.add_parser('deleteenv', aliases=["de"], help=delete_env_help)
    delete_env.add_argument('name', help=delete_env_name_help)
    delete_env.set_defaults(which=delete_env_command)

    list_env = subparsers.add_parser('listenv', aliases=["le"], help=list_env_help)
    list_env.set_defaults(which=list_env_command)

    view_library_env = subparsers.add_parser('viewlibenv', aliases=["vl"], help=view_library_env_help)
    view_library_env.add_argument('name', help=view_library_env_name_help)
    view_library_env.set_defaults(which=view_library_env_command)

    pull_notebook_env = subparsers.add_parser('pullenv', aliases=['p'], help=pull_notebook_env_help)
    pull_notebook_env.add_argument('notebook', help = pull_notebook_env_name_help)
    pull_notebook_env.set_defaults(which = pull_notebook_env_command)

    pull_library_env = subparsers.add_parser('pullenvlib', aliases=['pl'], help=pull_library_env_help)
    pull_library_env.add_argument('name', help = pull_library_env_name_help)
    pull_library_env.set_defaults(which = pull_library_env_command)

    add_library = subparsers.add_parser('addlibrary', aliases=["al"], help=add_library_help)
    add_library.add_argument('path', help=add_library_path_help)
    add_library.set_defaults(which=add_library_command)

    remove_library = subparsers.add_parser('removelibrary', aliases=["rl"], help=remove_library_help)
    remove_library.add_argument('path', help=remove_library_path_help)
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
    new_ruleset.set_defaults(which=new_ruleset_command)

    remove_ruleset = subparsers.add_parser('removeruleset', aliases=['rr'], help=remove_ruleset_help)
    remove_ruleset.set_defaults(which=remove_ruleset_command)

    list_rulesets = subparsers.add_parser('listrulesets', aliases=['lr'], help=list_rulesets_help)
    list_rulesets.set_defaults(which=list_rulesets_command)

    import_ruleset = subparsers.add_parser('importruleset', aliases=['ir'], help=import_ruleset_help)
    import_ruleset.set_defaults(which=import_ruleset_command)

    view_ruleset = subparsers.add_parser('viewruleset', aliases=['vr'], help=view_ruleset_help)
    view_ruleset.set_defaults(which=view_ruleset_command)

    edit_ruleset = subparsers.add_parser('editruleset', aliases=['er'], help=edit_ruleset_help)
    edit_ruleset.set_defaults(which=edit_ruleset_command)

    activate_ruleset = subparsers.add_parser('activateruleset', aliases=['ar'], help=activate_ruleset_help)
    activate_ruleset.set_defaults(which=activate_ruleset_command)

    deactivate_ruleset = subparsers.add_parser('deactivateruleset', aliases=['dr'], help=deactivate_ruleset_help)
    deactivate_ruleset.set_defaults(which=deactivate_ruleset_command)

    update_model = subparsers.add_parser('updatemodel', aliases=['um'], help=update_model_help)
    update_model.set_defaults(which=update_model_command)

    args = parser.parse_args(command_line)

    if len(sys.argv[1:])==0:
        parser.print_help()
        print()
    
    return args


def start(args=None):
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
        " Consider changing your python version or running in a virtual environment to get model-based predictions for next actions.")
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
            try:
                cli.command(arg)
            except error.NotebookNotFoundError as e:
                print(e)
                return 1
            return 0
    try:
        cli.command(main())
    except (error.EndEndedSceneError, 
            error.EnvNotFoundError, 
            error.LastActiveSceneError, 
            error.LibraryNotFoundError, 
            error.NotebookNotFoundError, 
            error.SceneEndedError, 
            error.SceneNotFoundError)as e:
        print(e)
        return 1
    return 0


if __name__ == "__main__":
    """the runner of mtool. makes a call to start"""
    start()
