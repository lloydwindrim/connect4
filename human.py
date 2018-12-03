import numpy as np
import useful_tools

def bot( gameState , round, playerID ):
    # ---------------------------------------------------
    # description:
    #     #   takes human input. Should be 1:7
    # inputs:
    #   gameState ==> a copy of the current board (incl. tokens)
    #   round ==> the iteration number for the game (starting at 1)
    # outputs:
    #   col ==> column location to place token (between 1 and boardSize)
    # ---------------------------------------------------


    col = int(raw_input("Which column? [1,2,3,4,5,6,7]: "))


    return col




