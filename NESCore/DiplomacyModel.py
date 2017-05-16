class DiplomacyModel:
    def __init__(self, world):
        pass

    def owner_of_hex_with_id(self, i):
        pass

    def is_hex_neutral(self, i):
        return self.owner_of_hex_with_id(i) is None
