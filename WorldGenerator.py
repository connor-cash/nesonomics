import random


class WorldGenerator
    def __init__(self, seed):
        random.seed = seed
        random.randint();

    def setUseDrynessGradient(self, yes):
        self.useDrynessGradient = yes;

    def setLakeSize(self, min, max):
        self.lakeSize = [min, max];

    # Water bodies excluding ocean
    def setWaterBodyCount(self, min, max):
        self.waterbodiesToMake = [min, max];

    def setDesertCount(self, min, max):
        self.desertsToMake = [min, max];

    def setForestPercent(self, min, max):
        self.forestPercent = [min, max];

    def setOceanPercent(self, min, max):
        self.forestPercent = [min, max];

    def make(self):

# compute actual tile counts

# init all to lush
# compute ocean
# seed ocean
# ocean expands from top edges
# compute mountains
