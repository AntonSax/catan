import BoardCoordinate


class Board:

    def __init__(self, players):
        self.resources_left = {Lumber:19,Grain:19,Wool:19,Brick:19,Ore:19}
        self.players = players
