"""
This file contains all of the display functions for model management
"""

def display_init_model_root(root):
    """the display function for creating new model folder"""
    print(f"Created model directory at {root}")

def display_init_model_db(db_root):
    """the display function for initializing the model db"""
    print(f"Created model database at {db_root}")

def display_imported_model(name):
    """the display function for importing a model"""
    print(f"Model {name} imported successfully")