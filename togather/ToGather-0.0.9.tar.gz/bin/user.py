class User:
    """A class to store data about each user, a user name, a list of groups they are a part of"""
    "and list of constraint times. constraints are a pair of time variables to signify ranges"

    def __init__(self, name="", constraints=[], groups=[]):
        self._name = name
        self._groups = groups
        self._constraints = constraints

    @property
    def name(self):
        return self._name

    @property
    def constraints(self):
        return self._constraints

    @constraints.setter
    def constraints(self, constraints):
        self._constraints = constraints

    @property
    def groups(self):
        return self._groups

    @groups.setter
    def groups(self, groups):
        self._groups = groups
