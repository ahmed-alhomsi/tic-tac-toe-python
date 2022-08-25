players = ["x", "o"]
possible_game_states = ["win", "draw", "running"]
game_state = "running"
current_player = "x"

grid = [[], ["", " ", " ", " "], ["", " ", " ", " "], ["", " ", " ", " "]]
taken_boxes = []

def check_game_won(player, game_state):
    if grid[1][1] == player and grid[1][2] == player and grid[1][3] == player:
        print("congrats player " + player + "!!! you won won!")
        game_state = "win"
        exit()
    elif grid[2][1] == player and grid[2][2] == player and grid[2][3] == player:
        print("congrats player " + player + "!!! you won won!")
        game_state = "win"
        exit()
    elif grid[3][1] == player and grid[3][2] == player and grid[3][3] == player:
        print("congrats player " + player + "!!! you won won!")
        game_state = "win"
        exit()
    elif grid[1][1] == player and grid[2][2] == player and grid[3][3] == player:
        print("congrats player " + player + "!!! you won won!")
        game_state = "win"
        exit()
    elif grid[1][3] == player and grid[2][2] == player and grid[3][1] == player:
        print("congrats player " + player + "!!! you won won!")
        game_state = "win"
        exit()
    elif grid[1][2] == player and grid[2][2] == player and grid[3][2] == player:
        print("congrats player " + player + "!!! you won won!")
        game_state = "win"
        exit()
    elif grid[1][1] == player and grid[2][1] == player and grid[3][1] == player:
        print("congrats player " + player + "!!! you won won!")
        game_state = "win"
        exit()
    elif grid[1][3] == player and grid[2][3] == player and grid[3][3] == player:
        print("congrats player " + player + "!!! you won won!")
        game_state = "win"
        exit()
    else:
        if len(taken_boxes) == 9:
            print("draw")
            game_state = "draw"
            exit()


while game_state == "running":
    # grid
    row1col1 = grid[1][1]
    row1col2 = grid[1][2]
    row1col3 = grid[1][3]
    row2col1 = grid[2][1]
    row2col2 = grid[2][2]
    row2col3 = grid[2][3]
    row3col1 = grid[3][1]
    row3col2 = grid[3][2]
    row3col3 = grid[3][3]
    print("current player is: ", current_player)
    print("""    
                                                               |--------|--------|--------|
                                                               |        |        |        |
                                                               |    """+row1col1+"""   |   """+row1col2+"""    |     """+row1col3+"""  |
                                                               |        |        |        |
                                                               |--------|--------|--------|
                                                               |        |        |        |
                                                               |   """+row2col1+"""    |  """+row2col2+"""     |  """+row2col3+"""     |
                                                               |        |        |        |
                                                               |--------|--------|--------|
                                                               |        |        |        |
                                                               |   """+row3col1+"""    |  """+row3col2+"""     |  """+row3col3+"""     |
                                                               |        |        |        |
                                                               |--------|--------|--------|
                    """)
    correct_choice = False
    while not correct_choice:
        row_num = int(input("enter row number: "))
        col_num = int(input("enter column number: "))
        taken_boxes.append(current_player)
        if grid[row_num][col_num] != " ":
            print("box already taken, enter a different value! ")
        else:
            correct_choice = True
    grid[row_num][col_num] = current_player
    check_game_won("x", game_state)
    check_game_won("o", game_state)

    if current_player == "x":
        current_player = "o"
    else:
        current_player = "x"
