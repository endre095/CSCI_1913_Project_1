"""
Author: Andrew Endres

Due:  Fri, Feb 27, 2026 5pm

Kōnane
Parts of this section are from several National Park Service resources. One of which is liked to in the “More Info” section.

Kōnane is a two-player strategy board game from Hawaii. Played on a rectangular board, it begins with black and white counters 
filling the board in an alternating pattern. Before contact with Europeans the game was played using small pieces of white coral 
and black lava rock. Using a large carved that doubled as a board and table. Pu’uhonua o Hōnaunau National Historical Park is 
where one of our instructors first encountered this game.

Link to instructions: https://canvas.umn.edu/courses/541118
"""

import math
import random

'''These two helper functions create list types 1 and 2, which just means they
either start with 1 or 2 as the board switches between these as you go down
the rows.'''
def generate_board_helper_1(int):
    list = []
    count = 1
    for i in range(int):
        if count % 2 == 0:
            list.append(2)
        else:
            list.append(1)
        count += 1
    return list

def generate_board_helper_2(int):
    list = []
    count = 1
    for i in range(int):
        if count % 2 == 0:
            list.append(1)
        else:
            list.append(2)
        count += 1
    return list

'''This function creates the list of lists using the two helper functions above,
this function calls those two functions in accordance with the size of the list
as different sized nested lists would have different formats of 1's and 2's.'''
def generate_board(size):
    nested_list = []
    if size % 2 == 0:
        for i in range(size // 2):
            nested_list.append(generate_board_helper_1(size))
            nested_list.append(generate_board_helper_2(size))
        return nested_list
    else:
        nested_list.append(generate_board_helper_1(size))
        for i in range(size // 2):
            nested_list.append(generate_board_helper_2(size))
            nested_list.append(generate_board_helper_1(size))
    return nested_list

"""empty_cell = ["+-+","| |","+-+"]
    white_cell = ["+-+","|\u25CB|","+-+"]
    black_cell = ["+-+","|\u25CF|","+-+"]"""

#This function uses the boards list values to print out the 
# current state of the board to the terminal/screen
def get_board_as_string(board):
    size = len(board[0])
    size2 = len(board)
    if size != size2:
        return False
    board_as_string = ""
    border_string = " "
    print(end="  ")
    for i in range(0,size, 1): #creates the top numbering
        if i > 9:
            print(i%10, end=" ")
        else:
            print(i, end=" ")
    print()
    for i in range(size): #creates the top/bottom border of the cells
        border_string += "+-"
        if i == size-1:
            border_string += "+"
    for j in range(size): #creates the colored cells/blanks/pipes
        for i in range(size):
            board_as_string += "|"
            if board[j][i] == 0:
                board_as_string += " "
            elif board[j][i] == 1:
                board_as_string += "\u25CF"
            elif board[j][i] == 2:
                board_as_string += "\u25CB"
        board_as_string += "|"
        print(border_string)
        if j > 9:
            print(j%10, end="") #creates the side numbering
        else:
            print(j, end="")
        print(board_as_string)
        board_as_string = ""
    print(border_string)
    return board_as_string

#This function allows the board to be prepped for play by removing two 
#pieces if the moves are deemed valid
def prep_board_human(board):
    get_board_as_string(board)
    size = len(board[0])
    print("enter the two rows and two colums you wish to remove(R1 C1 R2 C2)")
    get_input = True
    while get_input == True:
        row1_to_remove = int(input())
        col1_to_remove = int(input())
        row2_to_remove = int(input())
        col2_to_remove = int(input())
        if board[row1_to_remove][col1_to_remove] == board[row2_to_remove][col2_to_remove]:
            print("Invalid input, need different colors.")
        elif row1_to_remove ==  0 or row2_to_remove == 0:
            print("Invalid input, need a different row1.")
        elif row1_to_remove == size or row2_to_remove == size: #tests all cases to make sure its a valid move
            print("Invalid input, need a different row1.")
        elif col1_to_remove == 0 or col2_to_remove == 0:
            print("Invalid input, need a different column.")
        elif col1_to_remove == size or col2_to_remove == size:
            print("Invalid input, need a different column.")
        else:
            board[row1_to_remove][col1_to_remove] = 0 #removes elements
            board[row2_to_remove][col2_to_remove] = 0
            return


"""
Mandatory Capture: A player must make a capture if one is available;
 if no jumps are possible, the player loses.

Orthogonal Jumps: Pieces can only jump over opponents horizontally 
or vertically, never diagonally.

Landing Spot: The piece must land in an immediately adjacent empty 
space directly behind the opponent's piece.

Directionality: A single turn can consist of one or more jumps using
 the same piece, but all jumps must continue in the same straight line.
 
"""

def is_valid_move(board, move): #move is a nested tuple ((start),(end))
    color = board[move[0][0]][move[0][1]]
    size = len(board)
    size2 = len(board[0])
    if size != size2:
        return False
    r1,c1 = move[0][0],move[0][1]
    r2,c2 = move[1][0],move[1][1]
    if size != size2:
        return False
    if len(move) > 2: #makes sure the input into the function was valid
        return False
    if board[r1][c1] == 0: #checks if starting square has a piece
        return False
    if r1 != r2 and c1 != c2: #checks if diagonal
        return False
    if color == 0: 
        return False
    if not (0 <= r1 < size and 0 <= c1 < size):
        return False
    if not (0 <= r2 < size and 0 <= c2 < size):
        return False
    # must move in straight line
    if r1 != r2 and c1 != c2:
        return False
    if r1 == r2:
        distance = abs(c1 - c2)
    else:
        distance = abs(r1 - r2)
    if distance < 2 or distance % 2 != 0: #must move at least 2 and be even
        return False
    opponent = 2 if color == 1 else 1
    if r1 == r2:  #horizontal
        if c2 > c1:
            step = 1
        else:
            step = -1
        for c in range(c1, c2, 2 * step):
            if board[r1][c + step] != opponent:
                return False
            if board[r1][c + 2 * step] != 0:
                return False
    else:  #vertical
        if r2 > r1:
            step = 1
        else:
            step = -1
        for r in range(r1, r2, 2 * step):
            if board[r + step][c1] != opponent:
                return False
            if board[r + 2 * step][c1] != 0:
                return False
        if board[r2][c2] != 0: #checks to make sure move to tile is empty
            return False
    return True


#This function checks for possible moves a stone can make once the board is human ready
def get_valid_moves_for_stone(board, stone):
    row1, col1 = stone       #creates a copy of the stone's position with accesible data type
    #print(row1, col1)
    stone_number = board[row1][col1] 
    move_list = [] 
    size = len(board)
    move_list = []
    if stone_number == 0:
        return []
    r = row1-2 #row to move to
    validity = True #using bools in place of break b/c not allowed
    while r >= 0 and validity:
        if is_valid_move(board, ((row1,col1), (r,col1))):
            move_list.append(((row1,col1),(r, col1)))
            r -= 2
        else:
            validity = False
    r = row1+2 #row to move to
    validity = True
    while r < size and validity:
        if is_valid_move(board,((row1,col1),(r, col1))):
            move_list.append(((row1,col1),(r, col1)))
            r += 2
        else:
            validity = False
    c = col1-2 #col to move to
    validity = True
    while c >= 0 and validity:
        if is_valid_move(board, ((row1,col1),(row1, c))):
            move_list.append(((row1,col1),(row1, c)))
            c -= 2
        else:
            validity = False
    c = col1+2 #col to move to
    validity = True
    while c < size and validity: 
        if is_valid_move(board, ((row1,col1),(row1, c))):
            move_list.append(((row1,col1),(row1, c)))
            c += 2
        else:
            validity = False
    return move_list #adds all moves to a tuple and returns it

"""iterates through the entire board and checks all tiles which have the correct color,
if they have possible moves, they are added to the move_return_list, which then is checked for zero values to
ensure the proper return type is created."""
def get_valid_moves(board, player): 
    move_return_list = []
    for index1,i in enumerate(board): 
        for index2,j in enumerate(i):
            if j == player:
                moves = (get_valid_moves_for_stone(board, (index1,index2)))
                move_return_list += moves
    '''for move in move_return_list:
        if len(move) == 0:
            move_return_list.remove(move)'''
    return move_return_list

"""
This function gets a human input and determines if the move is valid, if so it returns the move
otherwise it prompts the human to try a new input until it works, if there are no moves, the function 
returns with no value
"""
def human_player(board,player):
    player_tuple = ()
    valid_move = False
    row1,col1,row2,col2 = 0,0,0,0
    move_list = get_valid_moves(board,player)
    if len(move_list) == 0:
        return player_tuple
    else:
        print(move_list)
    while valid_move == False:
        row1 = int(input("Enter the first and second value of your first move (row column): "))
        col1 = int(input())
        row2 = int(input("Enter the first and second value of your second move (row column): "))
        col2 = int(input())
        player_tuple = ((row1, col1), (row2, col2))
        if player_tuple not in move_list:
            player_tuple = ()
            print("Move not possible, try again please.")
            continue
        else: 
            print("Valid move!")
            valid_move = True
        return player_tuple

"""
This function takes in the board and player number and returns either an empty tuple for no moves
or it returns a random move from the move list
"""
def random_player(board,player):
    move_list = get_valid_moves(board,player)
    return_tuple = ()
    if len(move_list) == 0:
        return return_tuple
    choice = random.randint(0,len(move_list)-1)
    return move_list[choice]
"""
This function simply returns no move or the final move available in the move list (length-1)
"""
def ai_player(board, player):
    ai_tuple = ()
    move_list = get_valid_moves(board,player)
    length = len(move_list)
    if length == 0:
        return ai_tuple
    return move_list[length-1]

"""
plays the game, switching the player back and forth every time, if there is no amount of player 1 or 2's pieces
left on the board, the opposite player wins
"""
def play_game(board):
     win = False
     player = 1
     while win == False:
        for list in board:
            for item in list:
                if item == player:
                    win = True
            move = ai_player(board,player)
            if len(move) == 0:
                if player == 1:
                    return 2
                else:
                    return 1
            (r1,c1),(r2,c2) = move
            color = board[r1][c1]
            if r1 == r2:  #horizontal
                if c2 > c1:
                    step = 1
                else:
                    step = -1
                for c in range(c1, c2, 2 * step):
                    board[r1][c + step] = 0
            if c1 == c2:  #vertical
                if r2 > r1:
                    step = 1
                else:
                    step = -1
                for r in range(r1, r2, 2 * step):
                    board[r + step][c1] = 0
            if player == 1:
                player += 1
            else:
                player -= 1
            board[r2][c2] = color
            board[r1][c1] = 0
     return 3-player

"""
if __name__ == "__main__":

    board = generate_board(6)
    print(get_board_as_string(board))

    board = generate_board(7)
    print(get_board_as_string(board))

    board = generate_board(8)
    print(get_board_as_string(board))

    move = ((-1, -1), (8, 8))
    assert is_valid_move(board, move) == False

    print("Running prep_board_human")

    prep_board_human(board)
    print(get_board_as_string(board))

    print("########################################")

    board = [[1,2,1,2],
             [2,0,2,1],
             [1,2,1,2],
             [2,1,2,1],]

    
    print("Testing is_valid_move")

    print(get_board_as_string(board))

    assert is_valid_move(board, ((3, 1),(1, 1))) == True
    assert is_valid_move(board, ((3, 2),(1, 1))) == False
    assert is_valid_move(board, ((3, 3),(1, 1))) == False

    board = [[1,2,1,2,1,2,1,2],
             [2,1,0,1,2,1,2,1],
             [1,2,1,2,1,2,1,2],
             [2,1,0,1,2,1,2,1],
             [1,2,1,2,1,2,1,2],
             [2,1,0,1,2,1,2,1],
             [1,2,1,2,1,2,1,2],
             [2,1,2,1,2,1,2,1],]

    assert is_valid_move(board, ((7, 2),(1, 2))) == True
    assert is_valid_move(board, ((7, 2),(3, 2))) == True
    assert is_valid_move(board, ((5, 2),(3, 2))) == False
    assert is_valid_move(board, ((5, 3),(3, 2))) == False
    assert is_valid_move(board, ((6, 3),(3, 2))) == False
    assert is_valid_move(board, ((7, 3),(3, 2))) == False

    print("Passed is_valid_move tests")

    print("########################################")

    print("Testing get_valid_moves_for_stone")

    board = [[1, 2, 0, 2, 0, 0, 0, 0, 1, 2],
             [2, 1, 2, 1, 0, 0, 2, 1, 2, 1],
             [1, 2, 1, 2, 1, 2, 1, 2, 1, 2],
             [2, 1, 2, 1, 2, 1, 2, 1, 2, 1],
             [1, 2, 1, 2, 1, 2, 1, 2, 1, 2],
             [2, 1, 0, 1, 2, 1, 2, 1, 2, 1],
             [1, 2, 1, 2, 1, 2, 1, 2, 1, 2],
             [2, 1, 2, 1, 2, 1, 2, 1, 2, 1],
             [1, 2, 1, 2, 1, 2, 1, 2, 1, 2],
             [2, 1, 2, 1, 2, 1, 2, 1, 2, 1]]

    assert get_valid_moves_for_stone(board, (3,5)) == [((3, 5), (1, 5))]
    assert get_valid_moves_for_stone(board, (5,5)) == []
    assert get_valid_moves_for_stone(board, (7,1)) == []
    assert get_valid_moves_for_stone(board, (7,2)) == [((7, 2), (5, 2))]
    assert get_valid_moves_for_stone(board, (1,7)) == [((1, 7), (1, 5))]

    print("Passed get_valid_moves_for_stone tests")

    print("########################################")

    print("Testing get_valid_moves")

    assert sorted(get_valid_moves(board, 1)) == [((0, 0), (0, 2)), ((0, 0), (0, 4)),
                                                 ((1, 7), (1, 5)), ((2, 2), (0, 2)),
                                                ((2, 6), (0, 6)), ((3, 5), (1, 5))]

    assert sorted(get_valid_moves(board, 2)) == [((0, 9), (0, 7)),
                                                 ((1, 2), (1, 4)),
                                                 ((2, 7), (0, 7)),
                                                 ((3, 2), (5, 2)),
                                                 ((3, 4), (1, 4)),
                                                 ((5, 0), (5, 2)),
                                                 ((5, 4), (5, 2)),
                                                 ((7, 2), (5, 2))]

    print("Passed get_valid_moves tests")

    print("########################################")

    print("Running random_player tests")


    board = [[1, 2, 0, 2, 0, 0, 0, 0, 1, 2],
             [2, 1, 2, 1, 0, 0, 2, 1, 2, 1],
             [1, 2, 1, 2, 1, 2, 1, 2, 1, 2],
             [2, 1, 2, 1, 2, 1, 2, 1, 2, 1],
             [1, 2, 1, 2, 1, 2, 1, 2, 1, 2],
             [2, 1, 0, 1, 2, 1, 2, 1, 2, 1],
             [1, 2, 1, 2, 1, 2, 1, 2, 1, 2],
             [2, 1, 2, 1, 2, 1, 2, 1, 2, 1],
             [1, 2, 1, 2, 1, 2, 1, 2, 1, 2],
             [2, 1, 2, 1, 2, 1, 2, 1, 2, 1]]
    for _ in range(10):
        print("Player 1: ", random_player(board, 1))
    for _ in range(10):
        print("Player 2: ", random_player(board, 2))

    board = [[1, 2, 0, 2, 0, 0, 0, 0, 1, 2],
             [2, 1, 2, 1, 0, 0, 2, 1, 2, 1],
             [1, 2, 1, 2, 1, 2, 1, 2, 1, 2],
             [2, 1, 2, 1, 2, 1, 2, 1, 2, 1],
             [1, 2, 1, 2, 1, 2, 1, 2, 1, 2],
             [2, 1, 0, 1, 2, 1, 2, 1, 2, 1],
             [1, 2, 1, 2, 1, 2, 1, 2, 1, 2],
             [2, 1, 2, 1, 2, 1, 2, 1, 2, 1],
             [1, 2, 1, 2, 1, 2, 1, 2, 1, 2],
             [2, 1, 2, 1, 2, 1, 2, 1, 2, 1]]
    
    print("Finished running random_player")

    print("########################################")

    print("Running human_player tests")

    human_player(board, 1)

    print("Finished running human_player")

    print("########################################")

    print("Running play_game -- start with prepping the board")

    print("ALL TESTS PASSED")

    board = generate_board(10)
    prep_board_human(board)

    print(play_game(board))
"""

"""board_test = generate_board(8)
prep_board_human(board_test)
get_board_as_string(board_test)
stone_test = (3,6)
move_test = ((3,6),(3,4))
#print(get_valid_moves(board_test, 1))
#human_player(board_test, 1)
#print(ai_player(board_test, 1))


#print(get_valid_moves_for_stone(board_test, stone_test))

if is_valid_move(board_test, move_test):
    print("TRUE")
else:
    print("FALSE")
"""
    
