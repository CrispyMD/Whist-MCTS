from games.game import Game

class TicTacToe(Game):
    '''
    Docstring for TicTacToe

    in form of 1,-1,0
    starting player is 1
    X=1, O=-1
    self.board is 3x3 matrix
    '''

    def __init__(self):
        super().__init__()
        self.board = [[0 for _ in range(3)] for _ in range(3)]
        self.current_player = 1
    

    def current_player(self):
        return self.current_player
    
    def is_terminal_state(self):
        for i in range(3):
            if self.board[i][0] != 0 and self.board[i][0] == self.board[i][1] == self.board[i][2]:
                return True
            if self.board[0][i] != 0 and self.board[0][i] == self.board[1][i] == self.board[2][i]:
                return True
        
        if self.board[0][0] != 0 and self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return True
        if self.board[0][2] != 0 and self.board[0][2] == self.board[1][1] == self.board[2][0]:
            return True
        
        for row in self.board:
            if 0 in row:
                return False
            
        return True
    
    def get_result(self):
        if not self.is_terminal_state():
            return None
        
        for i in range(3):
            if self.board[i][0] != 0 and self.board[i][0] == self.board[i][1] == self.board[i][2]:
                return self.board[i][0]
            if self.board[0][i] != 0 and self.board[0][i] == self.board[1][i] == self.board[2][i]:
                return self.board[0][i]
        
        if self.board[0][0] != 0 and self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return self.board[0][0]
        if self.board[0][2] != 0 and self.board[0][2] == self.board[1][1] == self.board[2][0]:
            return self.board[0][2]
        
        return 0
    
    def apply_move_rc(self, row, column):
        # assumes move is legal
        self.board[row][column] = self.current_player
        self.current_player = -self.current_player
    
    def apply_move(self, move):
        self.apply_move_rc(move[0], move[1])

    
    def get_legal_moves(self):
        legal_moves = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    legal_moves.append((i, j))
        return legal_moves
    
    def get_current_state(self):
        return [[self.board[i][j] for i in range(3)] for j in range(3)]


    def print_board(self):
        symbol = {1: "X", -1: "O", 0: " "}
        for i in range(3):
            row = " | ".join(symbol[self.board[i][j]] for j in range(3))
            print(row)
            if i < 2:
                print("-" * 9)