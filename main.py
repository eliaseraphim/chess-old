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

from helperFunctions import clear
from chessBoard import chessBoard
from player import player

def play(p1, p2, board):
    current_player = 1
    players = {
        1  : p1,
        -1 : p2
    }

    x = 1

    while(not board.game_over() and x < 10):
        board.display_ascii_board()

        # determine valid moves for current player
        players[current_player].update_valid_moves(board.logic_board)
        print(players[current_player].valid_moves)

        print(f'>> current turn: {players[current_player].color}')
        position = input('>> ')

        # what makes position legal?
        # assuming valid input
        #   --> if normal move:
        #       --> not occupied
        #       --> valid move for piece
        #       --> if king, not in check

        current_player = -current_player
        clear()

        # inform turn
        # get move
        #   if legal, apply move
        #   otherwise, re-ask for move
        # check for win
        # switch order
        # clear screen
        # repeat

        x += 1



def main():
    clear()  # clear screen on start

    # establish players, and player color
    p1, p2 = player('white'), player('black')
    board = chessBoard(p1, p2)

    play(p1, p2, board)


if __name__ == '__main__':
    main()
