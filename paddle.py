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

    def move_down(self):
        if(self.y + self.length < self.screen.get_height()):
            self.y += self.speed

    def move_up(self):
        if(self.y > 0):
            self.y -= self.speed

