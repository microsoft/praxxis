"""
This file imports a model and converter
"""

def import_model(args, model_db):
    """add model and converter to sqlite database"""
    from src.praxxis.sqlite import sqlite_model
    from src.praxxis.display import display_model
    import os

    model_path = args.modelpath
    converter_path = args.converterpath

    model_name = os.path.basename(model_path)

    sqlite_model.add_model(model_db, model_name, model_path, converter_path)
    display_model.display_imported_model(model_name)
