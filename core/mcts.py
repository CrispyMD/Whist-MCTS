from core import selection, expansion, rollout, backpropagation, node
from games.game import Game
from time import perf_counter

class MCTS:
    def __init__(self, game: Game, duration):
        self.game = game
        self.DURATION = duration
    
    def get_next_move(self):
        '''
        Up to mcts.py to create a node and link it to tree
        Returns the chosen move to play
        Up to mcts.py to check if ndoe is terminal (instead of either one of the 4 steps)
        '''


        number_of_players = self.game.get_number_of_players()
        start_time = perf_counter()
        iterations = 0
        root = node.node(number_of_players=number_of_players)
        root.set_untried_moves(self.game.get_legal_moves())

        while (perf_counter() - start_time) < self.DURATION:
            state = self.game.get_current_state().clone()

            selected_node, state = selection.selection(root, state)

            if not state.is_terminal_state():
                selected_move = expansion.expansion(selected_node)
                state.apply_move(selected_move)

                #attaching new node
                new_node = node.node(selected_move, selected_node, number_of_players)
                selected_node.children[selected_move] = new_node
                new_node.set_untried_moves(state.get_legal_moves())

                result_scores = rollout.rollout(state)
            else:
                #selected node is terminal
                result_scores = state.get_result()
                new_node = selected_node
            
            backpropagation.back_propagation(new_node, result_scores)
            iterations += 1

        for move, child in root.children.items():
            print(move, child.visits, child.scores)

        best_move = max(root.children, key=lambda k: root.children[k].visits)
        return best_move