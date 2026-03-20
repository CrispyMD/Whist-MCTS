from core.node import node
from random import choice

def expansion(node: node):
    '''
    Given a leaf called node, create a child node randomly
    Returns a pointer to the new node
    '''
    #TODO: Figure out what to do when the child is a leaf
    chosen_state = choice(node.unvisited_states)
    return chosen_state