from games.game import Game, State

class TicTacToe_State(State):
    def __init__(self):
        super().__init__()
        self.board = [[-1 for _ in range(3)] for _ in range(3)]
        self.current_player = 0

    def get_current_player(self):
        return self.current_player

    def apply_move_rc(self, row, column):
        # assumes move is legal
        self.board[row][column] = self.current_player
        self.current_player = 1 if self.current_player == 0 else 0

    def apply_move(self, move):
        self.apply_move_rc(move[0], move[1])

    def is_terminal_state(self):
        for i in range(3):
            if self.board[i][0] != -1 and self.board[i][0] == self.board[i][1] == self.board[i][2]:
                return True
            if self.board[0][i] != -1 and self.board[0][i] == self.board[1][i] == self.board[2][i]:
                return True
        
        if self.board[0][0] != -1 and self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return True
        if self.board[0][2] != -1 and self.board[0][2] == self.board[1][1] == self.board[2][0]:
            return True
        
        for row in self.board:
            if -1 in row:
                return False
            
        return True

    def get_result(self):
        if not self.is_terminal_state():
            return None
        
        for i in range(3):
            if self.board[i][0] != -1 and self.board[i][0] == self.board[i][1] == self.board[i][2]:
                return self.return_proper_results_list(self.board[i][0])
            if self.board[0][i] != -1 and self.board[0][i] == self.board[1][i] == self.board[2][i]:
                return self.return_proper_results_list(self.board[0][i])
        
        if self.board[0][0] != -1 and self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return self.return_proper_results_list(self.board[0][0])
        if self.board[0][2] != -1 and self.board[0][2] == self.board[1][1] == self.board[2][0]:
            return self.return_proper_results_list(self.board[0][2])
        
        return [0.5, 0.5]

    def return_proper_results_list(self, winner):
        if winner == 0:
            return [1, 0]
        return [0,1]

    def get_legal_moves(self):
        legal_moves = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == -1:
                    legal_moves.append((i, j))
        return legal_moves

    def clone(self):
        new_state = TicTacToe_State()
        new_state.board = [[self.board[i][j] for j in range(3)] for i in range(3)]
        new_state.current_player = self.current_player
        return new_state


class TicTacToe(Game):
    '''
    Using a 3x3 matrix of entries 1,-1,0
    starting player is 1
    X=1, O=-1
    self.board is 3x3 matrix
    '''

    def __init__(self):
        super().__init__()
        self.state = TicTacToe_State()

    

    def current_player(self):
        return self.state.current_player()
    
    def is_terminal_state(self):
        return self.state.is_terminal_state()
    
    def get_result(self):
        return self.state.get_result()
    
    def apply_move_rc(self, row, column):
        self.state.apply_move_rc(row, column)
    
    def apply_move(self, move):
        self.state.apply_move(move)

    
    def get_legal_moves(self):
        return self.state.get_legal_moves()
    
    def get_current_state(self):
        return self.state

    def get_number_of_players(self):
        return 2



    def print_board(self):
        symbol = {0: "X", 1: "O", -1: " "}
        for i in range(3):
            row = " | ".join(symbol[self.state.board[i][j]] for j in range(3))
            print(row)
            if i < 2:
                print("-" * 9)

    def normalize_score(self, score):
        return score #score is normalized since it is alawys on of: (0,1), (1,0), (0,0)

def number_to_position(n):
    if n < 1 or n > 9:
        raise ValueError("n must be between 1 and 9")
    
    n -= 1  # make it 0-based
    row = n // 3
    col = n % 3
    return (row, col)