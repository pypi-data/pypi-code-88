from .abstract_object import AbstractObject
from .transform import Transform


class GameObject(AbstractObject):
    def __init__(self, transform=None):
        super().__init__()
        if transform is None:
            transform = Transform()

        self.transform = transform
        self.transform.gameObject = self

    def __destroy__(self):
        self.transform.destroy()

    def update(self, dt):
        pass

    def draw(self):
        pass
