def remove_library(args, library_db):
    from src.mtool.util.sqlite import sqlite_library
    from src.mtool.display import display_library
    import shutil
    import os

    name = args.name
    try:
        sqlite_library.check_library_exists(library_db, name)
    except Exception as e:
        raise e

    sqlite_library.remove_library(library_db, name)
    #TODO: delete library folder 
    display_library.display_remove_success(name)

