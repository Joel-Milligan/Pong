import pygame
import colours
import math

class Ball:
    radius = 10

    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.colour = colours.white
        self.speed = 5
        self.unit_vector = [1/math.sqrt(2), 1/math.sqrt(2)]
        self.velocity = [i * self.speed for i in self.unit_vector]

    def draw(self):
        pygame.draw.circle(self.screen, self.colour, (int(self.x), int(self.y)), int(self.radius))

    def calculate_velocity(self):
        self.velocity = [i * self.speed for i in self.unit_vector]

    def update_position(self):
        self.x += self.velocity[0]
        self.y += self.velocity[1]