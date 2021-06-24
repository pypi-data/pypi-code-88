#!/usr/bin/python3
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
                if self.shape[i][l] == '*':
                    yield i, l
        return None, None

    def get_bottomright_edge(self):
        for i in range(self.y)[::-1]:
            for l in range(self.x)[::-1]:
                if self.shape[i][l] == '*': yield i, l
        return None, None

    def get_rightbottom_edge(self):
        for i in range(self.x)[::-1]:
            for l in range(self.y)[::-1]:
                if self.shape[l][i] == '*': yield l, i
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
        self.board = board
        self.token = token
        self.cont = True
        self.count = 0
        self.goal_x_left = False
        self.goal_y_top = False
        self.goal_x_right = False
        self.goal_y_bottom = False


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

        if x < 0 or y < 0:
            return 1
        if ((x + token.x) > board.x) or ((y + token.y) > board.y):
            return 1

        return 0


    def put_token_topleft(self, token_y, token_x):
        board = self.board
        for board_y in range(board.y):
            for board_x in range(board.x):
                if board.board[board_y][board_x] in (self.char, self.char.upper()):
                    x = board_x - token_x
                    y = board_y - token_y
                    if self.check_overflow(x, y) == 0 and \
                        self.check_overlap(x, y) == 0:
                        print(f"{y} {x}")
                        return True
        return False

    def put_token_lefttop(self, token_y, token_x):
        board = self.board
        for board_x in range(board.x):
            for board_y in range(board.y):
                if board.board[board_y][board_x] in (self.char, self.char.upper()):
                    x = board_x - token_x
                    y = board_y - token_y
                    if self.check_overflow(x, y) == 0 and \
                        self.check_overlap(x, y) == 0:
                        print(f"{y} {x}")
                        return True
        return False

    def put_token_leftbottom(self, token_y, token_x):
        board = self.board
        for board_x in range(board.x):
            for board_y in reversed(range(board.y)):
                if board.board[board_y][board_x] in (self.char, self.char.upper()):
                    x = board_x - token_x
                    y = board_y - token_y
                    if self.check_overflow(x, y) == 0 and \
                        self.check_overlap(x, y) == 0:
                        print(f"{y} {x}")
                        return True
        return False

    def put_token_topright(self, token_y, token_x):
        board = self.board
        for board_y in range(board.y):
            for board_x in reversed(range(board.x)):
                if board.board[board_y][board_x] in (self.char, self.char.upper()):
                    x = board_x - token_x
                    y = board_y - token_y
                    if self.check_overflow(x, y) == 0 and \
                        self.check_overlap(x, y) == 0:
                        print(f"{y} {x}")
                        return True
        return False

    def put_token_bottomleft(self, token_y, token_x):
        board = self.board
        for board_y in reversed(range(board.y)):
            for board_x in range(board.x):
                if board.board[board_y][board_x] in (self.char, self.char.upper()):
                    x = board_x - token_x
                    y = board_y - token_y
                    if self.check_overflow(x, y) == 0 and \
                        self.check_overlap(x, y) == 0:
                        print(f"{y} {x}")
                        return True
        return False

    def put_token_bottomright(self, token_y, token_x):
        board = self.board
        for board_y in reversed(range(board.y)):
            for board_x in reversed(range(board.x)):
                if board.board[board_y][board_x] in (self.char, self.char.upper()):
                    x = board_x - token_x
                    y = board_y - token_y
                    if self.check_overflow(x, y) == 0 and \
                        self.check_overlap(x, y) == 0:
                        print(f"{y} {x}")
                        return True
        return False

    def put_token_rightbottom(self, token_y, token_x):
        board = self.board
        for board_x in reversed(range(board.x)):
            for board_y in reversed(range(board.y)):
                if board.board[board_y][board_x] in (self.char, self.char.upper()):
                    x = board_x - token_x
                    y = board_y - token_y
                    if self.check_overflow(x, y) == 0 and \
                        self.check_overlap(x, y) == 0:
                        print(f"{y} {x}")
                        return True
        return False

    def put_random(self):
        # 先攻パターン
        # 急いで左を塞ぎ、その後右を塞ぐ
        if self.char == 'o':
            if (self.goal_x_left or self.goal_y_top) and not(self.goal_x_right or self.goal_y_bottom):
                for token_y, token_x in self.token.get_topleft_edge():
                    if self.put_token_rightbottom(token_y, token_x):
                        for board_y in range(self.board.y):
                            if self.board.board[board_y][self.board.x - 1].upper() == self.char.upper():
                                self.goal_x_right = True
                        for board_x in range(self.board.x):
                            if self.board.board[self.board.y - 1][board_x].upper() == self.char.upper():
                                self.goal_y_bottom = True
                        return True
            elif not(self.goal_x_right or self.goal_y_bottom):
                for token_y, token_x in self.token.get_rightbottom_edge():
                    if self.put_token_leftbottom(token_y, token_x):
                        for board_y in range(self.board.y):
                            if self.board.board[board_y][0].upper() == self.char.upper():
                                self.goal_x_left = True
                        for board_x in range(self.board.x):
                            if self.board.board[0][board_x].upper() == self.char.upper():
                                self.goal_y_top = True
                        return True
                for token_y, token_x in self.token.get_topleft_edge():
                    if self.put_token_leftbottom(token_y, token_x):
                        for board_y in range(self.board.y):
                            if self.board.board[board_y][0].upper() == self.char.upper():
                                self.goal_x_left = True
                        for board_x in range(self.board.x):
                            if self.board.board[0][board_x].upper() == self.char.upper():
                                self.goal_y_top = True
                        return True
            # 塞ぎ終わったら、左を優先して育てていく
            for token_y, token_x in self.token.get_bottomright_edge():
                if self.put_token_topleft(token_y, token_x):
                    return True
            for token_y, token_x in self.token.get_topleft_edge():
                if self.put_token_topleft(token_y, token_x):
                    return True
        # 後攻パターン
        else:
            if self.board.board[50][50] == '.':
                if self.char == 'x':
                    for token_y, token_x in self.token.get_topleft_edge():
                        if self.put_token_bottomright(token_y, token_x):
                            return True
                else:
                    for token_y, token_x in self.token.get_bottomright_edge():
                        if self.put_token_topleft(token_y, token_x):
                            return True
        self.count += 1
        if self.count % 4 == 1:
            for token_y, token_x in self.token.get_topleft_edge():
                if self.put_token_topright(token_y, token_x):
                    return True
        elif self.count % 4 == 2:
            for token_y, token_x in self.token.get_topleft_edge():
                if self.put_token_bottomright(token_y, token_x):
                    return True
        elif self.count % 4 == 3:
            for token_y, token_x in self.token.get_bottomright_edge():
                if self.put_token_bottomleft(token_y, token_x):
                    return True
        else:
            for token_y, token_x in self.token.get_bottomright_edge():
                if self.put_token_topleft(token_y, token_x):
                    return True
        for token_y, token_x in self.token.get_topleft_edge():
            if self.put_token_bottomright(token_y, token_x):
                return True
        for token_y, token_x in self.token.get_bottomright_edge():
            if self.put_token_topleft(token_y, token_x):
                return True

        print("0 0")
        self.cont = False
        return False

def main():
    _, _, p, _, _ = input().split(' ')

    p = Player(p, Board(), Token())
    while p.cont:
        p.board.read_board()
        p.token.read_token()
        p.put_random()


if __name__ == "__main__":
    main()
