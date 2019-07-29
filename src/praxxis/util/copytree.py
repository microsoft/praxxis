def copytree(src, dest):
    import shutil
    
    try:
        shutil.copytree(src, dest)
    except PermissionError:
        import os
        import stat
        os.chmod(src, stat.S_IRWXU)

        if os.path.exists(dest):
            from src.praxxis.util import rmtree
            rmtree.rmtree(dest)

        #os.mkdir(dest)
        #os.rmdir(dest)
        if not os.path.exists(dest):
            try:
                shutil.copytree(src,dest)
            except Exception as e:
                if sys.platform == "windows":
                    import pytest
                    pytest.exit("Windows permissions failure -- try re-running to resolve (Error " + e + ")")
                else:
                    raise e
        