# Using a pointy-edge up style
import BoardPiece

class BoardTile:

    def __init__(self, i, j, resource, probability):
        # Place on the board
        self.x = j
        self.y = i
        self.z = None # maybe not used
        # Corner of the hexes
        # Will be replaced with the BoardPiece object
        self.N = None
        self.NE = None
        self.NW = None
        self.S = None
        self.SE = None
        self.SW = None
        self.resource = None
        self.probability = 0
        self.robber = True if self.resource == "Nothing" else False
