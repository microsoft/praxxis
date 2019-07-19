"""
This file lists all of the parameter variables
"""

def list_param(current_scene_db, start, end):
    """lists the parameter variables in scene"""
    import os
    from src.mtool.util.sqlite import sqlite_scene
    from src.mtool.util.sqlite import sqlite_parameter
    from src.mtool.display import display_param
    
    param_list = sqlite_parameter.list_param(current_scene_db, start, end)

    display_param.display_list_param(param_list)
    return param_list


def list_notebook_param(args, library_db, current_scene_db):
    """List all parameters in the current notebook"""
    from src.mtool.util.sqlite import sqlite_parameter
    from src.mtool.notebook import notebook
    from src.mtool.display import display_param

    name = args.notebook
    tmp_name = notebook.get_notebook_by_ordinal(current_scene_db, name)
    if tmp_name != None:
        name = tmp_name

    sqlite_parameter.get_all_param(current_scene_db)

    parameters = sqlite_parameter.list_notebook_param(library_db, name)
    
    display_param.display_view_param(parameters, 
                                      sqlite_parameter.get_all_param(current_scene_db))
    
    return parameters


def list_library_param(args, library_db, current_scene_db):
    """Lists all parameters in the """
    from src.mtool.util.sqlite import sqlite_parameter
    from src.mtool.display import display_param
    from src.mtool.util import error

    if hasattr(args, "name"):
        name = args.name
    else:
        name = args
            
    try:
        parameters = sqlite_parameter.get_library_parameters(library_db, name)
    except error.LibraryNotFoundError as e:
        raise e
    
    display_param.display_view_param(parameters,
                             sqlite_parameter.get_all_param(current_scene_db))

    return parameters
