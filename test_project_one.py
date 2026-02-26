from project_one import generate_board, get_board_as_string, is_valid_move,\
      prep_board_human, get_valid_moves_for_stone, get_valid_moves, random_player,\
      human_player, play_game

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

    board = generate_board(10)
    prep_board_human(board)

    print(play_game(board))