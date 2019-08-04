"""
This file contains all of the display functions for model management
"""

def display_init_model_root(root):
    """display function for creating new model folder"""
    print("Created model directory at %s" %(root)) 


def display_init_model_db(db_root):
    """display function for initializing the model db"""
    print("Created model database at %s" %(db_root)) 


def display_imported_model(name):
    """display function for importing a model"""
    print("Model %s imported successfully" %(name)) 
