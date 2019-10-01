"""
This file opens a notebook in jupyter
Usually called as a subprocess.
"""


def open_jupyter():
    """opens file in jupyter"""
    import sys
    import nbopen
    import webbrowser

    try:
        nbopen.main([str(sys.argv[1])])
    except webbrowser.Error as e:
        print(e)
        print("Ctrl-C to exit")


if __name__ == "__main__":
    """calls function to open in jupyter"""
    open_jupyter()
