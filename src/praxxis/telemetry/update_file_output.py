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

    payload = {'op': 'DELETE'}
    r = requests.put(route, params=payload, headers={"Content-Type": "text/plain"}, verify=False, auth=HTTPBasicAuth(username, pswd))
    r.raise_for_status()
        
    payload = {'op': 'CREATE'}
    with open(local_copy, 'rb' ) as f:
        r = requests.put(route, data=f, params=payload, headers={"Content-Type": "text/plain"}, verify=False, auth=HTTPBasicAuth(username, pswd))
        r.raise_for_status()

if __name__ == "__main__":

    
    # TODO:
    # - check if telem off, if off do nothing
    # - warn if not updated in cluster ?
    # - delete cluster version
    # - send new one
    user_info_db = sys.argv[1]
    local_copy = sys.argv[2]    
    scene_identifier = sys.argv[3]
    
    backlog = sqlite_telemetry.get_backlog(user_info_db)
    if local_copy in backlog:
        print("DON'T SEND")
        pass
    else:
        try:
            update_file(user_info_db, local_copy, scene_identifier)
        except Exception as e:
            print(str(e))
            pass

    #user_info_db, local_copy, scene_identifier

    """
    if(backlog_size != 0):
        
        for telem in backlog:
            local_copy = telem[0]
            scene_identifier = telem[1]
            try:            
                send(user_info_db, local_copy, scene_identifier)
                sqlite_telemetry.delete_from_backlog(user_info_db, local_copy)
            except Exception as e:
                pass 
    
    try:            
        send(user_info_db, local_copy, scene_identifier)
        sqlite_telemetry.delete_from_backlog(user_info_db, local_copy)
    except Exception as e:
        sqlite_telemetry.add_to_backlog(user_info_db, local_copy, scene_identifier, str(e))
    """
            