
def add_rule_to_ruleset(args, prediction_db, library_db, current_scene_db, start, stop):
    from src.mtool.util.sqlite import sqlite_prediction
    from src.mtool.display import display_prediction
    from src.mtool.display import display_edit_ruleset
    from src.mtool.predictions.rules_engine import rules

    if hasattr(args, "name"):
        name = args.name
    else:
        name = args

    name = rules.get_ruleset_by_ordinal(name, prediction_db)

    ruleset_db = sqlite_prediction.get_ruleset_path(prediction_db, name)

    rulename = display_edit_ruleset.display_get_rule_name()
    

    from src.mtool.notebook import list_notebook
    list_notebook.list_notebook(library_db, current_scene_db, start, stop)

    filenames_with_ords = display_edit_ruleset.display_filename_input()
    print([string.strip() for string in filenames.split(",")])


def get_filenames_from_ordinals(filenames_with_ords):
    for filename in filenames_with_ords
