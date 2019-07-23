"""
handles accessing of model related things from the CLI
"""
from src.mtool.util.roots import _model_root
from src.mtool.util.roots import _model_db

def init_model(model_root, model_db):
    """
    initializes the model db, and directories
    """
    import os
    
    from src.mtool.display import display_model
    from src.mtool.sqlite import sqlite_init

    os.mkdir(model_root)
    display_model.display_init_model_root(model_root)
    sqlite_init.init_model_db(model_db)
    display_model.display_init_model_db(model_db)
    return

def import_model(arg, 
                 model_db = _model_db):
    """
    handles importing a new model.
    """
    from src.mtool.model import import_model
    import_model.import_model(arg, model_db)
    return

def update_model(arg):
    """
    handles updating a model. 
    """
    print("um:")
    return
