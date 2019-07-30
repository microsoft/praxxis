"""
library specific utilities
"""

def get_library_by_ordinal(library_db, ordinal, start, end):
    """gets library by ordinal using the sqlite history db"""
    from src.praxxis.sqlite import sqlite_library
    from src.praxxis.util import error

    if f"{ordinal}".isdigit():
        try:
            library = sqlite_library.list_libraries(library_db, start, end)
        except error.LibraryNotFoundError as e:
            raise e
        else:
            #this converts the ordinal to an int, and gets the name of that ordinal out of the list
            return(library[int(ordinal)-1][0])