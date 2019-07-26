def add_notebook(args, library_db):
    import os 
    from src.praxxis.util import error
    from src.praxxis.library import sync_library
    
    path = args.path

    notebook_name = args.path.split(os.path.sep)[-1]
    
    sync_library.load_notebook(notebook_name, os.path.abspath(args.path)[:-1], library_db, 'none', None)

    # sync_library.load_notebook()

    
    # if os.path.exists(path):
    #     if os.path.isdir(path):
    #         raise error.NotFileError(path)
    #     if file_extension == ".ipynb":
    #         from src.praxxis.sqlite import sqlite_library
    #         from src.praxxis.sqlite import sqlite_notebook
    #         from src.praxxis.display import display_error
    #         from src.praxxis.sqlite import sqlite_parameter
    #         from src.praxxis.notebook import notebook
    #         from src.praxxis.util import error

    #         try:
    #             sqlite_notebook.check_notebook_exists(library_db, file_name)
    #             sqlite_library.check_library_exists(library_db, "none")
    #         except error.NotebookNotFoundError:
    #             pass
    #         except error.LibraryNotFoundError:
    #             sqlite_library.add_none_library(library_db)
    #         else:
    #             display_error.duplicate_notebook_warning(file_name)

    #         notebook_data = notebook.Notebook([os.path.abspath(path), file_name, "none"])
    #         for parameter in notebook_data._parameters:
    #             sqlite_parameter.set_notebook_parameters(library_db, file_name, parameter[0].strip(), parameter[1], "none")
            
    #         sqlite_library.load_notebook(library_db, os.path.abspath(path), file_name, "none")
    #     else:
    #         raise error.NotNotebookError(path)
    # else:
    #     raise error.NotebookNotFoundError(path)