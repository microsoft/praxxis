"""
imports fixtures from the fixtures db so that they can be used by pytest 
"""

import pytest
from tests.src.praxxis.fixtures.set_roots import init_root, library_root, telemetry_db, library_db, output_root, scene_root, history_db, default_scene_name, current_scene_db, ads_location, rulesengine_root, rulesengine_db, model_root, model_db, start, stop, git_root
from tests.src.praxxis.fixtures.setup import setup
from tests.src.praxxis.fixtures.setup_library import notebooks_list, libraries_list, add_test_library
from tests.src.praxxis.fixtures.set_test_params import set_many_params, set_one_param
from tests.src.praxxis.fixtures.setup_scenes import create_many_scenes, create_one_scene, create_ended_scene, generate_short_history
from tests.src.praxxis.fixtures.setup_rulesengine import create_one_ruleset, create_deactivated_ruleset, mock_input_str