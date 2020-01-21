import pygame
import colours

# Variables
running = True
screen_size = (800, 600)
indent = 50

# Initialisation
pygame.init()
main_display = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()

# Functions
def held_keys(keys):
    pass
def update_screen():
    main_display.fill(colours.black)
    pygame.display.flip()

# Main Game Loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    held_keys(pygame.key.get_pressed())

    update_screen()
    clock.tick(60)

pygame.quit()
quit()
