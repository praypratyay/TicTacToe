from abc import ABC, abstractmethod
from models.enums import *
from strategies.BotPlayingStrategy import BotPlayingStrategyFactory

class Board:
    """ Using private attributes just to demonstrate that we can use
        property decorator to handle access modifiers.

        Getters and Setters in python are often used when:

         - We use getters & setters to add validation logic around getting and setting a value.
         - To avoid direct access of a class field i.e. private variables cannot be accessed directly or modified by external user.
    """
    __size = None
    __grid = None

    def __init__(self, size):
        self.__size = size
        self.__grid=[]
        for i in range(size):
            self.__grid.append([])
            for j in range(size):
                self.__grid[i].append(Cell(i,j))

    # | - | X | - |
    # | - | O | - |
    # | X | - | - |

    def display(self):
        for i in range(self.__size):
            print("|", end =" ")
            for j in range(self.__size):
                if (self.__grid[i][j].state == CellState.EMPTY):
                    print("-", end = " | ")
                else:
                    print(self.__grid[i][j].player.symbol.char, end =" | ")
            print()


    @property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self, size):
        self.__size = size

    @property
    def grid(self):
        return self.__grid
    
    @grid.setter
    def grid(self, grid):
        self.__grid = grid


class Cell:
    player = None
    row = None
    col = None
    state = None #FILLED/EMPTY/BLOCKED

    def __init__(self, i,j):
        self.row = i
        self.col = j
        self.state = CellState.EMPTY


class Player:
    name = ""
    symbol = None
    playerType = None #HUMAN/BOT/GUEST


    def __init__(self, name, symbol, playerType):
        self.name = name
        self.symbol = symbol
        self.playerType = playerType

    
    def makeMove(self, board):
        row = int(input("Please tell row no. = "))
        col = int(input("Please tell col no. = "))
        return Cell(row, col)


class Symbol:
    char = ""
    
    def __init__(self, char):
        self.char = char


class Bot(Player):
    difficultyLevel = None #EASY/MEDIUM/HARD
    botplayingStrategy =  None

    def __init__(self, name, symbol, difficultyLevel):
        super().__init__(name, symbol, PlayerType.BOT)
        self.difficultyLevel = difficultyLevel
        self.botplayingStrategy = BotPlayingStrategyFactory.getBotPlayingStrategyforDifficultyLevel(dl=difficultyLevel)

    def makeMove(self, board):
        return self.botplayingStrategy.makeMove(board)

class Move:
    cell = None
    player = None

    def __init__(self, cell, player):
        self.cell = cell
        self.player = player


class Game:
    board = None
    players = None
    currentPlayerindex = None
    moves = None
    winningStrategies = None
    winner = None
    gameStatus =  None #INPROGRESS/DRAW/ENDED

    def __init__(self, gameBuilder):
        self.moves = []
        self.players = gameBuilder.players
        self.board = Board(gameBuilder.dimension)
        self.currentPlayerindex = 0
        self.winningStrategies = gameBuilder.winningStrategies
        self.gameStatus = GameStatus.INPROGRESS

    def printBoard(self):
        self.board.display()
    
    def printResult(self):
        if self.gameStatus == GameStatus.ENDED :
            print("GAME has ENDED")
            print("Winner is : ", self.winner.name)
        if self.gameStatus == GameStatus.DRAW :
            print("GAME is a DRAW")

    def validateMove(self, cell):
        r = cell.row
        c = cell.col

        if (r<0 or c<0 or r>self.board.size-1 or c>self.board.size-1) :
            return False
        if (self.board.grid[r][c].state == CellState.EMPTY):
            return True
        return False

    def makeMove(self):

        currentP = self.players[self.currentPlayerindex]
        print("It is this player turn  = ", currentP.name)
        proposedCell = currentP.makeMove(self.board)

        # Validate if the move is correct
        if (self.validateMove(proposedCell) == False):
            print(" INVALID MOVE, TRY AGAIN")
            return None

        print(" MOVE SUCCESSFULL ")
        # Update cell in the board
        cellInBoard = self.board.grid[proposedCell.row][proposedCell.col]
        cellInBoard.state = CellState.FILLED
        cellInBoard.player = currentP

        # Add move to the list of moves
        mov = Move(cell=cellInBoard, player=currentP)
        self.moves.append(mov)

        # Check if this move results in winner
        for ws in self.winningStrategies:
            if(ws.checkWinner(self.board, mov)):
                self.gameStatus = GameStatus.ENDED
                self.winner = currentP
                return None
        
        # Check for DRAW (board is full)
        if (len(self.moves) == self.board.size*self.board.size):
            self.gameStatus = GameStatus.DRAW
            return None
        
        # Update turn to next player
        self.currentPlayerindex = (self.currentPlayerindex+1) % len(self.players)

    def UNDO(self):

        print("UNDOING LAST MOVE")
        if(len(self.moves) == 0):
            # Note: Handle exception in separate files.
            raise Exception("No Moves. Cant UNDO")
        lastMove = self.moves.pop()

        proposedCell = lastMove.cell

        # Update cell in the board
        cellInBoard = self.board.grid[proposedCell.row][proposedCell.col]
        cellInBoard.state = CellState.EMPTY
        cellInBoard.player = None

        # Undo maps in strategies
        for ws in self.winningStrategies:
            ws.handleUNDO(self.board, lastMove)

        # Update turn to next player
        self.currentPlayerindex = (self.currentPlayerindex-1+len(self.players)) % len(self.players)


class GameBuilder():
    dimension = None
    players = None
    winningStrategies = None

    def setDimension(self, dimension):
        self.dimension = dimension
        return self

    def setPlayers(self, players):
        self.players = players
        return self

    def setwinningStrategies(self, winningStrategies):
        self.winningStrategies = winningStrategies
        return self

    def validate(self):
        if (self.dimension <= 2):
            print("INVALID DIMENSION")
            return False
        if (len(self.players) !=  self.dimension-1):
            print("INVALID NO OF PLAYERS")
            return False
        
        botCount = 0
        for player in self.players:
            if (player.playerType == PlayerType.BOT):
                botCount += 1
        if (botCount >= 2):
            print("INVALID BOT COUNT")
            return False
 
        existingSymbols = set()
        for player in self.players:
            if (player.symbol in existingSymbols):
                print("INVALID SYMBOL")
                return False
            existingSymbols.add(player.symbol)

    def build(self):
        if (self.validate() == False):
            # Note: Handle exception in separate files.
            raise Exception("Invalid Parameters for Game")
        return Game(self)
