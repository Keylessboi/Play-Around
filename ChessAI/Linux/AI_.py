def test(num):
    print("Test " + str(num))
import sys
import os
test(1)
import pygame
test(2)
from PIL import Image
test(3)
#pygame.init()
test(4)
os.environ['SDL_AUDIODRIVER'] = 'alsa'
os.environ["SDL_VIDEODRIVER"] = 'dummy'
test(5)
image_filenames = ['img/black_bishop.png', 'img/black_king.png', 'img/black_knight.png', 'img/black_pawn.png','img/black_queen.png','img/black_rook.png','img/white_bishop.png', 'img/white_king.png', 'img/white_knight.png', 'img/white_pawn.png', 'img/white_queen.png', 'img/white_rook.png']
images = {}
test(6)
window_size = 400
square_size = window_size // 8
test(7)


pygame.display.set_caption('Scuffed Chess ai')
icon = pygame.Surface((1, 1))
icon.set_alpha(0)
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((window_size, window_size))
screen.fill((255, 255, 255))
test(8)
global board
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
test(9)
selected_piece = None
selected_pos = None
selected_pos = []
test(10)
def draw_board():
    for i in range(8):
        for j in range(8):
            color = (255, 255, 255) if (i + j) % 2 == 0 else (0, 0, 0)
            pygame.draw.rect(screen, color, (i * square_size, j * square_size, square_size, square_size))
    for i in range(8):
        for j in range(8):
            piece = board[i][j]
            if piece != ' ':
                if piece.islower():
                    color = (255, 255, 255)
                else:
                    color = (0, 0, 0)
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
                screen.blit(image, (j * square_size, i * square_size))
test(11)
running = True
test(12)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            col = pos[0]
            row = pos[1]
# Inside the mouse click event handling block
        if selected_piece:
            board[selected_pos[0]][selected_pos[1]] = ' '
            selected_pos = [row, col]
            board[row][col] = selected_piece
            selected_piece = None
            draw_board()
        else:
            pos = pygame.mouse.get_pos()
            col = pos[0]
            row = pos[1]
            if board[row][col] != ' ':
                selected_piece = board[row][col]
                selected_pos = [row, col]
                

        if selected_piece:
            # Draw a highlight around the selected piece
            pygame.draw.rect(screen, (255, 0, 0), (selected_pos[1] * square_size, selected_pos[0] * square_size, square_size, square_size), 4)
test(13)
# Quit pygame
pygame.quit()
