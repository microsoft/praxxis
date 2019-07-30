def copytree(src, dest):
    import shutil
    
    try:
        shutil.copytree(src, dest)
    except PermissionError:
        import os
        import stat
        os.chmod(src, stat.S_IRWXU)

        if os.path.exists(dest):
            from tests.src.praxxis.util import rmtree
            rmtree.rmtree(dest)

        if not os.path.exists(dest):
            try:
                shutil.copytree(src,dest)
            except Exception as e:
                if "WinError" in str(e):
                    import pytest
                    import colorama 
                    from colorama import Fore
                    if "Windows permissions failure" in str(e):
                        pytest.exit(str(e))
                    else:
                        pytest.exit(f"{Fore.RED}Windows permissions failure -- try re-running to resolve (Error " + str(e) + ")")
                else:
                    raise e
        