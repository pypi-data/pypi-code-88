from .game import Board, Token


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
                    if board.check_overflow(x, y, self.token) == 0 and board.check_overlap(x, y, self.token) == 0:
                        ansDict[(x, y)] = 1
        return ansDict

    def put_random(self):
        board: Board = self.board
        if not self.won and board.enemy_occupation <= self.enemy_occupation:
            # Won!
            self.won = True
        self.enemy_occupation = board.enemy_occupation

        tactics_attatck = [+25, +100, -20]
        # tactics_capture = [+5, -10, -12]
        tactics_capture = [+3, +10, -12]
        tactics_defend = [+5, +10, -2] 
        if board.occipied_rate < 0.15:
            tactics = tactics_attatck
        elif board.occipied_rate > 0.75:
            tactics = tactics_defend
        else:
            tactics = tactics_capture
#            tactics = random.choice([ tactics_attatck, tactics_capture, tactics_defend ])
        ansDict = {}
        token: Token = self.token
        for token_y, token_x in self.token.get_topleft_edge():
            self.put_token(token_y, token_x, ansDict)
        # for row in token.shape:
        #     print(row, file=sys.stderr)
        # for row in pmap:
        #     print(row, file=sys.stderr)
        if len(ansDict) > 0:
            # print(list(ansDict.keys()), file=sys.stderr)
            if self.won:
                ans = list(ansDict.keys())[0]
            else:
                pmap = potential_map(board.x, board.y, board.board, self.enemy_char, self.char, *tactics)
                ts = sorted([ (t, self.token_potential(token, t[0], t[1], pmap)) for t in ansDict.keys() ], key=lambda t:t[1])
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
        for ty in range(token.offset_y, token.inset_y):
            for tx in range(token.offset_x, token.inset_x):
                if token.shape[ty][tx] == "*":
                    s += potential[y + ty][x + tx]
        # print((x, y), s, file=sys.stderr)
        return s


    def neighbors(x: int, y: int, w: int, h: int, visited: dict):
        return [ t for t in [ (x+1,y), (x-1,y), (x,y+1), (x,y-1) ] if not t in visited and 0 <= t[0] and t[0] < w and 0 <= t[1] and t[1] < h ]

    def bfs(potential: list[list[int]], w: int, h: int, board: list[str], char: str, charge: float):
        visited = {}
        queue: dict[tuple[int,int], int] = {}
        d = 0
        for y in range(h):
            for x in range(w):
                if board[y][x] == char:
                    queue[(x,y)] = 1
        while len(queue) > 0:
            nq: dict[tuple[int,int], int] = {}
            for (x,y) in queue.keys():
                potential[y][x] += d * charge
                visited[(x,y)] = 1
                for n in self.neighbors(x, y, w, h, visited):
                    nq[n] = 0
            queue = nq
            d += 1



def potential_map(x: int, y: int, board: list[str], enemy_char: str, char: str, wall_charge: float, enemy_charge: float, my_charge: float):
    # for i in range(y):
    #     print("".join(board[i]))
    potentials: list[list[int]] = [ [0] * x for _ in range(y) ]
    for i in range(y):
        for j in range(x):
            potentials[i][j] = wall_charge * min(i, y - i - 1, j, x - j - 1)
    bfs(potentials, x, y, board, enemy_char, enemy_charge)
    bfs(potentials, x, y, board, char, my_charge)
    for i in range(y):
        for j in range(x):
            potentials[i][j] = int(potentials[i][j])
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
