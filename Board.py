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


    # Give resources to each person for the first phase of each turn
    def GiveResources(sum_of_dice):
        x = -1
        y = -1
        resource = None

        # Check which tiles are giving away resources
        # Loop through array of arrays (list of lists)
        for column in array:
            for tile in column:
                # Make sure tile is not a unused/null tile
                if tile != None
                    # Assign values if the probability matches the dice roll
                    if tile.probability == sum_of_dice:
                        x = tile.x
                        y = tile.y
                        resource = tile.resource
                        # Don't give any resources from this tile if the tile has a robber on it
                        if tile.robber == True:
                            print("Oh no! The tile at (", x, ",", y, ") which gives", resource, "has a robber on it!")
                            continue
                        # Otherwise find which players have a settlement or city on a corner of this tile.
                        player_list = []
                        player_list = FindSettlementsOnTile(tile)

    def FindSettlementsOnTile(board_tile):
        if board_tile.N != None:
            


    # Function to check if a Board Piece exists at Board Tile edge
    def IsBoardPiece(self, x, y, direction):
        if direction == "N":
            if self.array[y][x].corner_N != None:
                return False
        if direction == "NE":
            if self.array[y][x].corner_NE != None:
                return False
        if direction == "NW":
            if self.array[y][x].corner_NW != None:
                return False
        if direction == "S":
            if self.array[y][x].corner_S != None:
                return False
        if direction == "SE":
            if self.array[y][x].corner_SE != None:
                return False
        if direction == "SW":
            if self.array[y][x].corner_SW != None:
                return False


    # Function to set Settlement at corner
    # First line sets the piece at the current location
    # 2nd and 3rd line set the piece for the adjacent hexes,
    # since this is weird setup for the game board, and needs to be redundant.
    def SetSettlement(self, x, y, direction, color):
        if direction == "N":
            array[y][x].corner_N == BoardPiece(x, y, direction, color, "Settlement")
            array[y-1][x].corner_SE == BoardPiece(x, y, direction, color, "Settlement")
            array[y-1][x+1].corner_SW == BoardPiece(x, y, direction, color, "Settlement")
        if direction == "NE":
            array[y][x].corner_NE == BoardPiece(x, y, direction, color, "Settlement")
            array[y-1][x+1].corner_S == BoardPiece(x, y, direction, color, "Settlement")
            array[y][x+1].corner_NW == BoardPiece(x, y, direction, color, "Settlement")
        if direction == "NW":
            array[y][x].corner_NW == BoardPiece(x, y, direction, color, "Settlement")
            array[y][x-1].corner_NE == BoardPiece(x, y, direction, color, "Settlement")
            array[y-1][x].corner_S == BoardPiece(x, y, direction, color, "Settlement")
        if direction == "S":
            array[y][x].corner_S == BoardPiece(x, y, direction, color, "Settlement")
            array[y+1][x].corner_NW == BoardPiece(x, y, direction, color, "Settlement")
            array[y+1][x-1].corner_NE == BoardPiece(x, y, direction, color, "Settlement")
        if direction == "SE":
            array[y][x].corner_SE == BoardPiece(x, y, direction, color, "Settlement")
            array[y][x+1].corner_SW == BoardPiece(x, y, direction, color, "Settlement")
            array[y+1][x].corner_N == BoardPiece(x, y, direction, color, "Settlement")
        if direction == "SW":
            array[y][x].corner_SW == BoardPiece(x, y, direction, color, "Settlement")
            array[y+1][x-1].corner_N == BoardPiece(x, y, direction, color, "Settlement")
            array[y][x-1].corner_SE == BoardPiece(x, y, direction, color, "Settlement")


    # Function to set Road at edge
    # First line sets the piece at the current location
    # 2nd line sets the piece for the adjacent hex,
    # since this is weird setup for the game board.
    def SetRoad(self, x, y, direction, color):
        if direction == "NE":
            array[y][x].edge_NE == BoardPiece(x, y, direction, color, "Road")
            array[y-1][x+1].edge_SW == BoardPiece(x, y, direction, color, "Road")
        if direction == "E":
            array[y][x].edge_E == BoardPiece(x, y, direction, color, "Road")
            array[y][x+1].edge_W == BoardPiece(x, y, direction, color, "Road")
        if direction == "SE":
            array[y][x].edge_SE == BoardPiece(x, y, direction, color, "Road")
            array[y+1][x].edge_NW == BoardPiece(x, y, direction, color, "Road")
        if direction == "SW":
            array[y][x].edge_SW == BoardPiece(x, y, direction, color, "Road")
            array[y+1][x-1].edge_NE == BoardPiece(x, y, direction, color, "Road")
        if direction == "W":
            array[y][x].edge_W == BoardPiece(x, y, direction, color, "Road")
            array[y][x-1].edge_E == BoardPiece(x, y, direction, color, "Road")
        if direction == "NW":
            array[y][x].edge_NW == BoardPiece(x, y, direction, color, "Road")
            array[y-1][x].edge_SE == BoardPiece(x, y, direction, color, "Road")


    def PlaceBoardPiece(self, x, y, direction, board_piece, color):
        if !IsBoardPiece(x, y, direction):
            if board_piece == "Settlement":
                if array[y][x].IsSettlementPlaceable(direction, color):
                    self.SetSettlement(x, y, direction, color)
                return True # why do I return true here
            elif board_piece == "City":
                if array[y][x].IsSettlement(direction, color)
                self.SetCity(x, y, direction, color)
            elif board_piece == "Road":

                self.SetRoad(x, y, direction, color)
        else:
            print("There is already a piece there.")
            return False
