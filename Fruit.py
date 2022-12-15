import pygame
import random
from pygame.math import Vector2

screen = pygame.display.set_mode(
    (20 * 40, 20 * 40))
clock = pygame.time.Clock()


class FRUIT:
    def __init__(self):
        self.randomize()

    def draw_fruit(self):
        fruit_rectangle = pygame.Rect(
            self.pos.x * 40, self.pos.y * 40, 40, 40)
        pygame.draw.rect(screen, (126, 166, 114), fruit_rectangle)

    def randomize(self):
        self.x = random.randint(0, 20 - 1)
        self.y = random.randint(0, 20 - 1)
        self.pos = Vector2(self.x, self.y)
