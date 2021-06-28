class FlexDot:
    def __init__(self):
        self.data = {}

    def clear(self):
        self.data = {}

    def get(self, key):
        if key in self.data:
            return self.data[key]
        return 0

    def put(self, key, value):
        self.data[key] = value
