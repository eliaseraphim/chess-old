# author   | elia deppe
# filename | chessBoard.py

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
from helperFunctions import *
from colorama import init as colorama_init
from colorama import Fore, Back, Style

colorama_init(strip=False)

# ------------------------- BOARD INFO ------------------------- #

SIZE = 8
RANKS = '87654321'
FILES = 'abcdefgh'

CELL_WIDTH = 14
CELL_HEIGHT = 7
UNIT_DISPLAY_COLUMNS = (5, 6, 7, 8, 9)
UNIT_DISPLAY_ROWS = (2, 3, 4, 5)

# dictionaries for algebraic notation conversion to list positions
POS_TO_RANK = {i: RANKS[i] for i in range(SIZE)}
POS_TO_FILE = {i: FILES[i] for i in range(SIZE)}

# dictionaries for list positions conversion to algebraic notation
RANK_TO_POS = {RANKS[i]: i for i in range(SIZE)}
FILE_TO_POS = {FILES[i]: i for i in range(SIZE)}

# units and unit types, in starting order
UNIT = [rook, knight, bishop, queen, king, bishop, knight, rook]
TYPE = ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook']


# class / chessBoard
# description: chessboard class, upon which the game takes place
class chessBoard:
    """
    __init__
        parameter(s)
            self | chessBoard | current instance of the class chessBoard
            p1   | player     | player 1 - white (red)
            p2   | player     | player 2 - black (blue)
        return value(s)
            self | chessBoard | current instance of the class chessBoard

    description: constructor. initialize the chess board, and set the board for the start of a game.
        1) create an empty 2d list to represent the board. the outer list will be 8 lists long
            --> rows    | ranks
            --> columns | files
            chessBoard[file] --> access a position on the board
        2)
    """
    def __init__(self, p1, p2):
        self.logic_board = [[] for i in range(SIZE)]  # 8 x 8 logical chess board
        self.ascii_board = [[] for i in range(CELL_HEIGHT * SIZE + 1)]  # visual board for display
        self.p1, self.p2 = p1, p2

        self.set_board()
        self.generate_ascii_board()

    """
    set_board
        parameter(s)
            self | chessBoard | current instance of the class chessBoard
        return value(s)
            none
            
    description: sets the playing board to be used for logical operations. this playing board is an 8 x 8 list of 
        objects of parent type unit or None. All units will be a child class of unit: pawn, knight, bishop, rook,
        queen, or king. a piece that occupies this space on the logical board does so on the visual board as well.
        a position in the list that contains None represents an empty cell.
        
        set_board sets the logical board for the beginning of the game
        
        updates
            - 1/13/21
                - set_board now creates the unit and saves said unit to a variable before appending the
                    unit to the logical board, as well as the appropriate player's pieces
                - fixed unit construction 3rd argument to be position instead of (rank, position)
    """
    def set_board(self):
        for rank in range(SIZE):
            for file in range(SIZE):
                piece = None
                unit_type = TYPE[file]
                position = (rank, file)
                tile = POS_TO_FILE[file] + POS_TO_RANK[rank]

                print(unit_type, position, tile)

                # if we are currently upper or lower two ranks (starting ranks)
                if rank <= 1 or rank >= 6:
                    # upper --> black
                    if rank <= 1:
                        # assign piece to blacks pieces
                        if rank == 0:  # back row | black
                            piece = UNIT[file]('black', unit_type, position, tile)
                        elif rank == 1:  # front row | black
                            piece = pawn('black', 'pawn', position, tile)

                        self.p2.pieces.append(piece)

                    # lower --> white
                    else:
                        # assign piece to whites pieces
                        if rank == 6:  # front row | white
                            piece = pawn('white', 'pawn', position, tile)
                        elif rank == 7:  # front row | white
                            piece = UNIT[file]('white', unit_type, position, tile)

                        self.p1.pieces.append(piece)

                    # add to the board
                    self.logic_board[rank].append(piece)
                else:  # all other rows empty
                    self.logic_board[rank].append(None)

    """
    generate_ascii_board
        parameter(s)
            self | chessBoard | current instance of the class chessBoard
        return value(s)
            none
    
    description: generates a blank ascii board, and saves it to the current instance's ascii_board 2d list.
    """
    def generate_ascii_board(self):
        width = SIZE * CELL_WIDTH
        height = SIZE * CELL_HEIGHT

        for row in range(height + 1):
            for col in range(width + 1):
                if is_divisible(row, CELL_HEIGHT):  # horizontal edge
                    if self.is_corner(row, col, width, height):  # corners
                        self.ascii_board[row].append(Fore.WHITE + self.corner(row, col, width, height))
                    elif is_divisible(col, CELL_WIDTH):     # intersections
                        self.ascii_board[row].append(Fore.WHITE + self.intersection(row, col, width, height))
                    else:
                        self.ascii_board[row].append(Fore.WHITE + '─')

                elif is_divisible(col, CELL_WIDTH):   # vertical edge --> left / right
                    self.ascii_board[row].append(Fore.WHITE + '│')

                else:
                    if is_divisible(row // CELL_HEIGHT, 2):  # white is starting cell
                        self.ascii_board[row].append(Fore.WHITE + self.cell_character(row, col, 'white'))
                    else:                              # black is starting cell
                        self.ascii_board[row].append(Fore.WHITE + self.cell_character(row, col, 'black'))

    """
    is_corner (static)
        parameter(s)
            row    | Integer | current row in 2D grid for self.ascii_board
            col    | Integer | current column in 2D grid for self.ascii_board
            width  | Integer | the width of the board (length of the rows or lists)
            height | Integer | the height of the board (number of rows or lists)
        return value(s)
            True   | Boolean | True if the current row and col represents the corner of the board.
            False  | Boolean | False if the current row and col do not represent the corner of the board.
    """
    @staticmethod
    def is_corner(row, col, width, height):
        return (
                (row == 0 and col == 0) or
                (row == 0 and col == width) or
                (row == height and col == 0) or
                (row == height and col == width)
        )

    """
    corner (static)
        parameter(s)
            row    | Integer | current row in 2D grid for self.ascii_board
            col    | Integer | current column in 2D grid for self.ascii_board
            width  | Integer | the width of the board (length of the rows or lists)
            height | Integer | the height of the board (number of rows or lists)
        return value(s)
            '┌'    | String  | top left corner
            '┐'    | String  | top right corner
            '└'    | String  | bottom left corner
            '┘'    | String  | bottom right corner
            
    description: returns the correct corner given the current row and column
    """
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

    """
    intersection
        parameter(s)
            row    | Integer | current row in 2D grid for self.ascii_board
            col    | Integer | current column in 2D grid for self.ascii_board
            width  | Integer | the width of the board (length of the rows or lists)
            height | Integer | the height of the board (number of rows or lists)
        return value(s)
            '┬'    | String  | top border intersection
            '┴'    | String  | bottom border intersection
            '├'    | String  | left border intersection
            '┤'    | String  | right border intersection
            '┼'    | String  | inner intersection
            
    description: returns the correct intersection symbol given the current row and column
    """
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
        else:                # intersection
            return '┼'

    """
    cell_character
        parameter(s)
            row           | Integer | current row in 2D grid for self.ascii_board
            col           | Integer | current column in 2D grid for self.ascii_board
            starting_tile | String  | the starting tile for the row's color
        return value(s)
            ' '           | String  | a space for white tiles or empty positions
            '▒'           | String  | a symbol used for the border for black tiles
    
    description: returns the character that belongs in the cell at that current position. this is either a space or ▒
    which is used for the border of black tiles
    """
    @staticmethod
    def cell_character(row, col, starting_tile):
        local_row = row % CELL_HEIGHT
        local_col = col % CELL_WIDTH

        if starting_tile == 'white':
            if is_divisible(col // CELL_WIDTH, 2):  # white tile, just use spaces
                return ' '
            else:  # black tile
                if 2 <= local_row <= 5 and 3 <= local_col <= 11:  # within border
                    return ' '
                else:
                    return '▒'

        else:  # starting_tile == 'black'
            if is_divisible(col // CELL_WIDTH, 2):  # black tile
                if local_row == 1 or local_row == 6:  # top / bottom of black border
                    return '▒'
                elif 1 <= local_col <= 2 or 12 <= local_col <= 13:
                    return '▒'
                else:
                    return ' '
            else:
                return ' '

    """
    display_ascii_board
        parameter(s)
            self | chessBoard | current instance of the class chessBoard
        return value(s)
            none
    
    description: displays the ascii chess board to the user, printing one row at a time
    """
    def display_ascii_board(self):
        self.update_ascii_board()
        for row in self.ascii_board:
            print(''.join(row))

    """
    update_ascii_board
        parameter(s)
            self | chessBoard | current instance of the class chessBoard
        return value(s)
            none
    description: updates the ascii board to match the current state of logical board
    """
    def update_ascii_board(self):
        width = SIZE * CELL_WIDTH
        height = SIZE * CELL_HEIGHT

        for row in range(2, height, CELL_HEIGHT):
            cell_row = row // CELL_HEIGHT
            for col in range(5, width, CELL_WIDTH):
                cell_col = col // CELL_WIDTH
                self.draw_unit(row, col, self.logic_board[cell_row][cell_col])

    """
    is_occupied
        parameter(s)
            self       | chessBoard | current instance of the class chessBoard
            cell_row   | int        | row the cell occupies
            cell_col   | int        | column the cell occupies
        return value(s)
            True/False | boolean    | returns True or False depending on if a unit occupies the cell on the board
    """
    def is_occupied(self, cell_row, cell_col):
        return isinstance(self.logic_board[cell_row][cell_col], unit)

    """
    draw_unit
        parameter(s)
            self  | chessBoard | current instance of the class chessBoard
            row   | int        | current row of the ascii_board
            col   | col        | current col of the ascii_board
            _unit | unit       | the current unit to be drawn
        return value(s)
            none
    description: draws the unit on the ascii_board in full, starting from the top left corner. if there is no unit on 
    the current cell, then the cell is reset to the original board color.
    """
    def draw_unit(self, row, col, _unit):
        for i in range(DRAW_HEIGHT):
            for j in range(DRAW_WIDTH):
                if _unit is not None:
                    if _unit.color == 'white':
                        self.ascii_board[row + i][col + j] = Fore.RED + _unit.symbol[i][j]
                    else:
                        self.ascii_board[row + i][col + j] = Fore.CYAN + _unit.symbol[i][j]
                else:
                    self.ascii_board[row + i][col + j] = Fore.WHITE + ' '

    def game_over(self):
        pass