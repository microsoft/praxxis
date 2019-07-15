"""
This file contains the sqlite functions for predictions
"""

def init_prediction_db(prediction_db):
    """initializes the base prediction database"""
    from src.mtool.util.sqlite import connection

    conn = connection.create_connection(prediction_db)
    cur = conn.cursor()
    create_rules_table = f'CREATE TABLE "RulesEngine" (ID INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT, Path TEXT, Active INTEGER)'
    create_models_table = f'CREATE TABLE "Models" (Name TEXT PRIMARY KEY, Info TEXT, Date TEXT, Link TEXT)'
    cur.execute(create_rules_table)
    cur.execute(create_models_table)
    conn.commit()
    conn.close()

def init_ruleset(prediction_db, ruleset_name, ruleset_db):
    """creates a new ruleset database"""
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


def add_ruleset_to_list(prediction_db, ruleset_name, ruleset_root, active = 1):
    """adds ruleset to list"""
    from src.mtool.util.sqlite import connection

    import os
    ruleset_name = os.path.basename(ruleset_root).split(".db")[0]

    conn = connection.create_connection(prediction_db)
    cur = conn.cursor()
    add_rule = f'INSERT INTO "RulesEngine"(Name, Path, Active) VALUES (?, ?, ?)'
    cur.execute(add_rule, (ruleset_name, ruleset_root, active))
    conn.commit()
    conn.close()

def get_ruleset_path(prediction_db, name):
    """returns the path to a ruleset"""
    from src.mtool.util.sqlite import connection
    from src.mtool.util import error

    conn = connection.create_connection(prediction_db)
    cur = conn.cursor()
    get_ruleset_path = f'SELECT Path FROM "RulesEngine" WHERE Name = ?'
    cur.execute(get_ruleset_path, (name,))
    conn.commit()
    rows = cur.fetchone()
    conn.close()
    if rows == None:
        raise error.RulesetNotFoundError(name)
    return rows[0]

def remove_ruleset(prediction_db, name):
    """removes a ruleset from the list of rulesets"""
    from src.mtool.util.sqlite import connection
    from src.mtool.util import error

    conn = connection.create_connection(prediction_db)
    cur = conn.cursor()
    remove_ruleset = f'DELETE FROM "RulesEngine" WHERE Name = ?'
    cur.execute(remove_ruleset, (name,))
    conn.commit()
    conn.close()

def get_ruleset_by_ord(prediction_db, ordinal):
    """gets ruleset by ordinal"""
    from src.mtool.util.sqlite import connection
    from src.mtool.util import error

    conn = connection.create_connection(prediction_db)
    cur = conn.cursor()
    get_ruleset_by_ord = f'SELECT Name FROM "RulesEngine" ORDER BY Active DESC, ID LIMIT {ordinal-1}, {ordinal}'
    cur.execute(get_ruleset_by_ord)
    conn.commit()
    rows = cur.fetchall()
    conn.close()
    if rows == []:
        raise error.RulesetNotFoundError(ordinal)
    return rows[0][0]

def get_all_rulesets(prediction_db, start, end):
    """gets all rulesets"""
    from src.mtool.util.sqlite import connection
    
    conn = connection.create_connection(prediction_db)
    cur = conn.cursor()
    get_active_rulesets = f'SELECT Name, Active FROM "RulesEngine" ORDER BY ACTIVE DESC, ID ASC'
    cur.execute(get_active_rulesets)
    conn.commit()
    rows = cur.fetchall()
    conn.close()

    return rows

def get_active_rulesets(prediction_db, start, end):
    """gets all active rulesets"""
    from src.mtool.util.sqlite import connection
    
    conn = connection.create_connection(prediction_db)
    cur = conn.cursor()
    get_active_rulesets = f'SELECT Name FROM "RulesEngine" WHERE ACTIVE = 1 ORDER BY ID'
    cur.execute(get_active_rulesets)
    conn.commit()
    rows = cur.fetchall()
    conn.close()

    return rows

def get_inactive_rulesets(prediction_db):
    """gets all inactive rulesets"""
    from src.mtool.util.sqlite import connection
    
    conn = connection.create_connection(prediction_db)
    cur = conn.cursor()
    get_inactive_rulesets = f'SELECT Name FROM "RulesEngine" WHERE ACTIVE = 0 ORDER BY ID'
    cur.execute(get_inactive_rulesets)
    conn.commit()
    rows = cur.fetchall()
    conn.close()

    return rows

def activate_ruleset(prediction_db, name):
    """activates ruleset <name>"""
    from src.mtool.util.sqlite import connection
    from src.mtool.util import error
    conn = connection.create_connection(prediction_db)
    cur = conn.cursor()
    check_if_active = f'SELECT Active FROM "RulesEngine" WHERE Name = ?'
    cur.execute(check_if_active, (name,))
    result = cur.fetchone()

    if result == None:
        raise error.RulesetNotFoundError(name)
    elif result[0] == 1:
        raise error.RulesetActiveError(name)
    else:
        activate_ruleset = f'UPDATE RulesEngine SET Active = 1 WHERE Name = ?'
        cur.execute(activate_ruleset, (name,))
        conn.commit()
    conn.close()

def deactivate_ruleset(prediction_db, name):
    """deactivates ruleset <name>"""
    from src.mtool.util.sqlite import connection
    from src.mtool.util import error 

    conn = connection.create_connection(prediction_db)
    cur = conn.cursor()
    check_if_inactive = f'SELECT Active FROM "RulesEngine" WHERE Name = ?'
    cur.execute(check_if_inactive, (name,))
    result = cur.fetchone()

    if result == None:
        raise error.RulesetNotFoundError(name)
    elif result[0] == 0:
        raise error.RulesetNotActiveError(name)
    else:
        deactivate_ruleset = f'UPDATE RulesEngine SET Active = 0 WHERE Name = ?'
        cur.execute(deactivate_ruleset, (name,))
        conn.commit()
    conn.close()
    
