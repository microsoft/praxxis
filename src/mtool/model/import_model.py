def import_model(args, prediction_db):
    from src.mtool.util.sqlite import sqlite_model
    from src.mtool.display import display_model
    import os

    model_path = args.modelpath
    converter_path = args.converterpath

    model_name = os.path.basename(model_path)

    sqlite_model.add_model(prediction_db, model_name, model_path, converter_path)
    display_model.display_imported_model(model_name)
