
class Habit:

    def __init__(self, name, quota , period):
        self.name = name
        self.quota = quota
        self.period = period

    def __repr__(self):
        return "Habit('{}', '{}', {})".format(self.name, self.quota, self.period)