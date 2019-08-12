"""
This file exists to try to combat Windows permissions errors
TODO: needs reworking/reevaluation. does this actually fix any
of the copytree permissions errors?
"""

def copytree(src, dest, test = False):
    """recursively copies a directory tree"""
    import shutil
    
    try:
        shutil.copytree(src, dest)
    except PermissionError:
        import os
        import stat
        os.chmod(src, stat.S_IRWXU)

        if os.path.exists(dest):
            # removes files from half-done copytree
            from src.praxxis.util import rmtree
            rmtree.rmtree(dest, test=True)

        if not os.path.exists(dest):
            try:
                shutil.copytree(src,dest)
            except Exception as e:
                if test and "WinError" in str(e):
                    # exits pytest
                    import pytest
                    from src.praxxis.display import display_error
                    message = display_error.pytest_windows_permissions_error(str(e))
                    pytest.exit(message)
                else:
                    raise e
