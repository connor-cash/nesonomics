class CityModel:
    def __init__(self, world):
        self.world = world
        self.cities = {}

    def add_hex_to_city(self, hid, cid):

        if self.world.diplomacy.is_neutral(hid):
            self.cities[cid] = hid
            return True
        else:
            return False
