class UsefulTsgs:

    # List of the useful TSGs whose PRECONDITION CHECKs
    # are a match for the current cluster state
    #
    _useful_tsgs = []

    def add(self, filename):
        self._useful_tsgs.append(filename)

    @property
    def count(self):
        return len(self._useful_tsgs)

    def for_each(self, fn):
        for filename in self._useful_tsgs:
            fn(filename)