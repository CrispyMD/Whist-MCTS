from core import selection, expansion, rollout, backpropagation, node
from games.game import Game
from time import perf_counter, sleep

class MCTS:
    def __init__(self, game: Game):
        self.game = game
    
    def get_next_move(self):    
        duration = .5 #seconds
        start_time = perf_counter() + duration
        iterations = 0
        current_state = self.game.get_current_state()
        root = node(current_state)

        while (perf_counter() - start_time) < duration:
            leaf = selection(root)
            root_of_expansion = expansion(leaf) #TODO: Add logic of if leaf is terminal
            result = rollout(root_of_expansion)
            backpropagation(root_of_expansion, result)
            iterations += 1

        best_move = root.get_best_move()

        return best_move