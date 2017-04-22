from NEScore import *


class World:
    def __init__(self):
        self.city = CityModel()
        self.climate = ClimateModel()
        self.diplomacy = DiplomacyModel()
        self.improvements = ImprovementsModel()
        self.population = PopulationModel()
        self.resources = ResourceModel()
        self.trade = TradeModel()
