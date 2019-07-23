def get_library_by_ordinal(library_db, ordinal, start, end):
    """gets scene by ordinal using the sqlite history db"""
    from src.praxxis.sqlite import sqlite_library
    from src.praxxis.util import error
    if f"{ordinal}".isdigit():
        try:
            library = sqlite_library.list_libraries(library_db, start, end)[0]
        except error.LibraryNotFoundError as e:
            raise e
        else:
            return(library[0])