BOARD_SIZE = 10

VERTICAL_SHIP = '|'
HORIZONTAL_SHIP = '-'
EMPTY = 'O'
MISS = '.'
HIT = '*'
SUNK = '#'

class Board(object):
    def __init__(self):
        self.ship_locations = []
        self.grid = []
        for x in range(BOARD_SIZE):
            self.grid.append([])
            for y in range(BOARD_SIZE):
                self.grid[x].append(EMPTY)


def print_board_heading():
    print("   " + " ".join([chr(c) for c in range(ord('A'), ord('A') + BOARD_SIZE)]))


def print_board(board):
    print_board_heading()

    row_num = 1
    for row in board:
        print(str(row_num).rjust(2) + " " + (" ".join(row)))
        row_num += 1
