from circleshape import CircleShape
import pygame
from constants import COLOR_WHITE, PLAYER_SHOT_SPEED, SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y, rotation):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = pygame.Vector2(0, 1) * PLAYER_SHOT_SPEED
        self.rotation = rotation

    def draw(self, screen):
        pygame.draw.circle(screen, COLOR_WHITE, self.position, self.radius)

    def update(self, dt):
        # self.velocity.rotate(self.rotation)
        # self.position += self.velocity * dt
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SHOT_SPEED * dt
