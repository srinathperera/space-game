from dataclasses import dataclass
from kernel import GameObject, World
from configs import HEIGHT, WIDTH
import pygame



def createSpaceship(player_name: str, x=WIDTH/2, y=HEIGHT/2):
    return SpaceshipObject(player_name, x, y)

class SpaceshipObject(GameObject):
    def __init__(self, name, x,y):
        self.name=name
        self.x=x
        self.y=y
        self.speed=5
        self.direction="up"
        self.health=100
        self.energy=100
        self.weapon="laser"
        self.weapon_cooldown=0
        self.spaceship_img = pygame.image.load('images/ship-small.png').convert_alpha()


    def epochEvent(self, world: World):
        # Get pressed keys
        keys = pygame.key.get_pressed()
        
        # Movement controls - Arrow keys or WASD
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.x += self.speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.y -= self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.y += self.speed
        
        # Keep spaceship within screen bounds
        self.x = max(0, min(self.x, WIDTH))
        self.y = max(0, min(self.y, HEIGHT))

    def getDrawData(self, distroyed: bool):
        spaceship_rect = self.spaceship_img.get_rect(center=(self.x, self.y))
        return self.spaceship_img, spaceship_rect


