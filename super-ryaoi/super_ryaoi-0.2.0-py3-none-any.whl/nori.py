#!/usr/bin/env python3
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

    def get_topleft_edge(self):
        for i in range(self.y):
            for l in range(self.x):
                if self.shape[i][l] == '*': yield i, l
        return None, None

    def get_bottomright_edge(self):
        for i in range(self.y)[::-1]:
            for l in range(self.x)[::-1]:
                if self.shape[i][l] == '*': yield i, l
        return None, None

class Board():
    def __init__(self, y=None, x=None):
        self.y = y
        self.x = x
        self.board = []

    def read_board(self):
        self.y, self.x = map(int, input()[:-1].split(' ')[1:])
        _ = input()
        self.board = []
        for _ in range(self.y):
            self.board.append(input().split(' ')[1])
class Player():

    def __init__(self, p, board, token):
        self.p = p
        self.char = 'o' if self.p == "p1" else 'x'
        self.enemy_char = 'x' if self.char == 'o' else 'o'
        self.enemy_chars = [self.enemy_char, chr(ord(self.enemy_char) - 32)]
        self.board = board
        self.token = token

    def calc_manhattan_dist(self, x1, y1, x2, y2):
        #sum1 = x1 + y1
        #sum2 = x2 + y2
        #sub1 = x1 - y1
        #sub2 = x2 - y2

        #return min(abs(sum1 - sum2), abs(sub1 - sub2))
        return abs(x1 - x2) + abs(y1 - y2)

    def calc_min_manhattan_dist(self, x, y):
        board = self.board
        min_dist = board.x + board.y
        #for board_y in range(board.y):
        #    for board_x in range(board.x):
        #        if board.board[board_y][board_x] in (self.enemy_char, self.enemy_char.upper()):
        for enemy_y, enemy_x in self.enemy_lst:
            min_dist = min(min_dist, self.calc_manhattan_dist(x, y, enemy_x, enemy_y))
        return min_dist

    def calc_heat_map(self, board):
        heatmap = [[0] * board.x for i in range(board.y)]

        for board_y in range(board.y):
            for board_x in range(board.x):
                heatmap[board_y][board_x] = self.calc_min_manhattan_dist(board_x, board_y)
        self.heatmap = heatmap

    def check_overlap(self, x, y):
        token = self.token
        overlap_counter = 0

        for token_y in range(token.y):
            for token_x in range(token.x):
                if self.board.board[y + token_y][x + token_x] in (self.enemy_char, self.enemy_char.upper()):
                    return 1
                if token.shape[token_y][token_x] == '*' and \
                    self.board.board[y + token_y][x + token_x] in (self.char, self.char.upper()):
                        overlap_counter += 1
        if overlap_counter != 1:
            return 1
        return 0

    def check_overflow(self, x, y):
        token = self.token
        board = self.board

        if ((x + token.x) > board.x) or ((y + token.y) > board.y) or x < 0 or y < 0:
            return 1
        return 0

    def all_token(self, board_x, board_y, token_x, token_y):
        x = board_x - token_x
        y = board_y - token_y

        if self.check_overflow(x, y) == 0 and \
            self.check_overlap(x, y) == 0:
            self.token_places.append([y, x])

    def put_token(self, token_y, token_x):
        board = self.board

        for board_y in range(board.y):
            for board_x in range(board.x):
                if board.board[board_y][board_x] in (self.char, self.char.upper()):
                    self.all_token(board_x, board_y, token_x, token_y)

    def calc_sum_min(self, list1):
        heatmap = self.heatmap
        token_cood = self.mark_places
        tmp_list = []

        for y, x in list1:
            sum_heat_point = 0
            for token_y, token_x in token_cood:
                sum_heat_point += heatmap[y + token_y][x + token_x]
            tmp_list.append([sum_heat_point, [y, x]])
        list2 = sorted(tmp_list)
        print(*list2[0][1])

    def put_random(self):
        self.token_places = []
        self.mark_places = []
        for token_y, token_x in self.token.get_topleft_edge():
            self.mark_places.append([token_y, token_x])
            self.put_token(token_y, token_x)
        if self.token_places:
            self.calc_sum_min(self.token_places)
            return True
        print("0 0")
        return False

    def get_enemy_place(self):
        self.enemy_lst = []
        for y in range(self.board.y):
            for x in range(self.board.x):
                if self.board.board[y][x] in self.enemy_chars:
                    self.enemy_lst.append([y, x])

def fprint(content):
    with open('file.txt', 'a') as f:
        print(content, file=f)

def main():
    _, _, p, _, _ = input().split(' ')
    p = Player(p, Board(), Token())
    while True:
        p.board.read_board()
        p.get_enemy_place()
        p.calc_heat_map(p.board)
        p.token.read_token()
        if not p.put_random():
            break

if __name__ == "__main__":
    main()
