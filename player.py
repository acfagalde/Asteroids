import pygame #type: ignore
from CircleShape import *
from constants import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.SHOOT_COOLDOWN = 0.0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, (255,255,255), self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED*dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.SHOOT_COOLDOWN = max(0.0, self.SHOOT_COOLDOWN - dt)

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE] and self.SHOOT_COOLDOWN <= 0.0:
            self.shoot(self.position)
            self.SHOOT_COOLDOWN = 0.3

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED *dt

    def shoot(self, position):
        new_shot = Shot(self.position)
        new_shot.velocity = pygame.Vector2(0,1).rotate(self.rotation)
        new_shot.velocity *= PLAYER_SHOT_SPEED




class Shot(CircleShape):
    def __init__(self, position):
        x, y = position.x, position.y
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, SHOT_RADIUS)

    def update(self, dt):
        self.position += self.velocity*dt 