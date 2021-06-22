import os

from mgsc.blueprints import Repository


class Namespace:
    def __init__(self, name: str, parent=None, id=None):
        self.name = name
        self.parent = parent
        self.id = id
        self.repositories = None
        self.path = None

    def __repr__(self):
        return f"{self.path or self.name} ({self.id})"
