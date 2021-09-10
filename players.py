import math
import pygame

class Player:
    def __init__(self, symbol) -> None:
        self.symbol = symbol

    def select(self,board) -> None:
        pass

    def play(self, board) -> bool:
        pass

class HumanPlayer(Player):
    def __init__(self, symbol) -> None:
        super().__init__(symbol)

    def select(self,board):
        pos = pygame.mouse.get_pos()
        board.select(pos)

    def play(self, board) -> bool:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.select(board)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if board.add_at_selected(self.symbol):
                            return True
        return False

class AIPlayer(Player):
    def __init__(self, symbol) -> None:
        super().__init__(symbol)

    def play(self, board) -> bool:
        copy = board.copy()
        i = self.minimax(copy, -math.inf, math.inf, True, 0)
        board.add_at_i(self.symbol,i)
        return True


    def minimax(self, board, alpha: int, beta:int, maximizing:bool, depth: int) -> int:
        winner = board.has_winner()
        if winner:
            if winner == self.symbol:
                return board.cur_capacity() + 1
            elif winner != "D":
                return -1 * (board.cur_capacity() + 1)
            else:
                return 0

        if maximizing:
            maxEval = -math.inf
            best_idx = 0
            for i in range(9):
                if not board.add_at_i(self.symbol, i): continue
                eval = self.minimax(board, alpha, beta, False, depth +1)
                if (eval > maxEval):
                    best_idx = i
                    maxEval = eval
                board.delete_symbol(i)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            if depth == 0:
                return best_idx
            return maxEval
        else:
            minEval = math.inf
            symbol = "O" if self.symbol == "X" else "X"
            for i in range(9):
                if not board.add_at_i(symbol, i): continue
                eval = self.minimax(board, alpha, beta, True, depth +1)
                minEval = min(minEval, eval)
                board.delete_symbol(i)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return minEval