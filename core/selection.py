from core.node import node
from math import log, sqrt

def selection(current_node: node):
    return_node = current_node
    while not return_node.is_leaf():
        return_node = select_highest_value_child(return_node)
    return current_node

def select_highest_value_child(current_node: node):
    '''
    assuming current_node is not a leaf
    '''

    if current_node.untried_moves: #untried moves list is not empty
        move = current_node.untried_moves[0]
        return current_node.children[move]

    max_node = current_node.children[0]
    max_value = upper_confidence_bound(max_node)
    for child in current_node.children[1:]:
        if (ucb:=upper_confidence_bound(child)) > max_value:
            max_value = ucb
            max_node = child
    return max_node

def upper_confidence_bound(current_node: node):
    '''
    Calculates UCB value for current node
    '''
    c = sqrt(2)
    exploitation = current_node.wins / current_node.playouts
    exploration = c * sqrt(log(current_node.parent.playouts / current_node.playouts))
    return exploration + exploitation