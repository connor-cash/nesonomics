class HexManager:

    def __init__(self,world):
        self.world=world

    def promptAssignHex(self):
        hexid= raw_input("Hex id to assign");
        networkid = raw_input("Network id to assing this hex");
        targethex = self.world.getHexByID(hexid)
        targetNetwork = self.world.getNetwork(networkid)
        shouldContinue=False
        if(targetNetwork.hasOwner() && (targethex.getNetwork().getOwner() != targetNetwork.owner()):
            shouldContinue = raw_input("Requested action assigns hex to a different player, proceed?(y/n)")


        if(shouldContinue):
            self.world.assignHexToNetwork(targethex,targetNetwork)
            print "hex assigned"
        else:
            print "action aborted"

    def promptSetHex():
        pass


