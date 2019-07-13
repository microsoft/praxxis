def add_library(args, library_db, git_root):
    from urllib.parse import urlparse
    from src.mtool.util import error
    import re
    import os

    path = args.path

    remote = urlparse(path)
    ssh = re.match(r".*[@].*\..*[:].*\.(git)", path)
    
    if remote.scheme == "" and not ssh:
        if os.path.exists(path):
            if os.path.isdir(path):
                from src.mtool.library import sync_library

                sync_library.sync_library(os.path.abspath(path), library_db)
            else:
                raise error.NotDirectoryError(path)
        else: 
            raise error.LibraryNotFoundError
    else:
        from git import Repo
        import subprocess
        import shutil

        if not os.path.exists(git_root):
            os.mkdir(git_root)

        ##TODO: break into a top level and a bottom level 
        
        if ssh:
            repo_name = path.split(':')[1].split('.')[0]
        else:
            repo_name = remote.path[1:]
     
        repo_root = os.path.join(git_root, repo_name)
        
        if os.path.exists(repo_root):
            print("that repo already exists. Cloning and reimporting.")
            shutil.rmtree(repo_root)
        
        subprocess.call(["git", "clone", path, repo_root])
        
        print(git_root)
