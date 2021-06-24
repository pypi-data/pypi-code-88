import pygame
from PythonDefense.helper_functions import scale
from PythonDefense.enemy import Enemy

# Directions
UP, LEFT, DOWN, RIGHT = 0, 90, 180, 270


class Rounds:
    # TODO: remove enemy_size and enemy_sprite, class round shouldn't need to know about the enemies
    # changed round initialization to 0 so 1st level doesn't start until button is pressed
    def __init__(self, start_cords, enemy_size, enemy_sprite, round=0):
        self.enemy_size = enemy_size
        self.enemy_sprite = enemy_sprite
        self.x, self.y = start_cords
        self.round = round

    def spawn(self, num_enemies, speed, enemy_size, enemy_sprite):
        enemies = []
        for count in range(0, num_enemies):
            enemy_rect = pygame.Rect(0, 0, enemy_size, enemy_size)
            enemy = Enemy(f'enemy_{count}', 100, speed, enemy_rect, enemy_sprite)
            enemy.face(DOWN)
            enemy.y = Enemy.enemy_count * scale(-32)  # separates enemies when they spawn
            enemy.x = self.x
            enemies.append(enemy)
        return enemies

    def level(self):
        enemies = []
        if self.round == 1:
            enemies1 = self.spawn(5, 5, self.enemy_size, self.enemy_sprite)
            enemies = enemies1
        elif self.round == 2:
            enemies1 = self.spawn(5, 5, self.enemy_size, self.enemy_sprite)
            enemies2 = self.spawn(30, 5, self.enemy_size, self.enemy_sprite)
            enemies = enemies1 + enemies2
        elif self.round == 3:
            enemies1 = self.spawn(5, 5, self.enemy_size, self.enemy_sprite)
            enemies2 = self.spawn(3, 5, self.enemy_size, self.enemy_sprite)
            enemies = enemies1 + enemies2
        return enemies

    def next_round(self):
        self.round += 1
