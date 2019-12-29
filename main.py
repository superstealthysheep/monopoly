import csv

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


tile1 = Tile(1, "bep", 1, "blue")
print(tile1.name)
tile1.name = "bop"
print(tile1.name)
print(tile1.calculate_rent())
