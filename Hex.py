import Improvements.Improvement as Improvement


class Hex:

    def __init__(self, owner,name):

        #back reference to owner nation
        self.owner = owner
        self.name = name;
        #special improvements
        self.improvementList= []

        #actual land resources
        self.agricultureBase =0;
        self.agricultureImprovement =0;



    def __str__(self):
        str= "=="+self.name+"==" +"\n Improvements:\n" \
             + repr(self.improvementList) + "\nAgriculture: "+repr(self.getTotalAgriculture())
        return str

    def addImprovement(self,imp):
        if not isinstance(imp,Improvement):
            raise TypeError("Expected improvement object");

        if self.hasImprovement(imp):
            return False
        else:
            self.improvementList.append(imp)
    def hasImprovement(self,imp):
        return imp in self.improvementList; #say if the improvement is in the list
    def getTotalAgriculture(self):
        return self.agricultureBase +self.agricultureImprovement


    def computeShortages(self):
        pass

    def computePopulation(self):
        #get shortages
        #badness = unitsShort*deathProbability
        #sort shortages by badness
        #apply most bad shortage
