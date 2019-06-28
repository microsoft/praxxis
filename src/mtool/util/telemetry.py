import os
import sys

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import requests
from requests.auth import HTTPBasicAuth

from src.mtool.util import sqlite_util

# Include the helpers subfolder folder
#
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), "helpers"))


def send(root, local_copy, current_scene_db):    
    
    user_info_db = os.path.join(root, "user_id.db")

    
    host = [sqlite_util.get_telemetry_info(user_info_db, "Host")]
    print(host)
#    url = sqlite_util.get_telemetry_info(user_info_db, "URL")
#    username = sqlite_util.get_telemetry_info(user_info_db, "Username")
#    pswd =  sqlite_util.get_telemetry_info(user_info_db, "Password")

    installation_identifier = sqlite_util.get_telemetry_info(user_info_db, "ID")
    scene_identifier = sqlite_util.get_scene_id(current_scene_db)

    # TODO: Enable round-robin for all nodes in the K8s cluster (nodePort)
    web_hdfs_endpoint = url.format(host[0])

    #with open(filename, encoding="utf8") as infile:
    #    contents = infile.read()

    # Get the filename from the end of the url
    #
    basename = os.path.basename(local_copy)

    year = basename[0:4]
    month = basename[4:6]
    day = basename[6:8]

    # Create a file in hdfs
    #
    route = "{0}/{1}/{2}/{3}/ipynb/{4}/{5}/{6}".format(web_hdfs_endpoint, year, month, day, installation_identifier, scene_identifier, basename)

    payload = {'op': 'CREATE'}
    with open(local_copy, 'rb' ) as f:
        r = requests.put(route, data=f, params=payload, headers={"Content-Type": "text/plain"}, verify=False, auth=HTTPBasicAuth(username, pswd))
        r.raise_for_status()
       

if __name__ == "__main__":
    send(*sys.argv[1:])