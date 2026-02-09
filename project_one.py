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
# current state of the baord to the terminal/screen
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
            #print(board[row1_to_remove][col1_to_remove])
            #print(board[row2_to_remove][col2_to_remove])
            print("Invalid input, need different colors.")
        elif row1_to_remove ==  0 or row2_to_remove == 0:
            print("Invalid input, need a different row.")
        elif row1_to_remove == size or row2_to_remove == size: #tests all cases to make sure its a valid move
            print("Invalid input, need a different row.")
        elif col1_to_remove == 0 or col2_to_remove == 0:
            print("Invalid input, need a different column.")
        elif col1_to_remove == size or col2_to_remove == size:
            print("Invalid input, need a different column.")
        else:
            board[row1_to_remove][col1_to_remove] = 0 #removes elements
            board[row2_to_remove][col2_to_remove] = 0
            return

move_test = ((3,3),(3,4))

def is_valid_move(board, move): #move is a nested tuple ((start),(end))
    

board_test = generate_board(8)
prep_board_human(board_test)
get_board_as_string(board_test)

            

    
