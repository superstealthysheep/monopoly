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
    #Setup
    board = read_board("board_state.csv")
    p0 = Player()
    p1 = Player()
    p2 = Player()
    players = [p0, p1, p2]
    for i in range(0, 3):
        players.append(Player())

    t1 = Tile(70, "Bep Lane", 1, "Shrek green")

    print("MONOPOLY!")
    print(str(Player.num_players) + " players")

    #Setup over. Game begins below
    for round in range(0, 20):
        print("=" * 50)
        print("ROUND {}".format(round))
        for current_player in players:
            current_player.move(current_player.roll())
            print("{} is at {}".format(current_player.name, board[current_player.location]))
            current_player.turn_dispatcher(board)

run_game()
