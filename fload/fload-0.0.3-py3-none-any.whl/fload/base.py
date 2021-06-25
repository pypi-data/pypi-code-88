class FloadModule:
    def init(self, ops):
        pass

    def add_arguments(self, parser):
        pass 


class Pipeline(FloadModule):
    def process(self, item):
        pass


class Source(FloadModule):
    def start(self):
        pass
