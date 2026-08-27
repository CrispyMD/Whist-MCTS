from abc import ABC, abstractmethod

class Game(ABC):
    '''
    methods that refer to the current state of the game
    '''
    @abstractmethod
    def current_player(self) -> int:
        '''
        In {0, 1, ..., number_of_players}
        '''
        pass

    @abstractmethod
    def get_legal_moves(self):
        pass

    @abstractmethod
    def apply_move(self, move):
        pass

    @abstractmethod
    def is_terminal_state(self):
        pass

    @abstractmethod
    def get_result(self):
        pass

    @abstractmethod
    def get_current_state(self):
        pass
    
    @abstractmethod
    def normalize_score(self, score: float):
        pass


    @abstractmethod
    def get_number_of_players(self) -> int:
        pass

    

class State(ABC):
    @abstractmethod
    def get_current_player(self):
        pass
    
    @abstractmethod
    def apply_move(self, move):
        '''
        returns a state
        Does not change the parameter state!!!
        '''
        pass

    @abstractmethod
    def is_terminal_state(self):
        pass
    
    @abstractmethod
    def get_legal_moves(self):
        '''
        returns a list of moves
        '''
        pass


    @abstractmethod
    def get_result(self):
        '''
        Assumes state is terminal
        Returns a list of scores
        '''
        pass
    
    @abstractmethod
    def clone(self):
        '''
        Returns a deep copy of the state
        '''
        pass