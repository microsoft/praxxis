import pytest

@pytest.fixture(scope="function")
def set_many_params(scene_root, history_db, current_scene_db):
    from src.praxxis.parameter import set_param
    from src.praxxis.parameter import delete_param
    from tests.src.praxxis.util import dummy_object
    from src.praxxis.util import error

    name1 = dummy_object.make_dummy_parameter("generated_multiple_param", "test")
    set_param.set_param(name1, scene_root, history_db, current_scene_db)
    
    name2 = dummy_object.make_dummy_parameter("generated_multiple_param1", "test")
    set_param.set_param(name2, scene_root, history_db, current_scene_db)
    yield
    try:
        delete_param.delete_parameter(name1, scene_root, history_db, current_scene_db)
        delete_param.delete_parameter(name2, scene_root, history_db, current_scene_db)
    except error.ParamNotFoundError:
        pass


@pytest.fixture(scope="function")
def set_one_param(scene_root, history_db, current_scene_db):
    from src.praxxis.parameter import set_param
    from src.praxxis.parameter import delete_param
    from tests.src.praxxis.util import dummy_object
    from src.praxxis.util import error

    name1 = dummy_object.make_dummy_parameter("generated_single_param", "test")
    set_param.set_param(name1, scene_root, history_db, current_scene_db)
    
    yield 
    try:
        delete_param.delete_parameter(name1, scene_root, history_db, current_scene_db)
    except error.ParamNotFoundError:
        pass

