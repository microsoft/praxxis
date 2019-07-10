def pull_notebook_environment(args, library_db, current_scene_db):
    from src.mtool.util.sqlite import sqlite_environment
    from src.mtool.environment import list_env

    envs = list_env.list_notebook_env(args, library_db, current_scene_db)
    sqlite_environment.set_many_envs(current_scene_db, envs)


def pull_library_environment(args, library_db, current_scene_db):
    from src.mtool.util.sqlite import sqlite_environment
    from src.mtool.environment import list_env

    envs = list_env.list_library_env(args, library_db, current_scene_db)
    sqlite_environment.set_many_envs(current_scene_db, envs)
