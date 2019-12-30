from class_definitions import *

def run_game():
def read_board(board_file):
    board = []
    with open(board_file) as f:
        reader = csv.reader(f)
        line_number = 0
        for row in reader:
            if line_number != 0:
                board.append(Tile(*row)) #the * unpacks the row array into all the arguments that Tile needs
            line_number += 1
    return board

def run_game():
    board = read_board("board_state.csv")
    print(board)
    #next, initialize players and set positions

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
