
def add_rule_to_ruleset(args, prediction_db, library_db, current_scene_db, start, stop):
    from src.mtool.util.sqlite import sqlite_prediction
    from src.mtool.display import display_rulesengine
    from src.mtool.display import display_edit_ruleset
    from src.mtool.predictions.rules_engine import rules
    from src.mtool.display.display_error import predictions_ordinal_not_in_list_error
    from src.mtool.notebook.list_notebook import list_notebook

    if hasattr(args, "name"):
        name = args.name
    else:
        name = args

    name = rules.get_ruleset_by_ordinal(name, prediction_db)

    ruleset_db = sqlite_prediction.get_ruleset_path(prediction_db, name)

    # get a name for the rule
    rulename = display_edit_ruleset.display_get_rule_name()
    
    # get filenames 
    list_notebook(library_db, current_scene_db, start, stop)
    filenames_raw = display_edit_ruleset.display_filename_input()
    filenames_with_ords = [string.strip().strip('"').strip('\'') for string in filenames_raw.split(",")]
    filenames = get_filenames_from_ordinals(filenames_with_ords, current_scene_db)
    display_edit_ruleset.display_filenames(filenames)

    # get output strings
    output_raw = display_edit_ruleset.display_output_input()
    output = [item.strip().strip('"').strip('\'') for item in output_raw.split(",")]
    display_edit_ruleset.display_outputs(output)

    # get predicted notebooks
    list_notebook(library_db, current_scene_db, start, stop)
    predicted_raw = display_edit_ruleset.display_predicted_notebooks_input()
    predicted_with_ords = [prediction.strip() for prediction in predicted_raw.split(",")]
    predicted = get_filenames_from_ordinals(predicted_with_ords, current_scene_db, allow_errors=False)
    while predicted == 1:
        predictions_ordinal_not_in_list_error()

        predicted_raw = display_edit_ruleset.display_predicted_notebooks_input()
        predicted_with_ords = [prediction.strip() for prediction in predicted_raw.split(",")]
        predicted = get_filenames_from_ordinals(predicted_with_ords, current_scene_db, allow_errors=False)

    display_edit_ruleset.display_rulesengines(predicted)

    # display total rule and add it to db        
    display_rulesengine.display_rule(rulename, filenames, output, predicted)
    sqlite_prediction.add_rule(ruleset_db, rulename, filenames, output, predicted)
    
        

def get_filenames_from_ordinals(filenames_with_ords, current_scene_db, allow_errors = True):
    from src.mtool.notebook import notebook
    from src.mtool.util.error import NotebookNotFoundError
    filenames = []
    for filename in filenames_with_ords:
        try:
            nbname = notebook.get_notebook_by_ordinal(current_scene_db, filename)
            if nbname != None:
                filename = nbname
            elif not allow_errors:
                raise NotebookNotFoundError
        except NotebookNotFoundError as e:
            if allow_errors:
                from src.mtool.display import display_error
                display_error.display_ruleset_num_input_warning(filename)
            else:
                print(f'{e}: {filename}')
                return 1
        filenames.append(filename)

    return filenames
