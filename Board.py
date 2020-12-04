# Using a pointy-edge up style
import BoardTile


class Board:

    board_diameter = 5

    def __init__(self, players):
        self.resource_cards_left = {"Lumber":19,"Grain":19,"Wool":19,"Brick":19,"Ore":19}
                                  #{Forest:4,Fields:4,Pasture:4,Hills:3,Mountains:3,Desert:1}
        self.resource_tiles_left = {"Lumber":4,"Grain":4,"Wool":4,"Brick":3,"Ore":3,"Nothing":1}
        self.probability_tiles_left = {2:1,3:2,4:2,5:2,6:2,8:2,9:2,10:2,11:2,12:1}
        self.array = []
        for i in range(board_diameter):
            col = []
            for j in range (board_diameter):
                # Grab a resource tile and probability tile for board creation.
                resource_tile = random.choice(list(self.resource_tiles_left))
                probability_tile = random.choice(list(self.probability_tiles_left))
                # Append a BoardTile to the board.
                col.append(BoardTile(i, j, resource=resource_tile, probability=probability_tile))                           # BUG: will currently fill null hexes with tiles
                # Remove that resource tile and probability tile from useable pieces.
                resource_tiles_left[resource_tile] = resource_tiles_left[resource_tile] - 1
                probability_tiles_left[probability_tile] = probability_tiles_left[probability_tile] - 1
                if resource_tiles_left[resource_tile] = 0:
                    del resource_tiles_left[resource_tile]
                if probability_tiles_left[probability_tile] = 0:
                    del probability_tiles_left[probability_tile]
            array.append(col)
        print(array)


    # Function to check if a Board Piece exists at Board Tile edge
    def IsBoardPiece(self, x, y, direction):
        if direction == "N":
            if self.array[y][x].N != None:
                return False
        if direction == "NE":
            if self.array[y][x].NE != None:
                return False
        if direction == "NW":
            if self.array[y][x].NW != None:
                return False
        if direction == "S":
            if self.array[y][x].S != None:
                return False
        if direction == "SE":
            if self.array[y][x].SE != None:
                return False
        if direction == "SW":
            if self.array[y][x].SW != None:
                return False

    # Function to set Settlement at corner
    def SetSettlement(self, x, y, direction):
        if direction == "N":
            array[y][x].N == BoardPiece(x, y, direction, "Settlement")
        if direction == "NE":
            array[y][x].NE == BoardPiece(x, y, direction, "Settlement")
        if direction == "NW":
            array[y][x].NW == BoardPiece(x, y, direction, "Settlement")
        if direction == "S":
            array[y][x].S == BoardPiece(x, y, direction, "Settlement")
        if direction == "SE":
            array[y][x].SE == BoardPiece(x, y, direction, "Settlement")
        if direction == "SW":
            array[y][x].SW == BoardPiece(x, y, direction, "Settlement")

    def PlaceBoardPiece(self, x, y, direction, board_piece):
        if !IsBoardPiece(x, y, direction):
            if board_piece == "Settlement":
                self.SetSettlement(x, y, direction)
                return True
            elif board_piece == "City":
                self.SetCity(x, y, direction)
        else:
            print("There is already a piece there.")
            return False
