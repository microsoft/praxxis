"""
This file sends the telemetry from execution into HDFS.

Dependencies within mtool: helpers/config.py
"""

import os
import sys
import toml

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

import requests
from requests.auth import HTTPBasicAuth

from mtool.cli import config

def send(installation_identifier, scene_identifier, filename):
    """Send telemetry into HDFS
    
    Keyword arguments:
    installation_identifier -- identify user running the file
    scene_identifier -- identify current scene
    filename -- name of file that was run
    """
    # IP address for spe-sag4hp-23vm01.corp.microsoft.com, because the name doesn't resolve for everyone
    #
    # TODO: Retrieve address from configuration (TOML) file
    #
    curr = os.getcwd()

    dict = config.load(os.path.join(curr, "..", "mtool", "config.toml"))

    section = dict["telemetry"]
    telemetry_url_format_string = section["url"]
    telemery_hosts = section["hosts"]

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

    r = requests.put(route, data=contents.encode('utf-8'), params=payload, headers={"Content-Type": "text/plain"}, verify=False, auth=HTTPBasicAuth('root', 'Yukon900'))
    r.raise_for_status()

