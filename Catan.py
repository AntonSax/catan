import Board.py

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

    Board = Board(players, expansion) 

if __name__ == "__main__":
    main()
