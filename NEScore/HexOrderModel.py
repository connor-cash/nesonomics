from NESModel import NESModel
import random


class HexOrderModel(NESModel):
    def __init__(self, world):
        self.world = world

    def random_order(self):
        return random.shuffle(range(0, self.world.hexCount))
