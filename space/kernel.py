from abc import ABC, abstractmethod
from dataclasses import dataclass

   




def foo():
    """
    A function that can be called from the main game loop.
    This function can be used for game logic, updates, or any processing needed.
    """
    # Add your game logic here
    # For example: update game state, process events, etc.
    pass



class GameObject(ABC):
    """Interface frepresenting game object in the screen """

    @abstractmethod
    def epochEvent(self, world: World):
        pass

    @abstractmethod
    def getDrawData(self, distroyed: bool):
        pass

    def isAlive(self):
        return True

@dataclass
class World:
    game_objects: list[GameObject]
