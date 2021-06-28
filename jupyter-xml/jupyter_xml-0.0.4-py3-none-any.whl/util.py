import argparse
import re


class StopCellExecution(Exception):
    def _render_traceback_(self):
        pass


class MagicParser(argparse.ArgumentParser):

    def exit(self, status=0, message=None):
        if status:
            print("Parser exited with error: {}".format(message))
        raise StopCellExecution

    def error(self, message):
        print("Error: {}".format(message))
        self.exit()


def strip_comments(text):
    """Special comment strip function for formats which do not support comments (e.g. xpath)"""
    return re.sub("###.*$", '', text, 0, re.M)
