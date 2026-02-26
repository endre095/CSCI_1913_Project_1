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

#These two helper functions create list types 1 and 2, which just means they
#either start with 1 or 2 as the board switches between these as you go down
#the rows.
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

#This function creates the list of lists using the two helper functions above,
#this function calls those two functions in accordance with the size of the list
#as different sized nested lists would have different formats of 1's and 2's.
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
    r1,c1 = move[0][0],move[0][1]
    r2,c2 = move[1][0],move[1][1]
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
    if not ((abs(r1-r2) == 2 and c1==c2) or (abs(c1-c2) == 2 and r1==r2)):
        return False
    if (abs(r1-r2) == 2 and c1==c2):
        mid = board[(r1+r2)//2][c1]
        if mid == color or mid == 0:
            return False
    if (abs(c1-c2) == 2 and r1==r2): 
        mid = board[r1][(c1+c2)//2] #checks to make sure that the move was a jump & has a opponent between jump squares
        if mid == color or mid == 0:
            return False
    if board[r2][c2] != 0: #checks to make sure move-to tile is empty
        return False
    return True


#This function checks for possible moves a stone can make once the board is human ready
def get_valid_moves_for_stone(board, stone):
    row1, col1 = stone       #creates a copy of the stone's position with accesible data type
    #print(row1, col1)
    stone_number = board[row1][col1] 
    opponent = 2 if stone_number == 1 else 1 #determines which color stone should be checked against for moves
    move_list = [] 
    size = len(board)
    move_list = []
    if stone_number == 0:
        return []
    if row1 - 2 >= 0:
        if board[row1-2][col1] == 0 and board[row1-1][col1] == opponent:
            move_list.append(((row1,col1),(row1-2, col1)))
    if row1 + 2 < size:
        if board[row1+2][col1] == 0 and board[row1+1][col1] == opponent:
            move_list.append(((row1,col1),(row1+2, col1)))
    if col1 - 2 >= 0:
        if board[row1][col1-2] == 0 and board[row1][col1-1] == opponent:
            move_list.append(((row1,col1),(row1, col1-2)))
    if col1 + 2 < size:
        if board[row1][col1+2] == 0 and board[row1][col1+1] == opponent:
            move_list.append(((row1,col1),(row1, col1+2)))
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
    for move in move_return_list:
        if len(move) == 0:
            move_return_list.remove(move)
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
        return 

"""
This function takes in the board and player number and returns either an empty tuple for no moves
or it returns a random move from the move list
"""
def random_player(board,player):
    move_list = get_valid_moves(board,player)
    return_tuple = ()
    if len(move_list) == 0:
        return return_tuple
    choice = random.randint(0,len(move_list))
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
"""
def play_game(board):
     


board_test = generate_board(8)
prep_board_human(board_test)
get_board_as_string(board_test)
stone_test = (3,6)
move_test = ((3,6),(3,4))
#print(get_valid_moves(board_test, 1))
#human_player(board_test, 1)
#print(ai_player(board_test, 1))


#print(get_valid_moves_for_stone(board_test, stone_test))

'''if is_valid_move(board_test, move_test):
    print("TRUE")
else:
    print("FALSE")
''' 
    
