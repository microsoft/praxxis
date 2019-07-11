def add_notebook(args, library_db):
    import os 
    
    path = args.path

    file_name, file_extension = os.path.splitext(os.path.basename(path))

    if file_extension == ".ipynb":
        from src.mtool.util.sqlite import sqlite_library                  
        sqlite_library.load_notebook(library_db, path, file_name,"none")
    else:
        print("dawg that's not a notebook")