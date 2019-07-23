import re
import subprocess
import json

MTOOL_ROOT= "http://nmnode-0-svc:50070/webhdfs/v1/praxxis/"

def test(loc):
    """
    collect the sequences for all users and all scenes.
    should we record user/scene/time info for training?
    """
    import requests
    from datetime import date, timedelta

    date_path = (date.today() - timedelta(days=int(loc))).strftime('%Y/%m/%d/ipynb')

    global MTOOL_ROOT   
    basepath = MTOOL_ROOT + date_path

    params = (
        ('op', 'LISTSTATUS'),
    )

    response = requests.get(basepath, params=params)
    
    users = (response.json())['FileStatuses']['FileStatus']

    sequences = []
    for user in users:
        user_basepath = basepath + "/" + user['pathSuffix']
        response = requests.get(user_basepath, params=params)
    
        scenes = (response.json())['FileStatuses']['FileStatus']
        for scene in scenes:
            scene_basepath = user_basepath + "/" + scene['pathSuffix']
            response = requests.get(scene_basepath, params=params)
            files = (response.json())['FileStatuses']['FileStatus']
            sequence = []
            for f in files:
                fullname = f['pathSuffix']
                fullname.rstrip('.ipynb')
                # removes datetime info at start of string, and library name
                filename = ('-'.join(fullname.split('-')[3:])) #.rstrip('.ipynb')
                filename = filename[0:len(filename)-6] # removes .ipynb
                sequence.append(filename)
            sequences.append(sequence)

    
    return sequences

    """http://nmnode-0-svc:50070/webhdfs/v1/praxxis?op=LISTSTATUS"""

    """
    1. find model file
    2. load_model() on filename
    3. fit_on_batch or train_on_batch of sequences? OHE first tho 
       - make sure we're training on full names, not just prefixes!
    4. save model to current date!
    """