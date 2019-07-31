"""
This file contains the sqlite functions for the model management
"""

def add_model(model_db, model_name, model_path, converter_path):
    """adds a model to the list of models"""
    from src.praxxis.sqlite import connection 

    conn = connection.create_connection(model_db)
    cur = conn.cursor()

    add_model = 'INSERT INTO "Models" (Name, Path, ConverterPath) VALUES (?,?,?)'

    cur.execute(add_model, (model_name, model_path, converter_path))
    conn.commit()
    conn.close()

def get_model_paths(model_db, model_name):
    """fetches the model and converter paths for a specific model"""
    from src.praxxis.sqlite import connection 

    conn = connection.create_connection(model_db)
    cur = conn.cursor()

    get_model_paths = 'SELECT Path, ConverterPath FROM "Models" WHERE Name = ?'

    cur.execute(get_model_paths, (model_name,))
    conn.commit()
    paths = cur.fetchone()
    conn.close()

    return paths
    