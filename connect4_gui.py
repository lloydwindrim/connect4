# Connect Four GUI
# Author: Stuart Eiffert
# Created: 3rd Dec 2018
# 
# Based on pygame tutorials by Al Sweigart al@inventwithpython.com, http://inventwithpython.com/pygame
# Released under a "Simplified BSD" license
#

import  sys, pygame
from pygame.locals import *

class GUI():
    def __init__(self, debug_mode=False, scale=1.0, graphics_dir='graphics'):

        self.debug_mode = debug_mode
        print(self.debug_mode)
        # board and window size variables
        self.board_width = 7
        self.board_height = 6
        self.scale=scale
        self.window_width = int(640*self.scale)
        self.window_height = int(480*self.scale)
        self.grid_size = int(50*self.scale) # size of the tokens and individual board spaces in pixels
        self.x_margin = int((self.window_width - self.board_width * self.grid_size) / 2)
        self.y_margin = int((self.window_height - self.board_height * self.grid_size) / 2)
        self.bg_colour = (0, 50, 255)
        self.RED = 'red'
        self.BLACK = 'black'
        self.EMPTY = None

        # graphics variables
        pygame.init()
        self.gui_clock = pygame.time.Clock()
        self.display_window = pygame.display.set_mode((self.window_width, self.window_height))
        self.graphics_dir = graphics_dir
        self.red_stack_rect = pygame.Rect(int(self.grid_size / 2), self.window_height - int(3 * self.grid_size / 2), self.grid_size, self.grid_size)
        self.black_stack_rect = pygame.Rect(self.window_width - int(3 * self.grid_size / 2), self.window_height - int(3 * self.grid_size / 2), self.grid_size, self.grid_size)
        self.red_token_img = pygame.image.load(self.graphics_dir+'/connect4_red_circle.png')
        self.red_token_img = pygame.transform.smoothscale(self.red_token_img, (self.grid_size, self.grid_size))
        self.black_token_img = pygame.image.load(self.graphics_dir+'/connect4_black_circle.png')
        self.black_token_img = pygame.transform.smoothscale(self.black_token_img, (self.grid_size, self.grid_size))
        self.board_img = pygame.image.load(self.graphics_dir+'/connect4_board.png')
        self.board_img = pygame.transform.smoothscale(self.board_img, (self.grid_size, self.grid_size))
        self.red_win_img = pygame.image.load(self.graphics_dir+'/connect4_red_wins.png')
        self.red_win_img = pygame.transform.smoothscale(self.red_win_img, (self.window_width, self.window_height))
        self.black_win_img = pygame.image.load(self.graphics_dir+'/connect4_black_wins.png')
        self.black_win_img = pygame.transform.smoothscale(self.black_win_img, (self.window_width, self.window_height))
        self.tie_win_img = pygame.image.load(self.graphics_dir+'/connect4_everybody_loses.png')
        self.tie_win_img = pygame.transform.smoothscale(self.tie_win_img, (self.window_width, self.window_height))
        self.winner_rect = self.red_win_img.get_rect()
        self.winner_rect.center = (int(self.window_width / 2), int(self.window_height / 2))
        self.winner_img = None

        pygame.display.set_caption('ACFR Battle Royale')
        self.main_board = self.getNewBoard()
        self.startGame()


    def startGame(self):
        self.main_board = self.getNewBoard()
        self.drawBoard(self.main_board)
        pygame.display.update()
        self.gui_clock.tick()

    def move(self, playerID, col):
        col -=1 #changing 1 indexing to 0 indexing
        if playerID == 2:
            if not self.isValidMove(self.main_board, col):
                #BLACK loses by invalid choice
                self.winner_img = self.red_win_img
            else:
                if not self.debug_mode:
                    self.animateBlackMoving(self.main_board, col)
                self.makeMove(self.main_board, self.BLACK, col)
                if self.isWinner(self.main_board, self.BLACK):
                    self.winner_img = self.black_win_img

        elif playerID == 1:
            if not self.isValidMove(self.main_board, col):
                #self.BLACK loses by invalid choice
                self.winner_img = self.black_win_img
            else:
                if not self.debug_mode:
                    self.animateRedMoving(self.main_board, col)
                self.makeMove(self.main_board, self.RED, col)
                if self.isWinner(self.main_board, self.RED):
                    self.winner_img = self.red_win_img
        self.drawBoard(self.main_board)
        pygame.display.update()
        self.gui_clock.tick()
        if self.isBoardFull(self.main_board):
            self.winner_img = self.tie_win_img


    def finished(self):
        print("Click Screen to exit")
        while True:
            # Keep looping until player clicks the mouse or quits.
            self.drawBoard(self.main_board)
            if not self.debug_mode:
                self.display_window.blit(self.winner_img, self.winner_rect)
            pygame.display.update()
            self.gui_clock.tick()
            for event in pygame.event.get(): # event handling loop
                if event.type == QUIT or event.type == MOUSEBUTTONUP:
                    pygame.quit()
                    sys.exit()
                    break


    def cleanup(self):
        pygame.quit()
        #sys.exit()

    def getNewBoard(self):
        board = []
        for x in range(self.board_width):
            board.append([self.EMPTY] * self.board_height)
        return board

    def makeMove(self, board, player, column):
        lowest = self.getLowestEmptySpace(board, column)
        if lowest != -1:
            board[column][lowest] = player

    def isWinner(self, board, tile):
        # check horizontal spaces
        for x in range(self.board_width - 3):
            for y in range(self.board_height):
                if board[x][y] == tile and board[x+1][y] == tile and board[x+2][y] == tile and board[x+3][y] == tile:
                    return True
        # check vertical spaces
        for x in range(self.board_width):
            for y in range(self.board_height - 3):
                if board[x][y] == tile and board[x][y+1] == tile and board[x][y+2] == tile and board[x][y+3] == tile:
                    return True
        # check / diagonal spaces
        for x in range(self.board_width - 3):
            for y in range(3, self.board_height):
                if board[x][y] == tile and board[x+1][y-1] == tile and board[x+2][y-2] == tile and board[x+3][y-3] == tile:
                    return True
        # check \ diagonal spaces
        for x in range(self.board_width - 3):
            for y in range(self.board_height - 3):
                if board[x][y] == tile and board[x+1][y+1] == tile and board[x+2][y+2] == tile and board[x+3][y+3] == tile:
                    return True
        return False

    def isBoardFull(self, board):
        # Returns True if there are no empty spaces anywhere on the board.
        for x in range(self.board_width):
            for y in range(self.board_height):
                if board[x][y] == self.EMPTY:
                    return False
        return True


    def animateBlackMoving(self, board, column):
        x = self.black_stack_rect.left
        y = self.black_stack_rect.top
        speed = 1.0*(self.scale**2)
        # moving the black tile up
        while y > (self.y_margin - self.grid_size):
            y -= int(speed)
            speed += 0.5*(self.scale**2)
            self.drawBoard(board, {'x':x, 'y':y, 'color':self.BLACK})
            pygame.display.update()
            self.gui_clock.tick()
        # moving the black tile over
        y = self.y_margin - self.grid_size
        speed = 1.0*self.scale
        while x > (self.x_margin + column * self.grid_size):
            x -= int(speed)
            speed += 0.5*(self.scale**2)
            self.drawBoard(board, {'x':x, 'y':y, 'color':self.BLACK})
            pygame.display.update()
            self.gui_clock.tick()
        # dropping the black tile
        self.animateDroppingToken(board, column, self.BLACK)

    def animateRedMoving(self, board, column):
        x = self.red_stack_rect.left
        y = self.red_stack_rect.top
        speed = 1.0*(self.scale**2)
        # moving the black tile up

        while y > (self.y_margin - self.grid_size):
            y -= int(speed)
            speed += 0.5*(self.scale**2)
            self.drawBoard(board, {'x':x, 'y':y, 'color':self.RED})
            pygame.display.update()
            self.gui_clock.tick()
        # moving the red tile over
        y = self.y_margin - self.grid_size
        speed = 1.0*(self.scale**2)
        while x < (self.x_margin + column * self.grid_size):
            x += int(speed)
            speed += 0.5*(self.scale**2)
            self.drawBoard(board, {'x':x, 'y':y, 'color':self.RED})
            pygame.display.update()
            self.gui_clock.tick()
        # dropping the black tile
        self.animateDroppingToken(board, column, self.RED)

    def animateDroppingToken(self, board, column, color):
        x = self.x_margin + column * self.grid_size
        y = self.y_margin - self.grid_size
        dropSpeed = 1.0*(self.scale**2)

        lowestEmptySpace = self.getLowestEmptySpace(board, column)

        while True:
            y += int(dropSpeed)
            dropSpeed += 0.5*(self.scale**2)
            if int((y - self.y_margin) / self.grid_size) >= lowestEmptySpace:
                return
            self.drawBoard(board, {'x':x, 'y':y, 'color':color})
            pygame.display.update()
            self.gui_clock.tick()

    def getLowestEmptySpace(self, board, column):
        # Return the row number of the lowest empty row in the given column.
        for y in range(self.board_height-1, -1, -1):
            if board[column][y] == self.EMPTY:
                return y
        return -1

    def drawBoard(self, board, extraToken=None):
        self.display_window.fill(self.bg_colour)

        # draw tokens
        spaceRect = pygame.Rect(0, 0, self.grid_size, self.grid_size)
        for x in range(self.board_width):
            for y in range(self.board_height):
                spaceRect.topleft = (self.x_margin + (x * self.grid_size), self.y_margin + (y * self.grid_size))
                if board[x][y] == self.RED:
                    self.display_window.blit(self.red_token_img, spaceRect)
                elif board[x][y] == self.BLACK:
                    self.display_window.blit(self.black_token_img, spaceRect)

        # draw the extra token
        if extraToken != None:
            if extraToken['color'] == self.RED:
                self.display_window.blit(self.red_token_img, (extraToken['x'], extraToken['y'], self.grid_size, self.grid_size))
            elif extraToken['color'] == self.BLACK:
                self.display_window.blit(self.black_token_img, (extraToken['x'], extraToken['y'], self.grid_size, self.grid_size))

        # draw board over the tokens
        for x in range(self.board_width):
            for y in range(self.board_height):
                spaceRect.topleft = (self.x_margin + (x * self.grid_size), self.y_margin + (y * self.grid_size))
                self.display_window.blit(self.board_img, spaceRect)

        # draw the red and black tokens off to the side
        self.display_window.blit(self.red_token_img, self.red_stack_rect) # red on the left
        self.display_window.blit(self.black_token_img, self.black_stack_rect) # black on the right

    def isValidMove(self, board, column):
        # Returns True if there is an empty space in the given column.
        # Otherwise returns False.
        if column < 0 or column >= (self.board_width) or board[column][0] != self.EMPTY:
            return False
        return True  


