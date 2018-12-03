# connect4
An arena for python bots to play connect4 against each other 

## Usage

To play in command-line mode (DEBUG_MODE = false), run in the terminal:
```
python main.py random_bot stacker_bot
```

Otherwise to run in debug mode, set DEBUG_MODE = True


## Bots

Create a bot function using:
```
template_bot.py
```
which has inputs of the game state (0 for unoccupied, 1 or 2 for occupation by player 1 or 2 respectively), round number and the player's ID (1 or 2). The bot must use this information to return a column number to place the token (1 to number of columns e.g. 7).

There are also bot functions in:
```
useful_tools.py
```
which can be used to develop bots in debug mode.

## Rules

If you bot picks a column that is either full or not valid, it will be prompted to pick again. It will have a maximum of 10 re-picks before the player is declared the loser. There is also a time limit of 3 seconds or the bot to choose a valid column. There are tools for checking if a column is full or valid available in useful_tools.py

## Prerequisities
To use the gui:
- pygame
