import requests
import json
import warnings
import time
from requests.auth import HTTPBasicAuth

from src.mtool.util.sqlite import sqlite_scene
from src.mtool.predictions.rules_engine import rules_checker
#from src.mtool.predictions.model import score


def what_next(args, user_info_db, current_scene_db, prediction_db, start, end):
    data = sqlite_scene.get_recent_history(current_scene_db, 5)
    rules_checker.rules_check(prediction_db, "DIR 001", "output", start, end)
    #suggestions = score.predict(data)
    #print(suggestions)


