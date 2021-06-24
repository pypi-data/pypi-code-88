from PythonDefense.projectile import Projectile
import copy
import math


class Tower:
    def __init__(self, name, damage, attack_speed, range, rect, sprite, projectile_name, projectile_rect,
                 projectile_sprite, ticks, projectile_speed):
        self.name = name
        self.damage = damage
        self.attack_speed = 1000 / attack_speed
        self.range = range
        self.rect = rect
        self.x = rect.x
        self.y = rect.y
        self._sprite = sprite
        self.sprite = sprite
        self.projectile = Projectile(projectile_name, damage, projectile_speed, projectile_rect, projectile_sprite)
        self.ticks = ticks
        self.level = 1
        self.projectile_speed = projectile_speed

    # returns a new copy of its projectile, if it didn't the tower could only shoot once
    def fire_projectile(self, closest):
        self.projectile.closest = closest
        return copy.copy(self.projectile)

    def cords(self):
        return self.x, self.y

    def any_within_range(self, enemies):
        for i in range(len(enemies)):
            if self.within_range(enemies[i].x, enemies[i].y):
                return i
        return -1

    def within_range(self, enemy_x, enemy_y):
        if math.sqrt((enemy_x - self.x) ** 2 + (enemy_y - self.y) ** 2) <= self.range:
            return True
        return False

    # basic upgrade function for towers
    def basic_upgrade(self, damage, attack_speed, projectile_speed, range):
        self.damage += damage
        self.attack_speed -= 1000 / (attack_speed * 2)
        self.projectile_speed += projectile_speed
        self.projectile = Projectile(self.projectile.name, self.damage, self.projectile_speed, self.projectile.rect,
                                     self.projectile.sprite)
        self.range += range
        if self.level < 5:
            self.level = self.level + 1

    # Checks if you can level up tower (MAX LEVEL 5)
    def level_up(self):
        if self.level < 5:
            return True
        return False
