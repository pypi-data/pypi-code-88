from eval_kohkubo import Evaluation


def printFile(str):
    with open("./test_w.txt", mode='a') as f:
        f.write(f"{str}")

class Player():
    def __init__(self, p):
        self.p = p
        self.char = 'o' if self.p == "p1" else 'x'
        self.enemy_char = 'x' if self.char == 'o' else 'o'
        self.board = None
        self.token = None
        self.eval = Evaluation()

    def check_overlap(self, x, y):
        token = self.token
        overlap_counter = 0
        for token_y in range(token.y):
            for token_x in range(token.x):
                if self.board.board[y + token_y][x + token_x] in (
                    self.enemy_char,
                    self.enemy_char.upper(),
                ):
                    return True
                if token.shape[token_y][token_x] == '*' and self.board.board[
                    y + token_y
                ][x + token_x] in (self.char, self.char.upper()):
                        overlap_counter += 1
        if overlap_counter != 1:
            return True
        return False

    def check_overflow(self, x, y):
        token = self.token
        board = self.board
        if ((x + token.x) > board.x) or ((y + token.y) > board.y):
            return True
        if (x < 0) or (y < 0):
            return True
        return False

    def put_token(self, token_y, token_x):
        ansDict = {}
        board = self.board
        for board_y in range(board.y):
            for board_x in range(board.x):
                if board.board[board_y][board_x] in (self.char, self.char.upper()):
                    x = board_x - token_x
                    y = board_y - token_y
                    if self.check_overflow(x, y) == 0 and self.check_overlap(x, y) == 0:
                        ansDict[(y, x,)] = 0
        if len(ansDict) != 0:
            self.eval.choice_place(ansDict, self.board, self.enemy_char)
            return True
        else:
            return False

    def put_random(self):
        for token_y, token_x in self.token.get_topleft_edge():
            if token_y is None or token_x is None:
                break
            if self.put_token(token_y, token_x):
                return True
        print("0 0")
        return False
