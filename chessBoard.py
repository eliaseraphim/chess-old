# author   / elia deppe
# filename / chessBoard.py

"""
Tiles are 8 Tall and 14 Wide (Counting Intersection(s) and Corners)

Box Drawing Characters - ASCII
    Lines
        Vertical       >>  │  >>  179
        Horizontal     >>  ─  >>  196
    Corners
        Top Left       >>  ┌  >>  218
        Top Right      >>  ┐  >>  191
        Bottom Left    >>  └  >>  192
        Bottom Right   >>  ┘  >>  217
    Intersections
        Center         >>  ┼  >>  197
        Top Center     >>  ┬  >>  194
        Bottom Center  >>  ┴  >>  193
        Left Center    >>  ├  >>  195
        Right Center   >>  ┤  >>  180

White Tiles --> Spaces
Black Tiles --> Border
    Character
        ░  >>  176
        ▒  >>  177  * using this for now, subject to change
        ▓  >>  178
        █  >>   219


Column Order --> Vertically
    Hundreds
    Tens
    Ones

i =                                                                                                 1         1
          1         2         3         4         5         6         7         8         9         0         1
01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012
┌─────────────┬─────────────┬─────────────┬─────────────┬─────────────┬─────────────┬─────────────┬─────────────┐ j = 0
│             │▒▒▒▒▒▒▒▒▒▒▒▒▒│             │▒▒▒▒▒▒▒▒▒▒▒▒▒│             │▒▒▒▒▒▒▒▒▒▒▒▒▒│             │▒▒▒▒▒▒▒▒▒▒▒▒▒│ j = 1
│             │▒           ▒│             │▒           ▒│             │▒           ▒│             │▒           ▒│ j = 2
│             │▒           ▒│             │▒           ▒│             │▒           ▒│             │▒           ▒│ j = 3
│             │▒           ▒│             │▒           ▒│             │▒           ▒│             │▒           ▒│ j = 4
│             │▒           ▒│             │▒           ▒│             │▒           ▒│             │▒           ▒│ j = 5
│             │▒▒▒▒▒▒▒▒▒▒▒▒▒│             │▒▒▒▒▒▒▒▒▒▒▒▒▒│             │▒▒▒▒▒▒▒▒▒▒▒▒▒│             │▒▒▒▒▒▒▒▒▒▒▒▒▒│ j = 6
├─────────────┼─────────────┼─────────────┼─────────────┼─────────────┼─────────────┼─────────────┼─────────────┤ j = 7
│▒▒▒▒▒▒▒▒▒▒▒▒▒│             │▒▒▒▒▒▒▒▒▒▒▒▒▒│             │▒▒▒▒▒▒▒▒▒▒▒▒▒│             │▒▒▒▒▒▒▒▒▒▒▒▒▒│             │ j = 8
│▒           ▒│             │▒           ▒│             │▒           ▒│             │▒           ▒│             │ j = 9
│▒           ▒│             │▒           ▒│             │▒           ▒│             │▒           ▒│             │ j = 10
│▒           ▒│             │▒           ▒│             │▒           ▒│             │▒           ▒│             │ j = 11
│▒           ▒│             │▒           ▒│             │▒           ▒│             │▒           ▒│             │ j = 12
│▒▒▒▒▒▒▒▒▒▒▒▒▒│             │▒▒▒▒▒▒▒▒▒▒▒▒▒│             │▒▒▒▒▒▒▒▒▒▒▒▒▒│             │▒▒▒▒▒▒▒▒▒▒▒▒▒│             │ j = 13
├─────────────┼─────────────┼─────────────┼─────────────┼─────────────┼─────────────┼─────────────┼─────────────┤ j = 14
│             │▒▒▒▒▒▒▒▒▒▒▒▒▒│             │▒▒▒▒▒▒▒▒▒▒▒▒▒│             │▒▒▒▒▒▒▒▒▒▒▒▒▒│             │▒▒▒▒▒▒▒▒▒▒▒▒▒│ j = 15
│             │▒           ▒│             │▒           ▒│             │▒           ▒│             │▒           ▒│ j = 16
│             │▒           ▒│             │▒           ▒│             │▒           ▒│             │▒           ▒│ j = 17
│             │▒           ▒│             │▒           ▒│             │▒           ▒│             │▒           ▒│ j = 18
│             │▒           ▒│             │▒           ▒│             │▒           ▒│             │▒           ▒│ j = 19
│             │▒▒▒▒▒▒▒▒▒▒▒▒▒│             │▒▒▒▒▒▒▒▒▒▒▒▒▒│             │▒▒▒▒▒▒▒▒▒▒▒▒▒│             │▒▒▒▒▒▒▒▒▒▒▒▒▒│ j = 20
├─────────────┼─────────────┼─────────────┼─────────────┼─────────────┼─────────────┼─────────────┼─────────────┤ j = 21
│▒▒▒▒▒▒▒▒▒▒▒▒▒│             │▒▒▒▒▒▒▒▒▒▒▒▒▒│             │▒▒▒▒▒▒▒▒▒▒▒▒▒│             │▒▒▒▒▒▒▒▒▒▒▒▒▒│             │ j = 22
│▒           ▒│             │▒           ▒│             │▒           ▒│             │▒           ▒│             │ j = 23
│▒           ▒│             │▒           ▒│             │▒           ▒│             │▒           ▒│             │ j = 24
│▒           ▒│             │▒           ▒│             │▒           ▒│             │▒           ▒│             │ j = 25
│▒           ▒│             │▒           ▒│             │▒           ▒│             │▒           ▒│             │ j = 26
│▒▒▒▒▒▒▒▒▒▒▒▒▒│             │▒▒▒▒▒▒▒▒▒▒▒▒▒│             │▒▒▒▒▒▒▒▒▒▒▒▒▒│             │▒▒▒▒▒▒▒▒▒▒▒▒▒│             │ j = 27
├─────────────┼─────────────┼─────────────┼─────────────┼─────────────┼─────────────┼─────────────┼─────────────┤ j = 28
│             │▒▒▒▒▒▒▒▒▒▒▒▒▒│             │▒▒▒▒▒▒▒▒▒▒▒▒▒│             │▒▒▒▒▒▒▒▒▒▒▒▒▒│             │▒▒▒▒▒▒▒▒▒▒▒▒▒│ j = 29
│             │▒           ▒│             │▒           ▒│             │▒           ▒│             │▒           ▒│ j = 30
│             │▒           ▒│             │▒           ▒│             │▒           ▒│             │▒           ▒│ j = 31
│             │▒           ▒│             │▒           ▒│             │▒           ▒│             │▒           ▒│ j = 32
│             │▒           ▒│             │▒           ▒│             │▒           ▒│             │▒           ▒│ j = 33
│             │▒▒▒▒▒▒▒▒▒▒▒▒▒│             │▒▒▒▒▒▒▒▒▒▒▒▒▒│             │▒▒▒▒▒▒▒▒▒▒▒▒▒│             │▒▒▒▒▒▒▒▒▒▒▒▒▒│ j = 34
├─────────────┼─────────────┼─────────────┼─────────────┼─────────────┼─────────────┼─────────────┼─────────────┤ j = 35
│▒▒▒▒▒▒▒▒▒▒▒▒▒│             │▒▒▒▒▒▒▒▒▒▒▒▒▒│             │▒▒▒▒▒▒▒▒▒▒▒▒▒│             │▒▒▒▒▒▒▒▒▒▒▒▒▒│             │ j = 36
│▒           ▒│             │▒           ▒│             │▒           ▒│             │▒           ▒│             │ j = 37
│▒           ▒│             │▒           ▒│             │▒           ▒│             │▒           ▒│             │ j = 38
│▒           ▒│             │▒           ▒│             │▒           ▒│             │▒           ▒│             │ j = 39
│▒           ▒│             │▒           ▒│             │▒           ▒│             │▒           ▒│             │ j = 40
│▒▒▒▒▒▒▒▒▒▒▒▒▒│             │▒▒▒▒▒▒▒▒▒▒▒▒▒│             │▒▒▒▒▒▒▒▒▒▒▒▒▒│             │▒▒▒▒▒▒▒▒▒▒▒▒▒│             │ j = 41
├─────────────┼─────────────┼─────────────┼─────────────┼─────────────┼─────────────┼─────────────┼─────────────┤ j = 42
│             │▒▒▒▒▒▒▒▒▒▒▒▒▒│             │▒▒▒▒▒▒▒▒▒▒▒▒▒│             │▒▒▒▒▒▒▒▒▒▒▒▒▒│             │▒▒▒▒▒▒▒▒▒▒▒▒▒│ j = 43
│             │▒           ▒│             │▒           ▒│             │▒           ▒│             │▒           ▒│ j = 44
│             │▒           ▒│             │▒           ▒│             │▒           ▒│             │▒           ▒│ j = 45
│             │▒           ▒│             │▒           ▒│             │▒           ▒│             │▒           ▒│ j = 46
│             │▒           ▒│             │▒           ▒│             │▒           ▒│             │▒           ▒│ j = 47
│             │▒▒▒▒▒▒▒▒▒▒▒▒▒│             │▒▒▒▒▒▒▒▒▒▒▒▒▒│             │▒▒▒▒▒▒▒▒▒▒▒▒▒│             │▒▒▒▒▒▒▒▒▒▒▒▒▒│ j = 48
├─────────────┼─────────────┼─────────────┼─────────────┼─────────────┼─────────────┼─────────────┼─────────────┤ j = 49
│▒▒▒▒▒▒▒▒▒▒▒▒▒│             │▒▒▒▒▒▒▒▒▒▒▒▒▒│             │▒▒▒▒▒▒▒▒▒▒▒▒▒│             │▒▒▒▒▒▒▒▒▒▒▒▒▒│             │ j = 50
│▒           ▒│             │▒           ▒│             │▒           ▒│             │▒           ▒│             │ j = 51
│▒           ▒│             │▒           ▒│             │▒           ▒│             │▒           ▒│             │ j = 52
│▒           ▒│             │▒           ▒│             │▒           ▒│             │▒           ▒│             │ j = 53
│▒           ▒│             │▒           ▒│             │▒           ▒│             │▒           ▒│             │ j = 54
│▒▒▒▒▒▒▒▒▒▒▒▒▒│             │▒▒▒▒▒▒▒▒▒▒▒▒▒│             │▒▒▒▒▒▒▒▒▒▒▒▒▒│             │▒▒▒▒▒▒▒▒▒▒▒▒▒│             │ j = 55
└─────────────┴─────────────┴─────────────┴─────────────┴─────────────┴─────────────┴─────────────┴─────────────┘ j = 56

Midpoints
    Horizontal - Multiples of 13
    Vertical   - Multiples of 7
"""

# board diagram
#             ♔♔
#             0  1 2  3 4  5 6  7   < -- column
# rank -- | 8 ⬛ ⬜ ⬛ ⬜ ⬛ ⬜ ⬛ ⬜ 0 | -- row
#         | 7 ⬜ ⬛ ⬜ ⬛ ⬜ ⬛ ⬜ ⬛ 1 |
#         | 6 ⬛ ⬜ ⬛ ⬜ ⬛ ⬜ ⬛ ⬜ 2 |
#         | 5 ⬜ ⬛ ⬜ ⬛ ⬜ ⬛ ⬜ ⬛ 3 |
#         | 4 ⬛ ⬜ ⬛ ⬜ ⬛ ⬜ ⬛ ⬜ 4 |
#         | 3 ⬜ ⬛ ⬜ ⬛ ⬜ ⬛ ⬜ ⬛ 5 |
#         | 2 ⬛ ⬜ ⬛ ⬜ ⬛ ⬜ ⬛ ⬜ 6 |
#         | 1 ⬜ ⬛ ⬜ ⬛ ⬜ ⬛ ⬜ ⬛ 7 |
#   file -- > a  b c  d e  f g  h
# The board is navigated typically in row-major order.

from units import *
from colorama import Fore, Back, Style

SIZE = 8
RANKS = '87654321'
FILES = 'abcdefgh'

CELL_WIDTH = 14
CELL_HEIGHT = 7
UNIT_DISPLAY_COLUMNS = (5, 6, 7, 8, 9)
UNIT_DISPLAY_ROWS = (2, 3, 4, 5)

# dictionaries for algebraic notation conversion to list positions


RANK_TO_POS = {i: RANKS[i] for i in range(SIZE)}
FILE_TO_POS = {i: FILES[i] for i in range(SIZE)}

# dictionaries for list positions conversion to algebraic notation
POS_TO_RANK = {RANKS[i]: i for i in range(SIZE)}
POS_TO_FILE = {FILES[i]: i for i in range(SIZE)}

# units and unit types, in starting order
UNIT = [rook, knight, bishop, queen, king, bishop, knight, rook]
TYPE = ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook']


# class / chessBoard
# description: chessboard class, upon which the game takes place
class chessBoard:
    # constructor
    #   parameter(s)
    #       none
    #   return value(s)
    #       None
    #
    # description: initialize the chess board, and set the board for the start of a game.
    #   1) create an empty 2d list to represent the board. the outer list will be 8 lists long
    #       --> rows    | ranks
    #       --> columns | files
    #       chessBoard[file] --> access a position on the board
    #   2)
    def __init__(self):
        self.board = [[] for i in range(SIZE)]
        self.set_board()

    #
    def set_board(self):
        for rank in range(SIZE):
            for file in range(SIZE):
                unit_type = TYPE[file]
                position = (rank, file)
                tile = FILE_TO_POS[file] + RANK_TO_POS[rank]

                if rank == 0:  # back row | black
                    self.board[rank].append(UNIT[file]('black', unit_type, (rank, position), tile))
                elif rank == 1:  # front row | black
                    self.board[rank].append(pawn('black', 'pawn', (rank, position), tile))
                elif rank == 6:  # front row | white
                    self.board[rank].append(pawn('white', 'pawn', (rank, position), tile))
                elif rank == 7:  # front row | white
                    self.board[rank].append(UNIT[file]('white', unit_type, (rank, position), tile))
                else:  # all other rows empty
                    self.board[rank].append(None)

    # colors --> white tiles --> cyan
    #        --> black tiles --> red
    # row 1 --> white, black, white, black, white, ...
    # row 2 --> black, white, black, white,
    def print_board(self):
        width = SIZE * CELL_WIDTH
        height = SIZE * CELL_HEIGHT
        text = ''

        for row in range(height + 1):
            for col in range(width + 1):
                if self.is_divisible(row, CELL_HEIGHT):  # horizontal edge
                    if self.is_corner(row, col, width, height):  # corners
                        text += self.corner(row, col, width, height)
                    elif self.is_divisible(col, CELL_WIDTH):     # intersections
                        text += self.intersection(row, col, width, height)
                    else:
                        text += '─'

                elif self.is_divisible(col, CELL_WIDTH):   # vertical edge --> left / right
                    text += '│'

                else:
                    if (row // CELL_HEIGHT) % 2 == 0: # white is starting cell
                        text += self.cell_character(row, col, ' ', '▒')
                    else:                             # black is starting cell
                        text += self.cell_character(row, col, '▒', ' ')

            text += '\n'

        print(text)

    @staticmethod
    def is_divisible(a, b):
        return a % b == 0

    @staticmethod
    def is_remainder(a, b, c):
        return a % b == c

    @staticmethod
    def is_corner(row, col, width, height):
        return (
                (row == 0 and col == 0) or
                (row == 0 and col == width) or
                (row == height and col == 0) or
                (row == height and col == width)
        )

    @staticmethod
    def corner(row, col, width, height):
        if row == 0 and col == 0:         # top left
            return '┌'
        elif row == 0 and col == width:   # top right
            return '┐'
        elif row == height and col == 0:  # bottom left
            return '└'
        else:                             # bottom right
            return '┘'

    @staticmethod
    def intersection(row, col, width, height):
        if row == 0:         # top edge
            return '┬'
        elif row == height:  # bottom edge
            return '┴'
        elif col == 0:       # left edge
            return '├'
        elif col == width:   # right edge
            return '┤'
        else:
            return '┼'

    # NEED TO SET UP SITUATION TO RETURN PIECES SYMBOLS IF CELL IS OCCUPIED
    # This is a little convoluted and could be simplified since their is repetition. Perhaps if I decide on if it's a
    #   white tile or black tile, I can call the appropriate function for that colored tile instead?
    def cell_character(self, row, col, symbol1, symbol2):
        if symbol1 == ' ':                                   # white is starting cell
            if self.is_divisible(row // CELL_HEIGHT, 2):
                if self.is_divisible(col // CELL_WIDTH, 2):  # white cell
                    return symbol1

                else:                                        # black cell
                    if self.is_remainder(row, CELL_HEIGHT, 1) or self.is_remainder(row, CELL_HEIGHT, 6):
                        return symbol2

                    else:
                        if self.is_remainder(col, CELL_WIDTH, 1) or self.is_remainder(col, CELL_WIDTH, 13):
                            return symbol2
                        else:
                            return symbol1

        else:                                                # black is starting cell
            if self.is_divisible(col // CELL_WIDTH, 2):
                if self.is_remainder(row, CELL_HEIGHT, 1) or self.is_remainder(row, CELL_HEIGHT, 6):
                    return symbol1

                else:
                    if self.is_remainder(col, CELL_WIDTH, 1) or self.is_remainder(col, CELL_WIDTH, 13):
                        return symbol1
                    else:
                        return symbol2

            else:
                return symbol2