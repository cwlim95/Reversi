BOARD_SIZE = 8


class Board:
    def __init__(self):
        self.squares = [['0' for x in range(BOARD_SIZE)] for y in range(BOARD_SIZE)]

        # Initialize the starting arrangement of the game
        self.squares[3][3] = 'W'
        self.squares[4][4] = 'W'
        self.squares[3][4] = 'B'
        self.squares[4][3] = 'B'

        self.active_player = 'B'  # Black to move first

    def print_board(self):
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                print self.squares[row][col],
            print '\n',

    def move(self, row, col):


        if self.active_player == 'B':
            self.squares[row][col] = 'B'
        else:
            self.squares[row][col] = 'W'

    def valid_move(self, row, col):
        # At least one piece is reversed
        # Check 8 directions
        if row < 0 or row > 7 or col < 0 or col > 7:
            print 'Not in boundary.'
            return False

        if self.squares[row][col] is not '0':
            print 'Existed piece.'
            return False

        # Probably need to take care of boundary cases
        adjacent_pieces = []
        for x in range(row - 1, row + 2):
            for y in range(col - 1, col + 2):
                if x == row and y == col:  # Ignore the assumed place piece
                    continue
                adjacent_pieces.append(self.squares[x][y])

board = Board()
board.valid_move(4, 2)
board.print_board()
