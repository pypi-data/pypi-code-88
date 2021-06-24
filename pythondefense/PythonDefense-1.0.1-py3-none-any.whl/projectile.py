from PythonDefense.helper_functions import scale
import math


class Projectile:
    def __init__(self, name, damage, projectile_speed, rect, sprite):
        self.name = name
        self.damage = damage
        self.projectile_speed = projectile_speed
        self.rect = rect
        self.x = rect.x
        self.y = rect.y
        self._sprite = sprite
        self.sprite = sprite
        self.remove = False
        self.closest = -1

    def cords(self):
        return self.x, self.y

    def motion(self, change_x, change_y):
        x_component = change_x - self.x
        y_component = change_y - self.y
        if x_component == 0:
            x_component = .0000000000001
        x_direction = math.cos(math.atan2(y_component, x_component))
        y_direction = math.sin(math.atan2(y_component, x_component))
        self.x = (self.x + x_direction * scale(1) * self.projectile_speed)
        self.y = (self.y + y_direction * scale(1) * self.projectile_speed)
        self.rect.x = self.x
        self.rect.y = self.y

    def absolute_position(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        self.rect.x = self.x
        self.rect.y = self.y

    def flag_removal(self):
        self.remove = True
