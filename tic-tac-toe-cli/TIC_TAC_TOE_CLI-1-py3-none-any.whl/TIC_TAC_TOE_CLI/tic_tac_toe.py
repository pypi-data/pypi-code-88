"""
This file contains code for the game "Tic Tac Toe".
Author: GlobalCreativeCommunityFounder
"""


# Importing necessary libraries


import sys
import os
import random


# Creating necessary functions to be used throughout the game.


def player_wins(board: list) -> bool:
    for i in range(len(board)):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] == "X":
            return True

    for j in range(len(board[0])):
        if board[0][j] == board[1][j] and board[1][j] == board[2][j] and board[0][j] == "X":
            return True

    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] == "X":
        return True

    if board[2][0] == board[1][1] and board[1][1] == board[0][2] and board[2][0] == "X":
        return True

    return False


def opponent_wins(board: list) -> bool:
    for i in range(len(board)):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] == "O":
            return True

    for j in range(len(board[0])):
        if board[0][j] == board[1][j] and board[1][j] == board[2][j] and board[0][j] == "O":
            return True

    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] == "O":
        return True

    if board[2][0] == board[1][1] and board[1][1] == board[0][2] and board[2][0] == "O":
        return True

    return False


def board_is_full(board: list):
    for i in range(3):
        for j in range(3):
            if board[i][j] == "NONE":
                return False
    return True


def board_repr(board: list) -> str:
    res: str = ""  # initial value
    for i in range(len(board)):
        res += str(board[i]) + "\n"

    return res


def clear():
    # type: () -> None
    if sys.platform.startswith('win'):
        os.system('cls')  # For Windows System
    else:
        os.system('clear')  # For Linux System


# Creating main function used to run the game.


def main():
    """
    This main function is used to run the game.
    :return: None
    """

    print("Welcome to 'Tic Tac Toe' by 'GlobalCreativeCommunityFounder'.")
    print("This game is a command line interface version of 'Tic Tac Toe' where crosses (X) are used by the player "
          "and circles 'O' are used by the opponent.")
    print("Enter 'Y' for yes.")
    print("Enter anything else for no.")
    continue_playing: str = input("Do you want to continue playing 'Tic Tac Toe'? ")
    while continue_playing == "Y":
        # Clearing the command line window
        clear()

        # Initialising the Tic Tac Toe board
        board: list = [["NONE" for j in range(3)] for i in range(3)]

        turn: int = 0
        while not player_wins(board) and not opponent_wins(board) and not board_is_full(board):
            print("Current board representation: \n" + str(board_repr(board)))
            turn += 1

            # Checking whether it is player's turn or opponent's turn to make a move
            if turn % 2 == 1:
                print("It is your turn!")
                x: int = int(input("Please enter x-coordinates of where you want to put a cross (0-2): "))
                y: int = int(input("Please enter y-coordinates of where you want to put a cross (0-2): "))
                while x < 0 or x > 2 or y < 0 or y > 2 or board[y][x] != "NONE":
                    print("Sorry, your input is invalid!")
                    x = int(input("Please enter x-coordinates of where you want to put a cross (0-2): "))
                    y = int(input("Please enter y-coordinates of where you want to put a cross (0-2): "))

                board[y][x] = "X"
                if player_wins(board):
                    print("YOU WIN!")
                    break

                if board_is_full(board):
                    print("IT IS A TIE!")
                    break

            else:
                x: int = random.randint(0, 2)
                y: int = random.randint(0, 2)
                while board[y][x] != "NONE":
                    x = random.randint(0, 2)
                    y = random.randint(0, 2)

                board[y][x] = "O"
                if opponent_wins(board):
                    print("YOU LOSE!")
                    break

                if board_is_full(board):
                    print("IT IS A TIE!")
                    break

        print("Enter 'Y' for yes.")
        print("Enter anything else for no.")
        continue_playing = input("Do you want to continue playing 'Tic Tac Toe'? ")
    sys.exit()


if __name__ == '__main__':
    main()
