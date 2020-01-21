import pygame
import colours

# Variables
running = True
screen_size = (800, 600)

# Initialisation
pygame.init()
main_display = pygame.display.set_mode(screen_size)

# Functions
def update_screen():
    main_display.fill(colours.black)
    pygame.display.flip()

# Main Game Loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    update_screen()

pygame.quit()
quit()
