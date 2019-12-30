from class_definitions import *

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
    print(board[char.location])
    char.move(char.roll())
    print(board[char.location])
    #char.pay(1501,other_char)

run_game()
