def copytree(src, dest, test = False):
    import shutil
    
    try:
        shutil.copytree(src, dest)
    except PermissionError:
        import os
        import stat
        os.chmod(src, stat.S_IRWXU)

        if os.path.exists(dest):
            from src.praxxis.util import rmtree
            rmtree.rmtree(dest, test=True)

        if not os.path.exists(dest):
            try:
                shutil.copytree(src,dest)
            except Exception as e:
                if test and "WinError" in str(e):
                    import pytest
                    from src.praxxis.display import display_error
                    message = display_error.pytest_windows_permissions_error(str(e))
                    pytest.exit(message)
                else:
                    raise e
        