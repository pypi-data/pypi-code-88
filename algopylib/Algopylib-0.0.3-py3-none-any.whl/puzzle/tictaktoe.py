class TicTacToe:
    game_name = 'Tic-Tac-Toe'
    players = 2

    def __init__(self, seed=0):
        self.board = ['']*9
        self.current_player = 0
        self.history = []

    def get_state_and_actions(self):  # Does not mutate data!
        actions = [i for i, s in enumerate(self.board) if s == '']
        sna = {'state': (self.board, self.current_player), 'actions': actions}
        return tuple([sna if i == self.current_player else None for i in range(self.players)])

    def execute_actions(self, actions):  # Does change state
        self.history.append(actions)
        move_to_exec = actions[self.current_player]
        self.board[move_to_exec] = self.current_player
        # check if win
        if self.check_player_win(self.current_player):
            # we have a winner
            return tuple([1.0 if i == self.current_player else 0.0 for i in range(self.players)])
        # check if tie
        if len([x for x in self.board if x == '']) == 0:
            return 0.5, 0.5
        # finalize
        self.current_player = (self.current_player+1) % 2
        return None

    def check_player_win(self, player):  # does not change state
        for j in range(3):
            win = True
            for i in range(3):
                win &= self.board[3*j+i] == player
            if win:
                return win
        for j in range(3):
            win = True
            for i in range(3):
                win &= self.board[j+i*3] == player
            if win:
                return win
        if self.board[0] == self.board[4] == self.board[8] == player:
            return True
        if self.board[2] == self.board[4] == self.board[6] == player:
            return True
        return False
