"""
This file attempts to diagnose cluster problems.

Dependencies within mtool: mtool/mtool.py,
    diag/console.py, diag/useful_tsgs.py
"""
import os
import sys
from mtool.cli import mtool
from mtool.cli import console
from mtool.util import useful_tsgs  


m = None
console = console.Console()
useful_tsgs = useful_tsgs.UsefulTsgs()

def diag(arg):
    global m 
    m = mtool.MTool(arg)

    m.set_environment_overrides_for_scene()

    console.print_banner(m.working_dir)
    m.for_each_notebook(diagnose)
    console.print_finished()

    if useful_tsgs.count == 0:
        console.no_useful_tsgs()
    else:
        console.found_useful_tsgs(useful_tsgs.for_each, useful_tsgs.count)

    console.print_end_banner(m.working_dir)

    if useful_tsgs.count > 0:
        sys.exit(1)


def diagnose(filename):
    """Attempts to determine if notebook at filename is useful for issue"""
    notebook = m.notebook(filename)

    if len(sys.argv) == 2:
        category = sys.argv[1]
    else:
        category = 'install'        

    metadata = notebook.metadata
    if metadata.has_azdata_diagnostic_categories and metadata.has_category(category):

        if metadata.has_a_precondition_check:
            outputfile = notebook.get_local_copy_filename('.ipynb')

            notebook.generate_notebook_only_upto_precondition_check(metadata.notebook_content_as_json, outputfile, metadata.precondition_check_header)

            console.print_running(notebook.name)
            console.spinner_start()

            notebook.execute(outputfile)

            console.spinner_stop()
            console.remove_progress_text()

            # Run the shortened notebook (only up to the PRECONDITION CHECK)
            # to see if this TSG is helpful for the current cluster state
            executed_notebook = m.notebook(outputfile)

            if executed_notebook.metadata.is_precondition_true:
                console.print_match()
                useful_tsgs.add(filename)
            else:
                console.print_non_match()

            executed_notebook.convert_to_html(filename, outputfile) # For easy sharing with CSS etc.
        else:
            console.print_precondition_check_not_found(notebook.name)

