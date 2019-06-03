"""
This file DOES A THING

Dependencies within mtool: none
"""

class Log:

    @staticmethod
    def info(string, value=None):
        if value is None:
            print(string)
        else:
            print(f'{string}: {value}')

    @staticmethod
    def indent(string, value=None):
        Log.info(f'\t{string}', value)

    @staticmethod
    def indent_no_new_line(string, value=None):
        if value is None:
            print(f'\t{string}', end="")
        else:
            print(f'\t{string}: {value}', end="")

    @staticmethod
    def complete():
         print("\b\b\b\b: COMPLETE")

    @staticmethod
    def section(string, value=None):
        print()
        Log.info(string, value)

    @staticmethod
    def header(string, value=None):
        print()
        Log.info(f"{string}:", value)
        print()