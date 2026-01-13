import random
import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
 
    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, LINE_WIDTH)


    def update(self, delta_time):
        self.position += self.velocity * delta_time

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event('asteroid_split')
        new_angle = random.uniform(20,50)
        new_v1 = self.velocity.rotate(new_angle) * 1.2
        new_v2 = self.velocity.rotate(-1 * new_angle) * 1.2
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        (pos_x, pos_y) = (self.position[0], self.position[1])
        aster1 = Asteroid(pos_x, pos_y, new_radius)
        aster2 = Asteroid(pos_x, pos_y, new_radius)
        aster1.velocity = new_v1
        aster2.velocity = new_v2
