from dataclasses import dataclass
from kernel import GameObject, World
from configs import HEIGHT, WIDTH
import pygame


@dataclass
class Astroid:
    name: str
    x: int
    y: int


def createAstroid(player_name: str):
    return AstroidObject(Astroid(
        name=player_name,
        x=WIDTH ,
        y=HEIGHT,
    ))

class AstroidObject(GameObject):
    def __init__(self, astroid: Astroid):
        self.astroid = astroid
        self.astroid_img = pygame.image.load('images/astroid.png').convert_alpha()


    def epochEvent(self, world: World):
       self.astroid.x =  self.astroid.x - 1
       self.astroid.y =  self.astroid.y - 1

    def getDrawData(self, distroyed: bool):
        astroid_rect = self.astroid_img.get_rect(center=(self.astroid.x, self.astroid.y))
        return self.astroid_img, astroid_rect


