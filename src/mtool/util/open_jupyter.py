if __name__ == "__main__":
    import sys
    import nbopen
    import subprocess
    import os

    os.environ["CATALYST_LOG_LEVEL"] = "15"
    #this sets the log level for catalyst, the ipython logger to 15. 
    #15 corresponds to the critical warning level.

    nbopen.main([str(sys.argv[1])])
