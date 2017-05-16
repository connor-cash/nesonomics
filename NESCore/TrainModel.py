class TrainModel:

    def __init__(self):
        self.edge_info={}
        self.adjacency={}
        self.auto_increment=0;

    def edge_connecting_hexes(self,src,dest):
        return self.edge_info[(src,dest)]

