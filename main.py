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
    p1 = Player()
    p2 = Player()
    p3 = Player()
    players = [p1, p2, p3]
    #next, initialize players and set position
    for turn in range(0, 20):
        for current_player in players:
            print(current_player + "'s turn'")


run_game()
