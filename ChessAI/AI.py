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

# Draw the board
for row in range(8):
    for col in range(8):
        if (row + col) % 2 == 0:
            color = (255, 255, 255)
        else:
            color = (0, 0, 0)
        pygame.draw.rect(screen, color, (col * square_size, row * square_size, square_size, square_size))

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
