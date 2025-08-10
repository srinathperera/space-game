from dataclasses import dataclass
from kernel import GameObject, World
from configs import HEIGHT, WIDTH
import pygame


@dataclass
class Spaceship:
    name: str
    x: int
    y: int
    speed: int
    direction: str
    health: int
    energy: int
    weapon: str
    weapon_cooldown: int


def createSpaceship(player_name: str):
    return SpaceshipObject(Spaceship(
        name=player_name,
        x=WIDTH // 2,
        y=HEIGHT // 2,
        speed=5,
        direction="up",
        health=100,
        energy=100,
        weapon="laser",
        weapon_cooldown=0
    ))

class SpaceshipObject(GameObject):
    def __init__(self, spaceship: Spaceship):
        self.spaceship = spaceship
        self.spaceship_img = pygame.image.load('images/ship-small.png').convert_alpha()


    def epochEvent(self, world: World):
        # Get pressed keys
        keys = pygame.key.get_pressed()
        
        # Movement controls - Arrow keys or WASD
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.spaceship.x -= self.spaceship.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.spaceship.x += self.spaceship.speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.spaceship.y -= self.spaceship.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.spaceship.y += self.spaceship.speed
        
        # Keep spaceship within screen bounds
        self.spaceship.x = max(0, min(self.spaceship.x, WIDTH))
        self.spaceship.y = max(0, min(self.spaceship.y, HEIGHT))

    def getDrawData(self, distroyed: bool):
        spaceship_rect = self.spaceship_img.get_rect(center=(self.spaceship.x, self.spaceship.y))
        return self.spaceship_img, spaceship_rect


