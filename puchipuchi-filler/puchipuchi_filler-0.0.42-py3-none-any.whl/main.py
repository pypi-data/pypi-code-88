#!/usr/bin/env python3
import os, sys, random

class Token():

    def __init__(self, y=None, x=None):
        self.y = y
        self.x = x
        self.shape = []

    def read_token(self):
        self.y, self.x = map(int, input()[:-1].split(' ')[1:])
        self.shape = []
        for _ in range(self.y):
            self.shape.append(input())

    """
    左上からピースの形状を返す
    """
    def get_topleft_edge(self):
        for i in range(self.y):
            for l in range(self.x):
                if self.shape[i][l] == '*':
                    yield i, l
        return None, None

    """
    右下からピースの形状を返す
    """
    def get_bottomright_edge(self):
        for i in range(self.y)[::-1]:
            for l in range(self.x)[::-1]:
                if self.shape[i][l] == '*':
                    yield i, l
        return None, None

class Board():

    def __init__(self, y=None, x=None):
        self.y = y
        self.x = x
        self.board = []
        self.map = []

    def read_board(self):
        self.y, self.x = map(int, input()[:-1].split(' ')[1:])
        """ 列のインデックス表記を読み飛ばす """
        _ = input()
        self.board = []
        """ 行のインデックス表記を読み飛ばし、盤面をしまう """
        for _ in range(self.y):
            self.board.append(input().split(' ')[1])

class Player():

    def __init__(self, p, board, token):
        self.p = p
        self.char = 'o' if self.p == 'p1' else 'x'
        self.enemy_char = 'x' if self.char == 'o' else 'o'
        self.board = board
        self.token = token
        self.map = []

    """
    tokenのサイズがboardのサイズを超えてないかのチェック
    """
    def check_overflow(self, x, y):
        token = self.token
        board = self.board

        if ((x + token.x) > board.x) or ((y + token.y) > board.y):
            return 0
        return 1

    """
    tokenが配置可能かのチェック
    1. 自分のすでに配置されたトークンと重なっているか
    2. 敵のトークンが配置されていないか
    """

    def check_overlap(self, x, y):
        token = self.token
        overlap_counter = 0

        for token_y in range(token.y):
            for token_x in range(token.x):

                if self.board.board[y + token.y][x + token.x] in (self.enemy_char, self.enemy_char.upper()):
                    return 1

                if token.shape[token_y][token_x] == '*' and \
                    self.board.board[y + token_y][x + token_x] in (self.char, self.char.upper()):
                        overlap_counter += 1

    def manhattan_distance(self, y, x):
        dis = None
        dis_min = None
        for i in range(self.board.y):
            for l in range(self.board.x):
                if self.board.board[i][l] in (self.enemy_char, self.enemy_char.upper()):
                    dis = abs(i - y) + abs(l - x)
                    if dis_min == None or dis < dis_min:
                        dis_min = dis
        return dis_min

    def gen_map(self):
        if self.map == []:
            self.map = [[None] * self.board.x for i in range(self.board.y)]
        for y in range(self.board.y):
            for x in range(self.board.x):
                if self.board.board[y][x] in (self.enemy_char, self.enemy_char.upper(), self.char, self.char.upper()):
                    self.map[y][x] = self.board.board[y][x]
                else:
                    self.map[y][x] = self.manhattan_distance(y, x)

    def calc_sum(self, y, x):
        ans = 0
        for i in range(self.token.y):
            for l in range(self.token.x):
                if self.board.board[i + y][l + x] == '*':
                    ans += self.map[i + y][l + x]
        return ans

    def put_token(self, token_y, token_x):
        board = self.board
        heat = None
        tmp_x = None
        tmp_y = None

        for board_y in range(board.y):
            for board_x in range(board.x):
                if board.board[board_y][board_x] in (self.char, self.char.upper()):
                    x = board_x - token_x
                    y = board_y - token_y
                    if self.check_overflow(x, y) == 0 and self.check_overlap(x, y) == 0:
                        if heat == None or heat > self.calc_sum(board_y, board_x):
                            tmp_y = y                           
                            tmp_x = x
        print(f'{y} {x}')
        return True

    def put_random(self):
        for token_y, token_x in self.token.get_topleft_edge():
            if self.put_token(token_y, token_x):
                return True
        print('0 0')
        return False

def main_1():
    _, _, p, _, _ = input().split(' ')

    p = Player(p, Board(), Token())
    while True:
        """ 盤面を読み取る"""
        p.board.read_board()
        """ はめるピースを読み取る """
        p.token.read_token()
        """ 適当な位置にピースを配置する（今回の肝） """
#        p.gen_map()
#        for l in p.map:
#            print(l)
        p.put_random()

def main():
    try:
        cmd = os.path.join(os.path.dirname(__file__), random.choice(['carli.filler', 'lcharvol.filler', 'angavrel.filler']))
        print(cmd, file=sys.stderr)
        os.system(cmd)
    except Exception as e:
        print(e, file=sys.stderr)
        main_1()

if __name__ == "__main__":
        main()
