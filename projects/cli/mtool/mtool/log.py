"""
This file contains the Log class, which provides a base framework for eventual
logging in mtool.

Dependencies within mtool: none
"""

class Log:

    @staticmethod
    def info(string, value=None):
        """Prints/prints to log the string"""
        if value is None:
            print(string)
        else:
            print(f'{string}: {value}')

    @staticmethod
    def indent(string, value=None):
        """Indents the string and prints in the log"""
        Log.info(f'\t{string}', value)

    @staticmethod
    def indent_no_new_line(string, value=None):
        """Indents and prints the string without a newline"""
        if value is None:
            print(f'\t{string}', end="")
        else:
            print(f'\t{string}: {value}', end="")

    @staticmethod
    def complete():
        """Prints end-of-log message"""
         print("\b\b\b\b: COMPLETE")

    @staticmethod
    def section(string, value=None):
        """Prints a yet-to-be-specified portion of the log"""
        print()
        Log.info(string, value)

    @staticmethod
    def header(string, value=None):
        """Prints a header in the log"""
        print()
        Log.info(f"{string}:", value)
        print()