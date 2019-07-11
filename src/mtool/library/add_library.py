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
                from src.mtool.library import 