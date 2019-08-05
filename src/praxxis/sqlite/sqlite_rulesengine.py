"""
This file contains the sqlite functions for the rules engine
"""

def init_ruleset(rulesengine_db, ruleset_name, ruleset_db):
    """creates a new ruleset database"""
    from src.praxxis.sqlite import connection

    conn = connection.create_connection(ruleset_db)
    cur = conn.cursor()

    create_rules_table = 'CREATE TABLE "Rules" (Name TEXT PRIMARY KEY)'
    create_filenames_table = 'CREATE TABLE "Filenames" (Rule TEXT, Filename TEXT, CONSTRAINT fk_rule FOREIGN KEY(Rule) REFERENCES "Rules"(Name) ON DELETE CASCADE)'
    create_outputs_table = 'CREATE TABLE "OutputString" (Rule TEXT, Output TEXT, CONSTRAINT fk_rule FOREIGN KEY(Rule) REFERENCES "Rules"(Name) ON DELETE CASCADE)'
    create_prediction_table = 'CREATE TABLE "Predictions" (Rule TEXT, Position INTEGER, PredictedNotebook TEXT, Library TEXT, RawURL TEXT, CONSTRAINT fk_rule FOREIGN KEY(Rule) REFERENCES "Rules"(Name) ON DELETE CASCADE)'

    cur.execute(create_rules_table)
    cur.execute(create_filenames_table)
    cur.execute(create_outputs_table)
    cur.execute(create_prediction_table)
    conn.commit()
    conn.close()


def add_ruleset_to_list(rulesengine_db, ruleset_name, ruleset_root, active = 1):
    """adds ruleset to list"""
    from src.praxxis.sqlite import connection

    import os
    ruleset_name = os.path.basename(ruleset_root).split(".db")[0]

    conn = connection.create_connection(rulesengine_db)
    cur = conn.cursor()
    add_rule = 'INSERT INTO "RulesEngine"(Name, Path, Active) VALUES (?, ?, ?)'
    cur.execute(add_rule, (ruleset_name, ruleset_root, active))
    conn.commit()
    conn.close()


def get_ruleset_path(rulesengine_db, name):
    """returns the path to a ruleset"""
    from src.praxxis.sqlite import connection
    from src.praxxis.util import error

    conn = connection.create_connection(rulesengine_db)
    cur = conn.cursor()
    get_ruleset_path = 'SELECT Path FROM "RulesEngine" WHERE Name = ?'
    cur.execute(get_ruleset_path, (name,))
    conn.commit()
    rows = cur.fetchone()
    conn.close()
    if rows == None:
        raise error.RulesetNotFoundError(name)
    return rows[0]


def remove_ruleset(rulesengine_db, name):
    """removes a ruleset from the list of rulesets"""
    from src.praxxis.sqlite import connection

    conn = connection.create_connection(rulesengine_db)
    cur = conn.cursor()
    remove_ruleset = 'DELETE FROM "RulesEngine" WHERE Name = ?'
    cur.execute(remove_ruleset, (name,))
    conn.commit()
    conn.close()


def get_ruleset_by_ord(rulesengine_db, ordinal):
    """gets ruleset by ordinal"""
    from src.praxxis.sqlite import connection
    from src.praxxis.util import error

    conn = connection.create_connection(rulesengine_db)
    cur = conn.cursor()
    get_ruleset_by_ord = 'SELECT Name FROM "RulesEngine" ORDER BY Active DESC, ID LIMIT ?,?'
    cur.execute(get_ruleset_by_ord, (ordinal-1, ordinal))
    conn.commit()
    rows = cur.fetchall()
    conn.close()
    if rows == []:
        raise error.RulesetNotFoundError(ordinal)
    return rows[0][0]


def get_all_rulesets(rulesengine_db, query_start, query_end):
    """gets all rulesets"""
    from src.praxxis.sqlite import connection
    
    conn = connection.create_connection(rulesengine_db)
    cur = conn.cursor()
    get_active_rulesets = 'SELECT Name, Active FROM "RulesEngine" ORDER BY ACTIVE DESC, ID ASC'
    cur.execute(get_active_rulesets)
    conn.commit()
    rows = cur.fetchall()
    conn.close()

    return rows


def get_active_rulesets(rulesengine_db, query_start, query_end):
    """gets all active rulesets and paths"""
    from src.praxxis.sqlite import connection
    
    conn = connection.create_connection(rulesengine_db)
    cur = conn.cursor()
    get_active_rulesets = 'SELECT * FROM "RulesEngine" WHERE ACTIVE = 1 ORDER BY ID'
    cur.execute(get_active_rulesets)
    conn.commit()
    rows = cur.fetchall()
    conn.close()

    return rows


def get_inactive_rulesets(rulesengine_db):
    """gets all inactive rulesets"""
    from src.praxxis.sqlite import connection
    
    conn = connection.create_connection(rulesengine_db)
    cur = conn.cursor()
    get_inactive_rulesets = 'SELECT Name FROM "RulesEngine" WHERE ACTIVE = 0 ORDER BY ID'
    cur.execute(get_inactive_rulesets)
    conn.commit()
    rows = cur.fetchall()
    conn.close()

    return rows


def activate_ruleset(rulesengine_db, name):
    """activates ruleset <name>"""
    from src.praxxis.sqlite import connection
    from src.praxxis.util import error
    conn = connection.create_connection(rulesengine_db)
    cur = conn.cursor()
    check_if_active = 'SELECT Active FROM "RulesEngine" WHERE Name = ?'
    cur.execute(check_if_active, (name,))
    result = cur.fetchone()

    if result == None:
        raise error.RulesetNotFoundError(name)
    elif result[0] == 1:
        raise error.RulesetActiveError(name)
    else:
        activate_ruleset = 'UPDATE RulesEngine SET Active = 1 WHERE Name = ?'
        cur.execute(activate_ruleset, (name,))
        conn.commit()
    conn.close()


def deactivate_ruleset(rulesengine_db, name):
    """deactivates ruleset <name>"""
    from src.praxxis.sqlite import connection
    from src.praxxis.util import error 

    conn = connection.create_connection(rulesengine_db)
    cur = conn.cursor()
    check_if_inactive = 'SELECT Active FROM "RulesEngine" WHERE Name = ?'
    cur.execute(check_if_inactive, (name,))
    result = cur.fetchone()

    if result == None:
        raise error.RulesetNotFoundError(name)
    elif result[0] == 0:
        raise error.RulesetNotActiveError(name)
    else:
        deactivate_ruleset = 'UPDATE RulesEngine SET Active = 0 WHERE Name = ?'
        cur.execute(deactivate_ruleset, (name,))
        conn.commit()
    conn.close()
    

def add_rule(ruleset_db, rulename, filenames, outputs, predictions):
    """adds a rule to the ruleset"""
    from src.praxxis.sqlite import connection 

    conn = connection.create_connection(ruleset_db)
    cur = conn.cursor()
    add_name_to_rules = 'INSERT INTO "Rules" (Name) VALUES (?)'
    add_to_filenames = 'INSERT INTO "Filenames" (Rule, Filename) VALUES (?,?)'
    add_to_output = 'INSERT INTO "OutputString" (Rule, Output) VALUES (?,?)'
    add_to_predictions = 'INSERT INTO "Predictions" (Rule, Position, PredictedNotebook, Library, RawURL) VALUES (?,?,?,?,?)'

    cur.execute(add_name_to_rules, (rulename,))
    cur.executemany(add_to_filenames, [(rulename, string) for string in filenames])
    cur.executemany(add_to_output, [(rulename, out) for out in outputs])

    cur.executemany(add_to_predictions, predictions)
    conn.commit()
    conn.close()


def delete_rule(ruleset_db, rulename):
    """deletes a rule from the ruleset"""
    from src.praxxis.sqlite import connection 

    conn = connection.create_connection(ruleset_db)
    cur = conn.cursor()
    foreign_keys = 'PRAGMA foreign_keys = ON'
    delete_rule = 'DELETE FROM "Rules" WHERE Name = ?'

    cur.execute(foreign_keys)
    cur.execute(delete_rule, (rulename,))
    conn.commit()
    conn.close()


def list_rules_in_ruleset(ruleset_db):
    """returns a list of all rule names in a ruleset"""
    from src.praxxis.sqlite import connection 

    conn = connection.create_connection(ruleset_db)
    cur = conn.cursor()
    list_rules = 'SELECT * FROM "Rules" ORDER BY Name'
    
    cur.execute(list_rules)
    conn.commit()
    rules = cur.fetchall()
    conn.close()
    
    return rules


def get_filenames(ruleset_db, rule):
    """returns a list of all filenames for a rule in a ruleset"""
    from src.praxxis.sqlite import connection 

    conn = connection.create_connection(ruleset_db)
    cur = conn.cursor()
    list_filenames = 'SELECT Filename FROM "Filenames" WHERE Rule = ?'
    
    cur.execute(list_filenames, (rule,))
    conn.commit()
    filenames = cur.fetchall()
    conn.close()

    return filenames


def get_filenames_by_rule(ruleset_db):
    """returns a list of all filenames for all rules in a ruleset"""
    from src.praxxis.sqlite import connection 

    conn = connection.create_connection(ruleset_db)
    cur = conn.cursor()
    list_filenames = 'SELECT Filename, Rule FROM "Filenames" ORDER BY Rule'
    
    cur.execute(list_filenames)
    conn.commit()
    filenames = cur.fetchall()
    conn.close()

    return filenames

    
def get_outputs(ruleset_db, rule):
    """returns a list of all outputs for a rule in a ruleset"""
    from src.praxxis.sqlite import connection 

    conn = connection.create_connection(ruleset_db)
    cur = conn.cursor()
    list_outputs = 'SELECT Output FROM "OutputString" WHERE Rule = ?'
    
    cur.execute(list_outputs, (rule,))
    conn.commit()
    outputs = cur.fetchall()
    conn.close()

    return outputs


def get_outputs_for_rules(ruleset_db, ruleset):
    """returns a list of all outputs for all rules in a ruleset"""
    from src.praxxis.sqlite import connection 

    conn = connection.create_connection(ruleset_db)
    cur = conn.cursor()
    ruleslist = ','.join('"{0}"'.format(rule) for rule in ruleset)    
    list_outputs = 'SELECT Output, Rule FROM "OutputString" WHERE Rule IN (%s)' %(ruleslist)
    cur.execute(list_outputs)
    conn.commit()
    outputs = cur.fetchall()
    conn.close()

    return outputs


def get_predictions(ruleset_db, ruleset):
    """returns the ordered list of predictions for a set of rule matches"""
    from src.praxxis.sqlite import connection 

    conn = connection.create_connection(ruleset_db)
    cur = conn.cursor()
    ruleslist = ','.join('"{0}"'.format(rule) for rule in ruleset)
    get_predictions = 'SELECT DISTINCT PredictedNotebook, Library, RawURL FROM "Predictions" WHERE Rule IN (%s) ORDER BY Position ASC' %(ruleslist)

    cur.execute(get_predictions)
    conn.commit()
    predictions = cur.fetchall()
    conn.close()

    return predictions


def clear_ruleset_list(rulesengine_db):
    """removes all rulesets from list, for testing"""
    from src.praxxis.sqlite import connection 

    conn = connection.create_connection(rulesengine_db)
    cur = conn.cursor()
    cleanup = 'DELETE FROM "RulesEngine"'
    cur.execute(cleanup)
    conn.commit()
    conn.close()
