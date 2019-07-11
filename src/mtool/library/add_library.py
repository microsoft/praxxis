def add_library(args, library_root, library_db):
    from urllib.parse import urlparse
    import os

    path = args.path

    remote = urlparse(path)
    if remote.scheme == "":
        if os.path.exists(path):
            if os.path.isdir(path):
                from src.mtool.library import sync_library

                sync_library.sync_library(path, library_db)
            else:
                
                file_name, file_extension = os.path.splitext(os.path.basename(path))

                if file_extension == ".ipynb":
                    from src.mtool.util.sqlite import sqlite_library                  
                    sqlite_library.load_notebook(library_db, path, file_name,"none")
                else:
                    print("dawg that's not a notebook")
        else: 
            print("the path doesn't exist my guy")

                