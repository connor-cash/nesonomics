from NESCore import *

class WorldRunner(Runner):
    def __init__(self, oldWorld):
        #Clone thw world
        self.world = World(oldWorld);

    def run(self):
        #run layers
        pass

    def getNewWorld(self):
        pass
