
board_display_status = [[False for _ in range(16)] for _ in range(16)]


def display_full_board(board):
    for row in board:
        print(" ".join(row))


def display_partial_board(board):
    for row in range(len(board)):
        for tile in range(len(board)):
            if board_display_status[row][tile]:
                print(board[row][tile], end=" ")
            else:
                print("[ ]", end=" ")
        print("\n")


def reveal_spaces(pos_v: int, pos_h: int, board, board_display_status=board_display_status):
    board_size = len(board)

    if 0 <= pos_v < board_size and 0 <= pos_h < board_size and not board_display_status[pos_v][pos_h]:
        board_display_status[pos_v][pos_h] = True
        
        if board[pos_v][pos_h] == "[0]":
            local_squares = [
                (pos_v - 1, pos_h - 1),
                (pos_v - 1, pos_h),
                (pos_v - 1, pos_h + 1),
                (pos_v, pos_h - 1),
                (pos_v, pos_h + 1),
                (pos_v + 1, pos_h - 1),
                (pos_v + 1, pos_h),
                (pos_v + 1, pos_h + 1),
            ]
            
            for coordinate in local_squares:
                r, c = coordinate
                reveal_spaces(r, c, board, board_display_status)


def check_for_loss(pos_v: int, pos_h: int, board):
    return board[pos_v][pos_h] == "[X]"
