# author   / elia deppe
# filename / units.py

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
    pass


class queen(unit):
    pass


class rook(unit):
    pass


class bishop(unit):
    pass


class knight(unit):
    pass


class pawn(unit):
    pass
