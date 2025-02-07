from circleshape import CircleShape
import pygame
from constants import COLOR_WHITE, ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, COLOR_WHITE, self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        chunk_1_velocity = self.velocity.rotate(random_angle)
        chunk_2_velocity = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_chunk_1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_chunk_2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_chunk_1.velocity = chunk_1_velocity * 1.2
        asteroid_chunk_2.velocity = chunk_2_velocity * 1.2