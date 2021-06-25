import numpy as np


def printFile(str):
    with open("./test_w.txt", mode='a') as f:
        f.write(f"{str}")

class Evaluation():
    def read_enemy_pos(self, now_board, enemy_char):
        disDict = {}
        board = now_board.board
        enemyDict = {}
        for y in range(len(board)):
            for x in range(len(board[0])):
                if enemy_char.lower() == board[y][x].lower():
                    enemyDict[(y, x,)] = 0

        for y in range(len(board)):
            for x in range(len(board[0])):
                a = np.array([y, x])
                disDict[(y, x,)] = 0
                dis_tmp = 10000
                for i in enemyDict.items():
                    b = np.array([i[0][0], i[0][1]])
                    dis = np.linalg.norm(a - b, ord=1)
                    dis_tmp = min(dis, dis_tmp)
                disDict[(y, x,)] = dis_tmp
        return disDict

    def choice_place(self, ansDict, board, enemy_char):
        evalBoardDict = self.read_enemy_pos(board, enemy_char)
        for i in ansDict.keys():
            ansDict[i] = evalBoardDict[i]
        tmp = min(ansDict, key=ansDict.get)
        printFile(f"{tmp}\n")
        print(f"{tmp[0]} {tmp[1]}")
