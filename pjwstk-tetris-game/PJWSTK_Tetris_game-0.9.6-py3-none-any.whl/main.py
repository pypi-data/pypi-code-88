import pygame
import model
import window
import mechanics

"""
Classic Tetris game with play area made out of 10 x 20 square grid
Typical shapes: I, o, L, T, S, Z coded in the model 
"""

pygame.font.init()


def main():
    change_piece = False
    play_game = True
    current_piece = model.get_shape()
    next_piece = model.get_shape()
    clock = pygame.time.Clock()
    fall_time = 0
    score = 0
    fall_speed = 0.27

    while play_game:

        window.grid = window.create_grid(window.locked_positions)
        fall_time += clock.get_rawtime()
        clock.tick()
        # falling piece logic
        if fall_time / 1000 >= fall_speed:
            fall_time = 0
            current_piece.y += 1
            if not (mechanics.valid_space(current_piece, window.grid)) and current_piece.y > 0:
                current_piece.y -= 1
                change_piece = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play_game = False
                pygame.display.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_piece.x -= 1
                    if not mechanics.valid_space(current_piece, window.grid):
                        current_piece.x += 1

                elif event.key == pygame.K_RIGHT:
                    current_piece.x += 1
                    if not mechanics.valid_space(current_piece, window.grid):
                        current_piece.x -= 1
                elif event.key == pygame.K_UP:
                    # rotate shape
                    current_piece.rotation = current_piece.rotation + 1 % len(current_piece.shape)
                    if not mechanics.valid_space(current_piece, window.grid):
                        current_piece.rotation = current_piece.rotation - 1 % len(current_piece.shape)

                if event.key == pygame.K_DOWN:
                    # move shape down
                    current_piece.y += 1
                    if not mechanics.valid_space(current_piece, window.grid):
                        current_piece.y -= 1

                if event.key == pygame.K_SPACE:
                    while mechanics.valid_space(current_piece, window.grid):
                        current_piece.y += 1
                    current_piece.y -= 1

        shape_pos = mechanics.convert_shape_format(current_piece)

        # add piece to the grid for drawing
        for i in range(len(shape_pos)):
            x, y = shape_pos[i]
            if y > -1:
                window.grid[y][x] = current_piece.color

        # dropped piece
        if change_piece:
            for pos in shape_pos:
                p = (pos[0], pos[1])
                window.locked_positions[p] = current_piece.color
            current_piece = next_piece
            next_piece = model.get_shape()
            change_piece = False
            fall_speed -= 0.002
            # call four times to check for multiple clear rows
            score += mechanics.clear_rows(window.grid, window.locked_positions) * 15

        window.draw_window(win, score)
        window.draw_next_shape(next_piece, win)
        pygame.display.update()

        # Check if user lost
        if mechanics.check_lost(window.locked_positions):
            play_game = False

    window.draw_text_middle("GAME OVER", 40, model.white, win)
    pygame.display.update()
    pygame.time.delay(3000)
    window.locked_positions = {}  # reset the grid from the pieces from previous game


def main_menu(win):
    play_game = True
    while play_game:
        win.fill(model.black)
        window.draw_text_middle('Press any key to begin.', 60, model.white, win)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play_game = False

            if event.type == pygame.KEYDOWN:
                main()
    pygame.quit()


win = pygame.display.set_mode((window.window_width, window.window_height))
pygame.display.set_caption('Tetris1.0')

main_menu(win)  # start game
