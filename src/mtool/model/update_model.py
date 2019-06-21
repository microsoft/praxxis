"""
This file sends the telemetry from execution into HDFS.
"""

import os

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

import requests
from requests.auth import HTTPBasicAuth

from src.mtool.util import sqlite_util

def send(root, filename, current_scene_db):
    user_id = os.path.join(root, "user_id.db")

    """Send telemetry into HDFS
    
    Keyword arguments:
    installation_identifier -- identify user running the file
    scene_identifier -- identify current scene
    filename -- name of file that was run
    """
 
    telemetry_url_format_string = sqlite_util.get_telemetry_info(user_id, "URL")
    telemery_hosts = [sqlite_util.get_telemetry_info(user_id, "Host")]
    installation_identifier = sqlite_util.get_telemetry_info(user_id, "ID")
    scene_identifier = sqlite_util.get_scene_id(current_scene_db)

    username = sqlite_util.get_telemetry_info(user_id, "Username")
    pswd = sqlite_util.get_telemetry_info(user_id, "Password")

    # TODO: Enable round-robin for all nodes in the K8s cluster (nodePort)
    web_hdfs_endpoint = telemetry_url_format_string.format(telemery_hosts[0])

    with open(filename, encoding="utf8") as infile:
        contents = infile.read()

    # Get the filename from the end of the url
    basename = os.path.basename(filename)

    year = basename[0:4]
    month = basename[4:6]
    day = basename[6:8]

    # Create a file in hdfs
    route = "{0}/{1}/{2}/{3}/ipynb/{4}/{5}/{6}".format(web_hdfs_endpoint, year, month, day, installation_identifier, scene_identifier, basename)
    
    payload = {'op': 'CREATE'}

    r = requests.put(url=route, data=contents, params=payload, headers={"Content-Type": "text/plain"}, verify=False, auth=HTTPBasicAuth(username, pswd))
  
    r.raise_for_status()
