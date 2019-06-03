"""
This file contains the Console class, with useful dialog and a spinner for the
user experience of mtool. 

Dependencies within mtool: mtool/spinner.py
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))

import spinner

class Console:
    """Useful functions for console output"""
    progress_text = "RUNNING PRECONDITION CHECK... "

    # Twirling console spinner to show progress
    spinner = spinner.Spinner()

    def print_banner(self, directory):
        """Prints """
        print()
        print("Analyzing current cluster state for applicable TSGs.  View output at:")
        print()
        print("\tstart {0}".format(directory))
        print()

    def print_running(self, name):
        print("\t{0}:  ".format(name), end="")
        print(self.progress_text, end="")
        sys.stdout.flush()

    def spinner_start(self):
        self.spinner.start()

    def spinner_stop(self):
        self.spinner.stop()

    # Remove the progress_text i.e. 'RUNNING PRECONDITION CHECK...'
    def remove_progress_text(self):
        for x in range(len(self.progress_text) + 1):
            print("\b", end="")

    def print_match(self):
        print("PRE-CONDITIONS MATCH!               ")

    def print_non_match(self):
        print("NON-MATCH                           ")

    def print_precondition_check_not_found(self, name):
        print("\t{0}:  DOES NOT INCLUDE PRECONDITION CHECK... ".format(name))

    def print_finished(self):
        print()
        print("Finished analyzing cluster state. ", end="")

    def no_useful_tsgs(self):
        print("No useful TSGs found for current cluster state.")

    def found_useful_tsgs(self, fn_for_each, count):
        print("Found {0} TSG{1} that may be useful:  ".format(count, '' if count == 1 else 's'))
        print()
        fn_for_each(Console.print_tsg)
        print()
        print("Open the above notebook{0} in 'Azure Data Studio' to solve the issue (F1 -> Open Notebook).".format('' if count == 1 else 's'))
        print()
        print("To install 'Azure Data Studio', download from:")
        print()
        print("\thttps://docs.microsoft.com/en-us/sql/azure-data-studio/download")

    def print_tsg(filename):
        print("\t{0}".format(os.path.splitext(os.path.basename(filename))[0]))

    def print_end_banner(self, directory):
        print()
        print("View notebook HTML output from cluster analysis here:")
        print()
        print("\tstart {0}".format(directory))