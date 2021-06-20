class ToolDTO():

    def __init__(self, id, name, description, imageIDs):
        self.id = id
        self.name = name
        self.description = description
        self.imageIDs = imageIDs

    def getId(self):
        return self.id

    def get_name(self):
        return self.name

    def getDescription(self):
        return self.description

    def getImageIDs(self):
        return self.description
