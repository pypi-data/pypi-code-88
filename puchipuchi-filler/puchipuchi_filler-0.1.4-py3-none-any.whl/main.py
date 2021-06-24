
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
        self.board = board
        self.token = token


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

        if ((x + token.x) > board.x) or ((y + token.y) > board.y):
            return 1

        return 0


    def put_token(self, token_y, token_x):
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

    def put_random(self):
        for token_y, token_x in self.token.get_topleft_edge():
            if self.put_token(token_y, token_x): return True

        print("0 0")
        return False

def main():
    _, _, p, _, _ = input().split(' ')

    p = Player(p, Board(), Token())
    while True:
        p.board.read_board()
        p.token.read_token()
        p.put_random()


if __name__ == "__main__":
    main()
