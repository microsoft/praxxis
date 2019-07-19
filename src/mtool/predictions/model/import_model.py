def import_model(args, prediction_db):
    from src.mtool.util.sqlite import sqlite_prediction


    model_path = args.modelpath
    converter_path = args.converterpath
    print(model_path)
    print(converter_path)

    sqlite_prediction.add_model(prediction_db, model_path, converter_path)
    
