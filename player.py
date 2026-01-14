import random
from circleshape import CircleShape
from shot import Shot
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN_SECONDS
import pygame

class Player(CircleShape):

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.cooldown = 0 
        self.double_shot_cooldown = 0    

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen,'white', self.triangle(), LINE_WIDTH)        

    def rotate(self, delta_time):
        self.rotation += PLAYER_TURN_SPEED * delta_time

    def move(self, delta_time):
        unit_vector = pygame.Vector2(0,1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * delta_time
        self.position += rotated_with_speed_vector

    def update(self, delta_time):
        keys = pygame.key.get_pressed()
        self.cooldown -= delta_time
        self.double_shot_cooldown -= delta_time
        
        if keys[pygame.K_j] or keys[pygame.K_a]:
            # turn left
            self.rotate(delta_time * -1)

        if keys[pygame.K_l] or keys[pygame.K_d]:
            # turn right
            self.rotate(delta_time)

        if keys[pygame.K_i] or keys[pygame.K_w]:
            # move forward
            self.move(delta_time)

        if keys[pygame.K_k] or keys[pygame.K_s]:
            # move backward
            self.move(delta_time * -1)

        if keys[pygame.K_SPACE]:
            # shoot
            self.shoot()

        if keys[pygame.K_g] or keys[pygame.K_h]:
            # double shot
            self.double_shot()
        
        if keys[pygame.K_t] or keys[pygame.K_y]:
            # triple shot
            self.triple_shot()
    def shoot(self):
        if self.cooldown > 0:
            return
        self.cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS 
        shot = Shot(self.position[0], self.position[1])
        shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        
    def double_shot(self):
        if self.double_shot_cooldown > 0:
            return
        self.double_shot_cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS * 2
        angle = random.uniform(10,30)
        shot_one = Shot(self.position[0], self.position[1])
        shot_one.velocity = pygame.Vector2(0,1).rotate(self.rotation + angle) * PLAYER_SHOOT_SPEED
        shot_two = Shot(self.position[0], self.position[1])
        shot_two.velocity = pygame.Vector2(0,1).rotate(self.rotation - angle) * PLAYER_SHOOT_SPEED

    def triple_shot(self):
        if self.cooldown > 0:
            return
        self.cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS * 2.7
        shot_one = Shot(self.position[0], self.position[1])
        shot_one.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        shot_two = Shot(self.position[0], self.position[1])
        shot_two.velocity = pygame.Vector2(0,1).rotate(self.rotation - 5) * PLAYER_SHOOT_SPEED
        shot_three = Shot(self.position[0], self.position[1])
        shot_three.velocity = pygame.Vector2(0,1).rotate(self.rotation + 5) * PLAYER_SHOOT_SPEED
          
