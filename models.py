from abc import ABC, abstractmethod
from enum import Enum

""" ENUMS """
class GameStatus(Enum):
    INPROGRESS = 1
    ENDED = 2
    DRAW = 3

class CellState(Enum):
    EMPTY = 1
    FILLED = 2
    BLOCKED = 3

class PlayerType(Enum):
    HUMAN = 1
    BOT = 2
    GUEST = 3

class DifficultyLevel(Enum):
    EASY = 1
    MEDIUM = 2
    HARD = 3


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

    def __init__(self, name, symbol, type):
        self.name = name
        self.symbol = symbol
        self.playerType = type
        
class Symbol:
    char = ""
    
    def __init__(self, char):
        self.char = char
    
class Bot(Player):
    difficultyLevel = None #EASY/MEDIUM/HARD

    def __init__(self, name, symbol, dl):
        super.__init__(name,symbol, PlayerType.BOT)
        self.difficultyLevel = dl

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

    def __init__(self, dimension, players, winningstrategies):
        self.moves = []
        self.players = players
        self.board = Board(dimension)
        self.currentPlayerindex = 0
        self.winningStrategies = winningstrategies
        self.gameStatus = GameStatus.INPROGRESS

class WinningStrategy:
    pass

class RowWinningStrategy(WinningStrategy):
    pass

class ColumnWinningStrategy(WinningStrategy):
    pass

class DiagonalWinningStrategy(WinningStrategy):
    pass
