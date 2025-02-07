from circleshape import CircleShape
import pygame
from constants import COLOR_WHITE, PLAYER_SHOT_SPEED, SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, COLOR_WHITE, self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
