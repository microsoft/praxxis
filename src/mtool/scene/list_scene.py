"""
This file calls a function to list all scenes.

Dependencies within mtool: mtool/mtool.py
"""

import os

def list_scene(root):
    output = [dI for dI in os.listdir(root) if os.path.isdir(os.path.join(root,dI))]
    print(output)

 