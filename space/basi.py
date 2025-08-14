from kernel import World
from astroid import AstroidObject


class BAstroidObject(AstroidObject):
    def epochEvent(self, world: World):
        self.x = self.x - 10
        self.y = self.y - 10


def updateBasiObjects(world: World):
    world.game_objects.append(BAstroidObject("Bastroid", 100, 100))
    return world