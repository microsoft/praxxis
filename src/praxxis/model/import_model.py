def import_model(args, prediction_db):
    from src.praxxis.sqlite import sqlite_model
    from src.praxxis.display import display_model
    import os

    model_path = os.path.abspath(args.modelpath)
    converter_path = os.path.abspath(args.converterpath)

    try:
        assert os.path.exists(model_path)
        assert os.path.exists(converter_path)
    except AssertionError:
        #TODO: add error
        from src.praxxis.util import error

    model_name = os.path.basename(model_path)

    sqlite_model.add_model(prediction_db, model_name, model_path, converter_path)
    display_model.display_imported_model(model_name)
