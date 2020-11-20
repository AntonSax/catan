

class BoardCoordinate:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0
        self.port = false
        self.corner = false
        self.edge = false
        self.center = false
        self.road = false
        self.settlement = false
        self.city = false
        self.robber = false
        self.probability = 0
        self.resource = None
        self.trade_ratio_to_one = None
