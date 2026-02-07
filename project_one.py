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

def get_board_as_string(board):
    size = len(board[0])
    board_as_string = ""
    """print(size)
    for i in range(size): #creates the top/bottom border of the cells
        board_as_string += "+-"
        if i == size-1:
            board_as_string += "+"""
    for i in range(size):
        board_as_string += "|"
        ...

    return board_as_string

board_test = generate_board(5)
print(get_board_as_string(board_test))
            

    
