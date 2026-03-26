class node:
    def __init__(self, move=None, parent=None, number_of_players=4):
        '''
        :param state: State that the node is representing

        :param move: the move that leads to this node, from it's parent
        to get from parent to this node, play self.move
        '''
        
        self.visits = 0
        self.scores = [0 for _ in range(number_of_players)]
        self.children = dict({})
        #key is move and value is the corresponding child node
    
        self.parent = parent
        self.untried_moves = []
        self.move = move

    def set_untried_moves(self, moves):
        self.untried_moves = moves

    def is_leaf(self):
        return len(self.children) == 0
    
    def is_terminal(self):
        return (len(self.untried_moves) == 0) and (len(self.children) == 0)
    
    def untried_moves_exist(self):
        return len(self.untried_moves) != 0