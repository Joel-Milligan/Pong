import pygame
import colours

# Font Initialisation
menu_font = pygame.font.SysFont("arial", 72)

# Create all the text objects
start_game_text = menu_font.render("Start Game", True, colours.white)
quit_text = menu_font.render("Quit", True, colours.white)
