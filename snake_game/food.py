import pygame
import random

# Define colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Define food properties
FOOD_SIZE = 20

class Food:
    def __init__(self):
        self.position = (0, 0)
        self.generate()

    def generate(self):
        x = random.randint(0, SCREEN_WIDTH // FOOD_SIZE - 1) * FOOD_SIZE
        y = random.randint(0, SCREEN_HEIGHT // FOOD_SIZE - 1) * FOOD_SIZE
        self.position = (x, y)

    def draw(self, screen):
        pygame.draw.rect(screen, RED, (self.position[0], self.position[1], FOOD_SIZE, FOOD_SIZE))
