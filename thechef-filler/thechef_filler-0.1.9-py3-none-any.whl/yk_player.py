#!/usr/bin/env python
import sys
import random
from game import Board, Token

class Player():
    def __init__(self, p: str):
        self.p = p
        self.char = 'o' if self.p == "p1" else 'x'
        self.enemy_char = 'x' if self.char == 'o' else 'o'
        self.board = None
        self.token = None

    def put_token(self, token_y: int, token_x: int, pmap: list[list[int]]):
        ansDict = {}
        board: Board = self.board
        for board_y in range(board.y):
            for board_x in range(board.x):
                if board.board[board_y][board_x] == self.char:
                    x = board_x - token_x
                    y = board_y - token_y
                    if board.check_overflow(x, y, self.token) == 0 and board.check_overlap(x, y, self.token) == 0:
                        ansDict[(x, y)] = 1
        return ansDict

    def put_random(self):
        board: Board = self.board
        pmap = potential_map(board.x, board.y, board.board, self.enemy_char, self.char, +3, +10, -8)
        ansDict = {}
        token: Token = self.token
        for token_y, token_x in self.token.get_topleft_edge():
            for t in self.put_token(token_y, token_x, pmap).keys():
                ansDict[t] = 1
        # for row in token.shape:
        #     print(row, file=sys.stderr)
        # for row in pmap:
        #     print(row, file=sys.stderr)
        if len(ansDict) > 0:
            # print(ansList, file=sys.stderr)
            ts = sorted([ (t, self.token_potential(token, t[0], t[1], pmap)) for t in ansDict.keys() ], key=lambda t:t[1])
            # print(candList, file=sys.stderr)
            # print(ts, file=sys.stderr)
            ans = ts[0][0]
            # ans = random.choice(ansList)
            print(f"{ans[1]} {ans[0]}")
            # index = random.randrange(0, len(ansList))
            # print(f"{ansList[index][1]} {ansList[index][0]}")
            return True
        else:
            print("0 0")
            return False

    def token_potential(self, token: Token, x: int, y: int, potential: list[list[int]]):
        s = 0
        for ty in range(token.y):
            for tx in range(token.x):
                if token.shape[ty][tx] == "*":
                    s += potential[y + ty][x + tx]
        # print((x, y), s, file=sys.stderr)
        return s


def potential_map(x: int, y: int, board: list[str], enemy_char: str, char: str, wall_charge: float, enemy_charge: float, my_charge: float):
    # for i in range(y):
    #     print("".join(board[i]))
    potentials: list[list[int]] = [ [0] * x for _ in range(y) ]
    for i in range(y):
        for j in range(x):
            if board[i][j] == enemy_char or board[i][j] == char:
                potentials[i][j] = 0
                continue
            ep = (x * y) ** 2
            mp = (x * y) ** 2
            for u in range(y):
                for v in range(x):
                    if board[u][v] == enemy_char:
                        ep = min(ep, abs(i - u) + abs(j - v))
                    if board[u][v] == char:
                        mp = min(mp, abs(i - u) + abs(j - v))
            # potentials[i][j] = int(-wall_charge / (1 + min(i, y - i - 1, j, x - j - 1)) + -enemy_charge / (1 + ep))
            potentials[i][j] = int(wall_charge * min(i, y - i - 1, j, x - j - 1) + enemy_charge * ep + my_charge * mp)
        # print(potentials[i])
    return potentials
    


if __name__ == '__main__':
    x = 20
    y = 10
    enemy_char = "o"
    board: list[list[str]] = [ ["."] * x for _ in range(y) ]
    board[1][3] = enemy_char
    board[2][3] = enemy_char
    board[2][4] = enemy_char
    board[3][4] = enemy_char
    for row in potential_map(x, y, board, enemy_char, "x", 0, 1, 0):
        print(row)

