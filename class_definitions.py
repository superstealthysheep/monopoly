import csv
import random
DEF_NUM_DICE = 2
DEF_SIZE_DICE = 6
BOARD_SIZE = 40
GO_PASS_MONEY = 200

class MyExcept(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class Chance: #type 0 means pay, type 1 means jump, type 2 means move
    def __init__(self, type, value, source, target):
        if type == 0:
            #payment card: pay value from Player source to Player target
            if type(target) != list: #convert to a one-element list to make code easier
                target = [target]
            if value < 0:
                value = -value
                for item in targets:
                    pay(value, item, source)
            else:
                for item in targets:
                    pay(value, source, item)

        if type == 1:
            #jump card: move Player source from current tile to Tile target. If tile is owned, the rent is multiplied by Int value
                move_val = target.location -  source.location
                if target.location < source.location:
                    move_val += BOARD_SIZE
                source.move(move_val)

        if type == 2:
            #move card: move Player source Int value.
            source.move(value)

class Player:
    num_players = 0

    def __init__(self, name="###EMPTY###", location=0, money=1500, deeds=[], num_doubles=0, time_in_jail=0, last_roll=0):
        self.name = name
        if name == "###EMPTY###": #If a name isn't entered, default to "Player [Player Number]" (this feels like a BODGE though)
            self.name = "Player {}".format(Player.num_players)
        self.location = location
        self.money = money
        self.deeds = deeds
        self.num_doubles = num_doubles #Keeps track of num of consecutive doubles
        self.time_in_jail = time_in_jail
        self.last_roll = last_roll

        Player.num_players += 1


    def __repr__(self):
        return ("Player object with " +
                "name: {}, " +
                "location: {}, " +
                "money: {}, " +
                "deeds: {}, " +
                "num_doubles: {}, " +
                "time_in_jail: {}, " +
                "last_roll: {}").format(self.name, self.location, self.money, self.deeds, self.num_doubles, self.time_in_jail, self.last_roll)

    def roll(self, num_dice=DEF_NUM_DICE, size_dice=DEF_SIZE_DICE):
        sum = 0
        for i in range(num_dice):
            sum += random.randint(1,size_dice)
        self.last_roll = sum
        return sum

    def move(self, roll_value):
        new_location = self.location + roll_value #but this could be over the size of the board
        go_passes = max(new_location // BOARD_SIZE, 0)
        self.money += GO_PASS_MONEY * go_passes
        self.location = new_location % BOARD_SIZE
        print(self.location)

    def purchase_property(self, property):
        if self.money < property.price:
            print ("notenoughdollabills purpropfunc")
            raise MyExcept("Not enough dolla dolla purpropfunc")
        else:
            self.money -= property.price
            property.owner = self
            self.deeds.append(property)

    def turn_dispatcher(self, board):
        #at the end of the function prompt the player for options. use flags to set legal moves
        spot = board[self.location]
        if spot.tile_type != 0:
            if spot.owner == -1:
                print("Would you like to buy %s for $%d? (y/n)" % (spot.name, spot.price))
                player_response = input()
                if player_response != 'n':
                    self.purchase_property(spot)
            else:
                pay(spot.calculate_rent(self.last_roll), spot.owner)
        else:
            print(spot.tile_type, spot.name)

def pay(amount, sender, recipient): #function for players but outside class
    if sender.money < amount:
        print ("notenoughdollabills payfunc")
        raise MyExcept("Not enough dolla dolla payfunc")
    sender.money -= amount
    recipient.money += amount

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

    def __repr__(self):
        return ("Tile object with " +
                "location: {}, " +
                "name: {}, " +
                "tile_type: {}, " +
                "monopoly_group: {}, " +
                "owner: {}, " +
                "price: {}, " +
                "rent_level: {}, " +
                "rent0: {}, " +
                "rent1: {}, " +
                "rent2: {}, " +
                "rent3: {}, " +
                "rent4: {}, " +
                "rent5: {}, " +
                "mortgage_value: {}, " +
                "house_cost: {}, " +
                "currently_monopolied: {}").format(self.location, self.name, self.tile_type, self.monopoly_group, self.owner, self.price, self.rent_level, self.rent_array[0], self.rent_array[1], self.rent_array[2], self.rent_array[3], self.rent_array[4], self.rent_array[5], self.mortgage_value, self.house_cost, self.currently_monopolied)

    def __str__(self):
        return "{} (#{})".format(self.name, self.location)

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
