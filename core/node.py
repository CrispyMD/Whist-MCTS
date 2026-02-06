class node:
    def __init__(self, state, parent=None):
        self.state = state
        self.playouts = 0
        self.wins = 0
        self.children = []
        self.parent = parent
        self.unvisited_states = []

    def set_unvisited_states(self, states):
        self.unvisited_states = states