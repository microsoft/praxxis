if __name__ == "__main__":
    import sys
    import nbopen
    import webbrowser
    
    try:        
        nbopen.main([str(sys.argv[1])])
    except webbrowser.Error as e:
        print(e)
        print("Ctrl-C to exit")
