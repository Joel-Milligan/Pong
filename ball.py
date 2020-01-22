import pygame
import colours
import math

class Ball:
    radius = 10

    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x - self.radius, y - self.radius, self.radius * 2, self.radius * 2)
        self.colour = colours.white
        self.speed = 3
        self.unit_vector = [1, 1]
        self.velocity = [i * self.speed for i in self.unit_vector]

    def draw(self):
        pygame.draw.circle(self.screen, self.colour, (self.rect[0], self.rect[1]), int(self.radius))

    def calculate_velocity(self):
        self.velocity = [i * self.speed for i in self.unit_vector]

    def reflect_x(self):
        self.unit_vector[0] = self.unit_vector[0] * -1
        self.calculate_velocity()

    def reflect_y(self):
        self.unit_vector[1] = self.unit_vector[1] * -1
        self.calculate_velocity()

    def update_position(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]