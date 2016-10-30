class World:
    def __init__(self, width, height):
        self.serialVersion=1;
        self.nations = []
        self.hexes = list(width*height);
        self.width=width

    def indexToRectCoord(self,i):
        y = i/self.width;
        x = i%self.width;
        return [x,y]

    def rectCoordToID(self,x,y):
        return y*self.width +x

    def adjacent(self,x,y):
        #TODO handle wrapping
        l = [ self.rectCoordToID(x-1,y),self.rectCoordToID(x-1,y) ]

        l.append(self.rectCoordToID(x,y+2))
        l.append(self.rectCoordToID(x, y - 2))

        l.append(self.rectCoordToID(x+1, y +1))
        l.append(self.rectCoordToID(x - 1, y + 1))
        l.append(self.rectCoordToID(x + 1, y - 1))
        l.append(self.rectCoordToID(x - 1, y - 1))

        return l

    def step(self):
        pass

    def setHex(self,x,y, hex):
        pass

    def addNation(self, nation):
        pass

    def assignHexToNetwork(self, hex, network):
        pass

    def joinNetworks(self):


    def assignNationToPlayer(self, nation):
        pass
    def getPlayers(self):
        return self.players

    def canonicalRepresentation(self)
        dict={};
        dict["version"]=self.serialVersion;
        a=[];
        for n in self.nations
            a.append(n.canonicalRepresentation(self.hexes))

        dict["nations"]=a

        return dict