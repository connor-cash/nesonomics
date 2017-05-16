from NESModel import NESModel

class ImprovementModel(NESModel):


    def __init__(self):
        super.__init__(self)
        self.improvements={}

    def improvements_on_hex(self,hid):
        return self.improvements[hid]