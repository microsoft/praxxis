import json
import os

class Args:

    _argv = None

    def __init__(self, argv):
        self._argv = argv

    @property
    def first_arg_upper(self):
        return str(self._argv[1].upper())

    @property
    def the_ordinal(self):
        return int(self._argv[1])

    @property
    def the_value(self):
        if len(self._argv) != 3:
            raise Exception(f'\n\nPlease provide a value, i.e. m se 1 "My value"')

        return str(self._argv[2])

    @property
    def to_html(self):
        if len(self._argv) >= 3:
            if str(self._argv[2].lower()) == "--html":
                return True
            else:
                return False
        else:
            return False

    @property
    def first_arg_lower(self):
        return str(self._argv[1].lower())

    @property
    def second_arg(self):
        return str(self._argv[2])

    @property
    def search_term(self):
        if len(self._argv) == 1:
            raise Exception(f"\n\nPlease provide a search term, i.e. m search SOP")

        return self.first_arg_lower

    @property
    def arg_provided(self):
        if len(self._argv) == 1:
            return False
        else:
            return True

    def ordinal_to_list_item(self, list_filename):

        if len(self._argv) == 1:
            raise Exception(f"\n\nPlease provide an ordinal (a number from a list), or a name (e.g. of a notebook or scene)")

        list_item = None

        if str.isdigit(self.first_arg_lower):

            ordinal = int(self.first_arg_lower)

            with open(list_filename, encoding="utf8") as json_file: 
                items = json.loads(json_file.read())

                for item in items:
                    if (item[0] == ordinal):
                        list_item = item[1].lower()
                        break

            if list_item is None:
                raise Exception(f"\n\nOrdinal '{ordinal}' does not exist in list. Use any of the m l* commands to generate (and display) the list.")
        else:
            list_item = self.first_arg_lower

        return list_item