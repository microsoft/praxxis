"""
This file creates a new ruleset
"""

def new_ruleset(args, rulesengine_root, rulesengine_db):
    """create a new ruleset and associated db"""
    import os
    from src.praxxis.sqlite import sqlite_rulesengine
    from src.praxxis.display import display_rulesengine

    if hasattr(args, "name"):
        name = args.name
    else:
        name = args
        
    name = name.lower()

    if hasattr(args, "root"):
        root = args.root
    else:
        root = rulesengine_root
        
    path = os.path.join(root, "%s.db" %(name))

    if os.path.exists(path):
        i=1
        while os.path.exists(os.path.join(root, "%s-%s.db") %(name, i)):
            i+= 1
        path = os.path.join(root, "%s-%s.db" %(name, i))
        name = "%s-%s" %(name, i)
    
    sqlite_rulesengine.init_ruleset(rulesengine_db, name, path)
    sqlite_rulesengine.add_ruleset_to_list(rulesengine_db, name, path)

    display_rulesengine.display_new_ruleset(name)
    return name
