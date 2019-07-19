def pull_notebook_parameter(args, library_db, current_scene_db):
    from src.mtool.util.sqlite import sqlite_parameter
    from src.mtool.parameter import list_param

    params = list_param.list_notebook_param(args, library_db, current_scene_db)
    sqlite_parameter.set_many_params(current_scene_db, params)


def pull_library_parameter(args, library_db, current_scene_db):
    from src.mtool.util.sqlite import sqlite_parameter
    from src.mtool.parameter import list_param

    params = list_param.list_library_param(args, library_db, current_scene_db)
    sqlite_parameter.set_many_params(current_scene_db, params)
