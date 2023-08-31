from BoardGeneration import * 
from BoardDisplay import *

def main():
    board = generate_board_with_bomb_count(16, 32)

    display_partial_board(board)

    while True:
        v = int(input("v: "))
        h = int(input("h: "))

        reveal_spaces(v, h, board)

        display_partial_board(board)

        if check_for_loss(v, h, board):
            print("YOU LOST!!!!!")
            break

if __name__ == "__main__":
    main()