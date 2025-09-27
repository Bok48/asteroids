# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame

from constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
)
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    game()


def game():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Initialize pygame module
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Pygame groups for sprites
    updatable   = pygame.sprite.Group()
    drawable    = pygame.sprite.Group()
    asteroids   = pygame.sprite.Group()
    shots       = pygame.sprite.Group()
    
    # Method 1 of adding sprites to groups (class variable)
    Player.containers        = (updatable, drawable)
    Asteroid.containers      = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers          = (shots)

    # Initialize player with coordinates to middle of screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()
    
    # Method 2 of adding sprites to groups (adding directly)
    #player.add(updatable)
    #player.add(drawable)
    

    # Initialize clock to measure delta time between frames
    clock = pygame.time.Clock()
    dt = 0

    while True:
        # Events and updates
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Check if player closes window
                return
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.check_collision(player):
                print("Game over!")
                sys.exit()


        # Draw
        screen.fill("black")
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
