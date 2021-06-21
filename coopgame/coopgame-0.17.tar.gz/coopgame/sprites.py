import pygame
from coopstructs.vectors import Vector2
from coopgame.colors import Color
from typing import Dict, Tuple

class MySprite(pygame.sprite.Sprite):
    def __init__(self, id:str, init_pos: Vector2, width: int, height: int):
        super().__init__()

        self.id = id

        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.surf = pygame.Surface([width, height]).convert()
        self.surf.fill(Color.PINK.value)
        self.surf.set_colorkey(Color.PINK.value)

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.surf.get_rect()
        self.set_pos(init_pos)

    def set_pos(self, pos: Vector2):
        self.rect = self.surf.get_rect(
            center=(
                pos.x,
                pos.y
            )
        )

    def blit(self, surface: pygame.Surface, display_handle: bool = False, display_rect: bool = False):

        surface.blit(self.surf, (self.rect.x, self.rect.y))
        if display_handle:
            pygame.draw.rect(surface, Color.RED.value, [self.rect.x, self.rect.y, 1, 1])
        if display_rect:
            pygame.draw.rect(surface, Color.RED.value, [self.rect.x, self.rect.y, self.rect.width, self.rect.height], 1)

class RectangleSprite(MySprite):
    def __init__(self, id:str, init_pos: Vector2, color: Color, width: int, height: int):
        # Call the parent class (Sprite) constructor
        MySprite.__init__(self, id, init_pos, width, height)

        pygame.draw.rect(self.surf, color.value, [0, 0, width, height])

class ImageSprite(MySprite):
    def __init__(self, id: str, init_pos: Vector2, color: Color, width: int, height: int):
        # Call the parent class (Sprite) constructor
        MySprite.__init__(self, id, init_pos, width, height)

class AnimatedSprite(MySprite):
    def __init__(self, id: str, init_pos: Vector2, animation_dict: Dict[str, Tuple], default_animation_key = None):
        self._animation_dict = animation_dict

        self._animation_key = default_animation_key
        self._animation_index = 0

        # Call the parent class (Sprite) constructor
        first_image = next(iter(self._animation_dict.values()))[0]
        MySprite.__init__(self, id, init_pos, first_image.get_width(), first_image.get_height())

        self.image = None
        self._set_image()

    def set_animation(self, animation: str):
        if animation in self._animation_dict.keys() and animation != self.current_animation:
            self._animation_key = animation
            self._animation_index = 0

    def increment_animation_phase(self, loop: bool = True):
        ''':return True if animation cycle has completed, False if still in cycle
        :param loop allows caller to specify whether or not to loop the aniimation (default True)'''
        ret = False
        self._animation_index += 1
        if self._animation_index >= len(self._animation_dict[self._animation_key]):
            self._animation_index = 0 if loop else len(self._animation_dict[self._animation_key]) - 1
            ret = True

        self._set_image()
        return ret

    def _set_image(self):
        self.surf.fill(Color.PINK.value)
        self.image = self._animation_dict[self._animation_key][self._animation_index]
        self.rect = self.image.get_rect( center = self.rect.center)
        self.surf.blit(self.image, (0, 0))

    @property
    def current_animation(self):
        return self._animation_key