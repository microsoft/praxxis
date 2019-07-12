"""
This file contains the sqlite functions for predictions
"""

def init_prediction_db(prediction_db):
    """initializes the base prediction database"""
    from src.mtool.util.sqlite import connection

    conn = connection.create_connection(prediction_db)
    cur = conn.cursor()
    create_rules_table = f'CREATE TABLE "RulesEngine" (Name TEXT PRIMARY KEY, Link TEXT)'
    create_models_table = f'CREATE TABLE "Models" (Name TEXT PRIMARY KEY, Info TEXT, Date TEXT, Link TEXT)'
    cur.execute(create_rules_table)
    cur.execute(create_models_table)
    conn.commit()
    conn.close()

def init_ruleset(prediction_db, ruleset_name, ruleset_db):
    """creates a new ruleset database and adds to list"""
    from src.mtool.util.sqlite import connection
    conn = connection.create_connection(ruleset_db)
    cur = conn.cursor()
    
    create_rules_table = f'CREATE TABLE "Rules" (Name TEXT PRIMARY KEY)'
    create_filenames_table = f'CREATE TABLE "Filenames" (Rule TEXT, Filename TEXT, FOREIGN KEY(Rule) REFERENCES "Rules"(Name))'
    create_outputs_table = f'CREATE TABLE "OutputString" (Rule TEXT, Output TEXT, FOREIGN KEY(Rule) REFERENCES "Rules"(Name))'
    create_prediction_table = f'CREATE TABLE "Predictions" (Rule TEXT, Position INTEGER, PredictedNotebook TEXT, FOREIGN KEY(Rule) REFERENCES "Rules"(Name))'

    cur.execute(create_rules_table)
    cur.execute(create_filenames_table)
    cur.execute(create_outputs_table)
    cur.execute(create_prediction_table)
    conn.commit()
    conn.close()

    add_ruleset_to_list(prediction_db, ruleset_name, ruleset_db)

def add_ruleset_to_list(prediction_db, ruleset_name, ruleset_root):
    """adds ruleset to list"""
    from src.mtool.util.sqlite import connection

    import os
    ruleset_name = os.path.basename(ruleset_root).split(".db")[0]
    print(ruleset_name)

    conn = connection.create_connection(prediction_db)
    cur = conn.cursor()
    add_rule = f'INSERT INTO "RulesEngine" VALUES (?, ?)'
    cur.execute(add_rule, (ruleset_name, ruleset_root))
    conn.commit()
    conn.close()


"""
example on foreign keys 
    create_metadata_table = f'CREATE TABLE "LibraryMetadata" (Root TEXT PRIMARY KEY, Readme TEXT, Name TEXT)'
    create_notebook_table = f'CREATE TABLE "Notebooks" (Root TEXT PRIMARY KEY, Name TEXT, LibraryName TEXT, FOREIGN KEY(LibraryName) REFERENCES "LibraryMetadata"(Name))'
    create_environment_table = f'CREATE TABLE "Environment" (Name TEXT PRIMARY KEY, Value TEXT)'
    create_notebook_environment_table = f'CREATE TABLE "NotebookEnvironment" (EnvironmentName TEXT, NotebookName TEXT, PRIMARY KEY(EnvironmentName, NotebookName), FOREIGN KEY(NotebookName) REFERENCES "Notebooks"(Name), FOREIGN KEY(EnvironmentName) REFERENCES "Environment"(Name))'
    cur.execute(create_metadata_table)
    cur.execute(create_notebook_table)
    cur.execute(create_environment_table)
    cur.execute(create_notebook_environment_table)
    conn.commit()
    conn.close()
"""