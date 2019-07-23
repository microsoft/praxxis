"""
This file requests a new model from HDFS.
"""

import os

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

import requests
from requests.auth import HTTPBasicAuth

from src.praxxis.sqlite import sqlite_telemetry

def update_model():
    #stubbed out :(
    pass