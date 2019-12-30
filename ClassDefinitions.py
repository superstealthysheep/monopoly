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


class Tile:
    row_array_order = ["location", "name", "tile_type", "monopoly_group", "price", "rent0", "rent1", "rent2", "rent3", "rent4", "rent5", "mortgage_value", "house_cost", "currently_monopolied"] #the order that the properties occur in the spreadsheet row
    def __init__(self, location, name, tile_type, monopoly_group, owner=-1, price=10, rent_level=0, rent0=10, rent1=40, rent2=60, rent3=80, rent4=100, rent5=120, mortgage_value=5, house_cost=10, currently_monopolied=False):
            self.location = location ##BODGE
            self.name = name
            self.tile_type = tile_type
            self.monopoly_group = monopoly_group
            self.owner = owner
            self.price = price
            self.rent_level = rent_level
            self.rent_array = [rent0, rent1, rent2, rent3, rent4, rent5]
            self.mortgage_value = mortgage_value
            self.house_cost = house_cost
            self.currently_monopolied = currently_monopolied

    def calculate_rent(self, last_roll=7):
        if self.tile_type == 1: #if the tile is as normal property:
            if self.currently_monopolied:
                if self.rent_level == 0:
                    return self.rent_array[0] * 2
                else:
                    return rent_array[rent_level]
            else: #if there isn't a monopoly
                return self.rent_array[0]
        elif self.tile_type == 2: #if the tile is a railroad
            return self.rent_array[self.rent_level]
        elif self.tile_type == 3: #if the tile is a utility
            return self.rent_array[self.rent_level] * last_roll


def set_up_game():
    with open("board_state.csv") as f:
        reader = csv.reader(f)
        line_number = 0
        for row in reader:
            if line_number != 0:
                board.append(Tile(*row)) #the * unpacks the row array into all the arguments that Tile needs
            line_number += 1

def run_game():
    board = []
    set_up_game()
    #next, initialize players and set positions
