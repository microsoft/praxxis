def test_telemetry(current_scene_db, add_test_library, outfile_root):
    from src.mtool.util import telemetry
    from src.mtool.notebook import run_notebook
    from tests.src.mtool.util import dummy_object

    notebook1 = dummy_object.make_dummy_notebook()

    local_copy = run_notebook.execute(current_scene_db, notebook1, outfile_root)