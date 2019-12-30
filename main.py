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
    t1 = Tile(70, "Bep Lane", 1, "Shrek green")
    players = [p0, p1, p2]
    print(t1)
    print(board[0])
    print(str(Player.num_players) + " players")
    #next, initialize players and set position
    for round in range(0, 1):
        for current_player in players:
            print(str(current_player) + "'s turn'")
            current_player.move(current_player.roll())
            print("{} is at {}".format(current_player.name, current_player.location))
    print(board[1].tile_type)
    board[1].currently_monopolied = False
    print(board[1].currently_monopolied)
    print(board[1].rent_array)
    print(board[1].calculate_rent())
    for turn in range(0, 1):
        for current_player in players:
            print(str(current_player) + "'s turn'")
            current_player.move(current_player.roll())
            print("{} is at {}".format(current_player.name, board[current_player.location]))
            current_player.turn_dispatcher(board)

run_game()
