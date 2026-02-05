from abc import ABC, abstractmethod

class Game(ABC):
    @abstractmethod
    def current_player(self):
        pass

    @abstractmethod
    def get_legal_moves(self):
        pass

    @abstractmethod
    def apply_move(self):
        pass

    @abstractmethod
    def is_terminal_state(self):
        pass

    @abstractmethod
    def get_result(self):
        pass