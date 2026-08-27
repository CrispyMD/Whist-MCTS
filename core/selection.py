from core.node import node
from math import log, sqrt
from games.game import State, Game

C = sqrt(2)

def selection(current_node: node, current_state: State) -> tuple[node, State, int]:
    '''
    Returns a pointer to the selected node,
    the state it is representing, and the player whose turn
    it is from return_node
    '''

    number_of_players = len(current_node.scores)
    current_player = current_state.get_current_player()
    return_node = current_node
    return_state = current_state
    while not return_node.is_leaf():
        if return_node.untried_moves_exist():
            return return_node, return_state

        return_node, return_state = select_highest_value_child(return_node, return_state, current_player)
        current_player = (current_player + 1) % number_of_players
    return (return_node, return_state)




def select_highest_value_child(current_node: node, current_state: State, current_player: int) -> tuple[node, State]:
    '''
    assuming current_node has no untried moves 
    '''
    
    max_node = None
    max_value = -1
    for child in current_node.children.values():
        if max_value == -1:
            max_node = child
            max_value = upper_confidence_bound(max_node, current_player)
        elif (ucb:=upper_confidence_bound(child, current_player)) > max_value:
            max_value = ucb
            max_node = child
    current_state.apply_move(max_node.move)
    return max_node, current_state




def upper_confidence_bound(current_node: node, current_player: int) -> float:
    '''
    Calculates UCB value for current node
    '''
    
    exploitation = current_node.scores[current_player] / current_node.visits
    exploration = C * sqrt(log(current_node.parent.visits) / current_node.visits)
    return exploration + exploitation