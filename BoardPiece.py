

class BoardPiece:

    def __init__(self, x, y, direction, color, piece=None):
        self.x = x
        self.y = y
        self.direction = direction
        self.piece = piece
        self.color = color
        self.earnings = 2 if piece == "City" else 1 if piece == "Settlement" else 0
        self.resources = None # maybe not used
        self.port = False
        self.port_resource = None
        self.trade_ratio_to_one = None

    def CheckIfPort():

    def SetResource():
