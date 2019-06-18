from src.mtool.notebook import run_notebook

def test_run_notebook(args, root, outfile_root, current_scene_db, library_root, library_db):
    run_notebook.run_notebook(args, root, outfile_root, current_scene_db, library_root, library_db)