"""
TicTacToe Game and AI

Started: 9/8/21
Finished: 9/14/21

Goal: Create a playable Tictactoe game with an unbeatable AI using the Minimax algorithm.
    Implement with PyGame
    use alpha-beta pruning to optimize


"""
import pygame
import time
from players import HumanPlayer, AIPlayer

pygame.init()

class TicTacToe:
    N = 3
    def __init__(self) -> None:
        self.board = [[" "] * TicTacToe.N for i in range(TicTacToe.N)]
        self.num_empty = TicTacToe.N * TicTacToe.N
        self.selected_pos = None
        
    def __repr__(self) -> str:
        return f"{self.board[0]}\n{self.board[1]}\n{self.board[2]}"

    def is_full(self) -> bool:
        return self.num_empty == 0

    def cur_capacity(self) -> int:
        return self.num_empty

    def add_at_selected(self, symbol: str):
        if self.is_full():
            return False

        x, y = self.selected_pos    
        if (self.board[y][x] == ' '):
            self.board[y][x] = symbol
            self.num_empty -= 1
            return True
        return False

    def add_at_i(self, symbol, i):
        if self.is_full():
            return False

        x = i % 3
        y = i // 3

        if (self.board[y][x] == ' '):
            self.board[y][x] = symbol
            self.num_empty -= 1
            return True
        return False

    def delete_symbol(self, i ):
        x = i % 3
        y = i // 3
        if (self.board[y][x] != " "):
            self.board[y][x] = " "
            self.num_empty += 1

    def has_winner(self) -> str:
        """returns a string representing if there is a winner or not.
        "" - no winner
        "X" - X wins
        "O" - O wins
        "D" - draw""" 
        for i in range(3):
            # check rows
            if self.board[i][0] != " " and self.board[i][0] == self.board[i][1] == self.board[i][2]:
                return self.board[i][0]
            
            #check columns
            if self.board[0][i] != " " and self.board[0][i] == self.board[1][i] == self.board[2][i]:
                return self.board[0][i]

        # check diagonals
        mid_sym = self.board[1][1]
        if mid_sym != " " and (self.board[0][0] == self.board[2][2] == mid_sym \
            or self.board[0][2] == self.board[2][0] == mid_sym):
            return mid_sym

        #check draw
        if self.cur_capacity() == 0:
            return "D"

        return ""

    def copy(self):
        copy = TicTacToe()
        copy.board = self.board.copy()
        copy.num_empty = self.num_empty
        return copy

    def draw(self):
        gap = Screen.LENGTH / TicTacToe.N
        for i in range(1, TicTacToe.N):
            #draw horizontals
            pygame.draw.line(Screen.WINDOW, (0,0,0), (0,i*gap), (Screen.LENGTH, i*gap), 5)
            #draw verticals
            pygame.draw.line(Screen.WINDOW, (0,0,0), (i*gap,0), (i*gap,Screen.HEIGHT-50), 5)

        for row in range(TicTacToe.N):
            for col in range(TicTacToe.N):
                if self.selected_pos == (col,row):
                    pygame.draw.rect(Screen.WINDOW, (155,207,225), (150 * col + 10, 150 * row + 10, 130, 130), 3)

                if self.board[row][col] == " ":
                    continue

                text = Screen.FONT.render(self.board[row][col], 1, (0,0,0))
                text_rect = text.get_rect(center=(75+150*col, 75+150*row))
                Screen.WINDOW.blit(text,text_rect)

    def select(self, position):
        if position[1] >= Screen.HEIGHT - 50:
            return

        x = int(position[0] // (Screen.LENGTH / TicTacToe.N))
        y = int (position[1] // ((Screen.HEIGHT - 50)/TicTacToe.N))
        self.selected_pos = (x,y)


class Screen:
    """Does not need to be instantiated.
    Screen class responsible for managing the pygame screen displaying text.
    Some class attributes include its dimensions, background color, default font and color."""
    LENGTH = 450
    HEIGHT = 500
    WINDOW = pygame.display.set_mode((LENGTH, HEIGHT))
    BG_COLOR = (255,255,255)    #white
    FONT = pygame.font.SysFont("msuigothic",130)
    SUBFONT = pygame.font.SysFont("arial", 70)

    def fill() -> None:
        """Fills the screen background with default background color"""
        Screen.WINDOW.fill(Screen.BG_COLOR)
    
    def display_welcome():
        text = Screen.SUBFONT.render("Welcome", True, (0,0,0))
        text_rect = text.get_rect(center=(Screen.LENGTH/2, 60))
        Screen.WINDOW.blit(text, text_rect)

    def display_menu(opt1, opt2):
        text = Screen.SUBFONT.render(opt1, True, (0,0,0))
        text_rect = text.get_rect(center=(Screen.LENGTH/2, Screen.HEIGHT/2-50))
        Screen.WINDOW.blit(text, text_rect)
        text = Screen.SUBFONT.render(opt2, True, (0,0,0))
        text_rect = text.get_rect(center=(Screen.LENGTH/2, Screen.HEIGHT/2+50))
        Screen.WINDOW.blit(text, text_rect)

    def display_winner(winner:str):
        if winner == "D":
            msg = "DRAW"
        else:
            msg = winner + " wins!"
        
        text = Screen.SUBFONT.render(msg, True, (0,0,0))
        text_rect = text.get_rect(center=(Screen.LENGTH/2, Screen.HEIGHT/2-50))
        Screen.WINDOW.blit(text, text_rect)
        text = pygame.font.SysFont("arial", 30).render("Press SPACE to play again", True, (0,0,0))
        text_rect = text.get_rect(center=(Screen.LENGTH/2, Screen.HEIGHT/2+50))
        Screen.WINDOW.blit(text, text_rect)

    def display_turn(player):
        text = pygame.font.SysFont("arial", 30).render(player.symbol + "'s TURN", True, (0,0,0))
        text_rect = text.get_rect(center=(Screen.LENGTH-70, Screen.HEIGHT-25))
        Screen.WINDOW.blit(text,text_rect)

    def display_score(scores):
        msg = f"P1: {scores[0]}  P2: {scores[1]}  D: {scores[2]}"
        text = pygame.font.SysFont("arial", 30).render(msg, True, (0,0,0))
        text_rect = text.get_rect(center=(110, Screen.HEIGHT-25))
        Screen.WINDOW.blit(text,text_rect)
    

class Game:
    def __init__(self) -> None:
        self.player1 = HumanPlayer()
        self.player2 = None
        self.cur_player = None
        self.other_player = None
        self.score = [0,0,0]  #[P1, P2, Draws]

    def set_players(self):
        while self.player2 is None:
            Screen.fill()
            Screen.display_welcome()
            Screen.display_menu("One Player", "Two Players")

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if Screen.HEIGHT/2-70 <= pos[1] <= Screen.HEIGHT/2-20:
                        self.player2 = AIPlayer()
                    elif Screen.HEIGHT/2+20 <= pos[1] <= Screen.HEIGHT/2+80:
                        self.player2 = HumanPlayer()                    

            pygame.display.update()
            
        self.set_symbols()

    def set_symbols(self):
         while self.cur_player is None:
            Screen.fill()
            Screen.display_welcome()
            Screen.display_menu("P1 choose:", "X or O")

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    ok_height = Screen.HEIGHT/2+20 <= pos[1] <= Screen.HEIGHT/2+80
                    if pos[0] < Screen.LENGTH/2 and ok_height:
                        self.player1.set_symbol("X")
                        self.cur_player = self.player1
                        self.player2.set_symbol("O")
                        self.other_player = self.player2
                    elif pos[0] > Screen.LENGTH/2 and ok_height:
                        self.player1.set_symbol("O")
                        self.other_player = self.player1
                        self.player2.set_symbol("X")
                        self.cur_player = self.player2

            pygame.display.update()

    def play(self, board):
        # Switch players if player finishes their turn
        if self.cur_player.play(board):
            self.cur_player, self.other_player = self.other_player, self.cur_player

    def restart(self):
        if self.player1.symbol == "X":
            self.cur_player = self.player1
            self.other_player = self.player2
        else:
            self.cur_player = self.player2
            self.other_player = self.player1

    def update_score(self,winner):
        if winner == "D":
            self.score[2] += 1
        elif winner == self.player1.symbol:
            self.score[0] += 1
        else:
            self.score[1] += 1

    def end_game(self, winner):
        self.update_score(winner)
        while True:
            Screen.fill()
            Screen.display_winner(winner)
            Screen.display_score(self.score)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        return

            pygame.display.update()


def game_loop():
    pygame.display.set_caption("TICTACTOE")
    board = TicTacToe()
    g = Game()
    g.set_players()
    while True:
        Screen.fill()
        g.play(board)
        board.draw()
        Screen.display_turn(g.cur_player)
        Screen.display_score(g.score)
        pygame.display.update()
        winner = board.has_winner()
        if winner:
            time.sleep(1)
            g.end_game(winner)
            board = TicTacToe()
            g.restart()

if __name__ == "__main__":
    game_loop()
    
    