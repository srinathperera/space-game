from kernel import World
from astroid import AstroidObject

class NithuAstroidObject(AstroidObject):
    def epochEvent(self, world: World):
        self.x = self.x - 1
        self.y = self.y - 1

def updateNithuObjects(world: World):
    world.game_objects.append(NithuAstroidObject("NithuAstroid", 100, 100))
    return world