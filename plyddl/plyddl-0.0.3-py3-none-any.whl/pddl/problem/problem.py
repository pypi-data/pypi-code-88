class Problem:

    def __init__(self, name, domain, objects, init, goal, metric=None):
        self.name = name
        self.domain_name = domain
        self.objects = objects
        self.init = init
        self.goal = goal
        self.metric = metric
