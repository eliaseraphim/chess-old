# author   / elia deppe
# filename / units.py

import helperFunctions

# ---------------------------- UNITS --------------------------- #

"""
EXTRA ANSII SYMBOLS --> ☺☻♥♦♣♠•◘○◙♂♀♪♫☺►◄↕‼¶§▬↨↑↓→←∟↔▲▼

UNIT SYMBOLS --> 5 characters wide x 4 characters tall

King

  ▲    0
▌ █ ▐  1
█▄█▄█  2
▀▀▀▀▀  3
01234

Queen

  ▼    0
 ▌■▐   1
▌███▐  2
▀▀▀▀▀  3
01234

Rook

▄ ▄ ▄  0
 ███   1
 ███   2
▀▀▀▀▀  3
01234

Bishop

  ┼    0
╬ ▄ ╬  1
▄▐█▌▄  2
▀▀▀▀▀  3
01234

Knight --> Not happy with this, but it works for now.

  ■╬╬  0
▲ █╬╬  1
│ ██▌  2
▀▀▀▀▀  3
01234

Pawn

  •    0
• ▄ •  1
 ▄█▄   2
▀▀▀▀▀  3
01234
"""

DRAW_WIDTH = 5
DRAW_HEIGHT = 4

king_symbol = (
    '  ▲  ',
    '▌ █ ▐',
    '█▄█▄█',
    '▀▀▀▀▀'
)

queen_symbol = (
    '  ▼  ',
    ' ▌■▐ ',
    '▌███▐',
    '▀▀▀▀▀'
)

rook_symbol = (
    '▄ ▄ ▄',
    ' ███ ',
    ' ███ ',
    '▀▀▀▀▀'
)

bishop_symbol = (
    '  ┼  ',
    '╬ ▄ ╬',
    '▄▐█▌▄',
    '▀▀▀▀▀'
)

knight_symbol = (
    '  ■╬╬',
    '▲ █╬╬',
    '│ ██▌',
    '▀▀▀▀▀'
)

pawn_symbol = (
    '  •  ',
    '• ▄ •',
    ' ▄█▄ ',
    '▀▀▀▀▀'
)

PIECES = {
    'king':   king_symbol,
    'queen':  queen_symbol,
    'rook':   rook_symbol,
    'bishop': bishop_symbol,
    'knight': knight_symbol,
    'pawn':   pawn_symbol,
}

SIZE = 8
RANKS = '87654321'
FILES = 'abcdefgh'

# dictionaries for algebraic notation conversion to list positions
POS_TO_RANK = {i: RANKS[i] for i in range(SIZE)}
POS_TO_FILE = {i: FILES[i] for i in range(SIZE)}

# dictionaries for list positions conversion to algebraic notation
RANK_TO_POS = {RANKS[i]: i for i in range(SIZE)}
FILE_TO_POS = {FILES[i]: i for i in range(SIZE)}

# class / unit
# description: unit parent class, for the individual unit types of chess
class unit:
    def __init__(self, color, unit_type, position, tile):
        self.color = color
        self.unit_type = unit_type
        self.position = position
        self.tile = tile

        if color == 'white':
            self.symbol = PIECES[unit_type]
        else:
            self.symbol = PIECES[unit_type]

        if unit_type == 'pawn':
            self.en_passant = False

    def get_info(self):
        print(self.unit_type + self.tile + ' ' + self.color)

    def __str__(self):
        return self.unit_type + self.tile + ' ' + self.color


class king(unit):
    def get_valid_moves(self, logic_board):
        return []


class queen(unit):
    # Queen can move diagonally, and in a straight line for all 8 cardinal directions.
    movement_options = [
        [1, 1],
        [1, -1],
        [-1, 1],
        [1, 1],
        [1, 0],
        [0, 1],
        [-1, 0],
        [0, -1]
    ]

    def get_valid_moves(self, logic_board):
        prefix = 'q'
        valid_moves = get_valid_slide_moves(self, logic_board, prefix)

        return [self.tile, valid_moves]


class rook(unit):
    # Rook can move in a straight line, in all 4 cardinal directions
    movement_options = [
        [1, 0],
        [0, 1],
        [-1, 0],
        [0, -1]
    ]

    def get_valid_moves(self, logic_board):
        prefix = 'r'
        valid_moves = get_valid_slide_moves(self, logic_board, prefix)

        return [self.tile, valid_moves]


class bishop(unit):
    # Bishop can move diagonally, in all 4 intercardinal directions.
    movement_options = [
        [1, 1],
        [1, -1],
        [-1, 1],
        [1, 1]
    ]

    def get_valid_moves(self, logic_board):
        prefix = 'b'
        valid_moves = get_valid_slide_moves(self, logic_board, prefix)

        return [self.tile, valid_moves]



class knight(unit):
    movement_options = [
        [2, 1],
        [2, -1],
        [-2, 1],
        [-2, -1],
        [1, 2],
        [1, -2],
        [-1, 2],
        [-1, -2]
    ]

    def get_valid_moves(self, logic_board):
        valid_moves = []
        prefix = 'n'

        for movement in self.movement_options:
            new_row = self.position[0] + movement[0]
            new_col = self.position[1] + movement[1]

            # If the move is on the board
            if 0 <= new_row < SIZE and 0 <= new_col < SIZE:
                # If cell is empty
                if logic_board[new_row][new_col] is None:
                    valid_moves.append(prefix + POS_TO_FILE[new_col] + POS_TO_RANK[new_row])

                # otherwise, cell must contain enemy if populated
                else:
                    if logic_board[new_row][new_col].color != self.color:
                        valid_moves.append(prefix + 'x' + POS_TO_FILE[new_col] + POS_TO_RANK[new_row])

        return [self.tile, valid_moves]


class pawn(unit):
    moves = 0

    def __init__(self, color, unit_type, position, tile):
        super().__init__(color, unit_type, position, tile)

        if self.color == 'white':
            self.movement = -1
        else:
            self.movement = 1

    def get_valid_moves(self, logic_board):
        valid_moves = []
        prefix = self.tile[0]

        # Basic Movement
        if logic_board[self.position[0] + self.movement][self.position[1]] is None:
            valid_moves.append(prefix + POS_TO_RANK[self.position[0] + self.movement])

            if self.moves == 0:
                if logic_board[self.position[0] + self.movement * 2][self.position[1]] is None:
                    valid_moves.append(prefix + POS_TO_RANK[self.position[0] + self.movement * 2])

        # Need to implement: Captures and En Passant

        return [self.tile, valid_moves]


def get_valid_slide_moves(piece, logic_board, prefix):
    valid_moves = []

    for movement in piece.movement_options:
        new_row = piece.position[0] + movement[0]
        new_col = piece.position[1] + movement[1]
        blocked = False

        # Can move diagonally until end of board or blocked by own/opponent piece
        while 0 <= new_row < SIZE and 0 <= new_col < SIZE and not blocked:
            if logic_board[new_row][new_col] is None:
                valid_moves.append(prefix + POS_TO_FILE[new_col] + POS_TO_RANK[new_row])

            # otherwise, diagonal is blocked, and must be enemy to capture
            else:
                blocked = True
                if logic_board[new_row][new_col].color != piece.color:
                    valid_moves.append(prefix + 'x' + POS_TO_FILE[new_col] + POS_TO_RANK[new_row])

    return valid_moves
