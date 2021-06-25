from thechef_filler.src.yk_player import Player
from thechef_filler.src.game import Board, Token


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
