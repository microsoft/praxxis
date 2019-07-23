"""
This file lists all scenes
"""

def list_scene(root, history_db):
    """lists scenes by fetching from sqlite db"""
    from src.praxxis.sqlite import sqlite_scene
    from src.praxxis.display import display_scene

    ended_scenes = sqlite_scene.get_ended_scenes(history_db)
    active_scenes = sqlite_scene.get_active_scenes(history_db)
    current_scene = sqlite_scene.get_current_scene(history_db)

    sqlite_scene.dump_scene_list(history_db)

    sqlite_scene.write_scene_list(history_db, ended_scenes)
    sqlite_scene.write_scene_list(history_db, active_scenes)
    sqlite_scene.write_scene_list(history_db, [(current_scene,)])

    display_scene.display_list_scene(ended_scenes, active_scenes, current_scene)

    return(ended_scenes + active_scenes)
