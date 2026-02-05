from games.game import Game
from random import choice

class RandomAgent:
    def __init__(self, game):
        self.game = game
    
    def make_move(self):
        '''
        returns chosen move
        '''

        if self.game.is_terminal_state():
            return
        legal_moves = self.game.get_legal_moves()
        move = choice(legal_moves)
        self.game.apply_move(move)
        return move
