import sys
import pygame
from logger import log_state, log_event
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from score import Score
from debris import Debris
from debrisfield import DebrisField
def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Initialization, before game loop
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    print('clock', clock)
    delta_time = 0
    score = Score()
    # Group initialization
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    debris_fields = pygame.sprite.Group()
    # Set groups
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable);
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    DebrisField.containers = (debris_fields, updatable, drawable)
    # Object initialization
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                print('Exiting game', "Score: ", score.total)
                return
        # Start display draw
        screen.fill('black')
        delta_time = clock.tick(60)/1000
        # Update sprites
        for sprite in updatable:
            sprite.update(delta_time)
        # Check Collision
        for aster in asteroids:
            for shot in shots:
                if aster.collides_with(shot):
                    log_event('asteroid_shot')
                    aster.split(score)
                    shot.kill()
                    
            if aster.collides_with(player):
                log_event("player_hit")
                print(f"Game over! Score: {score.total}")
                sys.exit()
        # Draw Sprites
        for sprite in drawable:
            sprite.draw(screen)
        score.draw(screen)
        # Refresh display
        pygame.display.flip()

if __name__ == "__main__":
    main()
