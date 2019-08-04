def add_notebook(args, library_db):
    import os 
    from src.praxxis.library import sync_library
    
    root = (os.path.sep).join(os.path.abspath(args.path).split(os.path.sep)[:-1])
    notebook_name = args.path.split(os.path.sep)[-1]
    print(root)

    relative_path = ""
    
    sync_library.load_notebook(notebook_name, root, library_db, "none", relative_path)
