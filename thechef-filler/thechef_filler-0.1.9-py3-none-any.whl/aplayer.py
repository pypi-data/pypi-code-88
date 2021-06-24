#!/usr/bin/env python
import random

class Player():
    def __init__(self, p: str):
        self.p = p
        self.char = 'o' if self.p == "p1" else 'x'
        self.enemy_char = 'x' if self.char == 'o' else 'o'
        self.board = None
        self.token = None
        # self.e = Evaluation()

    def put_token(self, token_y: int, token_x: int):
        ansList = []
        ansDict = {}
        board = self.board
        for board_y in range(board.y):
            for board_x in range(board.x):
                if board.board[board_y][board_x] == self.char:
                    x = board_x - token_x
                    y = board_y - token_y
                    if board.check_overflow(x, y, self.token) == 0 and board.check_overlap(x, y, self.token) == 0:
                        # ansList.append(f"{y} {x}")
                        ansList.append((y, x,))
                        ansDict[(y, x,)] = 0
        if len(ansList) != 0:
            index = random.randrange(0, len(ansList))
            # self.e.eval(ansDict)
            print(f"{ansList[index][0]} {ansList[index][1]}")
            return True
        else:
            return False

    def put_random(self):
        for token_y, token_x in self.token.get_topleft_edge():
            if self.put_token(token_y, token_x):
                return True
        print("0 0")
        return False

class Evaluation():
    def eval(self, ansDict):
        for i in ansDict.keys():
            path_w = './test_w.txt'
            with open(path_w, mode='a') as f:
                f.write("'========'\n")
                f.write(f"{i}\n")
                f.write(f"{i[0]}\n")

