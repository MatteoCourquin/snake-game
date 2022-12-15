import pygame
from pygame.math import Vector2

screen = pygame.display.set_mode(
    (20 * 40, 20 * 40))
clock = pygame.time.Clock()


class SNAKE:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(1, 0)
        self.new_block = False

    def draw_snake(self):
        for block in self.body:
            x_pos = block.x * 40
            y_pos = block.y * 40
            block_rectangle = pygame.Rect(x_pos, y_pos, 40, 40)
            pygame.draw.rect(screen, (183, 191, 122), block_rectangle)

    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True
