import requests
import json
import warnings
import time
from requests.auth import HTTPBasicAuth

from src.mtool.util.sqlite import sqlite_scene
from src.mtool.rulesengine import rules_checker
#from src.mtool.model import score


def what_next(args, user_info_db, current_scene_db, prediction_db, start, end):
    from src.mtool.display import display_rulesengine
    data = sqlite_scene.get_recent_history(current_scene_db, 5)
    if data == []:
        from src.mtool.util.error import EmptyRulesetError
        raise EmptyRulesetError()

    rules_based = rules_checker.rules_check(prediction_db, data[-1][0], data[-1][1], start, end)
    display_rulesengine.display_predictions(rules_based)
    #suggestions = score.predict(data)
    #print(suggestions)


