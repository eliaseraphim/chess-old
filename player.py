from helperFunctions import clear
from random import shuffle
import time

class player():
    def __init__(self, color):
        self.color = color
        self.pieces = []
        self.valid_moves = []

    def update_valid_moves(self, logic_board):
        self.valid_moves = []
        for piece in self.pieces:
            self.valid_moves.append(piece.get_valid_moves(logic_board))
