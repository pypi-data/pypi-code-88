from typing import Iterator, List, Optional, Tuple


class Token:
    def __init__(self, y: int = -1, x: int = -1):
        self.y = y
        self.x = x
        self.shape: List[str] = []

    def read(self) -> None:
        """標準入力からToken情報を読み取る"""
        self.y, self.x = map(int, input()[:-1].split(" ")[1:])
        self.shape = []
        for _ in range(self.y):
            self.shape.append(input())

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
        self.board = []
        for _ in range(self.y):
            self.board.append(input().split(" ")[1])


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

    def put_random(self) -> bool:
        """playerが出力すべき情報を出力する

        Returns:
            bool: Tokenを当てはめられる座標が見つかったらTrue, そうでないならFalse
        """
        for token_y, token_x in self.token.get_topleft_edge():
            if token_y is None or token_x is None:
                break
            if self.put_token(token_y, token_x):
                return True

        print("0 0")
        return False

    def put_token(self, token_y: int, token_x: int) -> bool:
        """Tokenを配置する座標を標準出力に出力する

        Args:
            token_y (int): tokenの座標(y)
            token_x (int): tokenの座標(x)

        Returns:
            bool: tokenを当てはめられたか
        """
        board = self.board

        for board_y in range(board.y):
            for board_x in range(board.x):
                if board.board[board_y][board_x] in (self.char, self.char.upper()):
                    x = board_x - token_x
                    y = board_y - token_y
                    if not self.check_overflow(x, y) and not self.check_overlap(x, y):
                        print(f"{y} {x}")
                        return True

        return False

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

                if self.board.board[y + token_y][x + token_x] in (
                    self.enemy_char,
                    self.enemy_char.upper(),
                ):
                    return True

                if token.shape[token_y][token_x] == "*" and self.board.board[
                    y + token_y
                ][x + token_x] in (self.char, self.char.upper()):
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
