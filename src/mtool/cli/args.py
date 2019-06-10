"""
This file contains class Args, which handles command line input.

Dependencies within mtool: none
"""
import json
import os

class Args:
    """Handles command line arguments"""
    _argv = None

    def __init__(self, argv):
        """Initialize self._argv as list of arguments from command line"""
        self._argv = argv

    @property
    def first_arg_upper(self):
        """Returns second command line input (1st argument), uppercase"""
        return str(self._argv[1].upper())

    @property
    def the_ordinal(self):
        """Returns first argument as int"""
        return int(self._argv[1])

    @property
    def the_value(self):
        """Returns 2nd argument (3rd input), raises error if not provided"""
        if len(self._argv) != 3:
            raise Exception(f'\n\nPlease provide a value, i.e. m se 1 "My value"')

        return str(self._argv[2])

    @property
    def to_html(self):
        """Checks if --html argument provided"""
        if len(self._argv) >= 3:
            if str(self._argv[2].lower()) == "--html":
                return True
            else:
                return False
        else:
            return False

    @property
    def first_arg_lower(self):
        """Returns 1st argument (2nd CL input) lowercase"""
        return str(self._argv[1].lower())

    @property
    def second_arg(self):
        """Returns 2nd argument"""
        return str(self._argv[2])

    @property
    def search_term(self):
        """Gets search term (1st argument)"""
        if len(self._argv) == 1:
            raise Exception(f"\n\nPlease provide a search term, i.e. m search SOP")

        return self.first_arg_lower

    @property
    def arg_provided(self):
        """Returns whether any arguments were given"""
        if len(self._argv) == 1:
            return False
        else:
            return True

    def ordinal_to_list_item(self, list_filename):
        """Returns list item referenced by input ordinal"""
        if len(self._argv) == 1:
            raise Exception(f"\n\nPlease provide an ordinal (a number from a list), or a name (e.g. of a notebook or scene)")

        list_item = None

        if str.isdigit(self.first_arg_lower):

            ordinal = int(self.first_arg_lower)

            with open(list_filename, encoding="utf8") as json_file: 
                items = json.loads(json_file.read())

                for item in items:
                    if (item[0] == ordinal):
                        list_item = os.path.join(item[2].lower(), item[2].lower(), item[1].lower())
                        break

            if list_item is None:
                raise Exception(f"\n\nOrdinal '{ordinal}' does not exist in list. Use any of the m l* commands to generate (and display) the list.")
        else:
            list_item = [self.first_arg_lower]

        return list_item