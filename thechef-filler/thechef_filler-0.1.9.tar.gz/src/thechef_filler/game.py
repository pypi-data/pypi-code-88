#!/usr/bin/env python

class Token():
    def __init__(self, x: int, y: int, shape: list[str]):
        self.y = y
        self.x = x
        self.shape = shape
        self.blank_line()

    def blank_line(self):
        xs = {}
        ys = {}
        for y in range(0, self.y):
            for x in range(0, self.x):
                if self.shape[y][x]:
                    xs[x] = ys[y] = 1
        self.offset_x = min(xs.keys())
        self.offset_y = min(ys.keys())
        # トークンの左(上)から数えた、「"*"が1つも存在しない列(行)」の数。
        # 例: ↓のトークンの場合、offset_x = 1, offset_y = 2
        # ....
        # ..*.
        # .***
        # ....
        self.inset_x = max(xs.keys()) + 1
        self.inset_y = max(ys.keys()) + 1
        # こっちは逆から数えて+1したもの

    @classmethod
    def read(cls):
        y, x = map(int, input()[:-1].split(' ')[1:])
        shape: list[str] = []
        for _ in range(y):
            shape.append(input())
        return cls(x, y, shape)

    def get_topleft_edge(self):
        for i in range(self.offset_y, self.inset_y):
            for l in range(self.offset_x, self.inset_x):
                if self.shape[i][l] == '*':
                    yield i, l
        return None, None

    def get_bottomright_edge(self):
        for i in range(self.offset_y, self.inset_y)[::-1]:
            for l in range(self.offset_x, self.inset_x)[::-1]:
                if self.shape[i][l] == '*':
                    yield i, l
        return None, None


class Board():
    def __init__(self, x: int, y: int, board: list[str], char: str, enemy_char: str):
        self.x = x
        self.y = y
        self.board = board
        self.char = char
        self.enemy_char = enemy_char
        self.cache = {}

    @classmethod
    def read(cls, char: str, enemy_char: str):
        y, x = map(int, input()[:-1].split(' ')[1:])

        _ = input()
        board: list[str] = []
        for _ in range(y):
            board.append(input().split(' ')[1].lower())
        return cls(x, y, board, char, enemy_char)

    def check_overlap(self, x: int, y: int, token: Token):
        overlap_counter = 0

        for token_y in range(token.offset_y, token.inset_y):
            for token_x in range(token.offset_x, token.inset_x):

                if self.board[y + token_y][x + token_x] == self.enemy_char:
                    return 1

                if token.shape[token_y][token_x] == '*' and \
                    self.board[y + token_y][x + token_x] == self.char:
                        overlap_counter += 1
                        if overlap_counter > 1:
                            return 1

        return 0

    def check_overflow(self, x: int, y: int, token: Token):

        if ((x + token.x) > self.x) or ((y + token.y) > self.y):
            return 1
        return 0
