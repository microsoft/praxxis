"""
This file contains the Console class, with useful dialog and a spinner for the
user experience of mtool. 

Dependencies within mtool: mtool/spinner.py
"""
import os
import sys

from src.mtool.util import spinner

class Console:
    """Useful functions for console output"""
    progress_text = "RUNNING PRECONDITION CHECK... "

    # Twirling console spinner to show progress
    spinner = spinner.Spinner()

    def print_banner(self, directory):
        """Prints message for TSG suggestions"""
        print()
        print("Analyzing current cluster state for applicable TSGs.  View output at:")
        print()
        print("\tstart {0}".format(directory))
        print()

    def print_running(self, name):
        """Prints message for running a file"""
        print("\t{0}:  ".format(name), end="")
        print(self.progress_text, end="")
        sys.stdout.flush()

    def spinner_start(self):
        """Starts the spinner"""
        self.spinner.start()

    def spinner_stop(self):
        """Stops the spinner"""
        self.spinner.stop()

    def remove_progress_text(self):
        """Remove the progress_text i.e. 'RUNNING PRECONDITION CHECK...'"""
        for x in range(len(self.progress_text) + 1):
            print("\b", end="")

    def print_match(self):
        """Print that pre-conditions match"""
        print("PRE-CONDITIONS MATCH!               ")

    def print_non_match(self):
        """Print that pre-conditions do not match"""
        print("NON-MATCH                           ")

    def print_precondition_check_not_found(self, name):
        """Print that there are no pre-conditions found"""
        print("\t{0}:  DOES NOT INCLUDE PRECONDITION CHECK... ".format(name))

    def print_finished(self):
        """Print end of analysis message"""
        print()
        print("Finished analyzing cluster state. ", end="")

    def no_useful_tsgs(self):
        """Print no useful TSGs found"""
        print("No useful TSGs found for current cluster state.")

    def found_useful_tsgs(self, fn_for_each, count):
        """Print list of useful TSGs, prompt to open in ADS"""
        print("Found {0} TSG{1} that may be useful:  ".format(count, '' if count == 1 else 's'))
        print()
        fn_for_each(Console.print_tsg)
        print()
        print("Open the above notebook{0} in 'Azure Data Studio' to solve the issue (F1 -> Open Notebook).".format('' if count == 1 else 's'))
        print()
        print("To install 'Azure Data Studio', download from:")
        print()
        print("\thttps://docs.microsoft.com/en-us/sql/azure-data-studio/download")
            
    def print_tsg(self, filename):
        """Print name of TSG"""
        print("\t{0}".format(os.path.splitext(os.path.basename(filename))[0]))

    def print_end_banner(self, directory):
        """Prompt to view HTML output"""
        print()
        print("View notebook HTML output from cluster analysis here:")
        print()
        print("\tstart {0}".format(directory))