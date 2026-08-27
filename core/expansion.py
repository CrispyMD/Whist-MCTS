from core.node import node
from random import randint

def expansion(leaf: node):
    '''
    Given a leaf, create a child node randomly
    Up to mcts.py to create a node and link it to tree
    Returns the chosen move from the leaf
    Up to mcts.py to check if ndoe is terminal
    '''

    random_index = randint(0, len(leaf.untried_moves) - 1)
    chosen_move = leaf.untried_moves[random_index]
    leaf.untried_moves.pop(random_index)
    return chosen_move