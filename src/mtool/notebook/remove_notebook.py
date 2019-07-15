def remove_notebook(args, library_db, current_scene_db):
    from src.mtool.util.sqlite import sqlite_library
    from src.mtool.util.sqlite import sqlite_notebook
    from src.mtool.notebook import notebook
    from src.mtool.util import error
    from src.mtool.notebook import list_notebook
    from src.mtool.display import display_notebook

    name = args.name

    try:
        tmp_name = notebook.get_notebook_by_ordinal(current_scene_db, name)
    except error.NotebookNotFoundError as e:
        raise e
    
    if tmp_name != None:
        name = tmp_name
    
    try:
        sqlite_notebook.check_notebook_exists(library_db, name)
    except error.NotebookNotFoundError as e:
        raise e

    sqlite_library.remove_notebook(library_db, name)
    display_notebook.display_remove_success(name)
