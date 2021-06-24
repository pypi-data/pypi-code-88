import pygame
from pygame import gfxdraw

def opacity_line(dimentions,color, op):
    """returns line surface with opacity 

    Args:
        dimentions (tuple): (width , height)
        color (tuble): (c1, c2, c3)
        op (float): number from 0 to 1 (percent of opacity)

    Returns:
        [surface]: surface to blit line
    """
    width, height = dimentions
    s = pygame.Surface((width, height), pygame.SRCALPHA)
    s.fill((color[0], color[1], color[2], int(op * 255)))

    return s

def opacity_rect(dimentions, color, op, lines_to_draw = (True, True, True, True), index = 0, breite = -1):
    """retruns multible surfaces with relativ drawing cords which together are the rectangle

    Args:
        dimentions (tuple): (width , height)
        color (tuble): (c1, c2, c3)
        op (float): number from 0 to 1 (percent of opacity)
        lines_to_draw (tuple with ints in): left, right, top, bottem
        index (int) : if every round is more relocated
        breite (int, optional): width of single line. Defaults to -1.

    Returns:
        [(rel_x,rel_y), surface]: list of relative_draw_cords, surface
    """
    width, height = dimentions

    if breite == -1:
        gesamt_surface = pygame.Surface((width, height), pygame.SRCALPHA)
        gesamt_surface.fill((color[0], color[1], color[2], int(op * 255)))
    else:
        gesamt_surface = []
        vertical = opacity_line((breite, height), color, op)
        horizontal = opacity_line((width - 2* breite, breite), color, op)
        if lines_to_draw[0]:
            gesamt_surface.append(((0 + index,0), vertical))
        if lines_to_draw[1]:
            gesamt_surface.append(((width - breite - index,0), vertical))
        if lines_to_draw[2]:
            gesamt_surface.append(((breite, 0 + index), horizontal))
        if lines_to_draw[3]:
            gesamt_surface.append(((breite, height- breite - index), horizontal,))

    return gesamt_surface

def draw_aacircle(win, color, cords, radius, filled = True):
    x,y = cords
    x, y, radius = int(x), int(y), int(radius)
    gfxdraw.aacircle(win, x, y, radius, color)
    if filled:
        gfxdraw.filled_circle(win, x, y, radius, color)

def draw_aatriangle(win, color, cords1 , cords2, cords3, filled = True):
    x1,y1 = cords1
    x2,y2 = cords2
    x3,y3 = cords3
    x1, y1, x2, y2, x3,y3 = int(x1), int(y1), int(x2), int(y2), int(x3),int(y3)
    
    pygame.gfxdraw.filled_trigon(win, x1, y1, x2, y2, x3, y3, color)
    if filled:
        pygame.gfxdraw.aatrigon(win, x1, y1, x2, y2, x3, y3, color)

    
# pygame.gfxdraw.aafilled_circle(WIN, 100, 100, 50, (255,0,0))


# x = opacity_rect((100,100), (255,255,0), 0.5, 5) 
# print(x)   