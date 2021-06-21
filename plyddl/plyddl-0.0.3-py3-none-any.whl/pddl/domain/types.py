class Type:

    def __init__(self, instances, type):
        self.instances = instances
        self.type = type

    def add(self, instance):
        self.instances.append(instance)


class Variables:

    def __init__(self, instances, type):
        self.instances = instances
        self.type = type

    def add(self, instance):
        self.instances.insert(0,instance)
