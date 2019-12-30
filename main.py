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
    p0 = Player()
    p1 = Player()
    p2 = Player()
    players = [p0, p1, p2]
    print(str(Player.num_players) + " players")
    #next, initialize players and set position
    for turn in range(0, 20):
        for current_player in players:
            print(current_player + "'s turn'")


run_game()
