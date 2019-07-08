def test_telemetry(setup, current_scene_db, add_test_library, outfile_root, library_root):
    import os
    from src.mtool.util import telemetry
    from src.mtool.notebook import run_notebook
    from tests.src.mtool.util import dummy_object

    notebook1 = dummy_object.make_dummy_notebook("", os.path.join(library_root,  'test_notebooks'))

    local_copy = run_notebook.execute(current_scene_db, notebook1, outfile_root)
    assert os.path.exists(local_copy)