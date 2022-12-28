import sys
import os
import subprocess
import pygame
import pygame.image
from PIL import Image

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Install pygame if it is not already installed
try:
    import pygame
except ImportError:
    install("pygame")
    import pygame

pygame.init()
os.environ['SDL_AUDIODRIVER'] = 'alsa'
os.environ["SDL_VIDEODRIVER"] = 'dummy'

# Load the images and store them in a dictionary
images = {
    'black_pawn': pygame.image.load('img/black_pawn.png'),
    'black_rook': pygame.image.load('img/black_rook.png'),
    'black_knight': pygame.image.load('img/black_knight.png'),
    'black_bishop': pygame.image.load('img/black_bishop.png'),
    'black_queen': pygame.image.load('img/black_queen.png'),
    'black_king': pygame.image.load('img/black_king.png'),
    'white_pawn': pygame.image.load('img/white_pawn.png'),
    'white_rook': pygame.image.load('img/white_rook.png'),
    'white_knight': pygame.image.load('img/white_knight.png'),
    'white_bishop': pygame.image.load('img/white_bishop.png'),
    'white_queen': pygame.image.load('img/white_queen.png'),
    'white_king': pygame.image.load('img/white_king.png'),
}

window_size = 800
square_size = window_size // 8

pygame.display.set_caption('Scuffed Chess ai')
icon = pygame.Surface((1, 1))
icon.set_alpha(0)
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((window_size, window_size))
screen.fill((255, 255, 255))

# Initialize the board and other variables
board = [
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
]
turn_counter = 0
current_player = 'white'

def draw_board():
    # Loop through each square of the board
    for i in range(8):
        for j in range(8):
            # Set the color of the square based on its position
            color = (255, 228, 181) if (i + j) % 2 == 0 else (165, 42, 42)
            # Draw the square on the screen
            pygame.draw.rect(screen, color, (i * square_size, j * square_size, square_size, square_size))

    # Loop through each piece on the board
    for i in range(8):
        for j in range(8):
            piece = board[i][j]
            if piece != ' ':
                # Set the color of the piece based on its color
                if piece.islower():
                    color = (255, 255, 255)
                else:
                    color = (0, 0, 0)
                # Load the image for the piece
                if piece == 'p':
                    image = images['black_pawn']
                elif piece == 'r':
                    image = images['black_rook']
                elif piece == 'n':
                    image = images['black_knight']
                elif piece == 'b':
                    image = images['black_bishop']
                elif piece == 'q':
                    image = images['black_queen']
                elif piece == 'k':
                    image = images['black_king']
                elif piece == 'P':
                    image = images['white_pawn']
                elif piece == 'R':
                    image = images['white_rook']
                elif piece == 'N':
                    image = images['white_knight']
                elif piece == 'B':
                    image = images['white_bishop']
                elif piece == 'Q':
                    image = images['white_queen']
                elif piece == 'K':
                    image = images['white_king']
                # Draw the piece on the screen
                if selected_piece:
                    pygame.draw.rect(screen, (255, 0, 0),
                                     (selected_pos[1] * square_size, selected_pos[0] * square_size, square_size,
                                      square_size),
                                     4)
                screen.blit(image, (j * square_size, i * square_size))

selected_piece = None
selected_pos = None
# Define the rules for each piece type
pawn_rules = ['forward']
rook_rules = ['horizontal', 'vertical']
knight_rules = ['L']
bishop_rules = ['diagonal']
queen_rules = ['horizontal', 'vertical', 'diagonal']
king_rules = ['horizontal', 'vertical', 'diagonal']

# Define the directions for each type of move
directions = {
    'horizontal': [(0, 1), (0, -1)],
    'vertical': [(1, 0), (-1, 0)],
    'diagonal': [(1, 1), (-1, -1), (1, -1), (-1, 1)],
    'L': [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
}



# Define a function to check for obstructions on the board
def check_obstructions(board, start, end, direction):
    row, col = start
    d_row, d_col = direction
    while (row, col) != end:
        row += d_row
        col += d_col
        if board[row][col] != ' ':
            return True
    return False


# Define a function to check for captures
def check_capture(board, start, end, current_player):
    row, col = end
    piece = board[row][col]
    if current_player == 'white' and piece.islower():
        return True
    elif current_player == 'black' and piece.isupper():
        return True
    return False


# Define a function to validate moves
def validate_move(board, start, end, piece, current_player):
    # Get the rules for the piece
    if piece == 'P':
        rules = pawn_rules
    elif piece == 'R':
        rules = rook_rules
    elif piece == 'N':
        rules = knight_rules
    elif piece == 'B':
        rules = bishop_rules
    elif piece == 'Q':
        rules = queen_rules
    elif piece == 'K':
        rules = king_rules
    else:
        return False
    row_diff = end[0] - start[0]
    col_diff = end[1] - start[1]
    if 'horizontal' in rules and row_diff == 0:
        direction = (0, col_diff // abs(col_diff))
        if check_obstructions(board, start, end, direction):
            return False
    elif 'vertical' in rules and col_diff == 0:
        direction = (row_diff // abs(row_diff), 0)
        if check_obstructions(board, start, end, direction):
            return False
    elif 'diagonal' in rules and abs(row_diff) == abs(col_diff):
        direction = (row_diff // abs(row_diff), col_diff // abs(col_diff))
        if check_obstructions(board, start, end, direction):
            return False
    elif 'L' in rules:
        for d in directions['L']:
            if d == (row_diff, col_diff):
                return True
        return False
    else:
        return False

    if check_capture(board, start, end, current_player):
        return True
    return False



for name, image in images.items():
    image = pygame.transform.scale(image, (100, 100))
    images[name] = image
draw_board()
pygame.display.flip()
running = True

running = True
while running:
    draw_board()
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            col = pos[0]
            row = pos[1]
            print(validate_move(board, selected_pos, [row, col], selected_piece, current_player))
            if selected_piece:
                print("FART")
                if validate_move(board, selected_pos, [row, col], selected_piece, current_player):
                    print("NOT FART")
                    if (selected_piece.isupper() and current_player == 'white') or (selected_piece.islower() and current_player == 'black'):
                        board[selected_pos[0]][selected_pos[1]] = ' '
                        selected_pos = [row, col]
                        board[row][col] = selected_piece
                        selected_piece = None
                        turn_counter += 1
                        current_player = 'white' if current_player == 'black' else 'black'
                        draw_board()
                        pygame.display.flip()
                    else:
                        print("NO")
                        selected_piece = None
                        draw_board()
                        pygame.display.flip()
            else:
                pos = pygame.mouse.get_pos()
                col = pos[0] // square_size
                row = pos[1] // square_size
                if board[row][col] != ' ':
                    if (board[row][col].isupper() and current_player == 'white') or (board[row][col].islower() and current_player == 'black'):
                        selected_piece = board[row][col]
                        selected_pos = [row, col]
                        draw_board()
                        pygame.display.flip()

pygame.quit()
