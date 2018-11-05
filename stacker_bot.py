import numpy as np
import useful_tools

def bot( gameState , round, playerID ):
    # ---------------------------------------------------
    # description:
    #   randomly chooses a column, and continues to place tokens in that column
    # inputs:
    #   gameState ==> a copy of the current board (incl. tokens)
    #   round ==> the iteration number for the game (starting at 1)
    # outputs:
    #   col ==> column location to place token (between 1 and boardSize)
    # ---------------------------------------------------

    [nRows, nCols] = np.shape(gameState)

    if round == 1:
        # first move is random
        col = make_random_move( gameState )
    else:
        # find column with most tokens from playerID
        col = np.argmax( np.sum( gameState==playerID , axis=0 ) ) + 1
        if (not useful_tools.isValid(col, nCols)) | (useful_tools.isColumnFull(col, gameState)):
            # if not valid, make a random move
            col = make_random_move(gameState)

    return col



def make_random_move( gameState ):

    [nRows, nCols] = np.shape(gameState)

    while (1):
        col = np.random.randint(nCols) + 1
        if (useful_tools.isValid(col, nCols)) & (not useful_tools.isColumnFull(col, gameState)):
            break

    return col





