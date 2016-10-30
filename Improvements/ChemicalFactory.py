import Improvement
class ChemicalFactory(Improvement):

    requires=[]
    def __init__(self):
        self.humanReadableNAme="Chemical Factory"

    def __str__(self):
        return self.humanReadableName;
    def run(self):
        pass
        #compute

