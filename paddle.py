import pygame
import colours

class Paddle:
    # Constant Variables
    height = 100
    width = 20
    colour = colours.white
    speed = 5
    
    def __init__(self, screen, x, y):
        # Parameter Variables
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.screen = screen

    def move_down(self):
        if(self.rect[1] + self.rect[3] < self.screen.get_height()):
            self.rect.y += self.speed

    def move_up(self):
        if(self.rect[1] > 0):
            self.rect.y -= self.speed

    def draw(self):
        pygame.draw.rect(self.screen, self.colour, self.rect)
