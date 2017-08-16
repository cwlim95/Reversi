class Board:
    def __init__(self, size):
        self.board_size = size
        self.squares = [['0' for x in range(self.board_size)] for y in range(self.board_size)]

        # Initialize the starting arrangement of the game
        self.squares[3][3] = 'B'
        self.squares[4][4] = 'B'
        self.squares[3][4] = 'W'
        self.squares[4][3] = 'W'

        self.active_player = 'B'  # Black to move first

    def print_board(self):
        # print column count
        print('  ', end='')
        for x in range(self.board_size):
            print(x, end=' ')
        print('\n', end='')
        for row in range(self.board_size):
            print(row, end=' ')
            for col in range(self.board_size):
                print(self.squares[row][col], end=' ')
            print('\n', end='')

    def move(self, row, col):

        if self.active_player == 'B':
            # check for valid_move
            self.squares[row][col] = 'B'
            self.active_player = 'W'
        else:
            self.squares[row][col] = 'W'
            self.active_player = 'B'

    def all_valid_moves(self):
        # Obtained all the valid moves that can be performed by the active players
        valid_moves = []
        for row in range(self.board_size):
            for col in range(self.board_size):
                if self.valid_move(row, col) is True:
                    valid_moves.append([row, col])

        return valid_moves

    def valid_move(self, row, col):
        # At least one piece is reversed
        # Check 8 directions
        if row < 0 or row > self.board_size or col < 0 or col > 7:
            #print('Not in boundary.')
            return False

        if self.squares[row][col] is not '0':
            #print('Existed piece.')
            return False

        # Probably need to take care of boundary cases
        '''
        adjacent_pieces = []
        for x in range(row - 1, row + 2):
            for y in range(col - 1, col + 2):
                if x == row and y == col:  # Ignore the assumed place piece
                    continue
                adjacent_pieces.append(self.squares[x][y])
        '''
        if row != 0 and col != 0:
            # tedious here, not sure how to simplify
            return self.checkValid(row,col,self.active_player,"NW") or \
            self.checkValid(row,col,self.active_player,"SE") or \
            self.checkValid(row,col,self.active_player,"NE") or \
            self.checkValid(row,col,self.active_player,"SW") or \
            self.checkValid(row,col,self.active_player,"E") or \
            self.checkValid(row,col,self.active_player,"S") or \
            self.checkValid(row,col,self.active_player,"W") or \
            self.checkValid(row,col,self.active_player,"N")

        ###following are boundary cases

        elif row == 0 and col != 0:
            # Top row
            return self.checkValid(row,col,self.active_player,"SE") or \
            self.checkValid(row,col,self.active_player,'SW') or \
            self.checkValid(row,col,self.active_player,"E") or \
            self.checkValid(row,col,self.active_player,"S") or \
            self.checkValid(row,col,self.active_player,"W")

        elif row != 0 and col == 0:
            # Left Column
            return self.checkValid(row,col,self.active_player,"SE") or \
            self.checkValid(row,col,self.active_player,"NE") or \
            self.checkValid(row,col,self.active_player,"E") or \
            self.checkValid(row,col,self.active_player,"S") or \
            self.checkValid(row,col,self.active_player,"N")

        elif row == self.board_size - 1 and col != 0:
            # Bottom Row
            return self.checkValid(row,col,self.active_player,"NW") or \
            self.checkValid(row,col,self.active_player,"NE") or \
            self.checkValid(row,col,self.active_player,"E") or \
            self.checkValid(row,col,self.active_player,"W") or \
            self.checkValid(row,col,self.active_player,"N")

        elif row != 0 and col == self.board_size - 1:
            #Right Column
            return self.checkValid(row,col,self.active_player,"NW") or \
            self.checkValid(row,col,self.active_player,"SW") or \
            self.checkValid(row,col,self.active_player,"S") or \
            self.checkValid(row,col,self.active_player,"W") or \
            self.checkValid(row,col,self.active_player,"N")

        ###following are corner points

        elif row == 0 and col == 0:
            #Top left corner
            return self.checkValid(row,col,self.active_player,"SE") or \
            self.checkValid(row,col,self.active_player,"E") or \
            self.checkValid(row,col,self.active_player,"S")

        elif row == self.board_size - 1 and col == 0:
            #Bottom Right Corner
            return self.checkValid(row,col,self.active_player,"NE") or \
            self.checkValid(row,col,self.active_player,"E") or \
            self.checkValid(row,col,self.active_player,"N")

        elif row == 0 and col == self.board_size - 1:
            #Top Right Corner
            return self.checkValid(row,col,self.active_player,"SW") or \
            self.checkValid(row,col,self.active_player,"S") or \
            self.checkValid(row,col,self.active_player,"W")

        elif row == self.board_size - 1 and col == self.board_size - 1:
            #Bottom Right Corner
            return self.checkValid(row,col,self.active_player,"NW") or \
            self.checkValid(row,col,self.active_player,"W") or \
            self.checkValid(row,col,self.active_player,"N")

        else:
            return None

    def nextPosition(self, row, col, direction):
        '''
        Iterator: returns the next position based on the direction & the current counter

        NW = North West, SE = South East, and so on
        '''
        if direction == "NW":
            return row - 1, col - 1
        elif direction == "SE":
            return row + 1, col + 1
        elif direction == "NE":
            return row - 1, col + 1
        elif direction == "SW":
            return row + 1, col - 1
        elif direction == "E":
            return row, col + 1
        elif direction == "S":
            return row + 1, col
        elif direction == "W":
            return row, col - 1
        elif direction == "N":
            return row - 1, col
        else:
            return None

    def checkValid(self,row,col,colour,direction):
        '''
        !!! Requires testing !!!, seems to work.
        Returns True if north-west direction is valid, else False;

        Doesn't handle border condition, (could be fixed here or handled in the calling function)
        Suggestion: calling function should identify which checkValid functions to call.
        '''
        curRow, curCol = self.nextPosition(row, col, direction)
        if curRow > 7 or curCol > 7 or self.squares[curRow][curCol] == '0' or self.squares[curRow][curCol] == colour:
            #first encounter cannot be the same colour
            return False
        else:
            curRow, curCol = self.nextPosition(curRow, curCol, direction)
            while curRow >=0 and curCol >=0 and self.squares[curRow][curCol] != '0':
                if self.squares[curRow][curCol] == colour:
                    #encounters a similar colour along the way, hence valid move in NW.
                    return True
                #print(curRow, curCol)
                curRow, curCol = self.nextPosition(curRow, curCol, direction)
            return False

#main
if __name__ == "__main__":
    board = Board(8)
    board.print_board()
    print(board.all_valid_moves())
    #print(board.checkValid(5,5,'B', 'NW'))
    #print(board.checkValid(4,5,'W', 'N'))

