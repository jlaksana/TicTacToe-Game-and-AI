"""
TicTacToe Game and AI

Started: 9/8/21
Finished:

Goal: Create a playable Tictactoe game with an unbeatable AI using the Minimax algorithm.
    Implement with PyGame



"""
import pygame

#pygame.init()

class TicTacToe:
    N = 3
    def __init__(self) -> None:
        self.board = [[" "] * TicTacToe.N for i in range(TicTacToe.N)]
        self.num_empty = 9
        
    def __repr__(self) -> str:
        return f"{self.board[0]}\n{self.board[1]}\n{self.board[2]}"

    def is_full(self) -> bool:
        return self.num_empty == 0

    def capacity(self) -> int:
        return self.num_empty

    def add_symbol(self, symbol: str, x_pos: int, y_pos: int) -> bool:
        if self.is_full():
            return False

        self.board[y_pos][x_pos] = symbol
        return True

    def has_winner(self) -> int:
        """returns a integer representing if there is a winner or not.
        0 - no winner
        1 - X wins
        2 - O wins
        3 - draw"""
        


class Screen:
    pass

class Game:
    pass


if __name__ == "__main__":
    t = TicTacToe()
    print(t)