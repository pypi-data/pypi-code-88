class StringBuilder(object):
    def __init__(self, s=""):
        self.s = s

    def append(self, s):
        self.s = self.s + s
        return self

    def __str__(self):
        return self.s
