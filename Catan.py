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
        # The oldest player goes first
        for player in Players[]:
            player.my_turn = True
            # Place 2 settlements and roads to start off the game
            if turn == 1 or turn == 2
                piece_placed = False
                while(!piece_placed):
                    print(player.name, "is placing a Settlement.")
                    piece_placed = Board.PlaceBoardPiece(3,3,"N","Settlement")


if __name__ == "__main__":
    main()
