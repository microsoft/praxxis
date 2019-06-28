"""
This file contains all of the display functions for scenes
"""

def display_change_scene(name):
    """the display function for chaging scene name"""
    print(f"Scene changed to: {name}")


def display_current_scene(name):
    """the display function for showing the current scene""" 
    print(f"Current scene: {name}")


def display_init_scene_folder(root):
    """the display function for initializing the scene folder"""
    print(f"Created scenes directory at {root}")


def display_init_scene_db(db_root):
    """the display function for initializing the scene database"""
    print(f"Created history db at {db_root}")


def display_new_scene(name):
    """the display function for creating a new scene"""
    print(f"Created new scene \"{name}\"")


def display_delete_scene_success(name):
    """the display function for successfully deleting a scene""" 
    print(f"Deleted scene: {name}")


def display_end_scene_success(name):
    """the display function for ending a scene""" 
    print(f"{name} ended")


def display_list_scene(ended, active, current):
    """the display function for listing scenes""" 
    i = 0
    print(f"Ended scenes:")
    for scene in ended:
        i += 1
        print(f"\t{i}.\t{scene[0]}")
    if (len(ended) == 0):
        print(f"\tNone")
    print(f"\nActive scenes:")
    for scene in active:
        i += 1
        print(f"\t{i}.\t{scene[0]}")
    if (len(active) == 0):
        print(f"\tNone")
    print(f"\nCurrent scene: {current}")

def display_resume_scene(name):
    """the display function for resuming the scene""" 
    print(f"{name} resumed")


def display_history(current_scene, notebooks):
    """the display function for showing the history of the current scene"""
    print(f"History for scene {current_scene}")
    print(f"\tTIMESTAMP\t\tLIBRARY\t\t\tNOTEBOOK")
    num = len(notebooks)
    for notebook in notebooks:
        print(f"  {num}.\t{notebook[0]}\t{notebook[2]}\t\t{notebook[1]}")
        num -= 1
