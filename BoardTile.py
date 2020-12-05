# Using a pointy-edge up style
import BoardPiece

class BoardTile:

    def __init__(self, i, j, resource, probability):
        # Place on the board
        self.x = j
        self.y = i
        self.z = None # maybe not used
        # Corners of the hexes
        # Will be replaced with the BoardPiece object
        # Make these into a dictionary
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
        print("TODO")

    # Returns a dictionary of players who get this resource
    # the key is the player
    # the value is how much of this resource they get
    def FindSettlementsOnTile():
        player_color_dict = dict()
        if corner_N != None:
            if corner_N.piece == "Settlement":
                # Add 1 to value, don't set value to 1,
                # as player may have multiple settlements on this tile
                player_color_dict[corner_N.color] = player_color_dict[corner_N.color] + 1
            elif corner_N.piece == "City":
                # Add 2 to value, don't set value to 2,
                # as player may have multiple settlements on this tile
                player_color_dict[corner_N.color] = player_color_dict[corner_N.color] + 2
        if corner_NE != None:
            if corner_NE.piece == "Settlement":
                player_color_dict[corner_NE.color] = player_color_dict[corner_NE.color] + 1
            elif corner_NE.piece == "City":
                player_color_dict[corner_NE.color] = player_color_dict[corner_NE.color] + 2
        if corner_NW != None:
            if corner_NW.piece == "Settlement":
                player_color_dict[corner_NW.color] = player_color_dict[corner_NW.color] + 1
            elif corner_NW.piece == "City":
                player_color_dict[corner_NW.color] = player_color_dict[corner_NW.color] + 2
        if corner_S != None:
            if corner_S.piece == "Settlement":
                player_color_dict[corner_S.color] = player_color_dict[corner_S.color] + 1
            elif corner_S.piece == "City":
                player_color_dict[corner_S.color] = player_color_dict[corner_S.color] + 2
        if corner_SE != None:
            if corner_SE.piece == "Settlement":
                player_color_dict[corner_SE.color] = player_color_dict[corner_SE.color] + 1
            elif corner_SE.piece == "City":
                player_color_dict[corner_SE.color] = player_color_dict[corner_SE.color] + 2
        if corner_SW != None:
            if corner_SW.piece == "Settlement":
                player_color_dict[corner_SW.color] = player_color_dict[corner_SW.color] + 1
            elif corner_SW.piece == "City":
                player_color_dict[corner_SW.color] = player_color_dict[corner_SW.color] + 2
        return player_color_dict
