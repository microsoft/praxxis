"""
This file exists to try to combat Windows permissions errors 
"""


def rmtree(root, test=False):
    """calls rmtree with onerror so windows doesn't have a terrible time"""
    import shutil
    import os

    try:
        shutil.rmtree(root, ignore_errors=False, onerror=onerror)
    except Exception as e:
        if test and "WinError" in str(e):
            import pytest
            from src.praxxis.display import display_error
            message = display_error.pytest_windows_permissions_error(str(e))
            pytest.exit(message)
        else:
            raise e


def onerror(func, path, exc_info):
    """what to do if there's an error -- try to get permissons from the os"""
    import stat
    import os
    ## https://stackoverflow.com/questions/1213706/what-user-do-python-scripts-run-as-in-windows

    if not os.access(path, os.W_OK):
        # Is the error an access error ?
        try:
            os.chmod(path, stat.S_IWUSR)
        except PermissionError:
            pass
        func(path)
    else:
        try:
            import uuid
            newname = str(uuid.uuid4())
            os.rename(path, newname)
            func(newname)
        except Exception as e:
            raise e
