import random

class Player:

    def __init__(self, color="red", name="first_name", age=random.randint(1,100)):
        self.name = name
        self.age = age
        self.color = color
        self.my_turn = False
        self.resources = {"Lumber":0,"Grain":0,"Wool":0,"Brick":0,"Ore":0}
        self.maritime_trade_ratio = {"Lumber":4,"Grain":4,"Wool":4,"Brick":4,"Ore":4}
        self.settlements = 0    # max=5
        self.cities = 0         # max=4
        self.roads = 0          # max=15
        self.development_cards = 0
        self.knight_cards = 0
        self.has_longest_road = False
        self.has_largest_army = False
        self.victory_points = 0 # cities & settlements count towards victory points


    def TradePhase(self):
        still_trading = True
        maritime_trading_possible = False

        while (still_trading):
            # Domestic
            print("Domestic Trade? (Y/N)")
            domestic_confirmation = input()
            if domestic_confirmation == "Y":
                DomesticTrade()

            # Maritime
            print("Maritime Trade? (Y/N)")
            maritime_confirmation = input()
            if maritime_confirmation == "Y":
                MaritimeTrade()

            print("Are you finished trading? Y/N")
            input_trading = input()
            if input_trading == "Y":
                still_trading = True
            else:
                still_trading = False

    # Domestic Trade is trading with the other players
    def DomesticTrade(self):
        print("What resource are you seeking?")
        for key, value in self.resources:
            print(key, ": ", "You have ", value, " currently.")
        resource_wanted = input()
        resource_wanted = resource_wanted.title()

        # Send this to the non-current players
        print("Current player is seeking a ", resource_wanted)
        print("Make an offer? (Y/N)")
        making_offer = input().title()
        if making_offer == "Y":
            print("Enter which resource you want and how much.")
            offer = input()
            offer_resource = filter(str.isalpha(), offer)
            offer_amount = filter(str.isdigit(), offer)

        # Send to all players
        if offer_amount > 0:
            # Realistically needs to print all player offers
            print("Non-current player will take ", offer_amount, " ", offer_resource, "s for the ", resource_wanted)

        # Asking current player again
        print("Take offer? (Y/N)")
        complete_deal = input()
        if complete_deal == "Y":
            print("Deal completed")
            # swap cards


    # Maritime Trade is trading with nobody/the bank.
    def MaritimeTrade(self):
        print("Listing trade for each available resource...")
        # List the best available trade for each card.
        for key, value in self.maritime_trade_ratio:
            print(self.maritime_trade_ratio.keys().index(key)+1, ". ", key, ":", value, "to 1 trade")
        print("Select resource you want (Input resource name): ")
        resource_wanted = input()
        resource_wanted = resource_wanted.title()

        print("Select what resource you will give up for it (Input resource name): ")
        # List what cards you can trade for, and how much you have of that card.
        for key, value in self.resources:
            print(key, ": ", "You have ", value, " currently.")
        resource_given = input()
        resource_given = resource_given.title()

        # If the players has enough cards to give away for their chosen resource
        if self.resources[resource_given] >= self.maritime_trade_ratio[resource_given]:
            print("You are trading ", self.maritime_trade_ratio[resource_given], " ", resource_given, " for 1 ", resource_wanted, ".")
            print("Is that OK? (Y/N)")
            trade_confirmation = input()
            if trade_confirmation == "Y":
                # Finish the trade
                self.resources[resource_wanted] = self.resources[resource_wanted] + 1
                self.resources[resource_given] = self.resources[resource_given] - self.maritime_trade_ratio[resource_given]
            elif trade_confirmation == "N":
                # Cancel the trade
                print("You canceled the trade.")
        # The player does not have enough cards
        else:
            print("You did not have enough ", resource_given, ".")
