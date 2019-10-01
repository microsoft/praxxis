"""
Adds a rule to the ruleset by user inputs in a console dialog
"""


def add_rule_to_ruleset(args, rulesengine_db, library_db, current_scene_db, query_start, query_end):
    """prompts user through adding a rule, given a ruleset"""
    from src.praxxis.sqlite import sqlite_rulesengine
    from src.praxxis.display import display_rulesengine
    from src.praxxis.display import display_edit_ruleset
    from src.praxxis.rulesengine import rules
    from src.praxxis.display.display_error import predictions_ordinal_not_in_list_error
    from src.praxxis.notebook.list_notebook import list_notebook

    if hasattr(args, "name"):
        name = args.name
    else:
        name = args

    name = rules.get_ruleset_by_ordinal(name, rulesengine_db)

    ruleset_db = sqlite_rulesengine.get_ruleset_path(rulesengine_db, name)

    # get a name for the rule
    rulename = display_edit_ruleset.display_get_rule_name()
    
    # get filenames 
    list_notebook(library_db, current_scene_db, query_start, query_end)
    filenames_raw = display_edit_ruleset.display_filename_input()
    filenames_with_ords = [string.strip().strip('"').strip('\'') for string in filenames_raw.split(",")]
    filenames = get_filenames_from_ordinals(filenames_with_ords, current_scene_db)
    display_edit_ruleset.display_filenames(filenames)

    # get output strings
    output_raw = display_edit_ruleset.display_output_input()
    output = [item.strip().strip('"').strip('\'') for item in output_raw.split(",")]
    display_edit_ruleset.display_outputs(output)

    # get predicted notebooks
    list_notebook(library_db, current_scene_db, query_start, query_end)
    predicted_raw = display_edit_ruleset.display_predicted_notebooks_input()
    predicted_with_ords = [prediction.strip() for prediction in predicted_raw.split(",")]
    predicted = get_fileinfo_from_ordinals(predicted_with_ords, current_scene_db, rulename)
    while predicted == 1:
        predictions_ordinal_not_in_list_error()

        predicted_raw = display_edit_ruleset.display_predicted_notebooks_input()
        predicted_with_ords = [prediction.strip() for prediction in predicted_raw.split(",")]
        predicted = get_fileinfo_from_ordinals(predicted_with_ords, current_scene_db, rulename)

    display_edit_ruleset.display_prediction_list(predicted)

    # display total rule and add it to db        
    display_rulesengine.display_rule(rulename, filenames, output, predicted)
    sqlite_rulesengine.add_rule(ruleset_db, rulename, filenames, output, predicted)

    return rulename
    

def get_filenames_from_ordinals(filenames_with_ords, current_scene_db, allow_errors = True):
    """get filenames, given ordinals"""
    from src.praxxis.notebook import notebook
    from src.praxxis.util.error import NotebookNotFoundError
    filenames = []
    for filename in filenames_with_ords:
        try:
            nbname = notebook.get_notebook_by_ordinal(current_scene_db, filename)
            if nbname != None:
                filename = nbname[0]
            elif not allow_errors:
                raise NotebookNotFoundError(nbname)
        except NotebookNotFoundError as e:
            if allow_errors:
                from src.praxxis.display import display_error
                display_error.display_ruleset_num_input_warning(filename)
            else:
                raise e
        filenames.append(filename)

    return filenames


def get_fileinfo_from_ordinals(predictions_with_ords, current_scene_db, rulename):
    """get all fileinfo and format it correctly for predictions entry"""
    # TODO: look at renaming/refactoring this
    from src.praxxis.notebook import notebook
    from src.praxxis.util.error import NotebookNotFoundError
    # format:    
    # (Rule, Position, PredictedNotebook, Library, RawURL)

    predictions = []
    position = 1
    for prediction in predictions_with_ords:
        try:
            nbname = notebook.get_notebook_by_ordinal(current_scene_db, prediction)
            
            if nbname == None:
                raise NotebookNotFoundError(prediction)
        except NotebookNotFoundError as e:
            raise e
        prediction = (rulename, position, nbname[0], nbname[1], None)
        if prediction[3] == []:
            prediction = (rulename, position, nbname[0], None, None)
        predictions.append(prediction)
        position += 1
        
    return predictions
