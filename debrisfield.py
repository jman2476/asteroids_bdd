import pygame
from debris import Debris


class DebrisField(pygame.sprite.Sprite):

    def __init__(self, x, y, radius):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.position = pygame.Vector2(x,y)
        self.radius = radius
        

    def field(self, size):
        pieces = size * 4
        delta_theta = 360 / pieces
        for i in range(0, pieces):
            # max a bunch of debris pieces
            angle = i * delta_theta
            pos = self.position + pygame.Vector2(1,0).rotate(angle) * self.radius
            piece = Debris(pos[0], pos[1], angle)
