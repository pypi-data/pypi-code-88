#!/usr/bin/env python3
import sys, random

class Token():
    def __init__(self, x: int, y: int, shape):
        self.y = y
        self.x = x
        self.shape = shape
        self.blank_line()

    def blank_line(self):
        xs = {}
        ys = {}
        for y in range(self.y):
            for x in range(self.x):
                if self.shape[y][x] == "*":
                    xs[x] = 1
                    ys[y] = 1
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
        shape = []
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
    def __init__(self, x: int, y: int, board, char: str, enemy_char: str):
        self.x = x
        self.y = y
        self.board = board
        self.char = char
        self.enemy_char = enemy_char
        self.cache = {}
        self.my_occupation = 0
        self.enemy_occupation = 0
        self.occipied_rate = 0

    @classmethod
    def read(cls, char: str, enemy_char: str):
        y, x = map(int, input()[:-1].split(' ')[1:])
        _ = input()
        board = []
        mo = 0
        eo = 0
        for _ in range(y):
            row = input().split(' ')[1].lower()
            mo += row.count(char)
            eo += row.count(enemy_char)
            board.append(row)
        b = cls(x, y, board, char, enemy_char)
        b.occipied_rate = (mo + eo) / (x * y)
        b.my_occupation = mo
        b.enemy_occupation = eo
        return b

    def check_overlap(self, x: int, y: int, token: Token):
        overlap_counter = 0

        # for token_y in range(token.y):
        #     for token_x in range(token.x):
        for token_y in range(token.offset_y, token.inset_y):
            for token_x in range(token.offset_x, token.inset_x):

                if self.board[y + token_y][x + token_x] == self.enemy_char:
                    return 1

                if token.shape[token_y][token_x] == '*' and \
                    self.board[y + token_y][x + token_x] == self.char:
                        overlap_counter += 1
                        if overlap_counter > 1:
                            return 1

        if overlap_counter > 1:
            return 1
        return 0

    def check_overflow(self, x: int, y: int, token: Token):

        if ((x + token.inset_x) > self.x) or ((y + token.inset_y) > self.y):
            return 1
        return 0


class Player():
    def __init__(self, p: str):
        self.p = p
        self.char = 'o' if self.p == "p1" else 'x'
        self.enemy_char = 'x' if self.char == 'o' else 'o'
        self.board = None
        self.token = None
        self.won = False
        self.enemy_occupation = 0

    def put_token(self, token_y: int, token_x: int, ansDict: dict):
        board: Board = self.board
        for board_y in range(board.y):
            for board_x in range(board.x):
                if board.board[board_y][board_x] == self.char:
                    x = board_x - token_x
                    y = board_y - token_y
                    if (x,y) in ansDict:
                        continue
                    of = board.check_overflow(x, y, self.token)
                    if of == 0:
                        ol = board.check_overlap(x, y, self.token)
                    else:
                        ol = None
                    # print(f"{(board_x, board_y)}, {(token_x, token_y)} -> {(x,y)} / {of} / {ol}", file=sys.stderr)
                    if of == 0 and ol == 0:
                        ansDict[(x, y)] = 1
        return ansDict

    def put_random(self):
        board: Board = self.board
        if not self.won and board.enemy_occupation <= self.enemy_occupation:
            # Won!
            self.won = True
            print("won!!", file=sys.stderr)
        self.enemy_occupation = board.enemy_occupation

        ansDict = {}
        token: Token = self.token
        for token_y, token_x in self.token.get_topleft_edge():
            # print(f"[ {token.x}, {token.y} | {token.offset_x}, {token.offset_y} | {token.inset_x}, {token.inset_y} ] / [{token_x}, {token_y}]", file=sys.stderr)
            self.put_token(token_y, token_x, ansDict)
        if len(ansDict) > 0:
            # print(list(ansDict.keys()), file=sys.stderr)
            if self.won:
                ans = random.choice(list(ansDict.keys()))
            else:
                if board.occipied_rate < 0.25:
                    pmap = voronoi_potential(board.x, board.y, board.board, self.enemy_char, self.char, 4, 7, -5)
                else:
                    # tactics_attatck = [+25, +100, -20]
                    tactics_capture = [+3, +10, -22]
                    # tactics_defend = [+5, +10, -2] 
                    tactics = tactics_capture
                    pmap = potential_map(board.x, board.y, board.board, self.enemy_char, self.char, *tactics)
                ts = sorted([ (t, self.token_potential(token, t[0], t[1], pmap)) for t in ansDict.keys() ], key=lambda t:t[1])
                ans = ts[0][0]
            print(f"{ans[1]} {ans[0]}")
            return True
        else:
            print("withdraw!!", file=sys.stderr)
            print("0 0")
            return False

    def token_potential(self, token: Token, x: int, y: int, potential):
        s = 0
        for ty in range(token.offset_y, token.inset_y):
            for tx in range(token.offset_x, token.inset_x):
                if token.shape[ty][tx] == "*":
                    s += potential[y + ty][x + tx]
        return s


def neighbors(x: int, y: int, w: int, h: int, visited: dict):
    return [ t for t in [ (x+1,y), (x-1,y), (x,y+1), (x,y-1) ] if not t in visited and 0 <= t[0] and t[0] < w and 0 <= t[1] and t[1] < h ]

def bfs(potential: list, w: int, h: int, board, char: str, charge: float):
    visited = {}
    queue = {}
    d = 0
    for y in range(h):
        for x in range(w):
            if board[y][x] == char:
                queue[(x,y)] = 1
    while len(queue) > 0:
        nq = {}
        for (x,y) in queue.keys():
            potential[y][x] += d * charge
            visited[(x,y)] = 1
            for n in neighbors(x, y, w, h, visited):
                nq[n] = 0
        queue = nq
        d += 1

def voronoi_potential(x: int, y: int, board, enemy_char: str, char: str, wall_charge: float, enemy_charge: float, my_charge):
    potentials: list = [ [0] * x for _ in range(y) ]
    bfs(potentials, x, y, board, enemy_char, enemy_charge)
    bfs(potentials, x, y, board, char, my_charge)
    for i in range(y):
        for j in range(x):
            potentials[i][j] = wall_charge * (0.01 + min(i, y - i - 1, j, x - j - 1)) - 1 / (0.01 + abs(potentials[i][j]))
    return potentials

def potential_map(x: int, y: int, board, enemy_char: str, char: str, wall_charge: float, enemy_charge: float, my_charge: float):
    potentials: list = [ [0] * x for _ in range(y) ]
    for i in range(y):
        for j in range(x):
            potentials[i][j] = wall_charge * min(i, y - i - 1, j, x - j - 1)
    bfs(potentials, x, y, board, enemy_char, enemy_charge)
    bfs(potentials, x, y, board, char, my_charge)
    return potentials


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
