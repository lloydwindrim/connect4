import numpy as np

def isValid( col, numCols ):
    # ---------------------------------------------------
    # description:
    #   check of column is in board (valid)
    # inputs:
    #   col ==> which column player desires to place token. 1:cols inclusive
    #   numCols ==> how many columns the board has
    # outputs:
    #   ==> 1-valid move, 0-invalid move
    # ---------------------------------------------------

    if (numCols - col < 0) | (col < 1):
        return 0
    else:
        return 1



def isColumnFull( col, gameState ):
    # ---------------------------------------------------
    # description:
    #   check if column is full
    # inputs:
    #   col ==> which column player desires to place token. 1:cols inclusive
    #   gameState ==> the current board (incl. tokens)
    # outputs:
    #   ==> 1-column full, 0-column not full
    # ---------------------------------------------------

    if gameState[0,col-1] > 0:
        return 1
    else:
        return 0


def debug_bot1(gameState, round, playerID ):
    # ---------------------------------------------------
    # description:
    #   a bot1 template for running in DEBUG mode
    # inputs:
    #   gameState ==> a copy of the current board (incl. tokens)
    #   round ==> the iteration number for the game (starting at 1)
    # outputs:
    #   col ==> column location to place token (between 1 and boardSize)
    # ---------------------------------------------------

    col = 1

    return col


def debug_bot2(gameState, round, playerID ):
    # ---------------------------------------------------
    # description:
    #   a bot2 template for running in DEBUG mode
    # inputs:
    #   gameState ==> a copy of the current board (incl. tokens)
    #   round ==> the iteration number for the game (starting at 1)
    # outputs:
    #   col ==> column location to place token (between 1 and boardSize)
    # ---------------------------------------------------

    col = 2

    return col




