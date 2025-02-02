import pygame
from constants import *
from player import Player

BLACK = (0, 0, 0)

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()

Player.containers = (updatable, drawable)

def main():
    pygame.init()
    game_clock = pygame.time.Clock()
    dt = 0
    print("Starting asteroids!")
    screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_HEIGHT))
    player_x = SCREEN_WIDTH / 2
    player_y = SCREEN_HEIGHT / 2
    player = Player(player_x, player_y)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        screen.fill(BLACK)
        for entity in drawable:
            entity.draw(screen)
        pygame.display.flip()
        dt = game_clock.tick(60) / 1000

if __name__ == "__main__":
    main()
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

