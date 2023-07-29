from models import *

class WinningStrategy:

    def checkWinner(self, board, last_move):
        pass

class RowWinningStrategy(WinningStrategy):
    def checkWinner(self, board, last_move):
        return False

class ColumnWinningStrategy(WinningStrategy):
    def checkWinner(self, board, last_move):
        return False

class DiagonalWinningStrategy(WinningStrategy):
    def checkWinner(self, board, last_move):
        return False

class BotPlayingStrategy:

    @abstractmethod
    def makeMove(self, board):
        pass

class EASYBotPlayingStrategy(BotPlayingStrategy):
    
    def makeMove(self, board):
        return None

class MEDIUMBotPlayingStrategy(BotPlayingStrategy):
    
    def makeMove(self, board):
        return None

class HARDBotPlayingStrategy(BotPlayingStrategy):
    
    def makeMove(self, board):
        return None

class BotPlayingStrategyFactory:
    
    def getBotPlayingStrategyforDifficultyLevel(self, dl):
        if (dl == DifficultyLevel.EASY) :
            return EASYBotPlayingStrategy()
        elif (dl == DifficultyLevel.MEDIUM) :
            return MEDIUMBotPlayingStrategy()
        else :
            return HARDBotPlayingStrategy()
