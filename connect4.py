import numpy as np

class Game( ):

    def __init__( self, boardSize=[6,7], target=4 ):
        # ---------------------------------------------------
        # inputs:
        #   boardSize ==> number of columns vs rows of board. [rows,cols]. default=[6,7]
        #   target ==> how many consecutive to win. default=4
        # outputs:
        #   creates gameState
        # ---------------------------------------------------

        self.boardSize = boardSize
        self.target = target

        # setup board
        self.gameState = np.zeros( boardSize, np.int )

        # result indicator
        self.result = 'on-going'



    def take_turn( self, playerID, col ):
        # ---------------------------------------------------
        # inputs:
        #   player id ==> player whose turn it is. 1 or 2
        #   col ==> which column player desires to place token. 1:cols inclusive
        # outputs:
        #   modifies gameState
        #   FLAG_valid ==> 1-valid move, 0-invalid move
        # ---------------------------------------------------

        # check if playerID is correctly input
        if not ( (playerID == 1) | (playerID == 2) ):
            raise ValueError('Player ID must be either 1 or 2.')

        col -= 1

        FLAG_valid = 1

        # check if valid move
        if (self.boardSize[1] - (col+1) < 0) | (col<0):
            FLAG_valid = 0
        # check if column full
        elif self.gameState[0,col] > 0:
            FLAG_valid = 0

        # place token
        if FLAG_valid == 1:
            # determine which row token lands in given col
            row = ( np.sum( ( self.gameState == 0 ), axis=0 ) - 1 )[col]

            # update gameMat
            self.gameState[row,col] = playerID

        # check if someone has won/drawn
        if self.check_for_win(playerID, self.target):
            self.result = 'player%i wins'%(playerID)
        elif self.check_for_draw():
            self.result = 'draw'

        return FLAG_valid


    def check_for_win( self, playerID, target=4 ):
        # ---------------------------------------------------
        # inputs:
        #   player id ==> player to check. 1 or 2
        #   target ==> how many consecutive tokens to win. default=4
        # outputs:
        #   FLAG_win ==> 1-player wins, 0-no win
        # ---------------------------------------------------

        # identify playerID's tokens
        playerState = self.gameState == playerID

        FLAG_win = 0

        # check for horizontal win
        for i in range( self.boardSize[0] ):
            if np.sum( np.convolve( playerState[i,:] , np.ones((target))) >= target ):
                FLAG_win = 1

        # check for vertical win
        for i in range( self.boardSize[1] ):
            if np.sum( np.convolve( playerState[:,i] , np.ones((target))) >= target ):
                FLAG_win = 1

        # check for diagonal win
        diag1 = np.eye(target)
        diag2 = diag1[::-1,:]
        for i in range( self.boardSize[0] - target + 1 ):
            for j in range(self.boardSize[1] - target + 1):
                if (np.sum( diag1*playerState[i:i+target,j:j+target] ) == target) | (np.sum( diag2*playerState[i:i+target,j:j+target] ) == target):
                    FLAG_win = 1
                    break

        return FLAG_win


    def check_for_draw( self ):
        # ---------------------------------------------------
        # inputs:
        #   none
        #
        # outputs:
        #   ==> 1-draw, 0-no draw --------------------------------

        # draw if no free spaces on top row
        if np.sum( self.gameState[0,:] == 0 ) == 0:
            return 1
        else:
            return 0