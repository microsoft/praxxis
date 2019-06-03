"""
This file contains a stub class, UsefulTsgs, that may be useful for 
implementing Bayesian suggestions based on current cluster state.

Dependencies within mtool: none
"""

class UsefulTsgs:
    """Manages useful TSGs for suggestions"""
    # List of the useful TSGs whose PRECONDITION CHECKs
    # are a match for the current cluster state
    _useful_tsgs = []

    def add(self, filename):
        """Adds a file to list of useful TSGs"""
        self._useful_tsgs.append(filename)

    @property
    def count(self):
        """Returns number of useful TSGs"""
        return len(self._useful_tsgs)

    def for_each(self, fn):
        for filename in self._useful_tsgs:
            fn(filename)