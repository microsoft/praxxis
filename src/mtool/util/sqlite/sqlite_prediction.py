"""
This file contains the sqlite functions for predictions
"""

def init_prediction_db(prediction_db):
    """initializes the base prediction database"""
    from src.mtool.util.sqlite import connection

    conn = connection.create_connection(prediction_db)
    cur = conn.cursor()
    create_rules_table = f'CREATE TABLE "RulesEngine" (ID INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT, Path TEXT)'
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
    add_rule = f'INSERT INTO "RulesEngine"(Name, Path) VALUES (?, ?)'
    cur.execute(add_rule, (ruleset_name, ruleset_root))
    conn.commit()
    conn.close()

def get_ruleset_path(prediction_db, name):
    """returns a specific notebook"""
    from src.mtool.util.sqlite import connection
    from src.mtool.util import error

    conn = connection.create_connection(prediction_db)
    cur = conn.cursor()
    get_ruleset_path = f'SELECT "Link" FROM "RulesEngine" WHERE Name = {name} LIMIT 0, 1'
    cur.execute(get_ruleset_path)
    conn.commit()
    rows = cur.fetchall()
    conn.close()
    if rows == []:
        raise error.NotebookNotFoundError(name)
    return rows[0]

