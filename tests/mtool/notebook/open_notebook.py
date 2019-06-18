from src.mtool.notebook import open_notebook

def test_open_notebook(args, current_scene_db, library_db, ads_location):
    open_notebook.open_notebook(args, current_scene_db, library_db, ads_location)


def test_display_as_html(filename, html_outfile):
    open_notebook.display_as_html(filename, html_outfile)