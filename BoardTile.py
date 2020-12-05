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
        self.corner_N = None
        self.corner_NE = None
        self.corner_NW = None
        self.corner_S = None
        self.corner_SE = None
        self.corner_SW = None
        self.edge_NE = None
        self.edge_E = None
        self.edge_SE = None
        self.edge_SW = None
        self.edge_W = None
        self.edge_NW = None
        self.resource = None
        self.probability = 0
        self.robber = True if self.resource == "Nothing" else False


    # Checks to see if a road of the same color is on an adjacent edge
    # (or ignored if turn 1 or 2)
    # and verifies that there are no cities on an adjacent corner.
    # If those conditions pass, this function returns true.
    def IsSettlementPlaceable(self, direction, color):
        if direction == "N":
            self.corner_N



    def IsSettlement(self, direction, color):
