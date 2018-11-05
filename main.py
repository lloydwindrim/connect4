import connect4
import useful_tools
import sys
import time

DEBUG_MODE = False

if not DEBUG_MODE:

    # load bots from command-line arguments
    bot1Name = sys.argv[1]
    bot2Name = sys.argv[2]
    bot1 = __import__(bot1Name)
    bot2 = __import__(bot2Name)



if __name__ == "__main__":

    # start at round 1
    round = 1

    # setup game (parameters)
    BOARDSIZE = [6,7] # board dimensions [rows,cols]
    TARGET = 4 # how many consecutive tokens to win
    PERIOD_OF_TIME = 3 # number of seconds before time-out
    MAX_COUNT = 10  # number of consecutive invalid moves before time-out

    game = connect4.Game( boardSize=BOARDSIZE, target=TARGET )

    while(1):

        # player 1: get location from bot
        if DEBUG_MODE:
            col = useful_tools.debug_bot1(game.gameState.copy(), round, playerID=1)
        else:
            start = time.time()
            col = bot1.bot(game.gameState.copy(), round, playerID=1)
            if time.time() > start + PERIOD_OF_TIME:
                game.result = 'player2 wins by time-out'

        # player 1: take turn
        valid = 0
        count = 0
        while valid == 0:
            valid = game.take_turn(playerID=1, col=col)
            count += 1
            if count > MAX_COUNT:
                game.result = 'player2 wins by time-out'
                break

        # display board
        print '--------- round %i -------------------'%(round)
        print game.gameState

        # check if player 1 won
        if (game.result == 'player1 wins') | (game.result == 'draw') | (game.result == 'player2 wins by time-out'):
            print game.result
            break


        # player 2: get location from bot
        if DEBUG_MODE:
            col = useful_tools.debug_bot2(game.gameState.copy(), round, playerID=2)
        else:
            start = time.time()
            col = bot2.bot(game.gameState.copy(), round, playerID=2)
            if time.time() > start + PERIOD_OF_TIME:
                game.result = 'player1 wins by time-out'

        # player 2: take turn
        valid = 0
        count = 0
        while valid == 0:
            valid = game.take_turn(playerID=2, col=col)
            count += 1
            if count > MAX_COUNT:
                game.result = 'player1 wins by time-out'
                break

        # display board
        print game.gameState

        # check if player 2 won
        if (game.result == 'player2 wins') | (game.result == 'draw') | (game.result == 'player1 wins by time-out'):
            print game.result
            break


        round += 1



