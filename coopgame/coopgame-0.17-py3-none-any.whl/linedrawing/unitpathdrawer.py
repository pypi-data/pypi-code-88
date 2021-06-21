from coopgame.pygridhandler import PyGridHandler
from coopgraph.grids import GridSystem
from coopgame.colors import Color
import pygame
import math
from typing import Hashable
import numpy as np

class UnitPathDrawer():

    def __init__(self, toggled_key: Hashable):
        self.toggled_key = toggled_key

    def draw(self
             , grid: GridSystem
             , grid_handler: PyGridHandler
             , surface:pygame.Surface
             , line_color: Color = None
             , margin: int = 1):
        if line_color is None:
            line_color = Color.GREEN

        grid_box_rect = grid_handler.grid_box_rectangle(width=surface.get_width(), height=surface.get_height(), grid=grid, margin=margin)

        for row in range(0, grid.nRows):
            for col in range(0, grid.nColumns):

                cell = grid.at(row, col)
                if not cell.state[self.toggled_key].value:
                    continue

                left = cell.left.state[self.toggled_key].value if cell.left else None
                right = cell.right.state[self.toggled_key].value if cell.right else None
                up = cell.up.state[self.toggled_key].value if cell.up else None
                down = cell.down.state[self.toggled_key].value if cell.down else None
                connection_count = sum(x for x in [left, right, up, down] if x)

                # array = np.array([[grid[row][column].state[self.toggled_key]
                #             for column in range(grid.nColumns)]
                #             for row in range(grid.nRows)])

                if left and right:
                    # Horizontal Line
                    pygame.draw.line(surface, line_color.value,
                                     (col * (grid_box_rect.width + margin), (row + .5) * (grid_box_rect.height + margin)),
                                     ((col + 1) * (grid_box_rect.width + margin), (row + .5) * (grid_box_rect.height + margin)))

                if up and down:
                    # Vertical Line
                    pygame.draw.line(surface, line_color.value,
                                     ((col + .5) * (grid_box_rect.width + margin), row * (grid_box_rect.height + margin)),
                                     ((col + 0.5) * (grid_box_rect.width + margin), ((row + 1) * (grid_box_rect.height + margin))))

                if up and right:
                    pygame.draw.arc(surface, line_color.value, (
                    (col + .5) * (grid_box_rect.width + margin), (row - .5) * (grid_box_rect.height + margin), grid_box_rect.width,
                    grid_box_rect.height), math.pi, 3 * math.pi / 2, 2)

                if up and left:
                    pygame.draw.arc(surface, line_color.value, (
                    (col - .5) * (grid_box_rect.width + margin), (row - .5) * (grid_box_rect.height + margin), grid_box_rect.width + margin,
                    grid_box_rect.height + margin), 3 * math.pi / 2, 0, 2)

                if right and down:
                    pygame.draw.arc(surface, line_color.value, (
                    (col + .5) * (grid_box_rect.width + margin), (row + .5) * (grid_box_rect.height + margin), grid_box_rect.width,
                    grid_box_rect.height), math.pi / 2, math.pi, 2)

                if down and left:
                    pygame.draw.arc(surface, line_color.value, (
                    (col - .5) * (grid_box_rect.width + margin), (row + .5) * (grid_box_rect.height + margin), grid_box_rect.width,
                    grid_box_rect.height), 0, math.pi / 2, 2)

                if connection_count == 1:
                    if up:
                        # Vertical Line
                        pygame.draw.line(surface, line_color.value,
                                         ((col + .5) * (grid_box_rect.width + margin), row * (grid_box_rect.height + margin)),
                                         ((col + 0.5) * (grid_box_rect.width + margin), ((row + 0.5) * (grid_box_rect.height + margin))))
                    elif down:
                        # Vertical Line
                        pygame.draw.line(surface, line_color.value,
                                         ((col + .5) * (grid_box_rect.width + margin), (row + .5) * (grid_box_rect.height + margin)),
                                         ((col + 0.5) * (grid_box_rect.width + margin), ((row + 1) * (grid_box_rect.height + margin))))
                    elif right:
                        # Horizontal Line
                        pygame.draw.line(surface, line_color.value,
                                         ((col + .5) * (grid_box_rect.width + margin), (row + .5) * (grid_box_rect.height + margin)),
                                         ((col + 1) * (grid_box_rect.width + margin), (row + .5) * (grid_box_rect.height + margin)))
                    elif left:
                        # Horizontal Line
                        pygame.draw.line(surface, line_color.value,
                                         (col * (grid_box_rect.width + margin), (row + .5) * (grid_box_rect.height + margin)),
                                         ((col + .5) * (grid_box_rect.width + margin), (row + .5) * (grid_box_rect.height + margin)))
                elif connection_count == 0:
                    pygame.draw.ellipse(surface, line_color.value, (
                    col * (grid_box_rect.width + margin), row * (grid_box_rect.height + margin), grid_box_rect.width, grid_box_rect.height), 1)