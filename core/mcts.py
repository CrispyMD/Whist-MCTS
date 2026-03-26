from core import selection, expansion, rollout, backpropagation, node
from games.game import Game
from time import perf_counter

class MCTS:
    def __init__(self, game: Game):
        self.game = game
    
    def get_next_move(self):
        '''
        Up to mcts.py to create a node and link it to tree
        Returns the chosen move to play
        Up to mcts.py to check if ndoe is terminal
        '''
        

        number_of_players = self.game.get_number_of_players()
        duration = 0.5 #seconds
        start_time = perf_counter() + duration
        iterations = 0
        root = node.node(number_of_players=number_of_players)


        while (perf_counter() - start_time) < duration:
            state = self.game.get_current_state().clone()

            selected_node, state = selection.selection(root, state)

            selected_move = expansion.expansion(selected_node) 
            #TODO: Add logic of if move leads to terminal state

            #attaching new node
            new_node = node.node(selected_move, selected_node, number_of_players)
            new_node.set_untried_moves(state.get_legal_moves())

            result_scores = rollout.rollout(state)
            
            backpropagation.back_propagation(new_node, result_scores)
            iterations += 1

        best_move = max(root.children, key=lambda k: root.children[k].visits)
        return best_move