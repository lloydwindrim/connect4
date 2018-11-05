import numpy as np
import useful_tools

def bot( gameState , round, playerID ):
    # ---------------------------------------------------
    # description:
    #     #   randomly chooses a column to place token
    # inputs:
    #   gameState ==> a copy of the current board (incl. tokens)
    #   round ==> the iteration number for the game (starting at 1)
    # outputs:
    #   col ==> column location to place token (between 1 and boardSize)
    # ---------------------------------------------------

    [nRows , nCols] = np.shape( gameState )


    while (1):
        col = np.random.randint(nCols) + 1
        if (useful_tools.isValid(col,nCols)) & (not useful_tools.isColumnFull(col,gameState)):
            break

    return col




