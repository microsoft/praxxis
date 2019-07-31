import pytest

def test_add_one_output(setup, generate_short_history, output_root, current_scene_db, telemetry_db):
    from src.praxxis.notebook import add_output
    from tests.src.praxxis.util import dummy_object
    from src.praxxis.sqlite import sqlite_scene
    import json

    test_str = "TESTING\n123"

    test_args = dummy_object.make_dummy_output_to_add(test_str)

    message = add_output.add_output(test_args, output_root, current_scene_db, telemetry_db)

    assert message == test_str

    history = sqlite_scene.get_recent_history(current_scene_db, 1)
    with open(history[0][1]) as f:
        file_data = json.load(f)
        f.close()
    
    assert file_data["cells"]
    found_cell = False
    for cell in file_data["cells"]:
        # check if cell format is correct to be the output added cell
        output = cell.get('outputs')
        if output != None and output[0].get("text") != None:
            # check if this cell output matches up
            if output[0].get("text")[0] == test_str:
                found_cell = True

    assert found_cell