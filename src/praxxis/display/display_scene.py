"""
This file contains all of the display functions for scenes
"""

def display_change_scene(name):
    """the display function for chaging scene name"""
    print("Scene changed to: %s" %(name))


def display_current_scene(name):
    """the display function for showing the current scene""" 
    print("Current scene: %s" %(name))


def display_init_scene_folder(root):
    """the display function for initializing the scene folder"""
    print("Created scenes directory at %s" %(root))


def display_init_scene_db(db_root):
    """the display function for initializing the scene database"""
    print("Created history db at %s" %(db_root))


def display_new_scene(name):
    """the display function for creating a new scene"""
    print("Created new scene \"%s\"" %(name))


def display_delete_scene_success(name):
    """the display function for successfully deleting a scene""" 
    print("Deleted scene: %s" %(name))


def display_end_scene_success(name):
    """the display function for ending a scene""" 
    print("%s ended" %(name))


def display_list_scene(ended, active, current):
    """the display function for listing scenes""" 
    i = 0
    print("Ended scenes:")
    for scene in ended:
        i += 1
        print("\t%s.\t%s" %(i, scene[0]))
    if (len(ended) == 0):
        print("\tNone")
    print("\nActive scenes:")
    for scene in active:
        i += 1
        print("\t%s.\t%s" %(i, scene[0]))
    if (len(active) == 0):
        print("\tNone")
    print("\nCurrent scene: %s" %(current))


def display_resume_scene(name):
    """the display function for resuming the scene""" 
    print("%s resumed" %(name))


def display_history(current_scene, notebooks):
    """the display function for showing the history of the current scene"""
    print("History for scene %s" %(current_scene))
    print("\tTIMESTAMP (UTC)\t\tLIBRARY\t\t\tNOTEBOOK")
    num = len(notebooks)
    for notebook in notebooks:
        print("  %s.\t%s\t%s\t\t%s" %(num, notebook[0], notebook[2], notebook[1]))
        num -= 1
