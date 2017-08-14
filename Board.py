BOARD_SIZE = 8


class Board:
    def __init__(self):
        self.squares = [['0' for x in range(BOARD_SIZE)] for y in range(BOARD_SIZE)]

        # Initialize the starting arrangement of the game
        self.squares[3][3] = 'W'
        self.squares[4][4] = 'W'
        self.squares[3][4] = 'B'
        self.squares[4][3] = 'B'

    def print_board(self):
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                print self.squares[row][col],
            print '\n',

board = Board()
board.print_board()
