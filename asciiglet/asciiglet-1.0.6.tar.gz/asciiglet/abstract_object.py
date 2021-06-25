class AbstractObject:
    def __init__(self):
        self.destroying = False

        self.name = ""

    def __destroy__(self):
        pass

    def destroy(self):
        self.destroying = True
        self.__destroy__()
