import os
import sys

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import requests
from requests.auth import HTTPBasicAuth

from src.praxxis.sqlite import sqlite_telemetry

def update_file(user_info_db, local_copy, scene_identifier):   

    telem_info = sqlite_telemetry.get_telemetry_info(user_info_db)
    username = telem_info[2]
    pswd = telem_info[3]
    
    installation_identifier = telem_info[4]

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
    
    try:
        payload = {'op': 'DELETE'}
        r = requests.delete(route, params=payload, headers={"Content-Type": "text/plain"}, verify=False, auth=HTTPBasicAuth(username, pswd))
        r.raise_for_status()
        try:
            payload = {'op': 'CREATE'}
            with open(local_copy, 'rb' ) as f:
                r = requests.put(route, data=f, params=payload, headers={"Content-Type": "text/plain"}, verify=False, auth=HTTPBasicAuth(username, pswd))
                r.raise_for_status()
        except Exception as e:
            # add file that simply needs to be pushed to hdfs to backlog
            sqlite_telemetry.add_to_backlog(user_info_db, local_copy, scene_identifier, str(e))
    except Exception as e:
        # add file that needs to be deleted to backlog
        sqlite_telemetry.add_to_backlog(user_info_db, local_copy, scene_identifier, str(e), operation = 1)    
    
    
if __name__ == "__main__":
    user_info_db = sys.argv[1]
    local_copy = sys.argv[2]    
    scene_identifier = sys.argv[3]
    
    telem_enabled = sqlite_telemetry.telem_on(user_info_db)

    backlog = sqlite_telemetry.get_backlog(user_info_db)
    if telem_enabled and local_copy not in backlog:
        try:
            update_file(user_info_db, local_copy, scene_identifier)
        except Exception as e:
            # should never be hit but if sqlite error occurs, don't want to interrupt console
            pass
            