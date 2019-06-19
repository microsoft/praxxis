import requests
<<<<<<< HEAD
import json
import warnings
import time
=======
>>>>>>> 7eb7723458cd73decb1041493c017cff328612ab
from requests.auth import HTTPBasicAuth

from src.mtool.util import sqlite_util

<<<<<<< HEAD

def what_next(args, user_info_db, current_scene_db):
    """
    print(time.time())
    #10.193.23.1:30778"
=======
def what_next(args, user_info_db, current_scene_db):
    #10.193.23.1:30778",
>>>>>>> 7eb7723458cd73decb1041493c017cff328612ab
    #"basePath": "/api/app/mtool-model-app/v1

    host = sqlite_util.get_telemetry_info(user_info_db, "Host")
    route = f"https://{host}:30778/api/app/mtool-model-app/v1/run"

    # get access token
    ctl_url = f'https://{host}:30080/token'
    auth = HTTPBasicAuth('arisctrl', 'Yukon900')
<<<<<<< HEAD
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        res = requests.post(ctl_url, verify=False, auth=auth)
=======
    res = requests.post(ctl_url, verify=False, auth=auth)
>>>>>>> 7eb7723458cd73decb1041493c017cff328612ab

    res_json = res.json()
    headers = {'Authorization': '{} {}'.format(res_json['token_type'], res_json['access_token'])}

<<<<<<< HEAD
    data_json = dict(seq=["SOP027", "SOP023", "SOP023"])
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        res = requests.post(route, headers=headers, json=data_json, verify=False)

    res_json = res.json()
    suggestions = (res_json["outputParameters"]["score"]["notebook"][0:5])
    for i in range(len(suggestions)):
        print(str(1+i) + ". " + suggestions[i])
    """
    print(time.time())

    from src.mtool.notebook.mtool_model_app import score
    data = ["SOP027", "SOP023", "SOP023"]
    suggestions = score.predict(data)

 
    print(time.time())
    
=======
    data_json = dict(seq=["SOP023", "SOP023", "SOP023"])
    res = requests.post(route, headers=headers, json=data_json, verify=False)

    res_json = res.json()
    print(res_json)
    # TODO: Enable round-robin for all nodes in the K8s cluster (nodePort)

    params = {"seq": "['ES002', 'ES002', 'ES003', 'ES003', 'SOP002', 'SOP003', 'SOP003']"} # RunService

   
    # https://docs.microsoft.com/en-us/sql/big-data-cluster/concept-application-deployment?view=sqlallproducts-allversions







  
>>>>>>> 7eb7723458cd73decb1041493c017cff328612ab
