from dataclasses import dataclass
from kernel import GameObject, World
from configs import HEIGHT, WIDTH
import pygame

def createAstroid(name, x=0.9*WIDTH, y=0.9*HEIGHT, epoch_function=None):
    return AstroidObject(name, x, y, epoch_function)
    

class AstroidObject(GameObject):
    def __init__(self, name, x, y, epoch_function=None):
        self.name = name
        self.x = x
        self.y = y
        self.astroid_img = pygame.image.load('images/astroid.png').convert_alpha()
        # Store the custom epoch function, or use default if none provided
        self.image = self.astroid_img
        self.epoch_function = epoch_function or self._default_epoch_event

    def _default_epoch_event(self, world: World):
        """Default epoch event behavior for the asteroid"""
        self.x = self.x - 1
        self.y = self.y - 1

    def fast_epoch_event(self, world: World):
        self.x = self.x - 10
        self.y = self.y - 10


    def epochEvent(self, world: World):
        # Call the custom epoch function (or default) with the world parameter
        self.epoch_function(world)

    def getDrawData(self, distroyed: bool):
        astroid_rect = self.image.get_rect(center=(self.x, self.y))
        return self.image, astroid_rect


