"""
TicTacToe Game and AI

Started: 9/8/21
Finished:

Goal: Create a playable Tictactoe game with an unbeatable AI using the Minimax algorithm.
    Implement with PyGame
    use alpha-beta pruning to optimize



"""
import pygame

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

    def add_symbol(self, symbol: str) -> bool:
        if self.is_full():
            return False

        x, y = self.selected_pos    

        self.board[y][x] = symbol
        self.num_empty -= 1
        return True

    def delete_symbol(self):
        x, y = self.selected_pos
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
                text_rect = text.get_rect(center=(75+150*col, 17+150*row))
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
    FONT = pygame.font.SysFont("msuigothic",30)

    def fill() -> None:
        """Fills the screen background with default background color"""
        Screen.WINDOW.fill(Screen.BG_COLOR)
    
    def start_screen():
        pass

    def end_screen():
        pass

    def display_turn(player):
        pass
    

class Game:
    def __init__(self) -> None:
        self.x_player = None
        self.o_player = None

    def set_players(self):
        while True:
            Screen.fill()
            Screen.start_screen()

            # ask for one player or two 

    def play(self):
        pygame.display.set_caption("TICTACTOE")
        board = TicTacToe()
        cur_player = self.x_player
        other_player = self.o_player

        while True:
            Screen.fill()
            board.draw()

            # Commands for user inputs
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Game.quit_game()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    board.select(pos)

            pygame.display.update()
    

    def end_game(self):
        pass

    def quit_game():
        """Quits the game in safe state."""
        pygame.quit()
        quit()


if __name__ == "__main__":
    Game.play()
    