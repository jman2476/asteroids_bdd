import pygame
from constants import DEBRIS_SPEED, DEBRIS_LENGTH

class Debris(pygame.sprite.Sprite):

    def __init__(self, x, y, angle):
        super.__init___()
        self.position = pygame.Vector2(x,y)
        self.length = DEBRIS_LENGTH

    def __draw__(self, screen):
        pygame.draw.line(screen, 'white', self.position, self.position.rotate(self.angle) + self.length, 2)

    def update(self):
        self.position += pygame.Vector2(1,0).rotate(self.angle) * DEBRIS_SPEED
