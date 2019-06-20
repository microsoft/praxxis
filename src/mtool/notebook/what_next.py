import requests
import json
import warnings
import time
from requests.auth import HTTPBasicAuth

from src.mtool.util import sqlite_util


def what_next(args, user_info_db, current_scene_db):
    """
    print(time.time())
    #10.193.23.1:30778"
    #"basePath": "/api/app/mtool-model-app/v1

    host = sqlite_util.get_telemetry_info(user_info_db, "Host")
    route = f"https://{host}:30778/api/app/mtool-model-app/v1/run"

    # get access token
    ctl_url = f'https://{host}:30080/token'
    auth = HTTPBasicAuth('arisctrl', 'Yukon900')
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        res = requests.post(ctl_url, verify=False, auth=auth)

    res_json = res.json()
    headers = {'Authorization': '{} {}'.format(res_json['token_type'], res_json['access_token'])}

    data_json = dict(seq=["SOP027", "SOP023", "SOP023"])
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        res = requests.post(route, headers=headers, json=data_json, verify=False)

    res_json = res.json()
    suggestions = (res_json["outputParameters"]["score"]["notebook"][0:5])
    for i in range(len(suggestions)):
        print(str(1+i) + ". " + suggestions[i])
    """
    from src.mtool.notebook.mtool_model_app import score
    data = sqlite_util.
    #["SOP027", "SOP023", "SOP023"]
    suggestions = score.predict(data)

