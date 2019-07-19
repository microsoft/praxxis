from src.mtool.util.roots import _query_start
from src.mtool.util.roots import _query_end
from src.mtool.util.roots import _model_root
from src.mtool.util.roots import _model_db
from src.mtool.util.roots import _library_db
from src.mtool.util.roots import _scene_root
from src.mtool.util.roots import _history_db
from src.mtool.util.roots import _query_start
from src.mtool.util.roots import _query_end

def init_model(model_root, model_db):
    import os
    
    from src.mtool.display import display_model
    from src.mtool.sqlite import sqlite_model

    os.mkdir(model_root)
    display_model.display_init_model_root(model_root)
    sqlite_model.init_model_db(model_db)
    display_model.display_init_model_db(model_db)
    return

def import_model(arg, 
                    model_db = _model_db):
    from src.mtool.model import import_model
    import_model.import_model(arg, model_db)
    return

def update_model(arg):
    print("um:")
    return
