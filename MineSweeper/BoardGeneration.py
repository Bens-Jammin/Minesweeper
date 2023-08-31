import random
from BoardDisplay import * 

BOARD_SIZE = 16

def generate_board(size: int, bombs: int):
    """
    param: size -> int
    param: bombs -> int
    return: board: -> list

    generates a grid with sidelengths 'size', fills the board
    with 'bombs'  total bombs, and returns the generated board
    """

    board = [["[-]" for _ in range(size)] for _ in range(size)]


    # bomb generation
    placed = 0 
    
    while placed < bombs:
        pos_v = random.randint(0, size - 1)
        pos_h = random.randint(0, size - 1)

        if board[pos_v][pos_h] != "[X]":
            board[pos_v][pos_h] = "[X]"
            placed += 1
    
    return board


def generate_local_bomb_count(pos_v: int, pos_h: int, board: list):
    """
    param: pos_v -> int
    param: pos_h -> int
    param: board -> list
    return: total_local_bombs -> int
    
    returns a number between 0 and 8 of the the number of bombs surrounding the given tile
    """
    if board[pos_v][pos_h] == "[X]":
        return None

    total_local_bombs = 0

    local_squares = [
        (pos_v - 1, pos_h - 1),
        (pos_v - 1, pos_h ),
        (pos_v - 1, pos_h + 1),
        (pos_v, pos_h - 1),
        (pos_v, pos_h + 1),
        (pos_v + 1, pos_h - 1),
        (pos_v + 1, pos_h ),
        (pos_v + 1, pos_h + 1),
    ]

    for coordinate in local_squares:
        r = coordinate[0]
        c = coordinate[1]
        board_size = len(board)
        if board_size > r >= 0 and board_size > c >= 0 and board[r][c] == "[X]":
            total_local_bombs += 1 

    
    return total_local_bombs


def generate_board_with_bomb_count(size: int, bombs: int):

    board = generate_board(size, bombs)

    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] != "[X]":
                board[r][c] = f"[{generate_local_bomb_count(r, c, board)}]"
    
    return board
