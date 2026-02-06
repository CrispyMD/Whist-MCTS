class node:
    def __init__(self, state, move=None, parent=None):
        '''
        :param state: State that the node is representing

        :param move: the move that leads to this node, from it's parent
        to get from parent to this node, play self.move
        '''

        self.state = state
        self.playouts = 0
        self.wins = 0
        self.children = []
        self.parent = parent
        self.unvisited_states = []
        self.move = move

    def set_unvisited_states(self, states):
        self.unvisited_states = states
    
    def get_best_move(self):
        '''
        Returns the move that leads to the best state
        '''
        pass