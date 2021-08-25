# author / elia deppe
# email / elia.deppe
# github / eliaseraphim
#
# file / main.py
# program title / chess
# description / chess program
#
#
# start date: 03/18/21

from chessBoard import chessBoard


def players():
    return 1, 2


def play():
    pass


def main():
    p1, p2 = players()
    board = chessBoard()

    board.display_ascii_board()

    play()


if __name__ == '__main__':
    main()
