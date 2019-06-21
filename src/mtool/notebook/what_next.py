import requests
import json
import warnings
import time
from requests.auth import HTTPBasicAuth

from src.mtool.util import sqlite_util
from src.mtool.notebook.model_management import score


def what_next(args, user_info_db, current_scene_db):
    data = sqlite_util.get_recent_history(current_scene_db, 5)

    suggestions = score.predict(data)

