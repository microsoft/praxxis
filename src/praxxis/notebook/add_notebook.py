def add_notebook(args, library_db):
    import os 
    from src.praxxis.util import error
    
    path = args.path

    file_name, file_extension = os.path.splitext(os.path.basename(path))
    
    if os.path.exists(path):
        if os.path.isdir(path):
            raise error.NotFileError(path)
        if file_extension == ".ipynb":
            from src.praxxis.sqlite import sqlite_library
            from src.praxxis.sqlite import sqlite_notebook
            from src.praxxis.display import display_error
            from src.praxxis.util import error

            try:
                sqlite_notebook.check_notebook_exists(library_db, file_name)
            except error.NotebookNotFoundError:
                pass
            else:
                display_error.duplicate_notebook_warning(file_name)
            
            sqlite_library.load_notebook(library_db, os.path.abspath(path), file_name, "none")
        else:
            raise error.NotNotebookError(path)
    else:
        raise error.NotebookNotFoundError(path)