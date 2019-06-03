"""
This file contains the Spinner class, which implements a twirling console
spinner as a loading animation.

Dependencies within mtool: none
"""

import sys, time, threading

# Twirling console spinner to show progress
#
# https://stackoverflow.com/questions/4995733/how-to-create-a-spinning-command-line-cursor
class Spinner:
    """Twirling console spinner animation for console"""
    busy = False
    delay = 0.2

    @staticmethod
    def spinning_cursor():
        """Gets next step in spinning cursor"""
        while 1: 
            for cursor in '|/-\\': yield cursor

    def __init__(self, delay=None):
        """Initializes spinner"""
        self.spinner_generator = self.spinning_cursor()
        if delay and float(delay): self.delay = delay

    def spinner_task(self):
        """Spinner writes and flushes to create appearance of spin"""
        while self.busy:
            sys.stdout.write(next(self.spinner_generator))
            sys.stdout.flush()
            time.sleep(self.delay)
            sys.stdout.write('\b')
            sys.stdout.flush()

    def start(self):
        """Starts the spinner on a new thread"""
        self.busy = True
        threading.Thread(target=self.spinner_task).start()

    def stop(self):
        """Stops the spinner"""
        self.busy = False
        time.sleep(self.delay)