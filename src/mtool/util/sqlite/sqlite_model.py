"""
This file contains the sqlite functions for the model management
"""

def init_model_db(model_db):
    """initializes the base model database"""
    from src.mtool.util.sqlite import connection

    conn = connection.create_connection(model_db)
    cur = conn.cursor()
    create_models_table = f'CREATE TABLE "Models" (Name TEXT PRIMARY KEY, Info TEXT, Date TEXT, Path TEXT, ConverterPath TEXT)'
    cur.execute(create_models_table)
    conn.commit()
    conn.close()

def add_model(model_db, model_name, model_path, converter_path):
    """adds a model to the list of models"""
    from src.mtool.util.sqlite import connection 

    conn = connection.create_connection(model_db)
    cur = conn.cursor()

    add_model = 'INSERT INTO "Models" (Name, Path, ConverterPath) VALUES (?,?,?)'

    cur.execute(add_model, (model_name, model_path, converter_path))
    conn.commit()
    conn.close()

