import json


class Improvement:
    improvementTypes = {}

    def __init__(self, hexOwner):
        self.owner = hexOwner;
        self.humanReadableName = str(self.__class__);

    def run(self):
        pass

    def loadTypesFromJsonString(self, s):
        dictionary = json.loads(s)
        Improvement.improvementTypes.update(dictionary)
