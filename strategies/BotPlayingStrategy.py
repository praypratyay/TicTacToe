from abc import abstractmethod
from models.enums import CellState

class BotPlayingStrategy:

    @abstractmethod
    def makeMove(self, board):
        pass

class EASYBotPlayingStrategy(BotPlayingStrategy):
    
    def makeMove(self, board):
        for i in range(board.size):
            for j in range(board.size):
                if (board.grid[i][j].state == CellState.EMPTY):
                    return board.grid[i][j]
        return None # The code never comes here.

class MEDIUMBotPlayingStrategy(BotPlayingStrategy):
    
    def makeMove(self, board):
        return None

class HARDBotPlayingStrategy(BotPlayingStrategy):
    
    def makeMove(self, board):
        return None
    
class BotPlayingStrategyFactory:
    """ For simplifying we will return one strategy """
    def getBotPlayingStrategyforDifficultyLevel(dl):
        return EASYBotPlayingStrategy()
        """
        if (dl == DifficultyLevel.EASY) :
            return EASYBotPlayingStrategy()
        elif (dl == DifficultyLevel.MEDIUM) :
            return MEDIUMBotPlayingStrategy()
        else :
            return HARDBotPlayingStrategy()
        """