from core.mcts import MCTS
from games.game import Game

class mcts_agent:
    def __init__(self, game: Game, duration = 0.5):
        self.core = MCTS(game, duration)
        

    def make_move(self):
        '''
        Returns chosen move
        '''
        if self.core.game.is_terminal_state():
            return
        move = self.core.get_next_move()
        self.core.game.apply_move(move)
        return move