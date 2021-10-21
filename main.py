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
from player import player


def play():
    pass


def main():
    p1, p2 = player('Player 1'), player('Player 2')
    board = chessBoard(p1, p2)
    play(p1, p2, board)


if __name__ == '__main__':
    main()
