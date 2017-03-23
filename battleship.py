from board import Board, print_board_heading, print_board
from player import Player
from ship import Ship
import os


SHIP_INFO = [
    ("Aircraft Carrier", 5),
    ("Battleship", 4),
    ("Submarine", 3),
    ("Cruiser", 3),
    ("Patrol Boat", 2)
]


if __name__ == "__main__":
    aircraft_carrier = Ship("Aircraft Carrier", 5)
    battleship = Ship("Battleship", 4)
    submarine = Ship("Submarine", 3)
    cruiser = Ship("Cruiser", 3)
    patrol_boat = Ship("Patrol Boat", 2)

    player_name = raw_input("Player 1, enter your name: ")
    player1 = Player(1, player_name)
    player1_board = Board()
    player1_opponent_board = Board()
    print_board(player1_board.grid)
