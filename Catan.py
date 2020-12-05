import Board.py
import Player.py

def main():
    players = 0
    expansion = None

    print("Some questions before you start:")
    print("How many players are playing?")
    players = input()
    #print("Are you using a scenario? (Not yet implemented)")
    #b_answer = input()
    print("Which version of the game would you like to use?")
    print("1: Base")
    print("2: Seafarers")
    print("3: Cities and Knights")
    print("4: Traders and Barbarians")
    print("5: Explorers and Pirates")
    expansion = input()

    # Create board and players
    Board = Board(players, expansion)
    Players = [Player() for i in range(players)]
    # Sort the players by age to easily make oldest player go first
    Players.sort(key=lambda x: x.age, reverse=True)

    # Turn counter
    turn = 0
    # Create loops for turns
    while(!gameover):
        turn = turn + 1

        # Phase 1: Resource Production
        sum_of_dice = dice(2) # Roll 2 dice and get their sum.
        Board.GiveResources(sum_of_dice)

        # Phase 2: Trade
        # Phase 3: Build
        # The oldest player goes first during players phase
        for player in Players[]:
            player.my_turn = True
            # Place 2 settlements and roads to start off the game
            if turn == 1 or turn == 2
                settlement_placed = False
                while(!settlement_placed):
                    print(player.name, "is placing a Settlement.")
                    settlement_placed = Board.PlaceBoardPiece(3,3,"N","Settlement", player.color)
                road_placed = False
                while(!road_placed):
                    print(player.name, "is placing a Road.")
                    road_placed = Board.PlaceBoardPiece(3,3,"N","Road", player.color)


def dice(n):
    return sum(random.randint(1, 6) for _ in range(n))


if __name__ == "__main__":
    main()
