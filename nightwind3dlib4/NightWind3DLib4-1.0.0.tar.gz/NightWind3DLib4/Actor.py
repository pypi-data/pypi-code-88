from direct.directbase.DirectStart import base
from panda3d.core import *
from direct.actor.Actor import Actor


class Character:
    def __init__(self, ModelName, AnimsName, pos, ColliderName):
        self.actor = Actor(ModelName, AnimsName)
        self.actor.reparentTo(render)
        self.actor.setPos(pos)

        capsule = CollisionBox((0.5, -11, 5), 3.5, 7, 5)
        ColliderNode = CollisionNode(ColliderName)
        ColliderNode.addSolid(capsule)
        self.collider = self.actor.attachNewNode(ColliderNode)
        self.collider.show()

    def CleanUp(self):
        if self.collider is not None:
            base.cTrav.removeCollider(self.collider)
            self.collider = None
        if self.actor is not None:
            self.actor.cleanup()
            self.actor.removeNode()
            self.actor = None
