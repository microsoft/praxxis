"""
adds a library from git or path
"""

def add_library(args, library_db, git_root):
    """ adds a library from git or path"""
    from src.praxxis.util import error
    from src.praxxis.display import display_error
    from src.praxxis.display import display_library
    from src.praxxis.library import sync_library
    import giturlparse
    import os

    path = args.path

    remote = giturlparse.parse(path)

    if not remote.valid:
        #if it is not a valid github remote

        if os.path.exists(path):
            #check if the path exists and is a directory
            if os.path.isdir(path):
                sync_library.sync_library(os.path.abspath(path), library_db, custom_path=True)
            else:
                raise error.NotDirectoryError(path)
        else: 
            raise error.LibraryNotFoundError(path)
    else:
        #if the path is a valid git remote
        from src.praxxis.util import rmtree
        from git import Repo
        import sys
        import subprocess

        if not os.path.exists(git_root):
            #check if the git root exists, and if it doesn't, make it here
            os.mkdir(git_root)
            display_library.display_init_git_library(git_root)
        
        repo_author = remote.data["owner"]
        repo_name = remote.data["repo"]
        repo_root = os.path.join(git_root, repo_author, repo_name)
              
        if os.path.exists(repo_root):
            # if the path exits, remove it and clone again
            rmtree.rmtree(repo_root)
            display_error.repo_exists_warning()

        try:
            #git clone the repo
            subprocess.call(["git", "clone", path, repo_root])
        except KeyboardInterrupt:
            #if it is interrupted, delete the empty directory that git creates
            repo_author_root = os.path.join(git_root, repo_author)
            if len(os.listdir(repo_author_root) ) == 0:
                os.rmdir(repo_author_root)
            sys.exit(0)

        remote_https = giturlparse.parse(path).url2https
        repo_root_abspath = os.path.abspath(repo_root)
        sync_library.sync_library(repo_root_abspath, library_db, custom_library_name=f"{repo_author}_{repo_name}", custom_path=True, remote=path, remote_origin=remote_https)
