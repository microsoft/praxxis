"""
Rule-engine and model-based predictions based on user history.
"""
import requests
import json
import warnings
import time
from requests.auth import HTTPBasicAuth

from src.praxxis.sqlite import sqlite_scene
from src.praxxis.rulesengine import rules_checker


def what_next(args, user_info_db, current_scene_db, library_db, prediction_db, start, end):
    """calls prediction endpoints to get next notebooks"""
    from src.praxxis.display import display_rulesengine
    data = sqlite_scene.get_recent_history(current_scene_db, 5)
    if data == []:
        from src.praxxis.util.error import EmptyHistoryError
        raise EmptyHistoryError()

    rules_based = rules_checker.rules_check(prediction_db, data[-1][0], data[-1][1], start, end)
    if rules_based != []:
        display_rulesengine.display_predictions(rules_based)
        write_to_list(rules_based, current_scene_db, library_db)
    else:
        import sys
        if sys.version_info.major == 3 and sys.version_info.minor > 6:
            from src.praxxis.display import display_error
            display_error.tensorflow_version_error(str(sys.version_info.major), str(sys.version_info.minor))
            sys.exit(1)
    
        """
        from src.praxxis.model import score
        suggestions = score.predict(data)
        print(suggestions)
        """

    
def write_to_list(notebook_library_list, current_scene_db, library_db):
    """grabs paths and writes to notebook list so ordinal referencing works"""
    from src.praxxis.sqlite import sqlite_notebook

    notebooklist = []
    for notebook in notebook_library_list:
        path = sqlite_notebook.get_notebook_path(library_db, notebook[0], notebook[1])
        notebook = (notebook[0], path, notebook[1], None)
        notebooklist.append(notebook)

    sqlite_notebook.write_list(current_scene_db, notebooklist)
    