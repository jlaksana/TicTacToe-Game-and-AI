import math

class Player:
    def __init__(self, symbol) -> None:
        self.symbol = symbol

    def select(self,board):
        pass

    def play(self, board):
        pass

class HumanPlayer(Player):
    def __init__(self, symbol) -> None:
        super().__init__(symbol)

    def select(self,board):
        pass

    def play(self, board):
        pass

class AIPlayer(Player):
    def __init__(self, symbol) -> None:
        super().__init__(symbol)

    def play(self, board):
        copy = board.copy()
        i = self.minimax(copy, -math.inf, math.inf)
        # calculate pos based on i, then add to board


    def minimax(self, board, alpha, beta) -> int:
        pass