from core.node import node
from random import choice

def expansion(leaf: node):
    '''
    Given a leaf, create a child node randomly
    Up to mcts.py to create a node and link it to tree
    Returns the chosen move from the leaf
    Up to mcts.py to check if ndoe is terminal
    '''

    chosen_move = choice(leaf.untried_moves)
    return chosen_move