import model
import pygame

# GLOBALS VARS
window_width = 1000
window_height = 800
play_width = 300  # meaning 300 // 10 = 30 width per block
play_height = 600  # meaning 600 // 20 = 20 height per block
block_size = 30

top_left_corner_of_play_area_x = (window_width - play_width) // 2
top_left_corner_of_play_area_y = window_height - play_height

global grid


def create_grid(locked_positions=None):
    if locked_positions is None:
        locked_positions = {}
        # color and size of the play grid build
    grid = [[model.black for _ in range(10)] for _ in range(20)]

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j, i) in locked_positions:
                c = locked_positions[(j, i)]
                grid[i][j] = c
    return grid


def draw_grid(surface, row, col):
    start_x = top_left_corner_of_play_area_x
    start_y = top_left_corner_of_play_area_y
    for i in range(row):
        pygame.draw.line(surface, model.grey, (start_x, start_y + i * block_size),
                         (start_x + play_width, start_y + i * block_size))  # horizontal lines
        for j in range(col):
            pygame.draw.line(surface, model.grey, (start_x + j * block_size, start_y),
                             (start_x + j * block_size, start_y + play_height))  # vertical lines


locked_positions = {}  # dictionary of all played pieces
grid = create_grid(locked_positions)


def draw_window(surface, score):
    surface.fill((125, 125, 125))
    # Tetris Title
    font = pygame.font.SysFont('calibri', 60)
    game_title = font.render('TETRIS 1.0', True, model.white)

    font2 = pygame.font.SysFont('calibri', 20)
    controls = font2.render('Use arrow keys to control the piece', True, model.white)
    controls2 = font2.render('Arrow up rotates, Space instant drops', True, model.white)
    current_score = font2.render('Your score: ' + str(score), True, model.white)
    surface.blit(game_title, (round(top_left_corner_of_play_area_x + play_width / 2 - (game_title.get_width() / 2)), 50))
    surface.blit(controls, (round(window_width - (window_width * 0.975)), (round(window_height / 2))))
    surface.blit(controls2, (round(window_width - (window_width * 0.975)), (round(window_height / 2) + 30)))
    surface.blit(current_score, (round(top_left_corner_of_play_area_x + play_width + 50), (round(top_left_corner_of_play_area_y + play_height / 2) - 300)))

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(surface, grid[i][j], (top_left_corner_of_play_area_x + j * block_size,
                                                   top_left_corner_of_play_area_y + i * block_size, block_size,
                                                   block_size), 0)

    # draw grid and border
    draw_grid(surface, 20, 10)
    pygame.draw.rect(surface, (6, 60, 255), (top_left_corner_of_play_area_x,
                                             top_left_corner_of_play_area_y,
                                             play_width, play_height), 5)


def draw_next_shape(shape, surface):
    font = pygame.font.SysFont('calibri', 30)
    label = font.render('Next Shape', True, model.white)

    sx = top_left_corner_of_play_area_x + play_width + 50
    sy = top_left_corner_of_play_area_y + play_height / 2 - 100
    format_shape = shape.shape[shape.rotation % len(shape.shape)]

    for i, line in enumerate(format_shape):
        row = list(line)
        for j, column in enumerate(row):
            if column == 'X':
                pygame.draw.rect(surface, shape.color, (round(sx + j * block_size), round(sy + i * block_size),
                                                        block_size, block_size), 0)

    surface.blit(label, (round(sx + 10), round(sy - 30)))


def draw_text_middle(text, size, color, surface):
    font = pygame.font.SysFont('calibri', size, bold=True)
    label = font.render(text, True, color)

    surface.blit(label, (round(top_left_corner_of_play_area_x + play_width / 2 - (label.get_width() / 2)),
                         round(top_left_corner_of_play_area_y + play_height / 2 - label.get_height() / 2)))
