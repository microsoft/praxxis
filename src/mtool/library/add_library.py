def add_library(args, library_db, git_root):
    from urllib.parse import urlparse
    from src.mtool.util import error
    from src.mtool.display import display_error
    from src.mtool.display import display_library
    from src.mtool.library import sync_library
    import giturlparse
    import re
    import os

    path = args.path

    remote = giturlparse.parse(path)

    if not remote.valid:
        if os.path.exists(path):
            if os.path.isdir(path):
                sync_library.sync_library(os.path.abspath(path), library_db)
            else:
                raise error.NotDirectoryError(path)
        else: 
            raise error.LibraryNotFoundError
    else:
        from git import Repo
        import sys
        import subprocess
        import shutil

        if not os.path.exists(git_root):
            os.mkdir(git_root)
            display_library.display_init_git_library(git_root)
        
        repo_author = remote.data["owner"]
        repo_name = remote.data["repo"]

        repo_root = os.path.join(git_root, repo_author, repo_name)
              
        if os.path.exists(repo_root):
            shutil.rmtree(repo_root)
            display_error.repo_exists_warning()

        try:
            subprocess.call(["git", "clone", path, repo_root])
        except KeyboardInterrupt:
            repo_author_root = os.path.join(git_root, repo_author)
            if len(os.listdir(repo_author_root) ) == 0:
                os.rmdir(repo_author_root)
            sys.exit(0)
        
        remote_https = giturlparse.parse(path).url2https
        
        sync_library.sync_library(os.path.abspath(repo_root), library_db, library_name=f"{repo_author}_{repo_name}", remote=path, remote_origin=remote_https)
