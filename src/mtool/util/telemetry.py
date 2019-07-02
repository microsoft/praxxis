import os
import sys

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import requests
from requests.auth import HTTPBasicAuth

from src.mtool.util.sqlite import sqlite_telemetry

def send(root, local_copy, current_scene_db):    
    
    user_info_db = os.path.join(root, "user_id.db")

    telem_info = sqlite_telemetry.get_telemetry_info(user_info_db)
    username = telem_info[2]
    pswd = telem_info[3]
    
    installation_identifier = telem_info[4]
    scene_identifier = sqlite_telemetry.get_scene_id(current_scene_db)

    # TODO: Enable round-robin for all nodes in the K8s cluster (nodePort)
    url = telem_info[1]

    web_hdfs_endpoint = url.format(telem_info[0])

    # Get the filename from the end of the url
    basename = os.path.basename(local_copy)

    year = basename[0:4]
    month = basename[4:6]
    day = basename[6:8]

    # Create a file in hdfs
    route = "{0}/{1}/{2}/{3}/ipynb/{4}/{5}/{6}".format(web_hdfs_endpoint, year, month, day, installation_identifier, scene_identifier, basename)

    payload = {'op': 'CREATE'}
    with open(local_copy, 'rb' ) as f:
        r = requests.put(route, data=f, params=payload, headers={"Content-Type": "text/plain"}, verify=False, auth=HTTPBasicAuth(username, pswd))
        r.raise_for_status()
       

if __name__ == "__main__":
    send(*sys.argv[1:])