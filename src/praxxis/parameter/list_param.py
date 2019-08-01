"""
This file lists all of the parameters
"""

def list_param(current_scene_db, query_start, end):
    """lists the parameters in scene"""
    import os
    from src.praxxis.sqlite import sqlite_scene
    from src.praxxis.sqlite import sqlite_parameter
    from src.praxxis.display import display_param
    
    param_list = sqlite_parameter.list_param(current_scene_db, query_start, end)

    display_param.display_list_param(param_list)
    return param_list


def list_notebook_param(args, library_db, current_scene_db):
    """List all parameters in the current notebook"""
    from src.praxxis.sqlite import sqlite_parameter
    from src.praxxis.sqlite import sqlite_notebook
    from src.praxxis.notebook import notebook
    from src.praxxis.util import error
    from src.praxxis.display import display_param

    name = args.notebook

    notebook_data = notebook.get_notebook(current_scene_db, library_db, name)

    sqlite_parameter.get_all_param(current_scene_db)

    parameters = sqlite_parameter.list_notebook_param(library_db, notebook_data[1], notebook_data[2])
    
    display_param.display_view_param(parameters, 
                                      sqlite_parameter.get_all_param(current_scene_db))
    
    return parameters


def list_library_param(args, library_db, current_scene_db, query_start, end):
    """Lists all parameters in the """
    from src.praxxis.sqlite import sqlite_parameter
    from src.praxxis.display import display_param
    from src.praxxis.library import library
    from src.praxxis.util import error

    if hasattr(args, "name"):
        name = args.name
    else:
        name = args

    if name.isdigit():
        name = library.get_library_by_ordinal(library_db, name, query_start, end)
            
    try:
        parameters = sqlite_parameter.get_library_parameters(library_db, name)
    except error.LibraryNotFoundError as e:
        raise e
    
    display_param.display_view_param(parameters,
                             sqlite_parameter.get_all_param(current_scene_db))

    return parameters
