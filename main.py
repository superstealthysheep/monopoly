import csv
from ClassDefinitions import *



char = Character()
other_char = Character()
for i in range(20):
    char.move(char.roll())
#char.pay(1501,other_char)
print("Would you like to buy %s for $%d" % ("hi", 2))


tile1 = Tile(1, "bep", 1, "blue")
print(tile1.name)
tile1.name = "bop"
print(tile1.name)
print(tile1.calculate_rent())
