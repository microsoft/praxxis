def add_notebook(args, library_db):
    import os 
    from src.mtool.util import error
    
    path = args.path

    file_name, file_extension = os.path.splitext(os.path.basename(path))
    
    if os.path.exists(path):
        if os.path.isdir(path):
            raise error.NotFileError(path)
        if file_extension == ".ipynb":
            from src.mtool.util.sqlite import sqlite_library                  
            sqlite_library.load_notebook(library_db, path, file_name, "none")
        else:
            raise error.NotNotebookError(path)
    else:
        raise error.NotebookNotFoundError(path)