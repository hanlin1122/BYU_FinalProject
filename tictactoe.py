# Tic Tac Toe

#imports all the necessary modules
import time
import random
#need to install colorama package for access to this module
import colorama
from colorama import Fore, Back, Style 

#initializes the color for x and o
colorama.init()

#Creates the class for OOP
class Tic:

    #Gives the introduction to the player
    def __init__(self):
        print ('Welcome to Tic Tac Toe!')
        print ('Player one, choose your symbol')

    #Draws the sample board for the instructions
    def drawSampleBoard(self):
        print('''This is how the numbering will work. Put the number that you would like to place your symbol in:
           |   |   
         7 | 8 | 9
           |   |  
        -----------
           |   |
         4 | 5 | 6
           |   | 
        -----------
           |   |
         1 | 2 | 3
           |   |
        ''')
        time.sleep(3)

    #Draw the actual game board
    def drawBoard (self, board):
        # This function prints out the board that it was passed.
        # "board" is a list of 10 strings representing the board (ignore index 0)
        print ('   |   |')
        print (' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
        print ('   |   |')
        print ('-----------')
        print ('   |   |')
        print (' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
        print ('   |   |')
        print ('-----------')
        print ('   |   |')
        print (' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
        print ('   |   |')


    #Gets the input of the player
    def inputPlayerLetter(self):
        # Lets the player type which letter they want to be.
        # Returns a list with the player's letter as the first item, and the computer's letter as the second.
        letter = ''
        while not (letter == 'X' or letter == 'O'):
            print('Do you want to be ' + Fore.RED + 'X' + Style.RESET_ALL + ' or ' + Fore.BLUE + 'O?' + Style.RESET_ALL)
            letter = input().upper()

        # the first element in the tuple is the player's letter, the second is the computer's letter.
        if letter == 'X':
            return [Fore.RED + 'X' + Style.RESET_ALL, Fore.BLUE + 'O' + Style.RESET_ALL]
        else:
            return [Fore.BLUE + 'O' + Style.RESET_ALL, Fore.RED +  'X' + Style.RESET_ALL]

    #Randomly sees who goes first
    def whoGoesFirst(self):
        # Randomly choose the player who goes first.
        if random.randint(0, 1) == 0:
            return 'player2'
        else:
            return 'player1'

    #Simple play again function at the end of the game
    def playAgain(self):
        # This function returns True if the player wants to play again, otherwise it returns False.
        print('Do you want to play again? (yes or no)')
        return input().lower().startswith('y')

    #Just puts the letter of your move onto the board
    def makeMove(self, board, letter, move):
        board[move] = letter

    #Checks all the possibilities of winning
    def isWinner(self, bo, le):
        # Given a board and a player's letter, this function returns True if that player has won.
        # We use bo instead of board and le instead of letter so we don't have to type as much.
        return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
        (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
        (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
        (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
        (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
        (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
        (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
        (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal

    def getBoardCopy(self, board):
        # Make a duplicate of the board list and return it the duplicate.
        dupeBoard = []

        for i in board:
            dupeBoard.append(i)

        return dupeBoard

    def isSpaceFree(self, board, move):
        # Return true if the passed move is free on the passed board.
        if [board[move] == '1' or board[move] == '2' or board[move] == '3' or board[move] == '4' or board[move] == '5' or
            board[move] == '6' or board[move] == '7' or board[move] == '8' or board[move] == '9']:
            return True
        else:
            return False

    def getPlayer1Move(self, board):
        # Let the player type in his move.
        move = ' '
        while move not in '1 2 3 4 5 6 7 8 9'.split() or not self.isSpaceFree(board, int(move)):
            if move != ' ': print('I\'m sorry, that wasn\'t a registered spot, or the space is already taken!')
            print('Player one, what is your next move? (1-9)')
            move = input()
        return int(move)

    def chooseRandomMoveFromList(self, board, movesList):
        # Returns a valid move from the passed list on the passed board.
        # Returns None if there is no valid move.
        possibleMoves = []
        for i in movesList:
            if isSpaceFree(board, i):
                possibleMoves.append(i)

        if len(possibleMoves) != 0:
            return random.choice(possibleMoves)
        else:
            return None

    def getPlayer2Move(self, board, player2Letter):
        # Let the player type in his move.
        move = ' '
        while move not in '1 2 3 4 5 6 7 8 9'.split() or not self.isSpaceFree(board, int(move)):
            if move != ' ': print('I\'m sorry, that wasn\'t a registered spot, or the space is already taken!')
            print('Player two, what is your next move? (1-9)')
            move = input()
        return int(move)

    def isBoardFull(self, board):
        # Return True if every space on the board has been taken. Otherwise return False.
        for i in range(1, 10):
            if self.isSpaceFree(board, i):
                return False
        return True


#This is where everything gets called in a while loop
while True:
    # Reset the board

    tic = Tic()

    theBoard = ['0', '1', '2', '3', '4', '5', '6' ,'7', '8', '9']
    player1Letter, player2Letter = tic.inputPlayerLetter()
    turn = tic.whoGoesFirst()
    if turn == 'player1': 
        print('Player one will go first.')
    else: 
        print('Player two will go first.')
    tic.drawSampleBoard()
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player1':
            # Player one's turn.
            tic.drawBoard(theBoard)
            move = tic.getPlayer1Move(theBoard)
            tic.makeMove(theBoard, player1Letter, move)

            if tic.isWinner(theBoard, player1Letter):
                tic.drawBoard(theBoard)
                print('Hooray! Player one won the game!')
                gameIsPlaying = False
            else:
                if tic.isBoardFull(theBoard):
                    tic.drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player2'

        else:
            # Player two's turn.
            tic.drawBoard(theBoard)
            move = tic.getPlayer2Move(theBoard, player2Letter)
            tic.makeMove(theBoard, player2Letter, move)

            if tic.isWinner(theBoard, player2Letter):
                tic.drawBoard(theBoard)
                print('Horray! Player two has won the game!')
                gameIsPlaying = False
            else:
                if tic.isBoardFull(theBoard):
                    tic.drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player1'

    if not tic.playAgain():
        break
