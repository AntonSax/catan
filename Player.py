

class Player:

    def __init__(self):
        self.color = None
        self.resources = {Lumber:0,Grain:0,Wool:0,Brick:0,Ore:0}
        self.settlements = 0    # max=5
        self.cities = 0         # max=4
        self.roads = 0          # max=15
        self.development_cards = 0
        self.knight_cards = 0
        self.has_longest_road = false
        self.has_largest_army = false
        self.age = 0
        self.victory_points = 0 # cities & settlements count towards victory points
