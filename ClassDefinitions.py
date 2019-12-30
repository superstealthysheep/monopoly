import random
DEF_NUM_DICE = 2
DEF_SIZE_DICE = 6
BOARD_SIZE = 40

class MyExcept(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class Character:
    def __init__(self):
        self.location = 0
        self.money = 1500
        self.deeds = []
        self.num_doubles = 0 #Keeps track of num of consecutive doubles
        self.time_in_jail = -1
        self.last_roll = 0

    def roll(self, num_dice=DEF_NUM_DICE, size_dice=DEF_SIZE_DICE):
        sum = 0
        for i in range(num_dice):
            sum += random.randint(1,size_dice)
        self.last_roll = sum
        return sum

    def move(self, roll_value):
        self.location = (self.location + roll_value) % BOARD_SIZE
        print(self.location)

    def pay(self, amount, recipient):
        if self.money < amount:
            print ("notenoughdollabills payfunc")
            raise MyExcept("Not enough dolla dolla payfunc")
        self.money -= amount
        recipient.money += amount

    def purchase_property(self, property):
        if self.money < property.price:
            print ("notenoughdollabills purpropfunc")
            raise MyExcept("Not enough dolla dolla purpropfunc")
        else:
            self.money -= property.price
            property.owner = self

    def turn_dispatcher(self, board):
        #at the end of the function prompt the player for options. use flags to set legal moves
        spot = board[self.location]
        if spot.tile_type != 0:
            if spot.owner == -1:
                print("Would you like to buy %s for $%d? (y/n)" % (spot.name, spot.price))
                char_response = input()
                if char_response != 'n':
                    self.purchase_property(spot)
            else:
                pay(spot.calculate_rent(self.last_roll), spot.owner)
        else:
            print(spot.tile_type, spot.name)


    #The structure of a turn:
    #trade or purchases
    #roll and move
    #buy property
    #or do rent
    #do what it tells you
