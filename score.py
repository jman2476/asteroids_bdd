import pygame
import pygame.freetype as ft
from constants import ASTEROID_MIN_RADIUS
class Score(pygame.sprite.Sprite):
    __base_points = 60
    

    def __init__(self):
        super().__init__()
        self.position = pygame.Vector2(0,0)
        self.total = 0
        self.surface = pygame.Surface((60, 20))
        self.surface.fill('white')
        self.__font = ft.SysFont('Arial', 12, bold=False, italic=False)
        ft.init()
    def update(self, asteroid):
        global __base_points
        multiplier = asteroid.radius/ASTEROID_MIN_RADIUS

        self.total += Score.__base_points * multiplier
        print("New score:", self.total)
    def draw(self, screen):
        self.__font.render_to(self.surface, self.position, f"Score: {self.total}", fgcolor='black')
        
