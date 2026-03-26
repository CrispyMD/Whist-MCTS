from games.game import  State
from random import choice

def rollout(state: State) -> int:
    '''
    :param state: The starting state of the rollout
    Returns list of scores
    '''
    while not state.is_terminal_state():
        random_move = choice(state.get_legal_moves())
        state.apply_move(random_move)
    return state.get_result()