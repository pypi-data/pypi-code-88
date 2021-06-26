from typing import Dict, Iterator, List, Optional, Tuple


class Token:
    def __init__(self, y: int = -1, x: int = -1):
        self.y = y
        self.x = x
        self.shape: List[str] = []

    def read(self) -> None:
        """標準入力からToken情報を読み取る"""
        self.y, self.x = map(int, input()[:-1].split(" ")[1:])
        self.shape = [input() for _ in range(self.y)]

    def get_topleft_edge(self) -> Iterator[Tuple[Optional[int], Optional[int]]]:
        """*の座標(左上0, 0)を取得する。座標は左上から右 → 下に向かって探索する

        Returns:
            tuple: *の座標(なければNone, None)

        Yields:
            Iterator[Tuple[Optional[int], Optional[int]]]: *の座標
        """
        for y in range(self.y):
            for x in range(self.x):
                if self.shape[y][x] == "*":
                    yield y, x
        return None, None

    def get_bottomright_edge(self) -> Iterator[Tuple[Optional[int], Optional[int]]]:
        """get_topleft_edgeの右下から探索版。未使用"""
        for y in range(self.y)[::-1]:
            for x in range(self.x)[::-1]:
                if self.shape[y][x] == "*":
                    yield y, x
        return None, None


class Board:
    def __init__(self, y: int = -1, x: int = -1) -> None:
        self.y = y
        self.x = x
        self.board: List[str] = []

    def read(self) -> None:
        """標準入力からBoard情報を読み取る"""
        self.y, self.x = map(int, input()[:-1].split(" ")[1:])
        _ = input()
        self.board = [input().split(" ")[1] for _ in range(self.y)]


class Player:
    def __init__(self, p_player_num: str) -> None:
        """Playerを初期化する

        Args:
            p_player_num (str): pPLAYER＿NUMBER (p1 or p2)
        """
        self.p = p_player_num
        self.char = "o" if self.p == "p1" else "x"
        self.enemy_char = "x" if self.char == "o" else "o"
        self.board = Board()
        self.token = Token()

    def is_enemy_char(self, cell: str) -> bool:
        """敵のマスか判定する"""
        return cell in (self.enemy_char, self.enemy_char.upper())

    def is_player_char(self, cell: str) -> bool:
        """自分のマスか判定する"""
        return cell in (self.char, self.char.upper())

    def put_random(self) -> bool:
        """playerが出力すべき情報を出力する

        Returns:
            bool: Tokenを当てはめられる座標が見つかったらTrue, そうでないならFalse
        """
        self.enemies = self.get_enemy_pos_list()
        self.scores: Dict[Tuple[int, int], int] = {}
        if self.put_token():
            return True

        print("0 0")
        return False

    def put_token(self) -> bool:
        """Tokenを配置する座標を標準出力に出力する

        Returns:
            bool: tokenを当てはめられたか
        """
        board = self.board
        answers: List[Tuple[int, Tuple[int, int]]] = []

        for y in range(board.y):
            for x in range(board.x):
                # Tokenを当てはめられるなら、スコアと座標をリストに追加する
                if not self.check_overflow(x, y) and not self.check_overlap(x, y):
                    answers.append((self.calc_token_score(x, y), (y, x)))
        if answers:
            answers.sort()
            answer = answers[0][1]
            print(f"{answer[0]} {answer[1]}")
            return True
        return False

    def calc_token_score(self, x: int, y: int) -> int:
        """Tokenを配置した場合のスコアを計算する"""
        score = 0
        for token_y in range(self.token.y):
            for token_x in range(self.token.x):
                if self.token.shape[token_y][token_x] != "*":
                    continue
                if self.board.board[token_y + y][token_x + x] != ".":
                    continue
                score += self.calc_cell_score(token_x + x, token_y + y)
        return score

    def calc_cell_score(self, x: int, y: int) -> int:
        """マスのスコアを返す"""
        score = self.scores.get((y, x))
        if score is None:
            score = min(
                [abs(y - enemy[0]) + abs(x - enemy[1]) for enemy in self.enemies]
            )
            self.scores[(y, x)] = score
        return score

    def get_enemy_pos_list(self) -> List[Tuple[int, int]]:
        """敵のマスリストを返す"""
        enemies: List[Tuple[int, int]] = []
        for y in range(self.board.y):
            for x in range(self.board.x):
                if self.is_enemy_char(self.board.board[y][x]):
                    enemies.append((y, x))
        return enemies

    def check_overflow(self, x: int, y: int) -> bool:
        """tokenがboardからはみ出ていないかチェックする

        Args:
            x (int): tokenを配置するx座標
            y (int): tokenを配置するy座標

        Returns:
            bool: はみ出ているならTrue
        """
        token = self.token
        board = self.board

        if ((x + token.x) > board.x) or ((y + token.y) > board.y):
            return True
        if (x < 0) or (y < 0):
            return True
        return False

    def check_overlap(self, x: int, y: int) -> bool:
        """tokenが敵のマスと重なっていないか、自分のマスと1つだけ重なっていないかを確認する

        Args:
            x (int): tokenを配置するx座標
            y (int): tokenを配置するy座標

        Returns:
            bool: 配置可能=False/配置不可=True
        """
        token = self.token
        overlap_counter = 0

        for token_y in range(token.y):
            for token_x in range(token.x):
                if token.shape[token_y][token_x] != "*":
                    continue
                if self.is_enemy_char(self.board.board[y + token_y][x + token_x]):
                    return True
                if self.is_player_char(self.board.board[y + token_y][x + token_x]):
                    overlap_counter += 1

        if overlap_counter != 1:
            return True

        return False


def main() -> None:
    """fillerのmain部分"""
    _, _, p_player_num, _, _ = input().split(" ")

    player = Player(p_player_num)
    while True:
        player.board.read()
        player.token.read()
        player.put_random()
