import requests
from requests.auth import HTTPBasicAuth

from src.mtool.util import sqlite_util

def what_next(args, user_info_db, current_scene_db):
    #10.193.23.1:30778",
    #"basePath": "/api/app/mtool-model-app/v1

    host = sqlite_util.get_telemetry_info(user_info_db, "Host")
    route = f"https://{host}:30778/api/app/mtool-model-app/v1/run"

    # get access token
    ctl_url = f'https://{host}:30080/token'
    auth = HTTPBasicAuth('arisctrl', 'Yukon900')
    res = requests.post(ctl_url, verify=False, auth=auth)

    res_json = res.json()
    headers = {'Authorization': '{} {}'.format(res_json['token_type'], res_json['access_token'])}

    data_json = dict(seq=["SOP023", "SOP023", "SOP023"])
    res = requests.post(route, headers=headers, json=data_json, verify=False)

    res_json = res.json()
    print(res_json)
    # TODO: Enable round-robin for all nodes in the K8s cluster (nodePort)

    params = {"seq": "['ES002', 'ES002', 'ES003', 'ES003', 'SOP002', 'SOP003', 'SOP003']"} # RunService

   
    # https://docs.microsoft.com/en-us/sql/big-data-cluster/concept-application-deployment?view=sqlallproducts-allversions







  