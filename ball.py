import pygame
import colours
import math
import random

class Ball:
    radius = 10

    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x - self.radius, y - self.radius, self.radius * 2, self.radius * 2)
        self.colour = colours.white
        self.speed = 5
        self.angle = random.uniform(-math.pi / 4.0, math.pi / 4.0)
        self.calculate_velocity()

    def draw(self):
        pygame.draw.circle(self.screen, self.colour, (self.rect[0], self.rect[1]), int(self.radius))

    def calculate_velocity(self):
        self.velocity = [self.speed * math.cos(self.angle), self.speed * math.sin(self.angle)]
        
    def reflect_x(self):
        if(-math.pi / 2 < self.angle < math.pi / 2):
            self.angle = math.pi - random.uniform(-math.pi / 4.0, math.pi / 4.0)
        else:
            self.angle = random.uniform(-math.pi / 4.0, math.pi / 4.0)

        self.calculate_velocity()

    def reflect_y(self):
        self.angle = -self.angle
        self.calculate_velocity()

    def update_position(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]