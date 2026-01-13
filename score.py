import pygame
import pygame.freetype as ft
from constants import ASTEROID_MIN_RADIUS
class Score(pygame.sprite.Sprite):
    __base_points = 60
    

    def __init__(self):
        super().__init__()
        self.position = pygame.Vector2(0,0)
        self.total = 0
        self.surface = pygame.Surface((300, 20))
        self.__font = ft.SysFont('Arial', 20, bold=False, italic=False)
        ft.init()
    def update(self, asteroid):
        global __base_points
        multiplier = ASTEROID_MIN_RADIUS/asteroid.radius
        self.total += int(Score.__base_points * multiplier)

    def draw(self, screen):
        self.surface.fill('white')
        self.__font.render_to(self.surface, self.position, f"Score: {self.total}", fgcolor='black')
        screen.blit(self.surface, (10,10))
