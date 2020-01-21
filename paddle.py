import pygame
import colours

class Paddle:
    # Constant Variables
    length = 100
    width = 100
    colour = colours.white
    speed = 5
    
    def __init__(self, screen, x, y):
        # Parameter Variables
        self.x = x
        self.y = y
        self.screen = screen

