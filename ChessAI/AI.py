import pygame

window_size = 400
square_size = window_size / 8

pygame.init()

pygame.display.set_caption('Chess Board')
icon = pygame.Surface((1, 1))
icon.set_alpha(0)
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((window_size, window_size))
screen.fill((255, 255, 255))

black_bishop = pygame.image.load('black_bishop.png')
black_king = pygame.image.load('black_king.png')
black_knight = pygame.image.load('black_knight.png')
black_pawn = pygame.image.load('black_pawn.png')
black_queen = pygame.image.load('black_queen.png')
black_rook = pygame.image.load('black_rook.png')
white_bishop = pygame.image.load('white_bishop.png')
white_king = pygame.image.load('white_king.png')
white_knight = pygame.image.load('white_knight.png')
white_pawn = pygame.image.load('white_pawn.png')
white_queen = pygame.image.load('white_queen.png')
white_rook = pygame.image.load('white_rook.png')

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


selected_piece = None
selected_pos = None


def draw_board():
    # Draw the board
    for row in range(8):
        for col in range(8):
            if (row + col) % 2 == 0:
                color = (255, 255, 255)
            else:
                color = (0, 0, 0)
            pygame.draw.rect(screen, color, (col * square_size, row * square_size, square_size, square_size))

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
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if a piece was clicked
            pos = pygame.mouse.get_pos()
            col = pos[0] // square_size
            row = pos[1] // square_size
            if board[row][col] != ' ':
                # Select the piece
                selected_piece = board[row][col]
                selected_pos = (row, col)
            else:
                # Deselect the piece
                selected_piece = None
                selected_pos = None
        elif event.type == pygame.MOUSEBUTTONUP:
            # Check if a piece was released
            pos = pygame.mouse.get_pos()
            col = pos[0] // square_size
            row = pos[1] // square_size
        if selected_piece and selected_pos and (row, col) != selected_pos:
            # Move the piece
            board[selected_pos[0]][selected_pos[1]] = ' '
            board[row][col] = selected_piece
            selected_piece = None
            selected_pos = None
            draw_board()


    # Draw a highlight around the selected piece, if any
    if selected_piece:
        pygame.draw.rect(screen, (255, 0, 0), (selected_pos[1] * square_size, selected_pos[0] * square_size, square_size, square_size), 4)

    # Update the display
    pygame.display.update()

# Quit pygame
pygame.quit()


