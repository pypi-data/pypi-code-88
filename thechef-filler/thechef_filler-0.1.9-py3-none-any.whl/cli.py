#!/usr/bin/env python
from yk_player import Player
from game import Board, Token
import sys

def main():
    _, _, p, _, _ = input().split(' ')

    p = Player(p)
    while True:
        p.board = Board.read(p.char, p.enemy_char)
        p.token = Token.read()
        res = p.put_random()
        if not res:
            break


if __name__ == "__main__":
    main()
