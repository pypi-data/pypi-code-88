# -*- coding: utf-8 -*-

class StringStdOut:
    """
    This is a dummy stdout to retrieve the output of asciitable.write().
    """
    def __init__(self):
        self.content = ''

    def write(self, content):
        self.content += content