import pygame

# colors
BLUE = (0, 150, 255)
PINK = (255,13,255)
GREEN = (81, 225, 13)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 87, 51)
CLAY = (63,176,172)

class Node:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = width * row
        self.y = width * col
        self.neighbor = []
        self.width = width
        self.total_rows = total_rows
        self.color = WHITE
        
    def get_pos(self):
        return (self.row,self.col)
    
    def get_color(self):
        self.color = self.color
    
    def get_coord(self):
        return (self.x,self.y)
    
    def is_closed(self):
        return self.color == RED
    
    def is_open(self):
        return self.color == GREEN 
    
    def is_barrier(self):
        return self.color == BLACK
    
    def is_start(self):
        return self.color == BLUE
    
    def is_end(self):
        return self.color == PINK
    
    def make_start(self):
        self.color = BLUE
    
    def make_end(self):
        self.color = PINK

    def make_barrier(self):
        self.color = BLACK  
        
    def make_open(self):
        self.color = GREEN

    def make_closed(self):
        self.color = RED
    
    def reset(self):
        self.color = WHITE
        
    def make_path(self):
        self.color = CLAY
        
