from django.db import models


class WorkflowDTO():

    def __init__(self, id, toolID, name, description, isPublic, owner):
        self.id = id
        self.toolID = toolID
        self.name = name
        self.description = description
        self.isPublic = isPublic
        self.owner = owner

    def getId(self):
        return self.id

    def getToolID(self):
        return self.toolID

    def get_name(self):
        return self.name

    def getDescription(self):
        return self.description

    def get_IsPublic(self):
        return self.isPublic

    def getOwner(self):
        return self.owner
