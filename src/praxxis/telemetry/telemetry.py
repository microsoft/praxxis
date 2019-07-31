import os
import sys

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import requests
from requests.auth import HTTPBasicAuth

from src.praxxis.sqlite import sqlite_telemetry

def send(user_info_db, local_copy, scene_identifier):    
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

    payload = {'op': 'CREATE'}
    with open(local_copy, 'rb' ) as f:
        r = requests.put(route, data=f, params=payload, headers={"Content-Type": "text/plain"}, verify=False, auth=HTTPBasicAuth(username, pswd))
        r.raise_for_status()


def telem_entrance(user_info_db=None, new_local_copy=None, scene_identifier=None):
    if user_info_db == None:
        user_info_db = sys.argv[1]
    if new_local_copy == None:
        new_local_copy = sys.argv[2]
    if scene_identifier == None:
        scene_identifier = sys.argv[3]

    backlog_size = sqlite_telemetry.backlog_size(user_info_db)

    if(backlog_size != 0):
        backlog = sqlite_telemetry.get_backlog(user_info_db)
        for telem in backlog:
            local_copy = telem[0]
            scene_identifier = telem[1]
            operation = telem[2]
            try:            
                if operation == 1:
                    from src.praxxis.telemetry import update_file_output
                    update_file_output.update_file(user_info_db, local_copy, scene_identifier)
                else:
                    send(user_info_db, local_copy, scene_identifier)
                
                sqlite_telemetry.delete_from_backlog(user_info_db, local_copy)
            except Exception:
                pass 
    try:            
        send(user_info_db, new_local_copy, scene_identifier)
    except Exception as e:
        sqlite_telemetry.add_to_backlog(user_info_db, new_local_copy, scene_identifier, str(e))
    
if __name__ == "__main__":
    telem_entrance()
