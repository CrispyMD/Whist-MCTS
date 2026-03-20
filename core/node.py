class node:
    def __init__(self, move=None, parent=None):
        '''
        :param state: State that the node is representing

        :param move: the move that leads to this node, from it's parent
        to get from parent to this node, play self.move
        '''

        self.playouts = 0.0
        self.wins = 0.0
        self.children = dict({})
        #key is move and value is the corresponding child node

        self.parent = parent
        self.untried_moves = []
        self.move = move

    def set_unvisited_states(self, moves):
        self.untried_moves = moves

    def is_leaf(self):
        return not self.children