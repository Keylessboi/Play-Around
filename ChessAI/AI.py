import pygame

# Set the window size and the square size
window_size = 400
square_size = window_size / 8

# Initialize pygame
pygame.init()

# Set the window title and icon
pygame.display.set_caption('Chess Board')
icon = pygame.Surface((1, 1))
icon.set_alpha(0)
pygame.display.set_icon(icon)

# Create the window and set the background color
screen = pygame.display.set_mode((window_size, window_size))
screen.fill((255, 255, 255))

# Load the images of the chess pieces
black_bishop = pygame.image.load('img/black_bishop.png')
black_king = pygame.image.load('img/black_king.png')
black_knight = pygame.image.load('img/black_knight.png')
black_pawn = pygame.image.load('img/black_pawn.png')
black_queen = pygame.image.load('img/black_queen.png')
black_rook = pygame.image.load('img/black_rook.png')
white_bishop = pygame.image.load('img/white_bishop.png')
white_king = pygame.image.load('img/white_king.png')
white_knight = pygame.image.load('img/white_knight.png')
white_pawn = pygame.image.load('img/white_pawn.png')
white_queen = pygame.image.load('img/white_queen.png')
white_rook = pygame.image.load('img/white_rook.png')

# Set up the board and pieces
board = [
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
]

# Draw the board
for row in range(8):
    for col in range(8):
        if (row + col) % 2 == 0:
            color = (255, 255, 255)
        else:
            color = (0, 0, 0)
        pygame.draw.rect(screen, color, (col * square_size, row * square_size, square_size, square_size))

# Draw the pieces
# Draw the pieces
for row in range(8):
    for col in range(8):
        piece = board[row][col]
        if piece == 'r':
            screen.blit(black_rook, (col * square_size, row * square_size))
        elif piece == 'n':
            screen.blit(black_knight, (col * square_size, row * square_size))
        elif piece == 'b':
            screen.blit(black_bishop, (col * square_size, row * square_size))
        elif piece == 'q':
            screen.blit(black_queen, (col * square_size, row * square_size))
        elif piece == 'k':
            screen.blit(black_king, (col * square_size, row * square_size))
        elif piece == 'p':
            screen.blit(black_pawn, (col * square_size, row * square_size))
        elif piece == 'R':
            screen.blit(white_rook, (col * square_size, row * square_size))
        elif piece == 'N':
            screen.blit(white_knight, (col * square_size, row * square_size))
        elif piece == 'B':
            screen.blit(white_bishop, (col * square_size, row * square_size))
        elif piece == 'Q':
            screen.blit(white_queen, (col * square_size, row * square_size))
        elif piece == 'K':
            screen.blit(white_king, (col * square_size, row * square_size))
        elif piece == 'P':
            screen.blit(white_pawn, (col * square_size, row * square_size))

# Update the display
pygame.display.update()

# Run the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit pygame
pygame.quit()
