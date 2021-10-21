from random import choice

class player():
    def __init__(self, current_player):
        self.set_name(current_player)
        self.set_color()
        """
        steps
            1 --> Get Player Name
            2 --> Get Player Preferred Color
            3 --> Set Players Pieces --> This could be done from set_board in the chess_board class
                Pass in the player's to the constructor
        """

    """
    set_name
        parameter(s)
            self           | player  | current instance of the player
            current_player | str     | the current player, will be 'Player 1' or 'Player 2'
    """
    def set_name(self, current_player):
        self.name = None
        while self.name is None:
            self.name = input(f'{current_player} | Name: ')
            confirmation = input('Is this name correct? ').lower()

            if confirmation in ['y', 'yes']:
                print(f'{current_player} set to', self.name)
            elif confirmation in ['n', 'no']:
                print('Resetting...')
                self.name = None
            else:
                print('Invalid Response - Please enter Yes or No to confirm your name.')
                self.name = None

    @classmethod
    def set_color(cls, p1, p2):
        print('Please choose Player White, who will go first.')
        decision = None
        while decision is not None:
            decision = input('Enter player name for white or random: ').lower()
            if decision == p1.name:
                p1.order = 1
                p2.order = -1
            elif decision == p2.name:
                p1.order = -1
                p2.order = 1
            elif choice == 'random':
                x = choice([1, -1])
                p1.order = x
                p2.order = -x
            else:
                print('Invalid Response - Please enter the name for player White, or random.')



    def set_pieces(self):
        pass

    def update_pieces(self):
        pass

