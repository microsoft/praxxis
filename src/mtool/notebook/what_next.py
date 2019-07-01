import requests
import json
import warnings
import time
from requests.auth import HTTPBasicAuth

from src.mtool.util.sqlite import sqlite_scene
from src.mtool.model.scoring import score


def what_next(args, user_info_db, current_scene_db):
    data = sqlite_scene.get_recent_history(current_scene_db, 5)
    suggestions = score.predict(data)
